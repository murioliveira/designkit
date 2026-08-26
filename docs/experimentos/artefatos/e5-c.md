# Auditoria E5-c — Landing "Draftly" (método C · design-taste)

**Input auditado:** `docs/experimentos/artefatos/e1-c.html` (landing E1 "Draftly", gerada pelo método C / design-taste)
**Data:** 2026-08-26 · **Método:** design-taste (skill `~/.pi/agent/skills/design-taste/SKILL.md`) — pre-flight §14 + tells §9.G + WCAG 2.2 AA
**Modo:** inspeção estática read-only. **Não editei a página.**

---

## 0. Design Read (do corridor C, verificado)

"Lendo como: landing SaaS para freelancers individuais, tom calmo/ferramental/confiável, tendendo a CSS nativo honesto + accent único teal + sistema-ui." Dials declarados: VARIANCE 6 · MOTION 4 · DENSITY 3 — coerentes com o brief E1 ("calmo, ferramental, não-babar").

---

## 1. Anti-slop — scan do pre-flight §14 (design-taste)

| Check | Resultado | Nota |
|---|---|---|
| Em-dash `—` | **0** | ✅ ZERO — §9.G cumprido |
| En-dash `–` | **0** | ✅ ZERO |
| Inter como fonte | **0** (falsos positivos = `IntersectionObserver` em JS) | ✅ usa system-ui stack, sem Inter |
| Gradiente roxo de IA | **0** | ✅ accent único teal-700 `--accent:#0f766e` |
| 3 cards idênticos | **Não** | ✅ bento assimétrico: `tile-wide` + `tile-dark` + 2 tiles — layout e copy distintos |
| Scroll cues | **0** | ✅ |
| Version footer (v0.6/build) | **0** | ✅ footer limpo: © 2026 Draftly |
| Eyebrows (uppercase tracking) | **1** (só o hero) | ✅ dentro do limite (ceil(7 seções/3)=3) — §eyebrow restraint |
| Nomes genéricos (Jane/Acme/Lorem) | **0** | ✅ nomes reais pt-BR: Beatriz Lopes, Thiago Almeida, Larissa Costa |
| Fake screenshot de div | **Não** | ✅ o `.preview` é um mini-componente funcional real (rows com valores tabular-nums + total R$ 9.800 coeso), não divs desenhados como painel fake |
| Filler verbs ("elevate/seamless") | **0** | ✅ copy concreta ("Fecha proposta, assina e cobra") |
| Números falsos-preciosos (99.99%) | **0** | ✅ preços reais (R$ 29/49/99) e valores coerentes |
| Marquee, dots decorativos, locale strip | **0** | ✅ |
| Color lock (1 accent em tudo) | **✅** | ✅ teal único na página inteira |
| Shape lock | **✅** | ✅ documentada: botões pill, cards/inputs 14px |

**Veredito anti-slop: PASS.** Zero tells de §9.G. Uma das landing mais limpas do experimento — claramente submetida ao pre-flight do taste.

---

## 2. A11y — WCAG 2.2 AA

### Pontos fortes (verificados)
- **Landmarks/semântica:** `lang="pt-BR"` ✅, `<main id="principal">` ✅, skip-link real → `#principal` ✅, 2 `<nav aria-label>` ✅, hierarquia h1→h2 correta (1 h1, 5 h2 por seção).
- **Contraste (calculado, todos AA com folga):**

| Par | Ratio | AA |
|---|---|---|
| texto stone-900 / bg stone-50 | 16.74:1 | ✅ |
| text-soft stone-700 / bg | 9.84:1 | ✅ |
| muted stone-600 (hero-meta 14px) / bg | 7.30:1 | ✅ |
| accent teal-700 / bg (links/eyebrow) | 5.24:1 | ✅ |
| btn-primary branco text / teal-700 | 5.47:1 | ✅ |
| accent-ink branco / teal-800 | 7.58:1 | ✅ |
| dark: text #f5f5f4 / #0c0a09 | 18.11:1 | ✅ |
| dark: accent #14b8a6 / #0c0a09 | 7.94:1 | ✅ |

- **Imagens a11y:** 0 `<img>` sem alt (SVGs decorativos com `aria-hidden` + `focusable` herdado). ✓
- **Teclado:** 0 `tabindex>0`; menu mobile com `aria-expanded`/`aria-controls` corretos; toggle atualiza `aria-label` via JS. ✓
- **Reduced motion:** `.reveal` colapsa sob `prefers-reduced-motion: reduce` (opacidade 1, sem transição, scroll-behavior auto). ✓
- **Estados:** botões com `:hover`/`:active` (scale .98); CTAs com labels não quebrando; sem CTA wrapping.

### Achados (menores, não bloqueiam)

**P2 · Sem `aria-labelledby` nos títulos de seção** — 6 seções têm `<h2>` mas NENHUMA usa `aria-labelledby` ligando o h2 à section de landmark (só `#recursos`/`#como-funciona`/`#precos`/`#crie-conta` têm id, mas sem `aria-labelledby`; `.clients` usa `aria-label`). Leitores de tela ainda navegam por h2 (hierarchy bem feita), mas rotular landmarks via `aria-labelledby` melhoraria a navegação por região. *Correção: `aria-labelledby="titulo-recursos"` etc.* Esforço S.

**P3 · Sem `:focus-visible` explícito** — a página não define a pseudo-classe; usa o anel de foco padrão do navegador (aceitável, mas sem polimento de `--accent`). *Opcional.*

**P3 · `plan-featured` (fundo `--text` #1c1917, texto `--bg` #fafaf9)** — contraste 16.74:1 invertido, ✅ AA, mas o `li::before` dot usa `--accent-strong` (#115e59) sobre fundo escuro → é decorativo, não texto; conferível em browser (AA gráfico ≥3:1, ~4:1 estimado, dentro). OK como está.

**Nota informal:** `aria-label` fixo "Prévia do produto..." no `.preview` — aceitável para SR, mas o botão "Assinar contrato" dentro não tem `aria` ligando — comportamento padrão OK.

---

## 3. Pre-flight §14 — itens aplicáveis conferidos

- Brief/design read declarado ✅ · dials explícitos com razão ✅ · diz respeito a landing (Persuade, dentro do escopo do taste) ✅
- Zero `—`/`–` em texto visível ✅ · Theme lock (um tema — claro/escuro via media, sem inverter por seção) ✅ · Color lock (teal único) ✅ · Shape lock (documentado) ✅
- Button contrast (5.47:1) ✅ · CTA não quebra ✅ · hero: subtext 20 palavras (≤20), 2 CTAs visíveis, ≤4 elementos ✅
- Split-header banido (hero é split válido com preview real à direita, não "headline+explainer solto") ✅
- "Usado por" logo wall DEBAIXO do hero, com marcas SVG (não wordmark puro) ✅ · Logo-only (sem label categoria) ✅
- Motion motivado (reveal = hierarquia) + reduced-motion ✅ · marquee 0 ✅ · nav 1 linha ≤80px (64px) ✅
- Sem fake screenshot ✅ · imagens reais: usa mini-componente real (não picsum, mas não há foto exigida no brief) ✅
- Real design system: não se aplica (brief bespoke) → CSS nativo honesto, comentado ✅

---

## 4. Veredito

**APROVADO (método C).** Anti-slop: **PASS** — zero tells §9.G (em-dash 0, sem Inter, sem gradiente roxo, sem 3 cards iguais, sem fake screenshot, sem scroll cue, sem version footer, nomes reais pt-BR). A11y: **PASS com 1 P2 e 2 P3** (menores, não bloqueiam). Contraste CAA em todos os pares-chave (claro e escuro). A landing é genuinamente anti-slop e acessível — o pre-flight do design-taste foi aplicado e cumpriu.

**Observação de método C:** o taste proíbe em-dash e fake screenshot de forma rígida e a página obedece 100%. A única lacuna (P2 de aria-labelledby) é um refinement de a11y que o taste (foco em anti-slop visual/estética) não cobre — consistente com o escopo da skill.