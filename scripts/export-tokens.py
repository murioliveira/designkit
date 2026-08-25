#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT TOKENS — Design Kit
==========================
Exporta os design tokens de styles/tokens.css (fonte de verdade) para
formatos consumíveis por ferramentas e projetos:

  * tokens/tokens.json — todos os tokens SEMÂNTICOS, estruturados por tema
    (light = bloco :root; dark = bloco [data-theme="dark"]) e por categoria
    (color, typography, spacing, radius, shadow, motion, z). Valores
    var(--...) são resolvidos para o valor final onde possível.
  * tokens/tokens.css  — cópia nomeada do tokens.css para import direto
    em projetos (mesmo arquivo, sem dependências relativas).

Uso:
    python scripts/export-tokens.py

Saída (stdout): contagens — N tokens exportados, N resolvidos,
N não-resolvidos (com lista). Exit code 0 em sucesso.

Dependências: apenas stdlib (Python 3).

Categorias exportadas (semânticas):
  color      --color-*
  typography --font-*, --letter-spacing-*
  spacing    --space-*
  radius     --radius-*
  shadow     --shadow-*, --shadow-color, --focus-ring, --focus-ring-color
  motion     --motion-*
  z          --z-*

Fora do export (infra do próprio CSS, não semânticos): paleta bruta
(--c-*) e layout (--container-*, --breakpoint-*) — PARSEADOS para
resolução de var(), mas não listados no JSON. O bloco
@media (prefers-color-scheme: dark) é um fallback duplicado do dark
(regra CSS de cascata) — ignorado no export.
"""

import datetime
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "styles", "tokens.css")
OUT_DIR = os.path.join(ROOT, "tokens")
OUT_JSON = os.path.join(OUT_DIR, "tokens.json")
OUT_CSS = os.path.join(OUT_DIR, "tokens.css")

# ---------------------------------------------------------------------------
# Ordem estável e predicados de categoria (semânticas)
# ---------------------------------------------------------------------------
CATEGORIES = [
    ("color",      lambda k: k.startswith("--color-")),
    ("typography", lambda k: k.startswith("--font-") or k.startswith("--letter-spacing-")),
    ("spacing",    lambda k: k.startswith("--space-")),
    ("radius",     lambda k: k.startswith("--radius-")),
    ("shadow",     lambda k: k.startswith("--shadow-") or k.startswith("--focus-ring")),
    ("motion",     lambda k: k.startswith("--motion-")),
    ("z",          lambda k: k.startswith("--z-")),
]


def strip_comments(text):
    """Remove comentários CSS (/* ... */)."""
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def parse_blocks(text):
    """Retorna [(selector, body)] para blocos CSS de nível superior."""
    text = strip_comments(text)
    blocks = []
    i, n = 0, len(text)
    while i < n:
        # encontra a próxima chave de abertura no nível 0
        start = None
        depth = 0
        while i < n:
            c = text[i]
            if c == "{":
                if depth == 0:
                    start = i
                    break
                depth += 1
            elif c == "}":
                if depth > 0:
                    depth -= 1
            i += 1
        if start is None:
            break
        # fecha a chave correspondente
        depth = 1
        j = start + 1
        while j < n and depth > 0:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        selector = re.sub(r"^.*}", "", text[:start], flags=re.S).strip()
        body = text[start + 1:j - 1] if j > start + 1 else ""
        blocks.append((selector, body))
        i = j
    return blocks


def extract_props(body):
    """Extrai pares (--nome, valor) de um corpo de bloco CSS."""
    return re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", strip_comments(body))


def resolve_value(value, context, depth=0, visited=()):
    """Resolve var(--x[, fallback]) recursivamente. Retorna (texto, ok)."""
    if "var(" not in value:
        return value, True
    if depth > 10:
        return value, False

    def repl(m):
        name, fallback = m.group(1), (m.group(2) or "").strip()
        if name not in visited and name in context:
            sub, ok = resolve_value(context[name], context, depth + 1, visited + (name,))
            if ok:
                return sub
        if fallback:
            sub, ok = resolve_value(fallback, context, depth + 1, visited)
            if ok:
                return sub
        return m.group(0)

    out = re.sub(r"var\((--[\w-]+)(?:\s*,\s*([^)]*))?\)", repl, value)
    return out, "var(" not in out


def build_theme(token_block, context):
    """Estrutura {categoria: {nome: valor}} + lista de não-resolvidos."""
    theme = {cat: {} for cat, _ in CATEGORIES}
    unresolved = []
    for name, raw in sorted(token_block.items()):
        res = None
        for cat, pred in CATEGORIES:
            if pred(name):
                res = cat
                break
        if res is None:
            continue  # não-semântico (paleta/layout): fora do export
        resolved, ok = resolve_value(raw, context)
        if ok:
            theme[res][name] = resolved
        else:
            theme[res][name] = raw  # mantém o valor original (visível)
            unresolved.append(name)
    theme["$unresolved"] = unresolved
    return theme


def main():
    text = open(SRC, encoding="utf-8").read()
    root_defs, dark_defs = {}, {}
    for selector, body in parse_blocks(text):
        if selector == ":root":
            root_defs = dict(extract_props(body))
        elif selector == '[data-theme="dark"]':
            dark_defs = dict(extract_props(body))

    if not root_defs:
        print(f"[FAIL] :root não encontrado em {SRC}")
        return 1

    # contextos de resolução: dark herda :root e sobrescreve
    ctx_light = dict(root_defs)
    ctx_dark = dict(root_defs)
    ctx_dark.update(dark_defs)

    light = build_theme(root_defs, ctx_light)
    dark = build_theme(dark_defs, ctx_dark)

    # contagens
    def counts(theme, label):
        total = sum(len(v) for k, v in theme.items() if not k.startswith("$"))
        unres = theme["$unresolved"]
        return total, len(unres), unres, label

    lt, lu, lur, _ = counts(light, "light")
    dt, du, dur, _ = counts(dark, "dark")
    total = lt + dt
    unresolved_all = lur + dur

    payload = {
        "meta": {
            "name": "Design Kit tokens",
            "description": "Tokens semânticos do design system (export).",
            "source": "styles/tokens.css",
            "generated": datetime.datetime.now(datetime.timezone.utc)
                          .isoformat(timespec="seconds"),
            "by": "scripts/export-tokens.py",
            "themes": ["light", "dark"],
            "count": total,
        },
        "light": light,
        "dark": dark,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=True)
        fh.write("\n")
    shutil.copyfile(SRC, OUT_CSS)

    # relatório
    print(f"export: light {lt} tokens ({len(light['$unresolved'])} não-resolvidos), "
          f"dark {dt} tokens ({len(dark['$unresolved'])} não-resolvidos)")
    print(f"total: {total} tokens exportados, "
          f"{total - len(unresolved_all)} resolvidos, "
          f"{len(unresolved_all)} não-resolvidos")
    if unresolved_all:
        print(f"não-resolvidos: {', '.join(unresolved_all)}")
    print(f"arquivos: {os.path.relpath(OUT_JSON, ROOT)}, "
          f"{os.path.relpath(OUT_CSS, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())