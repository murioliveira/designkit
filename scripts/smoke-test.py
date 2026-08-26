#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMOKE TEST — Design Kit
=======================
Valida a integridade do design system kit (C:/Users/muzph/projetos/designkit).

Uso:
    python scripts/smoke-test.py

Saída: um bloco PASS/FAIL por check (com contagens) e um resumo final
"SMOKE TEST: PASS (N checks)" ou "FAIL (M falhas)" com exit code 0/1.

Dependências: apenas stdlib (Python 3). Node é usado opcionalmente no check 5
(se ausente, o check é pulado com aviso).

Checks:
  1. tokens      — todo var(--...) usado em styles/*.css e index.html está definido
                   (a união de definições inclui vars locais, ex.: --shell-* do layout.css)
  2. hex mágico  — nenhum hex hardcoded em styles/*.css e portal/*.css (cores via var()/color-mix)
  3. HTML        — tags balanceadas, ids únicos, âncoras da sidebar <-> seções 1:1,
                   aria-labelledby resolvem, lang presente
  4. CSS         — chaves {} balanceadas em todos os arquivos css (styles/ + portal/)
  5. JS          — node --check em js/*.js e portal/*.js (skip com nota se node ausente)
  6. Docs        — docs/componentes/README.md referencia arquivos que existem
  7. Skills      — frontmatter (name+description) em skills/*/SKILL.md;
                   .claude/skills/* 1:1 com skills/*
  8. Casos       — arquivos esperados em docs/casos/lumen/ e docs/casos/brisa/
"""

import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read(path):
    """Lê um arquivo; retorna "" se não existir (o check reporta FAIL)."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def strip_comments(text):
    """Remove comentários CSS (/* ... */) — útil para não contar hex em comentários."""
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def css_files():
    """Todos os .css em styles/ (ordem estável)."""
    return sorted(f for f in os.listdir(os.path.join(ROOT, "styles")) if f.endswith(".css"))


# ---------------------------------------------------------------------------
# Registro de checks
# ---------------------------------------------------------------------------
CHECKS = []


def check(name):
    """Decorator: registra uma função de check que retorna (ok: bool, detail: str)."""
    def deco(fn):
        CHECKS.append((name, fn))
        return fn
    return deco


# ---------------------------------------------------------------------------
# 1. Tokens
# ---------------------------------------------------------------------------
@check("tokens: var() usados estao definidos em tokens.css")
def check_tokens():
    css_dir = os.path.join(ROOT, "styles")
    all_defined = set()   # união de definições em todos os css (inclui vars locais)
    used = set()          # var(--...) usados em css + index.html

    for fname in css_files():
        text = read(os.path.join(css_dir, fname))
        if not text:
            return False, f"styles/{fname} ausente"
        all_defined.update(re.findall(r"--[a-zA-Z0-9-]+\s*:", text))
        used.update(re.findall(r"var\((--[a-zA-Z0-9-]+)", text))

    html = read(os.path.join(ROOT, "index.html"))
    if not html:
        return False, "index.html ausente"
    used.update(re.findall(r"var\((--[a-zA-Z0-9-]+)", html))

    # normaliza definições (remove o ":" final)
    defined_norm = {d.rstrip(":").strip() for d in all_defined}
    missing = sorted(u for u in used if u not in defined_norm)
    return (not missing,
            f"{len(used)} var() usados, {len(missing)} faltando"
            + (f": {', '.join(missing[:8])}" if missing else ""))


# ---------------------------------------------------------------------------
# 2. Hex mágico
# ---------------------------------------------------------------------------
@check("hex: nenhum hex hardcoded em styles/*.css e portal/*.css")
def check_hex():
    problems = []
    total_hex = 0
    for fname in css_files():
        # tokens.css é a fonte de verdade: hex são definidos aqui, não consumidos
        if fname == "tokens.css":
            continue
        path = os.path.join(ROOT, "styles", fname)
        text = read(path)
        if not text:
            problems.append(f"styles/{fname} ausente")
            continue
        hexes = re.findall(r"#[0-9a-fA-F]{3,8}\b", strip_comments(text))
        if hexes:
            problems.append(f"styles/{fname}: {', '.join(sorted(set(hexes))[:5])}")
            total_hex += len(hexes)
    return (not problems,
            f"{total_hex} hex encontrados" + (f": {'; '.join(problems[:5])}" if problems else ""))


# ---------------------------------------------------------------------------
# 3. HTML
# ---------------------------------------------------------------------------
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}


def balanced_tags(html):
    """Retorna lista de tags desbalanceadas (stack residual) e pares óbvios."""
    # remove comentários, script e style (evita falsos positivos com JS/CSS inline)
    text = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    text = re.sub(r"<script\b.*?</script>", "", text, flags=re.S | re.I)
    text = re.sub(r"<style\b.*?</style>", "", text, flags=re.S | re.I)

    stack = []
    tag_re = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:\"[^\"]*\"|'[^']*'|[^>\"'])*)>")
    for m in tag_re.finditer(text):
        closing, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if attrs.rstrip().endswith("/") or tag in VOID:
            continue
        if closing:
            if stack and stack[-1] == tag:
                stack.pop()
            else:
                stack.append("!" + tag)  # fechamento sem abertura correspondente
        else:
            stack.append(tag)
    return stack


@check("html: tags balanceadas, ids unicos, sidebar<->secoes 1:1, aria, lang")
def check_html():
    path = os.path.join(ROOT, "index.html")
    html = read(path)
    if not html:
        return False, "index.html ausente"

    problems = []

    # 3a. tags balanceadas
    residual = balanced_tags(html)
    if residual:
        problems.append(f"{len(residual)} tags desbalanceadas: {', '.join(residual[:6])}")

    # 3b. ids únicos
    ids = re.findall(r'id="([^"]+)"', html)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        problems.append(f"ids duplicados: {', '.join(dup[:6])}")

    # 3c. âncoras da sidebar <-> seções (1:1)
    sidebar = set(re.findall(r'<a class="sidebar__link"[^>]*href="#([a-z0-9-]+)"', html))
    sections = set(re.findall(r'<section id="([a-z0-9-]+)"', html))
    if sidebar != sections:
        problems.append(
            f"sidebar/seed sem âncora: {sorted(sidebar - sections) or '-'}; "
            f"secoes sem âncora: {sorted(sections - sidebar) or '-'}")

    # 3d. aria-labelledby resolve
    for ref in re.findall(r'aria-labelledby="([^"]+)"', html):
        for rid in ref.split():
            if rid not in ids:
                problems.append(f"aria-labelledby sem id: {rid}")

    # 3e. lang presente
    has_lang = bool(re.search(r'<html\s+lang="[^"]+"', html))
    if not has_lang:
        problems.append("atributo lang ausente em <html>")

    n_aria = len(re.findall(r'aria-labelledby=', html))
    detail = (f"{len(ids)} ids, {len(sidebar)} âncoras sidebar, {len(sections)} seções, "
              f"{n_aria} aria-labelledby, lang {'OK' if has_lang else 'AUSENTE'}")
    return (not problems, (detail + " | " + "; ".join(problems)) if problems else detail)


# ---------------------------------------------------------------------------
# 4. CSS: chaves balanceadas
# ---------------------------------------------------------------------------
@check("css: chaves {} balanceadas em styles/ e portal/")
def check_css_braces():
    problems = []
    total = 0
    n_files = 0
    for fname in css_files():
        text = read(os.path.join(ROOT, "styles", fname))
        if not text:
            problems.append(f"styles/{fname} ausente")
            continue
        n_files += 1
        text = strip_comments(text)
        opens = text.count("{")
        closes = text.count("}")
        total += opens
        if opens != closes:
            problems.append(f"styles/{fname}: {opens} aberturas vs {closes} fechamentos")
    portal_dir = os.path.join(ROOT, "portal")
    if os.path.isdir(portal_dir):
        for fname in sorted(os.listdir(portal_dir)):
            if fname.endswith(".css"):
                text = read(os.path.join(portal_dir, fname))
                if not text:
                    problems.append(f"portal/{fname} ausente")
                    continue
                n_files += 1
                text = strip_comments(text)
                opens = text.count("{")
                closes = text.count("}")
                total += opens
                if opens != closes:
                    problems.append(f"portal/{fname}: {opens} aberturas vs {closes} fechamentos")
    return (not problems,
            f"{n_files} arquivos, {total} pares de chaves"
            + (f" | {'; '.join(problems)}" if problems else ""))


# ---------------------------------------------------------------------------
# 5. JS: node --check
# ---------------------------------------------------------------------------
@check("js: node --check em js/*.js e portal/*.js")
def check_js():
    node = shutil.which("node")
    if not node:
        return True, "SKIP: node não encontrado no PATH"
    errors = []
    checked = 0
    for base_dir, label in [(os.path.join(ROOT, "js"), "js"), (os.path.join(ROOT, "portal"), "portal")]:
        if not os.path.isdir(base_dir):
            continue
        for fname in sorted(os.listdir(base_dir)):
            if not fname.endswith(".js"):
                continue
            path = os.path.join(base_dir, fname)
            if not os.path.exists(path):
                errors.append(f"{label}/{fname} ausente")
                continue
            proc = subprocess.run([node, "--check", path],
                                  capture_output=True, text=True)
            if proc.returncode != 0:
                err = (proc.stderr or "").strip().splitlines()
                errors.append(f"{label}/{fname}: {'; '.join(err[-3:])}" if err else f"{label}/{fname}: exit {proc.returncode}")
            checked += 1
    if not checked:
        return True, "SKIP: nenhum .js encontrado em js/ ou portal/"
    return (not errors,
            f"{checked} arquivo(s) JS válido(s)" + (f" | {'; '.join(errors)}" if errors else ""))


# ---------------------------------------------------------------------------
# 6. Docs: README de componentes referencia arquivos existentes
# ---------------------------------------------------------------------------
@check("docs: docs/componentes/README.md referencia arquivos existentes")
def check_docs():
    readme_path = os.path.join(ROOT, "docs", "componentes", "README.md")
    readme = read(readme_path)
    if not readme:
        return False, "docs/componentes/README.md ausente"
    # extrai links do tipo [nome.md](./nome.md)
    refs = sorted(set(re.findall(r"\]\(\./([a-z0-9-]+\.md)\)", readme)))
    missing = [r for r in refs if not os.path.exists(
        os.path.join(ROOT, "docs", "componentes", r))]
    return (not missing,
            f"{len(refs)} docs referenciados, {len(missing)} faltando"
            + (f": {', '.join(missing)}" if missing else ""))


# ---------------------------------------------------------------------------
# 7. Skills: frontmatter + espelho .claude/skills
# ---------------------------------------------------------------------------
@check("skills: frontmatter em skills/*/SKILL.md e espelho .claude 1:1")
def check_skills():
    problems = []
    skills_dir = os.path.join(ROOT, "skills")
    claude_dir = os.path.join(ROOT, ".claude", "skills")

    skill_names = []
    for entry in sorted(os.listdir(skills_dir)):
        spath = os.path.join(skills_dir, entry, "SKILL.md")
        if not os.path.isfile(spath):
            continue
        skill_names.append(entry)
        text = read(spath)
        if not text:
            problems.append(f"skills/{entry}/SKILL.md ausente")
            continue
        m = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.S)
        if not m:
            problems.append(f"skills/{entry}: sem frontmatter")
            continue
        fm = m.group(1)
        if not re.search(r"^name:\s*\S+", fm, flags=re.M):
            problems.append(f"skills/{entry}: frontmatter sem name")
        if not re.search(r"^description:\s*\S+", fm, flags=re.M):
            problems.append(f"skills/{entry}: frontmatter sem description")

    # espelho .claude/skills 1:1
    claude_names = sorted(
        e for e in os.listdir(claude_dir)
        if os.path.isfile(os.path.join(claude_dir, e, "SKILL.md")))
    if claude_names != sorted(skill_names):
        problems.append(
            f".claude/skills {claude_names} != skills/ {skill_names}")

    return (not problems,
            f"{len(skill_names)} skills com frontmatter, {len(claude_names)} espelhos"
            + (f" | {'; '.join(problems[:5])}" if problems else ""))


# ---------------------------------------------------------------------------
# 8. Casos: arquivos esperados
# ---------------------------------------------------------------------------
@check("casos: lumen e brisa com arquivos esperados")
def check_cases():
    expected = {
        "docs/casos/lumen": ["index.html", "lumen.css", "README.md"],
        "docs/casos/brisa": ["research.md", "ia.md", "critique.md", "handoff.md"],
    }
    problems = []
    total = 0
    for folder, files in expected.items():
        fdir = os.path.join(ROOT, folder)
        if not os.path.isdir(fdir):
            problems.append(f"{folder} ausente")
            continue
        for f in files:
            total += 1
            if not os.path.isfile(os.path.join(fdir, f)):
                problems.append(f"{folder}/{f} ausente")
    return (not problems,
            f"{total} arquivos esperados, {len(problems)} faltando"
            + (f": {'; '.join(problems[:6])}" if problems else ""))


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
def main():
    failures = 0
    print("=" * 70)
    print("SMOKE TEST — Design Kit")
    print(f"raiz: {ROOT}")
    print("=" * 70)
    for name, fn in CHECKS:
        try:
            ok, detail = fn()
        except Exception as exc:  # robustez: nenhum check pode derrubar o script
            ok, detail = False, f"erro inesperado: {exc!r}"
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"[{status}] {name}")
        print(f"         {detail}")
    print("-" * 70)
    total = len(CHECKS)
    if failures:
        print(f"SMOKE TEST: FAIL ({failures} falha(s) em {total} checks)")
        return 1
    print(f"SMOKE TEST: PASS ({total} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
