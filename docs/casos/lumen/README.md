# Caso Lumen — Prova de conceito do agente de design

> **Fase A** do roadmap (docs/arquitetura-agente-design.md): um caso real de ponta a
> ponta para validar o conceito de "agente que substitui um setor de design".
> Papel executado: **ui-designer** (Fase A), consumindo apenas os tokens do designkit.

## 1. Brief

- **Produto:** Lumen — assistente de foco e bem-estar digital com IA.
- **Público:** profissionais criativos e knowledge workers que se distraem com
  notificações e multitarefa.
- **Proposta:** planeja o dia em blocos de foco, silencia distrações por contexto e
  mede a energia com IA.
- **Tom:** calmo, moderno, premium, acolhedor — nada de gadgets agressivos.
- **Entregável:** landing page responsiva, em HTML/CSS/JS puros, consumindo o design
  system do kit (`styles/tokens.css` + `styles/base.css`), sem build e sem imagens
  externas (SVG inline).

## 2. Decisões de design (10)

1. **Paleta:** somente tokens semânticos do kit — primária índigo para ação/foco,
   neutra slate para superfícies e texto; `--color-success` reservado para o estado
   "distrações silenciadas" (semântica de bem-estar, não de conversão).
2. **Claro/escuro herdado:** a página não define cores de tema; o `data-theme` do kit
   (lido de `localStorage["dk-theme"]`, fallback `prefers-color-scheme`) faz todo o
   trabalho — valida o mecanismo de theming do design system fora do showcase.
3. **Hero com mockup de app em SVG puro:** anel de progresso (42/90 min), curva de
   energia e badge flutuante de pausa — prova que o designkit suporta "UI de produto"
   além de landing, sem assets externos.
4. **Header sticky com blur:** `color-mix()` sobre `--color-bg` com fallback
   `@supports` para navegadores sem suporte — segue o padrão já adotado no kit.
5. **Tipografia:** hierarquia clara via tokens (`--font-size-display` no hero em
   desktop, `h1/h2/h3` nas seções); `--letter-spacing-tight` em títulos grandes para
   o tom "calmo e premium".
6. **Escala de espaçamento 4px:** ritmo vertical consistente (`--space-4/6/8/12/16/20`),
   grid de features em 3 colunas no `lg`, 1 coluna mobile-first.
7. **Raios `--radius-full` em botões** (pill) e `--radius-lg/xl` em cards — contraste
   entre CTA e superfícies de conteúdo.
8. **Elevação sutil:** `--shadow-sm` em repouso → `--shadow-lg` + `translateY(-4px)`
   no hover (spring easing) — profundidade sem peso visual.
9. **Acessibilidade nativa:** skip-link, `aria-labelledby` em todas as seções,
   landmarks (`header/nav/main/section/footer`), foco visível via `--focus-ring` do
   base.css, `prefers-reduced-motion` desativa a animação do badge flutuante.
10. **Zero lorem ipsum:** copy real do produto (hero, 6 features, 3 passos,
    3 depoimentos, CTAs) escrita em pt-BR com tom acolhedor.

## 3. Critique e refine

O caso passou por **duas rodadas** do **design-critic**: a rodada 1 (`critique-report.md`)
resultou em **APROVADO COM RESSALVAS**, média **4.1/5** (clareza 5, hierarquia 5,
consistência 3, affordance 4, a11y 3, responsividade 4, copy 5). A rodada 2
(`critique-report-v2.md`), após o refine, fechou como **APROVADO**, média **4.7/5** —
veredito final do caso. Correções aplicadas no refine:

1. **Tokenização do espaçamento:** valores da escala de 4px substituídos por
   `var(--space-*)` (ex.: `4rem→var(--space-16)`, `1.25rem→var(--space-5)`,
   `2.5rem→var(--space-10)`, `3rem→var(--space-12)`, `40rem→var(--container-sm)`);
   valores off-scale justificados em comentário no CSS (ver §3.2).
2. **Contraste AA no tema claro:** `--color-text-muted` sobre `--color-surface-muted`
   (4.34:1) corrigido nos 3 pontos — chip de tempo agora usa `--color-text-strong`;
   label de energia e texto do CTA final usam `--color-text` (≥ 4.5:1).
3. **Navegação mobile restaurada:** menu colapsável `.menu-toggle`
   (`aria-expanded`/`aria-controls`, fecha em Esc/ao navegar/volta ao desktop).
4. Minors: `scroll-margin-top` inclui `main[id]` (skip-link), foco em pills restaura
   `border-radius: inherit`, CTA final aponta para placeholder `#cadastro`, estado
   acessível do toggle inicializado no bootstrap do `<head>`, `prefers-reduced-motion`
   zerado transforms/transitions/scroll.

### 3.1 Consistência com o kit (regra de tokens)

100% dos valores visuais de **cor/raio/sombra/fonte** vêm de tokens semânticos
(`--color-*`, `--radius-*`, `--shadow-*`, `--font-*`). O **espaçamento** usa a escala
`--space-*`; exceções off-scale estão **documentadas em comentário no CSS** logo acima
do uso, com a justificativa (geometria decorativa/SVG ou medida de leitura):

| Valor | Onde | Justificativa |
|---|---|---|
| `1px` | `.btn:active` | micro-deslocamento de "press" |
| `6px` | `.menu-toggle__line` | metade da distância entre linhas do ícone SVG |
| `12px` | header blur | valor de efeito (vidro), não de espaçamento |
| `88%` | header alpha | transparência intencional do vidro |
| `24rem` / `48rem 20rem` | glow do hero | geometria decorativa do fundo |
| `26rem` | mockup | largura do mockup (proporção de produto) |
| `9rem` | anel de progresso | geometria SVG (2 × raio 52 + stroke) |
| `34rem` | texto do CTA | medida de leitura confortável |
| `326.7` / `173` / `8` | anel | geometria do arco SVG (comentário no CSS) |

> Decisão: não criar tokens novos no `tokens.css` global sem passar por
> `impeccable extract` (fluxo da arquitetura §3) — os off-scale ficam documentados
> localmente até virarem candidatos a token.

## 4. Handoff (spec básico)

- **Cores usadas:** `--color-bg`, `--color-surface`, `--color-surface-muted`,
  `--color-text`, `--color-text-strong`, `--color-text-muted`, `--color-border`,
  `--color-border-strong`, `--color-primary`, `--color-primary-hover`,
  `--color-primary-active`, `--color-on-primary`, `--color-primary-soft`,
  `--color-primary-soft-strong`, `--color-success`, `--color-warning`.
- **Tipografia:** `--font-family-base`, `--font-size-display/h1/h2/h3/h5/h6/small/caption`,
  `--font-weight-semibold/bold`, `--letter-spacing-tight/wide`,
  `--font-line-height-tight/body/relaxed`.
- **Componentes usados (padrões do kit):** botões primário/secundário (pill),
  cards (`--radius-lg`, `--shadow-sm` → `lg` no hover), badges/estados
  (`--radius-full` em chips de tempo), listas de check, avatar de depoimento
  (círculo com iniciais), header sticky + tema claro/escuro.
- **Componentes novos propostos para o kit:** "app mockup card" (anel de progresso
  + sparkline, SVG puro) e "badge flutuante de notificação" — candidatos a
  componentes do design system via `impeccable extract`.
- **Implementação:** `index.html` + `lumen.css` + bootstrap de tema inline
  (mesmo mecanismo `dk-theme` do kit); nenhuma dependência de `js/app.js` da raiz.

## 5. Como abrir

Abra `docs/casos/lumen/index.html` direto no navegador (arquivo local). O tema segue
a preferência do sistema ou o `dk-theme` salvo; o toggle no header alterna e persiste.
O menu colapsável aparece em telas < 768px (`--breakpoint-md`).
