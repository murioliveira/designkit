# Bloco: Hero Manifesto Editorial

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, hero discipline §4.2, tells §4.1).

## Quando usar

Hero sem asset: a tipografia É a peça visual. Quase-pôster. Usar quando a mensagem é o design: manifesto, lançamento, editorial, estudo criativo, posicionamento de marca. O texto lidera, o fundo recua.

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 5-8 | Assimetria de margem e quebra de linha controlada |
| MOTION_INTENSITY | 2-5 | Entrada tipográfica sutil; nada de scramble/kinetic por padrão |
| VISUAL_DENSITY | 1-3 | Ar de galeria; espaço negativo é a mensagem |

**Presets:** editorial 6/4/3 · manifesto/launch 7/5/2 · estudio criativo 8/6/2.

**Não usar:** produto com asset forte (use o split), dashboard/app (Operate: densidade e scan, não manifesto), quando o cliente precisa ver o produto no primeiro viewport.

## Sketch

```
┌──────────────────────────────────────────┐
│                                          │
│   UMA FRASE                              │
│   QUE VIRA                                │
│   PÔSTER.                                │  ← tipografia display,
│                                          │     até 2-3 linhas
│   Parágrafo curto, 65ch.                 │     no viewport
│                                          │
│   [CTA primária]                         │
│                                          │
│   (fundo: cor sólida ou gradiente        │
│    de marca muito contido, nunca         │
│    roxo de IA)                           │
└──────────────────────────────────────────┘
```

## Componentes do kit reutilizados

- `.btn`, `.btn--primary`, `.btn--ghost` (components.css)
- `.container` (base.css)
- `.sr-only` / `.skip-link` (base.css + layout.css)
- Tema: `[data-theme]` + bootstrap inline (padrão dos casos)

## Esqueleto HTML

```html
<main id="main">
  <section class="manifesto-hero" aria-labelledby="manifesto-titulo">
    <div class="container manifesto-hero__inner">
      <p class="eyebrow">Manifesto</p>
      <h1 id="manifesto-titulo" class="manifesto-hero__title">
        Design é linguagem, não decoração
      </h1>
      <p class="manifesto-hero__lead">
        O que move uma tela é a intenção por trás de cada decisão, não o ornamento.
      </p>
      <div class="manifesto-hero__actions">
        <a class="btn btn--primary btn--lg" href="#cta">Ler o manifesto</a>
      </div>
    </div>
  </section>
</main>
```

## Esqueleto CSS (CSS puro, sem build)

```css
.manifesto-hero {
  padding-block: var(--space-24) var(--space-20);
  min-height: 100dvh;               /* nunca h-screen: §4.1 */
  display: flex;
  align-items: center;
  background-color: var(--color-bg);
}

.manifesto-hero__inner {
  max-width: var(--container-md);
}

.eyebrow {
  color: var(--color-primary);
  font-size: var(--font-size-caption);
  font-weight: var(--font-weight-semibold);
  letter-spacing: var(--letter-spacing-wide);
  text-transform: uppercase;
  margin-bottom: var(--space-6);
}

.manifesto-hero__title {
  font-size: var(--font-size-display);
  letter-spacing: var(--letter-spacing-tight);
  line-height: var(--font-line-height-tight);
  max-width: 12ch;                  /* pôster: headline curta e forte */
  font-weight: var(--font-weight-bold);
  text-wrap: balance;               /* quebra equilibrada, sem <br> */
}

.manifesto-hero__lead {
  margin-top: var(--space-6);
  font-size: var(--font-size-h6);
  line-height: var(--font-line-height-relaxed);
  color: var(--color-text);
  max-width: var(--container-sm);
}

.manifesto-hero__actions {
  margin-top: var(--space-10);
}

/* Desktop: headline cresce, margem esquerda assimétrica (VARIANCE 7) */
@media (min-width: var(--breakpoint-md)) {
  .manifesto-hero__inner {
    margin-left: var(--space-10);   /* assimetria deliberada, não central */
  }
  .manifesto-hero__title {
    font-size: clamp(var(--font-size-h1), 8vw, 6rem);
  }
}

/* Entrada tipográfica (MOTION 4): só transform/opacity, §4.4 */
@media (prefers-reduced-motion: no-preference) {
  .manifesto-hero__title {
    animation: manifesto-in var(--motion-duration-slow) var(--motion-easing-out) both;
  }
  @keyframes manifesto-in {
    from { opacity: 0; transform: translateY(var(--space-6)); }
    to   { opacity: 1; transform: none; }
  }
}
```

## Fallback mobile (explícito)

- `clamp(..., 8vw, ...)` ajusta a escala em telas médias; abaixo de `--breakpoint-md` usa `--font-size-display` fixo e a headline fica ≤ 3 linhas.
- Se a headline virar 4+ linhas no mobile, reduza a fonte (nunca encurte a copy por aqui: a copy curta é obrigação do design read).
- `text-wrap: balance` é progressive enhancement; sem suporte, a quebra natural ainda funciona.

## Anti-padrões

- **Eyebrow em toda seção**: este hero conta como 1 eyebrow; as próximas 2 seções não podem ter (§4.1).
- **`<br>` forçado + itálico** para "parecer design": banido (§9.F do taste-skill). A headline lê natural primeiro.
- **Textura/gradiente roxo de IA** no fundo: banido (§4.1).
- **Scroll cue** ("Scroll para ver"): banido (§4.1). O usuário sabe rolar.
- **Stripe decorativo** no rodapé do hero ("BRAND. MOTION. SPATIAL."): banido (§4.1).
- **Manifesto para produto SaaS mainstream**: se o brief é produto com valor de asset, use o split; manifesto aqui seria fuga.

## Exemplo real no repo

`docs/casos/aurora/` seção `.manifesto` (ateliê de cerâmica): bloco editorial com `border-top: 1px solid var(--color-border)`, título em `--font-size-h2` e copy em 65ch, voz da marca sustentada do hero ao rodapé. Use como referência de tom, não de escala (o hero manifesto é maior).
