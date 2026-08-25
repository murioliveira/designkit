# Block Library - Design Kit

> Composições de página reutilizáveis do Design Kit. Cada bloco combina as classes reais de `styles/components.css` com CSS puro de composição (sem build, sem dependências). Leia `DESIGN.md` antes de usar: dials §2, tells §4, pre-flight §6.
>
> Fonte: `styles/components.css`, `styles/tokens.css`, casos reais `docs/casos/` (Lumen, Norte, Aurora). Última revisão: 2026-08-25.

## Índice

| Bloco | Dials compatíveis (V/M/D) | Quando usar | Componentes do kit reutilizados |
|---|---|---|---|
| [Hero Split Assimétrico](hero-split-assimetrico.md) | 6-9 / 3-7 / 2-5 | Landing com asset forte: texto à esquerda, peça visual à direita | `.btn`, `.btn--primary`, `.btn--ghost`, `.container`, `.theme-toggle` |
| [Hero Manifesto Editorial](hero-manifesto-editorial.md) | 5-8 / 2-5 / 1-3 | A tipografia é a peça: manifesto, lançamento, estúdio criativo | `.btn`, `.btn--primary`, `.container` |
| [Bento Grid](bento-grid.md) | 6-9 / 3-7 / 2-5 | Features/capacidades com pesos visuais diferentes, grid assimétrico | `.card`, `.card--interactive`, `.badge`, `.badge--primary`, `.btn` |
| [Sticky Stack](sticky-stack.md) | 7-10 / 6-10 / 2-4 | Storytelling sequencial: cards que pinam e empilham no scroll | `.card`, `.card__title`, `.card__text`, `.btn` |
| [Marquee](marquee.md) | 3-8 / 6-10 / 2-5 | Banda de texto/logos em rolagem contínua (máx 1 por página) | `.container` (tipografia pura) |
| [Galeria Experience](galeria-experience.md) | 8-10 / 4-8 / 1-3 | Modo Experience: peças lideram, chrome mínimo (portfólios, vitrines) | `.btn`, `.btn--ghost`, `.container` (sem cards) |

## Como escolher

1. **Leia o brief e declare o Design Read** (DESIGN.md §2): tipo de página + audiência + vibe.
2. **Ajuste os dials** com razão do brief (baseline 8/6/4, presets no DESIGN.md §2).
3. **Cruze com a tabela acima**: cada bloco declara faixas compatíveis de VARIANCE/MOTION/DENSITY.
4. **Não misture blocos repetidos**: diversidade de layout (DESIGN.md §4.5) exige ≥ 4 famílias em uma página de 8 seções.
5. **Rode o pre-flight** (DESIGN.md §6) e o `scripts/smoke-test.py` antes de shipar.

## Regras de composição

- **Zero hex**: todo esqueleto usa `var(--token)` de `styles/tokens.css`. Hex novo = falha de pre-flight.
- **Zero em-dash**: o caractere travessão longo (U+2014) e o en-dash (U+2013) são proibidos em qualquer texto visível dos blocos e das páginas.
- **Mobile-first**: todo esqueleto começa em 1 coluna e expande via `@media (min-width: ...)` com os breakpoints do kit (`--breakpoint-md/lg/xl`).
- **Motion só transform/opacity** + `prefers-reduced-motion` (DESIGN.md §4.4). Nenhum bloco usa JS de scroll (`window.addEventListener('scroll')` é banido).
- **Sem build**: CSS puro, sem GSAP/Motion/Three.js. O kit roda direto no navegador.

## Validação

- `scripts/smoke-test.py` valida integridade do kit (tokens, hex, HTML, CSS, docs, skills, casos).
- Cada bloco foi conferido contra os tokens reais do kit (todos os `var(--...)` citados existem em `styles/tokens.css`) e contra as classes reais de `styles/components.css`.
- Exemplos reais citados: `docs/casos/aurora/` (hero split + manifesto), `docs/casos/lumen/` (split), `docs/casos/norte/` (dashboard, Operate).
