#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANTI-SLOP CHECK — Design Kit
============================
Varredura mecânica anti-slop sobre as UIs do repositório
(C:/Users/muzph/projetos/designkit), conforme DESIGN.md §4 (tells da IA)
e §5.3 (detecção determinística) e §6 (pre-flight).

Uso:
    python scripts/anti-slop-check.py

Alvos: index.html (raiz) + docs/casos/<nome>/index.html + docs/casos/<nome>/*.css

Checks por arquivo:
  1. em-dash   — zero `—` e zero `–` em texto visível (HTML: fora de
                 comentário/script/style; CSS: fora de comentário).
  2. hex       — zero cores hex hardcoded (CSS: fora de comentário e url();
                 HTML: apenas em contexto de cor — style/fill/stroke/bgcolor).
  3. inter     — zero Inter como fonte (font-family com Inter ou link do
                 Google Fonts pedindo Inter).
  4. eyebrows  — contagem de eyebrows (classes *eyebrow/kicker/overline ou
                 style inline uppercase+letter-spacing) <= ceil(seções/3);
                 se não der para contar, WARN com instrução.
  5. nomes     — zero nomes genéricos (Jane/John Doe, Acme, Lorem ipsum).
  6. paleta    — zero hex da família bege+latão+oxblood banida (DESIGN.md §4.1).
  7. scroll    — zero scroll cues óbvios ("Scroll to", "scroll para", "↓"
                 solto; "(↑↓)" de teclado é ignorado).

Exceções documentadas:
  - meta theme-color no <head> (#f8fafc / #020617): hex intencional de
    navegador, não cor de UI — removido antes do check de hex (reportado
    como nota, não falha).
  - #fragmentos em href/id e dados de negócio que parecem hex (ex.: números
    de fatura "#4821" no caso Norte) NÃO são cores — o check de hex em HTML
    só olha atributos de cor (style/fill/stroke/bgcolor).

Robustez: arquivo ausente = FAIL nesse check; nenhum check pode derrubar o
script (try/except por check).

Saída: bloco por arquivo com PASS/FAIL/WARN por check + evidência, e resumo
final "ANTI-SLOP: PASS (N checks, M arquivos)" ou "FAIL (K problemas)".
WARN não conta como falha, mas é impresso. Exit code 0 = sem FAIL; 1 = FAIL.

Dependências: apenas stdlib (Python 3).
"""

import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Constantes (tells — DESIGN.md §4)
# ---------------------------------------------------------------------------

# Paleta bege+latão+oxblood banida para briefs premium-consumer (DESIGN.md §4.1)
BANNED_PALETTE = {
    "#f5f1ea", "#f7f5f1", "#fbf8f1", "#efeae0", "#ece6db", "#faf7f1", "#e8dfcb",  # fundos "papel quente"
    "#b08947", "#b6553a", "#9a2436", "#9c6e2a", "#bc7c3a", "#7d5621",            # brass/clay/oxblood/ochre
    "#1a1714", "#1a1814", "#1b1814",                                              # espresso / warm near-black
}

GENERIC_NAMES = ["Jane Doe", "John Doe", "Acme", "Lorem ipsum"]

HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")


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


def strip_css_comments(text):
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def strip_html_shell(text):
    """Remove comentários, <script> e <style> do HTML (falsos positivos de JS/CSS inline)."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<script\b.*?</script>", "", text, flags=re.S | re.I)
    text = re.sub(r"<style\b.*?</style>", "", text, flags=re.S | re.I)
    return text


def strip_urls(text):
    """Mascara url(...) (ex.: url(#gradiente), data-URIs com hex)."""
    return re.sub(r"url\([^)]*\)", "url()", text, flags=re.S | re.I)


def target_files():
    """index.html raiz + TODOS os arquivos HTML/CSS de docs/casos/<nome>/ (ordem estável).

    Inclui qualquer .html/.css do caso (index.html, before.html, after.html etc.) para
    que o detector cubra todos os artefatos gerados — não só o index.html.
    """
    files = [os.path.join(ROOT, "index.html")]
    # todos os .css em styles/ (paletas, componentes, layout — cobertura completa)
    styles_dir = os.path.join(ROOT, "styles")
    if os.path.isdir(styles_dir):
        for fname in sorted(os.listdir(styles_dir)):
            if fname.endswith(".css"):
                files.append(os.path.join(styles_dir, fname))
    casos_dir = os.path.join(ROOT, "docs", "casos")
    if os.path.isdir(casos_dir):
        for name in sorted(os.listdir(casos_dir)):
            fdir = os.path.join(casos_dir, name)
            if not os.path.isdir(fdir):
                continue
            for fname in sorted(os.listdir(fdir)):
                if fname.endswith(".html") or fname.endswith(".css"):
                    files.append(os.path.join(fdir, fname))
    # portal/ — showcase portal (HTML + CSS)
    portal_dir = os.path.join(ROOT, "portal")
    if os.path.isdir(portal_dir):
        for fname in sorted(os.listdir(portal_dir)):
            if fname.endswith(".html") or fname.endswith(".css"):
                files.append(os.path.join(portal_dir, fname))
    return files


# Fixtures negativos (controle): arquivos DELIBERADAMENTE "slop" que existem como
# demonstração do detector (ex.: redesign-demo/before.html = estado "antes" do
# redesign, cheio de tells de IA de propósito). As falhas desses arquivos são
# ESPERADAS e não derrubam o gate; todo o resto do repo precisa passar limpo.
EXPECTED_FAIL_FIXTURES = {
    "docs/casos/redesign-demo/before.html",
    "styles/tokens.css",  # fonte canônica: hex são DEFINIDOS aqui
}


def is_html(path):
    return path.endswith(".html")


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


# ---------------------------------------------------------------------------
# Checks (cada um retorna status + evidência)
# ---------------------------------------------------------------------------

def check_emdash(path, text):
    """1. Zero em-dash/en-dash em texto visível."""
    if is_html(path):
        text = strip_html_shell(text)
    else:
        text = strip_css_comments(text)
    found = re.findall(r"[—–]", text)
    if not found:
        return "PASS", "0 em-dash/en-dash em texto visível"
    ctx = []
    for m in re.finditer(r".{0,28}[—–].{0,28}", text):
        ctx.append(m.group(0).strip()[:60])
    return "FAIL", f"{len(found)} em-dash/en-dash: {' | '.join(ctx[:4])}"


def check_hex(path, text):
    """2. Zero cores hex hardcoded (fora de tokens)."""
    if is_html(path):
        # exceção documentada: meta theme-color (cor de navegador, não de UI)
        text = re.sub(r'<meta[^>]*name="theme-color"[^>]*>', "", text, flags=re.I)
        text = strip_html_shell(text)
        # em HTML, hex só conta em contexto de cor: style, fill, stroke, bgcolor
        found = []
        for m in re.finditer(
                r'(?:style|fill|stroke|bgcolor|data-color)\s*=\s*"([^"]*)"', text, flags=re.I):
            for h in HEX_RE.findall(m.group(1)):
                found.append(h)
    else:
        text = strip_css_comments(text)
        text = strip_urls(text)
        found = HEX_RE.findall(text)
    if not found:
        return "PASS", "0 hex hardcoded fora de tokens"
    return "FAIL", f"{len(found)} hex: {', '.join(sorted(set(found))[:6])}"


def check_inter(path, text):
    """3. Zero Inter como fonte (font-family ou Google Fonts link)."""
    hits = []
    # font-family: ... Inter ...  (token, não "Interativo"/"Interação")
    for m in re.finditer(r"font-family\s*:\s*([^;}]+)", text, flags=re.I):
        family = m.group(1)
        if re.search(r"(?<![a-zA-Z])Inter(?![a-zA-Z])", family):
            hits.append("font-family: " + family.strip()[:50])
    # <link href="...fonts.googleapis...family=Inter...">
    for m in re.finditer(r'<link[^>]*href="([^"]*)"[^>]*>', text, flags=re.I):
        href = m.group(1)
        if "fonts.googleapis" in href and "Inter" in href:
            hits.append("Google Fonts link: " + href[:70])
    if not hits:
        return "PASS", "0 Inter como fonte"
    return "FAIL", " | ".join(hits[:4])


def check_eyebrows(path, text):
    """4. Eyebrows <= ceil(seções/3); WARN se não der para contar com precisão."""
    if not is_html(path):
        return "n/a", "check aplicável só a HTML"
    text = strip_html_shell(text)
    n_sections = len(re.findall(r"<section\b", text, flags=re.I))
    # marcação nomeada: classes *eyebrow/kicker/overline/section-label
    named = re.findall(
        r'class="([^"]*(?:eyebrow|kicker|overline|section-label)[^"]*)"', text, flags=re.I)
    # marcação inline: style com uppercase + letter-spacing (eyebrow típico)
    inline = []
    for m in re.finditer(r'style="([^"]*)"', text, flags=re.I):
        s = m.group(1)
        if re.search(r"text-transform\s*:\s*uppercase", s, flags=re.I) and \
           re.search(r"letter-spacing", s, flags=re.I):
            inline.append(s[:50])
    count = len(named) + len(inline)
    limit = math.ceil(n_sections / 3) if n_sections else 1

    # heurística de "não deu para contar": labels uppercase sem marcação nomeada
    # (ex.: classe custom com uppercase no CSS que não contém *eyebrow*).
    unnamed = re.findall(
        r'class="([^"]*)"[^>]*>(?:<[^>]+>)*[^<]{0,60}', text)
    suspicious = [c for c in unnamed if "uppercase" in c.lower()]
    evidence = (f"{count} eyebrow(s) em {n_sections} seções (limite {limit})"
                + (f": {', '.join(named[:4])}" if named else ""))

    if count > limit:
        return "FAIL", evidence + " — excede o limite do DESIGN.md (§4.1, máx 1 por 3 seções)"
    if suspicious and count == 0:
        return ("WARN",
                f"0 eyebrows nomeados, mas {len(suspicious)} classe(s) 'uppercase' "
                "sem marcação de eyebrow — revisar manualmente se são labels de seção")
    return "PASS", evidence


def check_names(path, text):
    """5. Zero nomes genéricos."""
    if is_html(path):
        text = strip_html_shell(text)
    else:
        text = strip_css_comments(text)
    low = text.lower()
    hits = [n for n in GENERIC_NAMES if n.lower() in low]
    if not hits:
        return "PASS", "0 nomes genéricos (Jane/John Doe, Acme, Lorem ipsum)"
    return "FAIL", f"nomes genéricos: {', '.join(hits)}"


def check_palette(path, text):
    """6. Zero hex da família bege+latão+oxblood banida (DESIGN.md §4.1)."""
    if is_html(path):
        text = strip_html_shell(text)
    else:
        text = strip_css_comments(text)
        text = strip_urls(text)
    found = sorted({h.lower() for h in HEX_RE.findall(text) if h.lower() in BANNED_PALETTE})
    if not found:
        return "PASS", "0 hex da paleta bege+latão+oxblood banida"
    return "FAIL", f"paleta banida: {', '.join(found[:6])}"


def check_scroll(path, text):
    """7. Zero scroll cues óbvios."""
    if not is_html(path):
        return "n/a", "check aplicável só a HTML"
    text = strip_html_shell(text)
    hits = []
    for cue in ("Scroll to", "scroll to", "Scroll para", "scroll para"):
        if cue in text:
            hits.append(cue)
    # "↓" solto conta como cue; "(↑↓)" / "↑↓" é documentação de teclado e é ignorado
    # ("↓" precedido de "↑" = par de setas de navegação)
    lone_down = len(re.findall(r"(?<!↑)↓", text))
    if lone_down:
        hits.append(f"'{lone_down}x ↓' sem ↑ (possível scroll cue)")
    if not hits:
        return "PASS", "0 scroll cues óbvios"
    return "FAIL", " | ".join(hits[:4])


CHECKS = [
    ("em-dash", check_emdash),
    ("hex", check_hex),
    ("inter", check_inter),
    ("eyebrows", check_eyebrows),
    ("nomes", check_names),
    ("paleta", check_palette),
    ("scroll", check_scroll),
]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def main():
    # Windows: stdout em cp1252 quebra com caracteres como ↓ e — (tells).
    # Reconfigura para UTF-8 com fallback, para a saída nunca derrubar o script.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    files = target_files()
    print("=" * 70)
    print("ANTI-SLOP CHECK — Design Kit")
    print(f"raiz: {ROOT}")
    print("=" * 70)

    if not files:
        print("[FAIL] nenhum arquivo alvo encontrado (index.html ou docs/casos/*)")
        print("ANTI-SLOP: FAIL (1 problema)")
        return 1

    total_checks = 0
    problems = 0
    warns = 0
    expected = 0
    for path in files:
        label = rel(path)
        text = read(path)
        if not text:
            print(f"\n[arquivo: {label}]")
            print("  [FAIL] arquivo ausente ou ilegível")
            problems += 1
            continue
        print(f"\n[arquivo: {label}]")
        is_fixture = label in EXPECTED_FAIL_FIXTURES
        for name, fn in CHECKS:
            total_checks += 1
            try:
                status, detail = fn(path, text)
            except Exception as exc:  # robustez: nenhum check derruba o script
                status, detail = "FAIL", f"erro inesperado: {exc!r}"
            if status == "FAIL":
                if is_fixture:
                    expected += 1  # falha esperada em fixture negativa (não derruba o gate)
                else:
                    problems += 1
            elif status == "WARN":
                warns += 1
            pad = " " * (10 - len(name))
            suffix = "  [fixture: falha esperada]" if status == "FAIL" and is_fixture else ""
            print(f"  [{status}] {name}{pad}{detail}{suffix}")

    print("-" * 70)
    print(f"arquivos: {len(files)} | checks: {total_checks} | "
          f"falhas: {problems} | esperadas: {expected} | avisos: {warns}")
    if problems:
        print(f"ANTI-SLOP: FAIL ({problems} problema(s))")
        return 1
    print(f"ANTI-SLOP: PASS ({total_checks} checks, {len(files)} arquivos"
          + (f", {expected} esperada(s) em fixture(s))" if expected else ")"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
