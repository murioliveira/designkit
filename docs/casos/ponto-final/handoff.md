# Handoff - Farol (spec: card de livro)

> Skill: `design-handoff` · Entrada: `ui.md` + `critique.md` + `refine.md` + `a11y.md` + `styles/tokens.css` · Saída: spec de 1 tela (card de livro) pronta para o dev implementar sem adivinhar.

## Tela: Card de livro (Catálogo e Vitrine) · Prioridade: P0

**Objetivo:** o livreiro reconhece um título à primeira vista (capa, autor, editora, preço) e pode selecioná-lo para a vitrine com um toque, mesmo de pé no balcão (tablet).

**Layout:** grid de cards (`grid` do kit, `gap: var(--space-4)`) dentro do container; 1 coluna no mobile, 2-3 no tablet (`--breakpoint-md/lg`), 4 no desktop. Cada card ocupa o espaço de um título real.

## Componentes usados

| Componente | Variante | Estados |
|---|---|---|
| `card` | `card--interactive` | hover (eleva) · focus `--focus-ring` · selected com `aria-pressed` + bordo accent |
| `badge` | estado (novidade/atraso) | neutro; sucesso/warning só para estado real |
| `btn` | `btn--sm` (ações inline) | hover · focus `--focus-ring` · disabled (sem ações) |

## Tokens aplicados

| Categoria | Tokens |
|---|---|
| Cor | `--color-surface` (fundo do card), `--color-surface-muted` (área de capa), `--color-text` (título), `--color-text-muted` (autor/editora/preço secundário), `--color-text-strong` (preço principal), `--color-primary` (bordo selecionado/destacado), `--color-primary-soft` (fundo selecionado), `--color-border` |
| Tipografia | `--font-size-h4` (título do livro), `--font-size-small` (autor/editora), `--font-size-body` (preço), `--font-weight-semibold` (título), `--font-weight-bold` (preço), `--font-line-height-tight` (título) |
| Espaço/raio/sombra | `--space-3`/`--space-4` (padding interno), `--space-2` (gap capa/título), `--radius-md` (card), `--radius-full` (badge), `--shadow-sm` (card em repouso), `--shadow-md` (hover/elevado) |
| Motion/z | `--motion-duration-fast` (hover/selected), `--motion-duration-base` (transição de estado) |
| Breakpoints | `--breakpoint-sm/md/lg/xl` (colunas do grid) |

## Estados e bordas

- **Empty (catálogo vazio):** card com "Nenhum título aqui ainda" + CTA "Trazer catálogo" (`btn--primary`).
- **Selected:** card com borda `--color-primary` + fundo `--color-primary-soft` + `aria-pressed="true"`.
- **Loading:** skeleton no formato do card (capa + 2 linhas) durante a importação/filtro.
- **Erro (capa não carrega):** área de capa com `--color-surface-muted` + texto "capa indisponível" em `--color-text-muted` (nunca quebrar o layout).

## A11y (herdado do `a11y-auditor`)

- Contraste AA: texto do card nos dois temas; badge com texto forte (não o tom de estado como cor de texto).
- Foco: `--focus-ring` no card inteiro; card selecionável por Tab + Enter/Espaço (`aria-pressed`, role check).
- Alvo de toque ≥ 44×44: o card INTEIRO é o alvo (requisito major do critique, aplicado no refine).
- `prefers-reduced-motion`: transições de hover/selected abreviadas sob a media query (regra do DESIGN.md §4.4).

## Dependências

- Capa do livro: imagem fornecida pelo catálogo do distribuidor; fallback (área `--color-surface-muted` + label) quando ausente.
- Preço: dado do catálogo ou definido pelo livreiro na seleção.

## Proposta nova (não aplicável)

Nenhum componente novo: o kit cobre o card de livro com `card--interactive` + badges. **[proposta - não há]**

## Checklist de aceite (dev)

- [ ] Funcional: selecionar título com 1 toque no tablet, desmarcar, ver preço
- [ ] Estados: vazio/erro/carregando/selecionado
- [ ] Visual: 100% tokens (grep por `#hex` = zero)
- [ ] Responsivo: sm (1 col) / md-lg (2-3) / xl (4)
- [ ] A11y: AA, foco no card, teclado, alvo ≥ 44×44
- [ ] Motion: `prefers-reduced-motion` respeitado