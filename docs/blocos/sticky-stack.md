# Bloco: Sticky Stack

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, motion §4.4, tells §4.1).

## Quando usar

Seções que pinam no topo do viewport e empilham conforme o scroll: storytelling sequencial, "uma ideia por tela" para features, narrativa de processo em fases. Forte para história de produto ou metodologia.

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 7-10 | Cada card empilhado é uma composição própria |
| MOTION_INTENSITY | 6-10 | O pin em si é motion de scroll; requer intenção |
| VISUAL_DENSITY | 2-4 | Uma mensagem por tela; cockpit quebra o ritmo |

**Presets:** agência 9/8/3 · landing de produto narrativo 8/7/3 · editorial longo 7/5/3.

**Não usar:** quando o conteúdo é referência rápida (Operate: scan vence storytelling), com muitos cards (empilhar 6+ telas cansa), em acessibilidade crítica sem reduced-motion bem testado, ou quando o design read não pede narrativa.

## Sketch

```
viewport:  ┌──────────────────┐
           │ CARD 1 (pin)     │ ← sticky top: 0
           │  "Descubra"      │
           └──────────────────┘
scroll →   ┌──────────────────┐
           │ CARD 2 (pin)     │ ← empilha sobre o 1
           │  "Configure"     │
           └──────────────────┘
           ┌──────────────────┐
           │ CARD 3 (pin)     │ ← último: para de pinar
           │  "Cresça"        │
           └──────────────────┘
```

## Componentes do kit reutilizados

- `.card`, `.card__title`, `.card__text`, `.card__footer` (components.css)
- `.badge` (número de etapa como chip discreto, ou sem número: "números de etapa genéricos" são tell §9.F do taste-skill)
- `.btn`, `.btn--primary`, `.btn--ghost`
- `.container` (base.css)

## Esqueleto HTML

```html
<section class="stack" aria-labelledby="stack-titulo">
  <div class="container">
    <h2 id="stack-titulo" class="stack__title">Como funciona</h2>
    <div class="stack__cards">
      <article class="card stack__card">
        <h3 class="card__title">Primeira etapa</h3>
        <p class="card__text">Uma ideia por tela, contada com calma.</p>
      </article>
      <article class="card stack__card">
        <h3 class="card__title">Segunda etapa</h3>
        <p class="card__text">O scroll empilha as ideias como um baralho.</p>
      </article>
      <article class="card stack__card">
        <h3 class="card__title">Terceira etapa</h3>
        <p class="card__text">A última tela para de pinar e libera o resto.</p>
      </article>
    </div>
  </div>
</section>
```

## Esqueleto CSS (CSS puro, sem build: `position: sticky`, zero GSAP)

```css
.stack {
  padding-block: var(--space-20);
}

.stack__title {
  font-size: var(--font-size-h2);
  letter-spacing: var(--letter-spacing-tight);
  line-height: var(--font-line-height-tight);
  margin-bottom: var(--space-10);
  max-width: var(--container-sm);
}

.stack__cards {
  display: grid;
  gap: var(--space-6);
}

.stack__card {
  /* O pin é puro CSS: cada card cola no topo enquanto o próximo sobe.
     O último card não precisa de sticky (não há próximo para empilhar). */
  position: sticky;
  top: var(--space-6);               /* respiro do topo; ajuste p/ nav fixa */
  min-height: 60vh;                  /* presença de tela inteira */
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: var(--space-3);
  padding: var(--space-8) var(--space-10);
}

/* Opcional: escurecer levemente os cards atrás (sem desfocar texto) */
.stack__card:not(:last-child) {
  box-shadow: var(--shadow-md);
}

/* Mobile: o sticky vira empilhamento simples para não roubar a tela */
@media (max-width: 480px) {
  .stack__card {
    position: static;                /* sem pin em telas muito pequenas */
    min-height: auto;
  }
}
```

**Nota sobre `top` e nav fixa:** se a página tem header sticky, use `top: calc(var(--space-6) + <altura do header>)` ou `scroll-margin-top` nos cards. O valor exato depende do header; documente no projeto.

## Fallback mobile (explícito)

- Cards empilham sem pin em < 480px (a tela é pequena demais para o efeito; pin rouba 100% do viewport).
- Em 480-768px o pin pode ficar com `min-height: 50vh` para não cansar.
- `prefers-reduced-motion: reduce` → todos os cards `position: static` (scroll normal, conteúdo completo visível, sem pin). O conteúdo NUNCA pode depender do pin para ser lido.

## Anti-padrões

- **Pin sem reduced-motion**: o pin é motion de scroll; com `reduce` deve virar scroll normal (§4.4).
- **`window.addEventListener('scroll')`** para ativar algo no pin: banido (§4.1). Sticky CSS resolve o pin sem JS.
- **Mais de 4-5 cards**: empilhar vira cansaço. Corte ou converta em marquee/tabs.
- **Cards com conteúdo denso**: uma tela = uma ideia. Tabela dentro de card empilhado é cockapito (use `.table` fora do stack).
- **Números "Etapa 1/2/3" genéricos** como label (§9.F do taste-skill): o título da etapa é o label.
- **Cards idênticos em composição**: cada card empilhado deve ter uma composição própria (variação de título, texto, CTA ou visual), senão é um 3-cards-iguais disfarçado.

## Exemplo real no repo

Sem sticky-stack nos casos atuais (Lumen/Norte usam grid). Este bloco é a referência canônica; implementação em CSS puro `position: sticky` validada por construção (sem GSAP, sem scroll listener), alinhada ao "sem build tooling" do kit.
