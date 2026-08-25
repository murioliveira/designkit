# Bloco: Hero Split Assimétrico

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, hero discipline §4.2, tells §4.1).

## Quando usar

Hero de persuasão com texto à esquerda e peça visual à direita, com espaço generoso e assimetria deliberada. O hero é o padrão para landing pages com um asset forte (produto, peça, imagem) e uma mensagem forte.

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 6-9 | Split 50/50 deslocado (6) até colunas fracionárias 2fr/1fr (9) |
| MOTION_INTENSITY | 3-7 | Reveal suave de entrada; física magnética só se > 5 |
| VISUAL_DENSITY | 2-5 | Ar é a mensagem; nunca cockpit |

**Presets:** landing mainstream 7/6/4 · premium consumer 7/6/3 · agência criativa 9/8/3.

**Não usar:** editorial/manifesto (use o bloco manifesto), serviço público trust-first (variação baixa, use split alinhado com simetria), quando o asset é mais fraco que o texto (o manifesto vence).

## Sketch

```
┌────────────────────────────────────────────────┐
│  [eyebrow]                                     │
│  Headline grande                              │  ← coluna esquerda
│  em 2 linhas                                  │     max-width 34rem
│                                              │
│  Subtexto ≤ 20 palavras                       │
│  [CTA primária] [CTA ghost]                   │
│                     ┌──────────────────┐       │
│                     │  peça visual     │       │  ← coluna direita
│                     │  (SVG/imagem)    │       │     largura 26rem
│                     └──────────────────┘       │
└────────────────────────────────────────────────┘
     mobile: empilha, peça abaixo do texto
```

## Componentes do kit reutilizados

- `.btn`, `.btn--primary`, `.btn--ghost`, `.btn--lg` (components.css)
- `.sr-only` / `.sr-only-focusable` / `.skip-link` (base.css + layout.css)
- `.container` (base.css)
- Toggle de tema: `.theme-toggle` (se o layout tiver tema) + bootstrap de tema inline no `<head>` (padrão dos casos)

## Esqueleto HTML

```html
<header class="site-header">
  <div class="container site-header__inner">
    <a class="site-header__brand" href="#main">Marca</a>
    <div class="site-header__actions">
      <a class="btn btn--primary btn--sm" href="#cta">Começar</a>
    </div>
  </div>
</header>

<main id="main">
  <section class="hero" aria-labelledby="hero-titulo">
    <div class="container hero__grid">
      <div class="hero__content">
        <p class="eyebrow">Label curto</p>
        <h1 id="hero-titulo" class="hero__title">Headline em até 2 linhas</h1>
        <p class="hero__lead">Subtexto curto, até 20 palavras, direto ao valor.</p>
        <div class="hero__actions">
          <a class="btn btn--primary btn--lg" href="#cta">Ação principal</a>
          <a class="btn btn--ghost btn--lg" href="#como">Saber mais</a>
        </div>
      </div>
      <div class="hero__visual" aria-hidden="true">
        <svg class="hero__piece" viewBox="0 0 400 400" role="img" aria-label="Peça do produto">
          <!-- SVG do produto: usar a silhueta real, nunca divs retangulares -->
        </svg>
      </div>
    </div>
  </section>
</main>
```

## Esqueleto CSS (CSS puro, sem build)

```css
.hero {
  padding-block: var(--space-16) var(--space-20); /* top ≤ 6rem: regra §4.2 */
  min-height: 100dvh;              /* nunca h-screen: §4.1 */
  display: flex;
  align-items: center;
}

.hero__grid {
  display: grid;
  grid-template-columns: 1fr;      /* mobile-first */
  gap: var(--space-12);
  align-items: center;
}

.hero__content {
  max-width: var(--container-md);
}

.eyebrow {
  color: var(--color-primary);
  font-size: var(--font-size-caption);
  font-weight: var(--font-weight-semibold);
  letter-spacing: var(--letter-spacing-wide);
  text-transform: uppercase;
  margin-bottom: var(--space-4);
}

.hero__title {
  font-size: var(--font-size-display);   /* 56px; display só com headline curta */
  letter-spacing: var(--letter-spacing-tight);
  line-height: var(--font-line-height-tight);
  max-width: 14ch;                        /* força a quebra em ≤ 2 linhas */
}

.hero__lead {
  margin-top: var(--space-6);
  font-size: var(--font-size-h6);
  line-height: var(--font-line-height-relaxed);
  color: var(--color-text);
  max-width: var(--container-sm);
}

.hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  margin-top: var(--space-8);
}

.hero__visual {
  display: flex;
  justify-content: center;
  padding: var(--space-6);
}

.hero__piece {
  width: 100%;
  max-width: 26rem;
}

/* Desktop: split assimétrico (VARIANCE 7) */
@media (min-width: var(--breakpoint-md)) {
  .hero__grid {
    grid-template-columns: minmax(0, 1fr) minmax(0, 26rem);
    gap: var(--space-16);
  }
  .hero__title {
    font-size: var(--font-size-display);
  }
}

/* Entrada com reveal (MOTION 6): só transform/opacity, §4.4 */
@media (prefers-reduced-motion: no-preference) {
  .hero__content {
    animation: hero-in var(--motion-duration-slow) var(--motion-easing-out) both;
  }
  @keyframes hero-in {
    from { opacity: 0; transform: translateY(var(--space-4)); }
    to   { opacity: 1; transform: none; }
  }
}
```

## Fallback mobile (explícito)

- Colunas empilham: `grid-template-columns: 1fr` já é o default (mobile-first).
- `.hero__title` volta para `--font-size-h1` se `--font-size-display` estourar em telas < 400px (teste: headline não pode virar 4 linhas; se virar, baixa a escala, nunca corta a copy).
- CTA wrap em `flex-wrap`; labels nunca quebram em 2 linhas (regra CTA §4.3).
- `min-height: 100dvh` evita salto de layout no iOS (barra de endereço).

## Anti-padrões

- **Headline em 4 linhas**: erro de escala de fonte, não de copy. Reduza para `--font-size-h1` ou encurte.
- **3 elementos de texto extras** (eyebrow + tagline + trust strip): o hero tem máx 4 elementos de texto (§4.2). Trust strip vai DEBAIXO do hero.
- **Fake screenshot de div** no lugar do asset: banido (§4.1). Use SVG real, imagem gerada, ou nada.
- **`h-screen`**: causa salto no mobile. Use `100dvh`.
- **Padding top > 6rem**: conteúdo flutua no meio do viewport; parece bug.
- **Gradiente roxo de IA** como fundo do hero: banido (§4.1).

## Exemplo real no repo

`docs/casos/aurora/` (hero split do ateliê de cerâmica, aprovado no pre-flight anti-slop 14/14). A peça é um SVG de vaso com `role="img"` e `aria-label`, o eyebrow diz "Ateliê de cerâmica artesanal" e o CTA é "Ver a coleção" (uma intenção, sem duplicata).
