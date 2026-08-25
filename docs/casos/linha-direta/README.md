# Caso Linha Direta - Landing de estúdio de design estratégico

> **Objetivo:** provar o nível ACIMA das skills externas: compor uma página
> inteira com a **block library do próprio kit** (`docs/blocos/`), produzindo
> um resultado que nenhuma skill genérica (impeccable ou design-taste)
> entregaria sozinha: 4 blocos próprios + identidade de marca + validação
> mecânica do detector anti-slop.

## Design Read (1 linha)

**Lendo como:** landing de agência de design estratégico para fundadores e
CMOs, linguagem de estúdio pequeno e feroz, monocromático de grafite frio com
pop âmbar de decisão, tendendo aos tokens do kit (slate + `--color-warning`)
com composição assimétrica deliberada.

## Dials (justificados pelo brief)

| Dial | Valor | Razão |
|---|---|---|
| DESIGN_VARIANCE | 9 | "Pequena e feroz, cara e decisiva" pede assimetria de estúdio criativo: grid 1.4fr/1fr, peça do hero deslocada meio bloco, bento com células de pesos diferentes, faixa de marquee. Nada de simetria de template. |
| MOTION_INTENSITY | 6 | Marquee (o movimento É a banda) + sticky-stack com pin CSS puro. Acima de 6 exigiria física/scroll-hijack que não servem à "decisão" seca do estúdio. |
| VISUAL_DENSITY | 3 | Ar generoso, editorial: cada seção respira. O estúdio vende direção, não densidade de dados. |

## Família estética (fora das proibidas)

**Monocromático de grafite frio + pop âmbar** (variante permitida do DESIGN.md
§4.1, "monocromático + single saturated pop").

- Neutro: slate do kit (fundos, texto, bordas) em quase todos os elementos.
- Accent único: `--color-warning` (âmbar queimado no claro, âmbar claro no
  escuro), reservado aos momentos de decisão: eyebrow, peça do hero, tag dos
  casos, hover da nav e o CTA primário.
- **Não é** bege+latão+oxblood (tell nº 2), **não é** índigo default do kit
  (a agência não quer "mais uma agência roxa"), **não é** gradiente de IA.
- Lock de 1 accent: o âmbar aparece só onde há decisão/ação; o resto é grafite.

## Blocos da block library usados

| Bloco (docs/blocos/) | Seção | Adaptações à identidade |
|---|---|---|
| hero-split-assimetrico.md | Hero | Colunas 1.4fr/1fr (VARIANCE 9, não o 1fr/1fr do bloco); peça deslocada `margin-top: var(--space-16)`; peça é a "linha direta" (reta diagonal + ponto de decisão), não fake screenshot |
| marquee.md | Banda de termos | Máx 1 por página; itens = termos do posicionamento; loop 22s; `prefers-reduced-motion` vira `overflow-x: auto` |
| bento-grid.md | Serviços | 6 células exatas (N itens = N células): herói (Posicionamento, com SVG) ocupa 2 linhas, 1 tinted de âmbar (`--color-warning-soft`), wide com citação real; sem célula vazia |
| sticky-stack.md | Casos | 3 cards que pinam em `top: var(--space-16)` (abaixo do header sticky); composição própria por card (cliente + verbo + resultado); `position: static` em < 480px e reduced-motion |

Seções adicionais com famílias de layout próprias (diversidade §4.5):
manifesto editorial (tipografia pura), método (2 colunas com coluna esquerda
sticky, lista com `border-top` sem hairline em toda linha), CTA final
(editorial, um CTA).

## Conteúdo e marca

> **Ilustrativo:** todos os casos desta página são fictícios (exemplo de demonstração do kit).

- Clientes fictícios com nomes reais de marca em pt-BR: **Mercado Beira**
  (empório), **Atlas Cargo** (logística B2B), **Vereda** (moda). Sem Jane
  Doe, sem Acme, sem números falsos-preciosos (resultados são qualitativos).
- Pessoas com nome real: **Helena Furtado**, CMO do Mercado Beira.
- CTA com UMA intenção e UMA label: "Pedir proposta" (hero, header e CTA
  final) + secundária "Ver o método" (hero). Sem duplicata de intenção.
- Zero em-dash/en-dash em texto visível; zero scroll cues; zero version
  footer; zero eyebrow numerado; zero dots decorativos.

## Decisões de acessibilidade

- Skip-link + `main[id]` com `scroll-margin-top` (não fica sob o header).
- Nav após `.site-header__actions` no DOM (tabulação chega ao painel do menu),
  ordem visual restaurada por `order`.
- Contraste: texto sempre `--color-text` (nunca muted sobre surface-muted);
  CTA âmbar usa `--color-on-primary` (5.0:1 claro, ~10:1 escuro); eyebrow
  âmbar 4.9:1 claro / 13:1 escuro; hero em alto contraste (AAA).
- `prefers-reduced-motion` colapsa marquee (estático rolável), sticky-stack
  (scroll normal) e todas as transições; `prefers-reduced-transparency` dá
  fallback sólido ao header de vidro.
- Mobile: hero empilha, bento empilha, stack perde o pin em < 480px,
  menu vira hambúrguer com `aria-expanded`.
- `min-height: 100dvh` no hero (nunca `h-screen`).

## Auto-avaliação do pre-flight (DESIGN.md §6)

- [x] Design Read declarado e dials explícitos com razão do brief
- [x] Zero em-dash e zero en-dash em texto visível (grep confirmado)
- [x] Theme lock: um tema por página (claro/escuro via dk-theme)
- [x] Color lock: um accent (âmbar) em tudo; Shape lock: raio do kit
- [x] Contraste AA nos botões/body, AAA no hero
- [x] CTA: label não quebra, uma intenção por CTA ("Pedir proposta")
- [x] Hero: headline 1 linha, subtext 14 palavras, CTA visível, 4 elementos,
      padding top 4rem (<= 6rem)
- [x] Eyebrows: 2 em 7 seções (hero + bento) <= ceil(7/3) = 3
- [x] Sem fake screenshots; peça do hero é SVG geométrico real
- [x] Sem scroll cues, version footers, strips decorativos, dots, eyebrows numerados
- [x] Motion motivado (marquee = conteúdo, pin = storytelling),
      só transform/opacity, reduced-motion coberto, sem scroll listener
- [x] Nav 1 linha <= 80px; bento 6 células com variação (herói + tinted);
      zigzag não se aplica (nenhum par imagem+texto repetido)
- [x] Mobile collapse explícito por seção; `min-h-100dvh`
- [x] Estados: loading/empty/error não se aplicam (landing estática; hero não depende de asset externo)
- [x] Copy auditada: zero frases quebradas, zero "elevate/seamless", números honestos (nenhum número falso)
- [x] Dark mode definido e testado nos dois temas (tokens do kit)
- [x] CWV plausíveis: hero SVG inline (LCP rápido), sem imagens externas (CLS 0), sem JS de scroll (INP ok)
- [x] Micro-gaps: `::selection` coerente, i18n pt-BR coeso, 1 família de ícones (SVG inline próprio da marca)
- [x] Detector: `python scripts/smoke-test.py` PASS + `python scripts/anti-slop-check.py` PASS

## Exceções documentadas (constantes de geometria de SVG)

Assim como o anel de progresso no caso Lumen, o SVG do hero usa constantes
de geometria (raio 14/26, `font-size 14`, `letter-spacing 2`, espessuras de
traço) que são parte da peça gráfica, não valores de UI; nenhuma cor é
hardcoded (tudo `var(--color-*)`).

## Validação

- `python scripts/smoke-test.py` → PASS (8 checks)
- `python scripts/anti-slop-check.py` → PASS (84 checks, inclui este caso)
- Tokens usados vs definidos em `styles/tokens.css` → 0 faltando
- `node --check` nos scripts inline do HTML → OK
