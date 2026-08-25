# Bloco: Bento Grid

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, §4.3 bento, tells §4.1).

## Quando usar

Grade assimétrica de células de tamanhos variados para apresentar features, serviços, capacidades ou conteúdos em um grid tipo Apple Control Center. Funciona quando os itens têm pesos visuais diferentes (um é o herói, os outros apoiam).

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 6-9 | Grids fracionários 2fr/1fr, células de tamanhos mistos |
| MOTION_INTENSITY | 3-7 | Reveal com stagger leve; nada de tilt 3D por padrão |
| VISUAL_DENSITY | 2-5 | Células respiram; densidade só se o conteúdo pede |

**Presets:** landing mainstream 7/6/4 · agência 9/8/3 · produto premium 7/6/3.

**Não usar:** 3 features iguais (vira 3 cards iguais, tell §4.1: use lista ou zigzag), dados de tabela densa (use `.table`), quando o conteúdo é homogêneo (células iguais não são bento, são grid comum).

## Sketch

```
┌─────────────────┬──────────────────────────┐
│ CÉLULA HERO     │ Célula B                │
│ (2 linhas de    │ (feature com imagem)    │
│  altura)        ├──────────────────────────┤
│  imagem/visual  │ Célula C (texto curto)   │
├─────────────────┴──────────────────────────┤
│ Célula D (largura cheia, citação ou CTA)   │
└────────────────────────────────────────────┘
   N itens → N células. Nunca célula vazia.
   2-3 células com variação visual real.
```

## Componentes do kit reutilizados

- `.card`, `.card--interactive`, `.card__title`, `.card__text`, `.card__footer` (components.css)
- `.badge`, `.badge--primary` (se precisar de chip)
- `.btn`, `.btn--ghost` (CTA dentro de célula)
- `.container` (base.css)

## Esqueleto HTML

```html
<section class="bento" aria-labelledby="bento-titulo">
  <div class="container">
    <h2 id="bento-titulo" class="bento__title">Como entregamos</h2>
    <div class="bento__grid">
      <article class="card bento__cell bento__cell--hero">
        <h3 class="card__title">Feature principal</h3>
        <p class="card__text">O que ela faz, em 1-2 frases.</p>
        <div class="bento__visual" aria-hidden="true">
          <!-- SVG ou imagem real da feature -->
        </div>
      </article>

      <article class="card bento__cell">
        <h3 class="card__title">Feature B</h3>
        <p class="card__text">Uma frase.</p>
      </article>

      <article class="card bento__cell bento__cell--tinted">
        <h3 class="card__title">Feature C</h3>
        <p class="card__text">Uma frase.</p>
        <span class="badge badge--primary">Novo</span>
      </article>

      <article class="card bento__cell bento__cell--wide">
        <p class="bento__quote">"Citação curta, até 3 linhas."</p>
        <div class="card__footer">
          <a class="btn btn--ghost" href="#cta">Ver tudo</a>
        </div>
      </article>
    </div>
  </div>
</section>
```

## Esqueleto CSS (CSS puro, sem build)

```css
.bento {
  padding-block: var(--space-20);
}

.bento__title {
  font-size: var(--font-size-h2);
  letter-spacing: var(--letter-spacing-tight);
  line-height: var(--font-line-height-tight);
  margin-bottom: var(--space-10);
  max-width: var(--container-sm);
}

.bento__grid {
  display: grid;
  grid-template-columns: 1fr;        /* mobile-first */
  gap: var(--space-4);
}

.bento__cell {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  min-height: 12rem;                 /* célula mínima respirável */
}

.bento__visual {
  margin-top: auto;
  display: flex;
  justify-content: center;
  padding: var(--space-4);
  background-color: var(--color-surface-muted);
  border-radius: var(--radius-md);
}

.bento__quote {
  font-size: var(--font-size-h5);
  line-height: var(--font-line-height-relaxed);
  color: var(--color-text-strong);
  max-width: var(--container-sm);
}

/* Desktop: grid fracionário assimétrico (VARIANCE 7) */
@media (min-width: var(--breakpoint-md)) {
  .bento__grid {
    grid-template-columns: 1.4fr 1fr; /* hero mais largo que os apoios */
  }
  .bento__cell--wide {
    grid-column: 1 / -1;
  }
  .bento__cell--hero {
    grid-row: span 2;
  }
}

/* Reveal com stagger (MOTION 5): só transform/opacity, §4.4 */
@media (prefers-reduced-motion: no-preference) {
  .bento__cell {
    animation: bento-in var(--motion-duration-slow) var(--motion-easing-out) both;
    animation-delay: calc(var(--bento-i, 0) * var(--motion-duration-fast));
  }
  @keyframes bento-in {
    from { opacity: 0; transform: translateY(var(--space-4)); }
    to   { opacity: 1; transform: none; }
  }
  /* defina --bento-i via style="--bento-i:1" por célula, ou JS simples */
}
```

## Fallback mobile (explícito)

- `grid-template-columns: 1fr` empilha todas as células; o herói perde o destaque de tamanho, então garanta que o conteúdo (título + visual) sustente sozinho.
- `min-height: 12rem` vira `min-height: auto` se o conteúdo for curto (use `@media (max-width: ...)` com `min-height: 0` quando o texto for 1 linha).
- Stagger desligado via `prefers-reduced-motion` (o animation é removido, sem delay fantasma).

## Anti-padrões

- **Célula vazia**: bento tem EXATAMENTE N células para N conteúdos (§4.3). Replaneje o grid, não cole um tile em branco.
- **6 células brancas só com texto**: pelo menos 2-3 células com variação visual real (imagem, gradiente de marca contido, fundo tinted) (§4.3).
- **Repetição de layout**: uma página com bento NÃO usa outro bento em outra seção (regra de diversidade §4.5).
- **Raios misturados**: célula usa `--radius-md` do `.card`; botão pill usa `--radius-full`. Shape lock do kit: documente a regra e siga (§3).
- **Célula clicável sem affordance**: se a célula é link, use `.card--interactive` com hover/focus do kit, não um card comum.

## Exemplo real no repo

Sem bento nos casos atuais (Lumen usa split + 3-col, Norte usa tabela). Este bloco é a referência canônica para quando o brief pedir grid assimétrico; valide com o design-critic antes de shipar (o critique verifica "bento com N células e variação visual" no pre-flight §6).
