# Bloco: Galeria Experience

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, modo Experience §1, tells §4.1).

## Quando usar

Curadoria para portfólios, galerias, vitrines, estúdios: as peças lideram desde o primeiro viewport, a interface recua ao mínimo. Cada item é uma obra (imagem, projeto, peça) e a página é a moldura. O modo Experience do kit (DESIGN.md §1) trata como disciplina de curadoria sobre Persuade: menos chrome, mais obra.

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 8-10 | Composição de galeria: assimetria, tamanhos mistos, respiro |
| MOTION_INTENSITY | 4-8 | Hover com leve zoom na peça; revelação de legenda |
| VISUAL_DENSITY | 1-3 | Ar de galeria; cada peça respira |

**Presets:** portfolio de estúdio 9/7/2 · portfolio dev 6/5/4 · vitrine de produto 8/6/3.

**Não usar:** quando o conteúdo é informação (Read/Operate), quando não há peças visuais reais (texto puro não é galeria), em página de produto (o produto merece split), ou quando o cliente não tem assets (evite fake screenshots de div: §4.1).

## Sketch

```
┌────────────────────────────────────────────────┐
│  (header mínimo, navegação discreta)           │
│                                                │
│  ┌─────────────┐  ┌─────────────────┐          │
│  │ peça 1      │  │ peça 2          │          │
│  │ (maior)     │  │                 │          │
│  └─────────────┘  └─────────────────┘          │
│                                                │
│  ┌─────────────────┐  ┌─────────────┐          │
│  │ peça 3          │  │ peça 4      │          │
│  │                 │  │ (menor)     │          │
│  └─────────────────┘  └─────────────┘          │
│                                                │
│  (rodapé mínimo)                               │
└────────────────────────────────────────────────┘
   Grade assimétrica 2 colunas com alturas mistas.
   Hover: zoom sutil na peça + legenda revelada.
```

## Componentes do kit reutilizados

- `.btn`, `.btn--ghost` (CTA discreto de contato)
- `.container` (base.css)
- `.sr-only` / `.skip-link` (base.css + layout.css)
- Nenhum card: as peças NÃO são cards (o card adicionaria chrome que o modo Experience remove)

## Esqueleto HTML

```html
<main id="main">
  <section class="gallery" aria-labelledby="gallery-titulo">
    <div class="container">
      <h1 id="gallery-titulo" class="sr-only">Trabalhos selecionados</h1>

      <div class="gallery__grid">
        <figure class="gallery__item gallery__item--wide">
          <img class="gallery__media"
               src="https://picsum.photos/seed/ateliê-1/1200/800"
               alt="Peça 1: descrição real do trabalho"
               loading="lazy" width="1200" height="800">
          <figcaption class="gallery__caption">
            <span class="gallery__title">Nome do projeto</span>
            <span class="gallery__meta">Categoria, ano</span>
          </figcaption>
        </figure>

        <figure class="gallery__item">
          <img class="gallery__media"
               src="https://picsum.photos/seed/ateliê-2/800/1000"
               alt="Peça 2: descrição real do trabalho"
               loading="lazy" width="800" height="1000">
          <figcaption class="gallery__caption">
            <span class="gallery__title">Nome do projeto</span>
            <span class="gallery__meta">Categoria, ano</span>
          </figcaption>
        </figure>

        <!-- repita com proporções variadas -->
      </div>
    </div>
  </section>
</main>
```

## Esqueleto CSS (CSS puro, sem build)

```css
.gallery {
  padding-block: var(--space-20) var(--space-24);
}

.gallery__grid {
  display: grid;
  grid-template-columns: 1fr;        /* mobile-first */
  gap: var(--space-8);
}

.gallery__item {
  position: relative;
  margin: 0;                         /* reset do <figure> */
  overflow: hidden;                  /* corta o zoom do hover */
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-muted);
}

.gallery__media {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 3;               /* proporção base; variar por item */
  object-fit: cover;
  transition: transform var(--motion-duration-base) var(--motion-easing-out);
}

.gallery__caption {
  position: absolute;
  inset-inline: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  padding: var(--space-6);
  background: linear-gradient(to top, var(--color-bg) 0%, transparent 100%);
  color: var(--color-text-strong);
}

.gallery__title {
  font-size: var(--font-size-h6);
  font-weight: var(--font-weight-semibold);
}

.gallery__meta {
  font-size: var(--font-size-caption);
  color: var(--color-text);
}

/* Desktop: grade assimétrica (VARIANCE 8) */
@media (min-width: var(--breakpoint-md)) {
  .gallery__grid {
    grid-template-columns: 1.2fr 1fr; /* coluna da esquerda mais larga */
  }
  .gallery__item--wide {
    grid-column: 1 / -1;             /* peça de abertura em largura total */
  }
}

/* Hover: zoom sutil na peça + legenda (MOTION 6), §4.4 */
@media (hover: hover) and (prefers-reduced-motion: no-preference) {
  .gallery__item:hover .gallery__media {
    transform: scale(1.03);          /* só transform, §4.4 */
  }
}

@media (prefers-reduced-motion: reduce) {
  .gallery__media {
    transition: none;
  }
}
```

## Fallback mobile (explícito)

- Grade 1 coluna, peças em largura total.
- A legenda em gradiente funciona em touch (sempre visível, não só no hover; o gradiente garante contraste em qualquer posição da imagem).
- `loading="lazy"` + `width`/`height` (reserva de espaço = CLS < 0.1, §6 do DESIGN.md).
- `aspect-ratio` mantém o layout estável antes da imagem carregar.

## Anti-padrões

- **Fake screenshots de div**: cada peça é uma obra real (imagem/SVG). Divs retangulares "simulando" peças = tell §4.1.
- **Cards em volta das peças**: card adiciona borda/sombra/chrome; Experience pede moldura mínima. Peça + legenda basta.
- **Scroll cues** ("Role para ver"): banido §4.1.
- **Chrome pesado**: nav gigante, footer com newsletter, sidebars. Experience = navegação mínima e discreta (§1).
- **Eyebrow em cada peça**: uma seção de galeria é 1 seção; eyebrows em excesso violam §4.1.
- **Hover sem fallback touch**: se a legenda só aparece no hover, usuário touch perde a informação. Sempre visível em mobile.

## Exemplo real no repo

Sem galeria Experience nos casos atuais (Lumen é Persuade, Norte é Operate). Este bloco é a referência canônica para o 4º modo; combine com o header mínimo do Aurora (`.site-header` com apenas marca + CTA discreto) como moldura.
