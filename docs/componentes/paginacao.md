# Paginação (`.pagination`)

> Grupo 9.5 de `styles/components.css`. Navegação entre páginas de listagens com página atual, reticências, setas e variante compacta. Demo interativa no showcase (JS do demo apenas — o componente é links HTML reais).

## 1. Visão geral

Paginação para listagens paginadas, cobrindo quatro necessidades:

1. **Semântica** — `nav` com `aria-label`; cada página é um link real (`<a>`).
2. **Estado atual** — `aria-current="page"` na página ativa (fundo primário).
3. **Intervalos longos** — reticências (`<span>` não interativo, `aria-hidden`) para omitir páginas.
4. **Densidade** — variante compacta `.pagination--sm` para rodapés de tabelas e listagens densas.

Acessibilidade é responsabilidade do HTML: `aria-current="page"` no link atual, `aria-disabled="true"` em itens sem ação (ex.: seta anterior na página 1), `aria-label` nas setas ícone-only.

## 2. Estrutura e classes

| Classe / atributo | Papel |
|---|---|
| `nav.pagination` | Container semântico (com `aria-label`) |
| `ul.pagination__list` | Lista flex com `gap: var(--space-1)` |
| `li.pagination__item` | Item da lista |
| `a.pagination__link` | Página clicável (pill, borda, hover) |
| `.pagination__link[aria-current="page"]` | Página atual — fundo `--color-primary`, `cursor: default` |
| `.pagination__link[aria-disabled="true"]` | Item sem ação (ex.: seta prev na página 1) |
| `span.pagination__ellipsis` | Reticências visuais (`aria-hidden="true"`, fora da ordem de Tab) |
| `svg.pagination__arrow` | Ícone das setas anterior/próxima |
| `.pagination--sm` | Variante compacta (fonte caption, célula 32px) |
| `p.pagination__status` | (Demo) texto "Página X de Y" com `aria-live="polite"` |

## 3. Exemplo de uso mínimo

```html
<nav class="pagination" aria-label="Paginação de projetos">
  <ul class="pagination__list">
    <li class="pagination__item">
      <a class="pagination__link" href="/projetos?p=2" aria-label="Página anterior">
        <svg class="pagination__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
             aria-hidden="true" focusable="false">
          <polyline points="15 18 9 12 15 6"/>
        </svg>
      </a>
    </li>
    <li class="pagination__item"><a class="pagination__link" href="/projetos?p=1">1</a></li>
    <li class="pagination__item"><a class="pagination__link" href="/projetos?p=2">2</a></li>
    <li class="pagination__item"><a class="pagination__link" href="/projetos?p=3" aria-current="page">3</a></li>
    <li class="pagination__item"><a class="pagination__link" href="/projetos?p=4">4</a></li>
    <li class="pagination__item"><span class="pagination__ellipsis" aria-hidden="true">…</span></li>
    <li class="pagination__item"><a class="pagination__link" href="/projetos?p=40">40</a></li>
    <li class="pagination__item">
      <a class="pagination__link" href="/projetos?p=4" aria-label="Próxima página">
        <svg class="pagination__arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
             aria-hidden="true" focusable="false">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </a>
    </li>
  </ul>
</nav>
```

Variante compacta (rodapé de tabela):

```html
<nav class="pagination pagination--sm" aria-label="Paginação de resultados">
  <ul class="pagination__list">
    <li class="pagination__item"><a class="pagination__link" href="?p=1">1</a></li>
    <li class="pagination__item"><span class="pagination__ellipsis" aria-hidden="true">…</span></li>
    <li class="pagination__item"><a class="pagination__link" href="?p=11">11</a></li>
    <li class="pagination__item"><a class="pagination__link" href="?p=12" aria-current="page">12</a></li>
  </ul>
</nav>
```

## 4. Tokens usados

| Token | Uso |
|---|---|
| `--space-1` / `--space-2` | Gap da lista / padding horizontal do link |
| `--space-10` | Altura e min-width do link (célula 40px) |
| `--space-8` | min-width do ellipsis / célula compacta |
| `--space-6` | min-width do ellipsis compacto |
| `--space-4` | Tamanho do ícone de seta |
| `--radius-full` | Forma pill dos links |
| `--color-surface` / `--color-surface-muted` | Fundo do link / hover e disabled |
| `--color-border` / `--color-border-strong` | Borda / borda no hover |
| `--color-text-strong` / `--color-text-muted` | Texto / itens secundários |
| `--color-primary` / `--color-on-primary` | Página atual (fundo / texto) |
| `--font-size-small` / `--font-size-caption` | Texto normal / compacto |
| `--font-weight-medium` / `--font-weight-semibold` | Peso normal / página atual |
| `--motion-duration-fast` / `--motion-easing-out` | Transição de hover/foco |

## 5. Acessibilidade

- **Semântica:** `nav[aria-label]` envolve a lista; cada página é um link real.
- **Página atual:** `aria-current="page"` — leitores de tela anunciam "página atual"; o CSS dá `cursor: default`.
- **Itens sem ação:** `aria-disabled="true"` (mantém o link na árvore acessível, mas anuncia desabilitado).
- **Setas ícone-only:** `aria-label` ("Página anterior" / "Próxima página") + `aria-hidden` no SVG.
- **Reticências:** `<span aria-hidden="true">` — não é interativo, fica fora da ordem de Tab.
- **Foco:** anel `--focus-ring` em `:focus-visible` (regra global do base.css).
- **Reduced motion:** transições desativadas em `@media (prefers-reduced-motion: reduce)` (seção 9.6 do CSS).

## 6. Pegadinhas

1. **Não usar `button` para páginas** — paginação é navegação; `aria-current="page"` exige link/âncora.
2. **Reticências não são links** — usar `<span>`, nunca `<a href="#">` sem destino; senão o usuário de teclado tabula para um link morto.
3. **`aria-disabled` em vez de `hidden`/remover** — manter o item na árvore mantém o layout estável e a semântica (é uma seta, não uma página que sumiu).
4. **Seta "anterior" desabilitada na página 1** — nunca apontá-la para `?p=0`; use `aria-disabled="true"`.
5. **JS do showcase é só demo** — `initPaginationDemo` atualiza o estado no clique; em produção o estado vem do backend e os links são URLs reais. Não copie o handler para produção.
