# Bloco: Marquee

> Composição de página do Design Kit. Leia `DESIGN.md` antes (dials §2, motion §4.4, tells §4.1).

## Quando usar

Banda de texto (ou logos) em rolagem contínua: palavras-chave, nomes de clientes, termos de posicionamento. Serve para dar ritmo e movimento entre seções, ou para uma lista de logos que não precisa de atenção individual. **Máx 1 por página** (tell: 2+ marquees = filler).

| Dial | Faixa | Nota |
|---|---|---|
| DESIGN_VARIANCE | 3-8 | A banda pode ser alinhada ou ligeiramente inclinada |
| MOTION_INTENSITY | 6-10 | O movimento É o bloco; abaixo de 6 não faz sentido |
| VISUAL_DENSITY | 2-5 | A banda é um intervalo, não um data-dump |

**Presets:** agência 9/8/3 · landing de produto 7/7/4 · manifesto 7/6/3.

**Não usar:** informação que precisa ser lida (marquee não é legível), mais de uma vez por página, em acessibilidade crítica sem pausa, ou com texto longo (uma frase curta por repetição).

## Sketch

```
┌──────────────────────────────────────────────┐
│  ┌─────────────────────────────────────────┐  │
│  │  DESIGN · MOTION · SPATIAL · DESIGN ·  │  │  ← banda
│  │  MOTION · SPATIAL · DESIGN · MOTION     │  │     rolando
│  └─────────────────────────────────────────┘  │     (content × 2
│                                              │      para loop
└──────────────────────────────────────────────┘      perfeito)
```

**Atenção:** a banda NÃO é o stripe decorativo proibido no rodapé do hero (§4.1). O marquee é um bloco próprio entre seções com conteúdo real (termos do posicionamento, nomes de clientes), não um enfeite colado no hero.

## Componentes do kit reutilizados

- `.container` (base.css)
- Opcional: `.badge` se a banda alterna texto com chips
- Nenhum outro componente: a banda é tipografia pura

## Esqueleto HTML

```html
<section class="marquee" aria-label="Termos do posicionamento">
  <div class="marquee__track">
    <ul class="marquee__list">
      <li>Design</li>
      <li>Tipografia</li>
      <li>Sistemas</li>
      <li>Interação</li>
      <li>Identidade</li>
    </ul>
    <!-- O mesmo <ul> repetido para o loop sem costura -->
    <ul class="marquee__list" aria-hidden="true">
      <li>Design</li>
      <li>Tipografia</li>
      <li>Sistemas</li>
      <li>Interação</li>
      <li>Identidade</li>
    </ul>
  </div>
</section>
```

## Esqueleto CSS (CSS puro, sem build)

```css
.marquee {
  overflow: hidden;                  /* corta a banda nas bordas */
  padding-block: var(--space-6);
  border-block: 1px solid var(--color-border);
  background-color: var(--color-surface-muted);
}

.marquee__track {
  display: flex;
  width: max-content;                /* deixa a banda crescer além da tela */
  /* Loop sem costura: -50% relativo ao TRACK (duas listas = 2W) = uma lista
     inteira (W). Se a animação ficasse na lista, -50% = meia lista e a
     costura apareceria no ciclo (bug conhecido deste bloco). */
  animation: marquee-scroll var(--motion-duration-slow) linear infinite;
  animation-duration: 20s;           /* velocidade por conteúdo; ajuste fino */
}

.marquee__list {
  display: flex;
  gap: var(--space-12);
  padding-right: var(--space-12);
  list-style: none;
  margin: 0;
  white-space: nowrap;
}

.marquee__list li {
  font-size: var(--font-size-h5);
  font-weight: var(--font-weight-semibold);
  letter-spacing: var(--letter-spacing-wide);
  color: var(--color-text-strong);
}

/* Loop perfeito: -50% do TRACK (duas listas idênticas) = uma lista inteira */
@keyframes marquee-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

/* Reduced motion: banda estática, sem loop (§4.4) */
@media (prefers-reduced-motion: reduce) {
  .marquee__track {
    animation: none;
  }
  .marquee {
    overflow-x: auto;                /* rolagem manual se precisar */
  }
}
```

## Fallback mobile (explícito)

- `gap` reduz para `--space-8` e `font-size` para `--font-size-h6` em telas < 640px (a banda não deve estourar a leitura).
- Com `prefers-reduced-motion`, a banda vira `overflow-x: auto` (rolável por gesto, sem movimento automático).
- Se o conteúdo for logos com `alt` descritivo, a segunda lista repetida usa `aria-hidden="true"` (já no HTML acima) para não duplicar leitura de tela.

## Anti-padrões

- **2+ marquees por página**: tell §4.1 e §4.4 (marquee max-one-per-page).
- **Marquee com texto longo**: uma frase curta por repetição; nada de parágrafos rolantes.
- **Marquee como stripe decorativo do hero**: o stripe no rodapé do hero é proibido; o marquee é bloco próprio entre seções.
- **Costura visível no loop**: animar a LISTA com `translateX(-50%)` desloca só meia lista (o percentual é relativo ao próprio elemento), e o ciclo salta. A animação deve estar no TRACK (duas listas = 2W; -50% = uma lista inteira W). Ver esqueleto CSS acima.
- **Sem reduced-motion**: banda automática sem pausa/estático viola §4.4 (motion > 3 obriga reduce).

## Exemplo real no repo

`docs/casos/linha-direta/` usa este bloco (banda de termos do posicionamento, loop no track com -50%, reduced-motion vira rolagem manual). Casos Lumen/Norte/Aurora não usam marquee. Este bloco é a referência canônica: CSS puro com `@keyframes` + `transform` no track (única propriedade animada, §4.4), loop sem costura, e `prefers-reduced-motion` coberto.
