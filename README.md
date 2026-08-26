# Design Kit: an entire design department in a box

[![Version](https://img.shields.io/badge/version-v0.9.0-blue)](https://github.com/murioliveira/designkit/releases/tag/v0.9.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Agents](https://img.shields.io/badge/agents-Claude_Code_%7C_Codex_%7C_pi-orange)
![Checks](https://img.shields.io/badge/QA-98_anti--slop_checks-success)

> **v0.9.0** (pre-1.0) · A package that turns any AI agent (Claude, Codex, pi) into a working design department: research, information architecture, UI, critique, accessibility, and developer handoff. No design team required.

**In one line:** you bring the idea. The agent designs it, critiques its own work, and only delivers what passes quality control.

🌐 Leia em português: [README.pt-BR.md](README.pt-BR.md)

---

## What it is

**Design Kit** is a **design system** (tokens + components) plus **packaged agent skills** plus **onboarding files** (`AGENTS.md` / `CLAUDE.md`) that turns any host agent (Claude, Codex, pi, Cursor) into an **entire design department**. Instead of hiring (or being) the designer, the implementer, and the reviewer, you talk to your agent and it runs the complete cycle: from a one-sentence idea to screens ready for development, with critique and an accessibility audit in between.

The **human stays the director**: you decide what gets made and approve at two mandatory checkpoints (before screens are built, and before handoff). The **agent acts as the department**: it executes, reviews its own work in closed loops, and moves forward only when no blockers remain.

One **honest limit**: primary research with real people (interviews, usability tests, analytics data) is **not replaced**. The agent structures, synthesizes, and transforms what you provide, and marks anything missing as `[assumption]`. What it replaces is the *execution* of design.

## How it works

The agent walks through a design department workflow, phase by phase, with two human approval checkpoints:

```
brief → research → concept/IA → ⏸️ YOU APPROVE → UI v1 → critique → refine
→ a11y/QA → ⏸️ YOU APPROVE → handoff
```

- **Closed quality loops:** critique and a11y fix, then re-review, then move on (max 2 refine rounds before escalating to you).
- **Consistency by tokens:** every generated UI consumes **only** `var(--...)` from `styles/tokens.css`. No magic colors, spacing, or radii. New patterns become new tokens in the kit.
- **Anti-slop by default:** `DESIGN.md` encodes the house method (built on the `impeccable` and `design-taste` skills): banned AI tells, three dials set per brief, hard locks on theme/accent/radius, and a final pre-flight checklist.
- **Impeccable floor:** semantic HTML, WCAG AA contrast, visible focus, keyboard support, mobile-first, zero lorem ipsum.

## What's inside

| Layer | Contents | Where |
|---|---|---|
| **Design system** | ~150 tokens (color, typography, spacing, radius, shadow, motion, z-index), light/dark; components: buttons, badges, cards, alerts, forms, tooltip, modal, tabs, progress, skeleton, avatar, dropdown, breadcrumb, table, stepper, pagination | `styles/`, `index.html` (live showcase, 14 sections) |
| **8 skills** | `design-researcher`, `information-architect`, `ui-designer`, `design-redesign`, `design-critic` (enriched scoring + cognitive load), `design-refine`, `a11y-auditor`, `design-handoff`. Original skills ship with SKILL.md + templates; wrappers carry embedded fallbacks so nothing breaks outside pi | `skills/` |
| **Design voice** | `DESIGN.md`: the kit's anti-slop manual (AI tells, dials, locks, redesign protocol, external design system map, pre-flight checklist) | root |
| **Deterministic QA** | `smoke-test.py`: 8 integrity checks · `anti-slop-check.py`: 98 mechanical checks across 14 files (em-dash, hardcoded hex, Inter defaults, eyebrow abuse, generic names, banned palettes, scroll cues) | `scripts/` |
| **Templates** | `brief.md`, `critique-report.md`, `spec-handoff.md` | `templates/` |
| **Validated cases** | Lumen landing (critique 4.7/5) · Norte dashboard (4.6/5, reuses 12 component groups from the kit) · Brisa (research-to-handoff flow) · Aurora (anti-slop reference, 14/14 checks) · Linha Direta (block library in practice) · Redesign Demo (skill-driven before/after) · Tereza Vilela (Experience mode portfolio) | `docs/casos/` |
| **Portability** | `CLAUDE.md` + `.claude/skills/` (Claude Code), `.codex/README.md` (Codex) | root, `.claude/`, `.codex/` |
| **Docs** | Agent architecture, human usage guide, per-component handoff docs, release checklist. Internal docs are currently written in Portuguese (pt-BR) | `docs/` |

## Install (como o /impeccable — via npx, GitHub como registry)

```bash
# Instala as 8 skills do Design Kit nos seus agentes de IA
# (Claude Code, Codex, Cursor e 15+ agentes; universal + symlink p/ Claude Code)
npx skills add murioliveira/designkit
```

Via npm (biblioteca CLI):

```bash
npm i -g design-kit        # depois:
npx design-kit install     # instala as 8 skills nos agentes
npx design-kit verify      # confere
```

*(O pacote já está pronto no repo; `npm i design-kit` funciona quando publicado no registry. O caminho `npx skills add` é imediato, sem depender de publicação npm.)*

## Quickstart

The package is a directory of skills plus an onboarding file. Hand it to your agent and it starts acting as the design department. No build step.

### In pi (recommended starting point)

```bash
# 1. Copy the skills where pi discovers them
cp -r skills/ ~/.pi/agent/skills/designkit/
# 2. Run pi inside the designkit directory (it reads AGENTS.md)
pi
```

### In Claude Code

```bash
# Open Claude Code at the designkit root. It reads CLAUDE.md and
# discovers skills in .claude/skills/ automatically
claude
```

### In Codex (OpenAI)

```bash
# Open Codex at the designkit root. It reads AGENTS.md (native format).
# Skills live in skills/ and are read during flow steps (see .codex/README.md)
codex
```

> **Portability:** the same skill directory works across all three agents; the only adaptation is the onboarding file (`AGENTS.md` ↔ `CLAUDE.md`). See `docs/guia-de-uso.md` for the full walkthrough.

## Example prompts

```text
Create a landing page for my product: a meal-planning app for people who
live alone. Audience: young adults (25 to 35) who rarely cook and order
takeout often. Tone: calm and welcoming, none of that startup hype.
```

```text
Critique the screen below. Tell me what is confusing, what works, and give
me a prioritized list of fixes.

[paste your HTML/CSS here, or describe the screen in detail]
```

```text
Audit this signup form for accessibility and fix everything below WCAG AA.
```

```text
Generate the handoff spec for the landing page we approved: everything the
developer needs to implement it, component by component, using the
designkit tokens.
```

## Roadmap

| Phase | Status |
|---|---|
| **1–2. Foundation + shell**: tokens, base, showcase | ✅ |
| **3. Agent architecture**: 8 department functions mapped to roles, roadmap A–F | ✅ |
| **4. Components**: advanced groups included (dropdown, breadcrumb, table, stepper, pagination) | ✅ |
| **A. Proof of concept**: Lumen case end-to-end, critique approved | ✅ |
| **B. Original skills**: researcher, IA, redesign, refine, handoff + wrappers | ✅ |
| **C. Onboarding + orchestration**: AGENTS.md, DESIGN.md, CLAUDE.md, .codex, usage guide | ✅ |
| **D. Component docs + block library** | ✅ |
| **E p1/p2. Multi-agent portability**: validated statically + live on pi | ✅ |
| **F. Distribution**: published on GitHub, tagged v0.9.0 | ✅ |
| **E p3. Runtime validation** on Claude Code and Codex | ⬜ (gates 1.0.0) |
| **Founder decisions**: target agents, research scope, images, license confirmation, product name | ⬜ (gate 1.0.0) |

## Live showcase

Run the design system showcase (tokens, components, demos):
- **Local:** open `index.html` in your browser (no build, no dependencies)
- **GitHub Pages:** `https://murioliveira.github.io/designkit/` (after enabling Pages under Settings → Pages → Deploy from branch → main/(root), or via the workflow in `.github/workflows/pages.yml`)

## Contributing / repository layout

```
designkit/
├── AGENTS.md / CLAUDE.md      ← agent onboarding (the design department)
├── DESIGN.md                  ← design voice: anti-slop manual
├── index.html                 ← live showcase (14 sections)
├── styles/
│   ├── tokens.css             ← single source of visual truth (light/dark)
│   ├── base.css               ← reset + utilities
│   ├── layout.css             ← showcase shell
│   └── components.css         ← components (9 CSS section groups)
├── js/app.js                  ← theme, mobile menu, scrollspy, demos
├── scripts/
│   ├── smoke-test.py          ← 8 integrity checks
│   └── anti-slop-check.py     ← deterministic AI-tell detector (98 checks)
├── docs/
│   ├── arquitetura-agente-design.md   ← agent architecture
│   ├── guia-de-uso.md                 ← human usage guide
│   ├── distribuicao.md                ← v1.0.0 release checklist
│   ├── blocos/                        ← block library (compositions + dials)
│   ├── componentes/                   ← handoff docs per group
│   ├── casos/                         ← 7 validated real cases
│   └── trend-critiques.md             ← critique history (department memory)
├── skills/                    ← the department roles (SKILL.md + templates)
├── templates/                 ← brief, critique-report, spec-handoff
├── .claude/skills/            ← discovery wrappers (Claude Code)
└── .codex/                    ← portability notes (Codex)
```

Working rules (details in `AGENTS.md`): tokens as the single source of truth; one writer per file; no build tooling; closed quality loops.

> **Language note:** the interface-facing files above are bilingual-ready; deeper internal docs (`docs/`, `skills/`, case studies) are currently written in Brazilian Portuguese.

## License

**MIT** (placeholder pending founder confirmation before v1.0.0; see `docs/distribuicao.md`).

---

📖 Este projeto também existe em português: [README.pt-BR.md](README.pt-BR.md)
