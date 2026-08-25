# Documentação de componentes — Design Kit

> Handoff por grupo de componentes. Fonte: `styles/components.css` (9 seções reais), `styles/tokens.css`, `index.html` (playgrounds) e `js/app.js` (interações). Última revisão: 2026-08-25.

## Índice

| Doc | Grupo | Resumo |
|---|---|---|
| [botoes.md](./botoes.md) | Botões | `.btn` + 4 variantes (`--primary`, `--secondary`, `--ghost`, `--danger`), 3 tamanhos, estados (hover/active/focus/disabled) e loading com spinner CSS puro. |
| [badges-cards-alerts.md](./badges-cards-alerts.md) | Badges, cards e alertas | Rótulos de status/contagem (ponto semântico AA), superfícies de conteúdo com elevação, e feedback contextual com barra de acento e fechamento animado. |
| [formularios.md](./formularios.md) | Formulários | Campo completo (`label`+controle+`hint`+erro), inputs/textarea/select, checkbox/radio customizados, toggle switch, validação no submit com `aria-invalid`. |
| [overlays.md](./overlays.md) | Overlays e feedback | Tooltip JS, modal com trap de foco, tabs WAI-ARIA, progress determinado/indeterminado, skeleton e avatar com status dot. |
| [dropdown.md](./dropdown.md) | Dropdown | Menus de ações e select-like em popup, com teclado completo (setas, Home/End, Esc, clique fora) e item destrutivo/checkmark. |
| [breadcrumb.md](./breadcrumb.md) | Breadcrumb | Trilha de navegação com separador via CSS (não textual) e item atual `aria-current="page"`; link truncado com ellipsis. |
| [tabela.md](./tabela.md) | Tabela | Dados tabulares com zebra, números tabulares, header fixo em container de rolagem e estado vazio com `colspan`. |
| [stepper.md](./stepper.md) | Stepper | Progresso por etapas (done/active/upcoming) com conector visual; variantes horizontal e vertical. |
| [paginacao.md](./paginacao.md) | Paginação | Navegação entre páginas com `aria-current="page"`, reticências não interativas, setas com `aria-label` e variante compacta. |

## Convenções comuns a todos os grupos

- **Tokens:** todo valor visual vem de `var(--...)` de `styles/tokens.css` — nunca hex/valor mágico. A paleta bruta (`--c-*`) só é consumida pelos tokens semânticos, não por componentes.
- **Tema:** claro/escuro automático via tokens semânticos; nenhum componente duplica regras por tema.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` desativa transições/animações (seções 7 e 8.7 do CSS); o spinner desacelera em vez de parar.
- **Foco:** anel `--focus-ring` em `:focus-visible` em todos os interativos; nunca `outline: none` sem substituto.
- **Interação:** os componentes com JS são inicializados pelo `js/app.js` em `DOMContentLoaded` (veja a lista de `init*()` no topo do arquivo).
