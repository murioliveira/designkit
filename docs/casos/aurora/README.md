# Caso Aurora e Cinza - Referência anti-slop do Design Kit

> **Objetivo do caso:** provar o método novo do kit (DESIGN.md) na prática: uma landing
> de marca premium que NÃO parece feita por IA. Papel executado: **ui-designer**
> (método impeccable + design-taste). Consome apenas os tokens de `styles/tokens.css`.

## 1. Brief

- **Marca:** Aurora e Cinza - ateliê de cerâmica artesanal (louças utilitárias, porcelana e cerâmica decorativa).
- **Público:** consumidores de design (arquitetos, colecionadores, chefs), sensíveis a materialidade e processo.
- **Tom:** calmo, tátil, artesanal; a mão do ceramista é o argumento.
- **Entregável:** landing responsiva em HTML/CSS/JS puros, sem build, sem assets externos (SVG inline + slots de foto marcados).

## 2. Design Read e dials

**Design Read (1 linha):**
> Lendo como: landing premium de ateliê de cerâmica para consumidores de design, com linguagem editorial calma e materialidade tátil, tendendo a monocromático de pedra com um único pop de accent (índigo do kit), motion contido.

**Dials (justificados pelo brief, NÃO baseline):**

| Dial | Valor | Razão |
|---|---|---|
| DESIGN_VARIANCE | **6** | Assimetria controlada: grid de coleção com células de larguras variadas (wide/padrão/retrato) e processo desalinhado (célula do meio desce). Não é caos de galeria (9-10): a marca é calma. |
| MOTION_INTENSITY | **3** | Motion mínimo e funcional: hover/active em botões e toggle, hambúrguer que vira X. Sem reveal on scroll, sem física, sem marquee. O produto é a peça, não a animação. |
| VISUAL_DENSITY | **2** | Galeria: seções espaçadas (padding-block 5rem), uma peça por célula com respiro, quotes com hairlines em vez de cards. A coleção precisa de ar para respirar. |

## 3. Família estética (anti-tell nº 2)

**Monocromático de pedra + pop índigo.** Deliberadamente DIFERENTE da paleta
bege+latão+oxblood que a IA alcança por padrão em briefs de "premium consumer"
(cookware, artesanato, wellness). Aqui:

- **Base:** slate frio do kit (osso/pedra) via `--color-bg`, `--color-surface`, `--color-surface-muted`.
- **Tinta:** grafite via `--color-text` / `--color-text-strong`.
- **Único accent:** índigo do kit (`--color-primary`) em CTAs, links, eyebrows e nas peças de porcelana em SVG (fill `--color-primary-soft`). Um accent, usado na página inteira (color lock).
- **Contraste de materialidade:** o frio da pedra contra o pop índigo comunica "ateliê contemporâneo", não "loja de artesanato rústico".

Por que não bege+latão: é o tell nº 2 do DESIGN.md. Por que não serifa: o DESIGN.md
desaconselha serifa por padrão ("creative brief = serif" é tell); a voz editorial aqui
vem da escala tipográfica (display 56px no hero) e do tracking apertado, não da família.

## 4. Decisões de design (10)

1. **Família estética monocromática de pedra + pop índigo** (acima): um accent em tudo, zero bege/brass/oxblood.
2. **Hero split assimétrico** (conteúdo | peça em SVG): headline ≤ 2 linhas ("Cerâmica que nasce da mão, não da máquina."), subtext 14 palavras, 1 CTA primário + 1 secundário (intenções distintas: ver coleção / conhecer processo), padding top 4rem (≤ 6rem), zero scroll cue, zero logo wall no hero.
3. **Manifesto editorial**: tipografia como voz, coluna estreita (max-width 40rem), sem imagem e sem split-header (headline + parágrafo empilhados).
4. **Coleção em grid assimétrico**: células de larguras variadas (4/2 colunas no desktop), cada peça com SVG próprio (silhuetas de porcelana) ou slot de foto; NENHUM trio de cards iguais.
5. **Processo desalinhado**: 3 células com a do meio deslocada 2rem (ritmo, não erro), cada uma com visual distinto (SVG do torno, SVG do forno, slot de foto da esmaltação); nomes em verbo-nome ("Moldar", "Queimar", "Esmaltar"), sem "Etapa 1/2/3" (tell banido).
6. **Depoimentos com hairlines**: quotes ≤ 3 linhas com atribuição nome + papel (arquiteta/colecionador/chef), separadas por border-top fina, sem cards e sem estrelas (sem dots decorativos).
7. **Imagens honestas**: 3 SVGs inline de peças + 3 slots `<!-- TODO: foto real ... -->` onde a fotografia faria o trabalho (bule, cumbuca, esmaltação); declarado aqui como "imagens a gerar/prover" (conforme DESIGN.md §4.8: nunca fake screenshot de div).
8. **Reuso do kit**: `components.css` linkado para `.btn` (primário/secundário), `base.css` para skip-link/container/sr-only, tokens para tudo; zero CSS de componente reimplementado.
9. **Acessibilidade**: skip-link, `aria-labelledby` em todas as seções, `role="img"` + `aria-label` nas peças SVG e slots de foto, foco visível (pills restauram `--radius-full`), `prefers-reduced-motion` zera transforms/transitions, nav mobile com padrão disclosure (aria-expanded/aria-controls, Esc fecha).
10. **Tema claro/escuro herdado**: mesmo bootstrap `dk-theme` do caso Lumen (auto-contido no head), toggle com `aria-pressed`; a página não define cores de tema (valida o theming do kit).

## 5. Tokens propostos para extract (candidatos)

A página usa 100% dos tokens existentes. Para a identidade futura da marca (quando o
fundador aprovar), estes candidatos a tokens novos deveriam passar por
`impeccable extract` antes de entrar no `tokens.css`:

| Token proposto | Valor proposto | Uso | Status |
|---|---|---|---|
| `--c-forest-600` | verde argila (ex.: `#4d7c4f`) | accent alternativo da marca (família "forest") | candidato, não aplicado |
| `--color-accent-soft` | derivado do accent | fundo soft de peças em destaque | candidato, não aplicado |
| `--border-width-thin` | `1px` | espessura de borda (hoje literal em vários pontos do kit) | candidato, não aplicado |
| `--space-28` / `--space-32` | `7rem` / `8rem` | seções de galeria mais altas | candidato, não aplicado |

**Regra respeitada:** nenhum hex ou valor novo foi inventado no CSS do caso; os
candidatos ficam só nesta tabela até o fluxo de extract (arquitetura §3).

## 6. Auto-avaliação contra o pre-flight (DESIGN.md §6)

- [x] Design Read declarado e dials explícitos com razão do brief (6/3/2)
- [x] **Zero `-` e zero `-`** em todo texto visível (grep nos arquivos, 0 ocorrências)
- [x] Theme lock: um tema por página (claro/escuro via `[data-theme]`, sem inversões de seção)
- [x] Color lock: um accent (índigo) em tudo; Shape lock: raios do kit (md em botões, lg em células, full em pills)
- [x] Contraste AA: texto `--color-text` sobre `--color-bg` (13:1), muted só em metadados pequenos; hero em AAA (headline `--color-text-strong` 15:1)
- [x] CTA: labels não quebram ("Ver a coleção", "Falar com o ateliê"), uma intenção por CTA (browse / learn / contact distintos)
- [x] Hero: headline 2 linhas, subtext 14 palavras, CTA visível sem scroll, 4 elementos (eyebrow + título + lead + ações), padding top 4rem
- [x] Eyebrows: 2 (hero + coleção) ≤ ceil(6 seções/3) = 2
- [x] Sem fake screenshots de div; SVGs reais + slots de foto marcados e declarados
- [x] Sem scroll cues, version footer, strips decorativos, dots decorativos, eyebrows numerados
- [x] Motion motivado (hover/active/toggle), só transform/opacity, reduced-motion coberto, sem `window scroll` listener
- [x] Nav em 1 linha no desktop, altura 4rem (≤ 80px); zigzag 0 (nenhum split repetido); células com variação visual real (SVG / slot de foto)
- [x] Mobile collapse explícito (grid 1 coluna, nav colapsável); hero `min-height: 100dvh` (nunca h-screen)
- [x] Estados: loading/empty/error não se aplicam (landing sem forms; notado como N/A)
- [x] Copy auditada: nomes reais de ceramistas e papéis (Duarte, Andrade, Prado), zero "elevate/seamless", números honestos ("mil e duzentos graus" é processo real de queima de cerâmica)
- [x] Dark mode definido (herdado do kit) e funcionando nos dois modos

## 7. Como abrir

Abra `docs/casos/aurora/index.html` direto no navegador. O tema segue `dk-theme`
salvo ou a preferência do sistema; o toggle alterna e persiste. O menu colapsável
aparece abaixo de 768px.

## 8. O que falta (honesto)

- **Fotografias reais**: 3 slots marcados no HTML (bule, cumbuca, esmaltação) precisam de fotos do ateliê; os SVGs das outras peças são representações de linha, não substituem a fotografia de produto.
- **Re-critique pelo design-critic** (agora com a heurística "Anti-slop" no scoring) e a11y-auditor em profundidade antes de considerar o caso fechado.
