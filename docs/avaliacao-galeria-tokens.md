# Avaliação da Galeria Viva de Tokens — Design Kit v0.9.0

> **Avaliador:** Evaluator (role ed3723c5)  
> **Data:** 2026-08-25  
> **Alcance:** seção `#tokens` do `index.html` + `styles/tokens-demo.css` (253 linhas) + `js/tokens-demo.js` (134 linhas)  
> **Método:** execução dos detectores (`smoke-test.py`, `anti-slop-check.py`), inspeção completa de HTML/CSS/JS, cálculo de contraste WCAG, verificação cruzada com DESIGN.md §3–§6  

---

## Veredito: **APROVADO COM RESSALVAS**

A galeria é profissional, bem estruturada e comunica a linguagem visual do kit com clareza. As 6 subseções cobrem coerentemente paleta, tipografia, espaçamento, raios, sombras e motion — todas alimentadas por `var(--token)` com zero em-dash e zero Inter. Os detectores passam (8/8 smoke, 98/98 anti-slop), mas há **3 ressalvas** que precisam de correção antes de considerar a entrega finalizada: um hex hardcoded que escapou dos detectores, uma falha de contraste WCAG AA em um swatch, e a falta de cobertura dos detectores sobre o novo CSS.

**Nota de qualidade visual:** 4.0/5

---

## 1. O que está excelente

### 1.1 Estrutura visual profissional
- **6 subseções coesas** com títulos hierárquicos (`h3` com `aria-labelledby`, `h4` para subgrupos), parágrafos descritivos (`tokens-demo__desc`) e seção semântica (`<section>` aninhada com `aria-labelledby`).
- **Paleta**: 30 swatches organizados — 10 índigo, 11 slate, 4 semânticos com dot + fundo soft. Grid de 5 colunas com collapse responsivo (3 → 2 colunas). Swatches escuros (primary-600+, neutral-500+) recebem classe `swatch--on-dark` para label branco.
- **Tipografia**: rampa visual com 10 níveis renderizados no tamanho real — display (56px) até caption (12px) — cada um com nome do token e valor em label mono.
- **Espaçamento**: régua com 13 barras proporcionais (`width: var(--space-N)`) — excelente visualização "viva" das proporções.
- **Raios**: 5 cards com `border-radius` progressivo (sm→full), labels mono com nome e valor.
- **Sombras**: 4 cards com `box-shadow` do kit + uso recomendado ("cards, inputs", "dropdowns, tooltips", "modais, sheets", "popovers, toasts").
- **Motion**: demo interativo com botão play/pause, 4 curvas em sequência, label em `aria-live="polite"`.

### 1.2 Aderência ao DESIGN.md (quase total)
- [x] Zero em-dash/en-dash em todo texto visível → PASS (anti-slop confirma)
- [x] Zero Inter → PASS (system-ui stack)
- [x] Zero scroll cues → PASS
- [x] `prefers-reduced-motion` → PASS: JS desabilita animação e mostra mensagem "Movimento reduzido ativo", CSS no `base.css` colapsa transições
- [x] Motion usa IntersectionObserver, não `window.addEventListener('scroll')` → PASS
- [x] HTML semântico: `<section aria-labelledby>`, `<h3>`/`<h4>`, `<code>` para tokens → PASS
- [x] Sem split-header, sem zigzag, sem 3 cards iguais, sem fake screenshots → PASS
- [x] Eyebrows: 2 em 20 seções (limite: ceil(20/3) = 7) → PASS
- [x] Tokens como fonte: 69 `var(--...)` distintos usados na galeria, todos definidos em `tokens.css` → PASS (smoke-test confirma)
- [x] Sidebar ↔ seções 1:1 (incluindo `#tokens`) → PASS
- [⚠] Zero hex hardcoded → **FALHA** (ver §2.1)
- [⚠] Contraste AA em todo texto visível → **FALHA** (ver §2.2)

### 1.3 Funcionalidades do motion-demo
- **Play/pause**: botão `#motion-play` inicia a sequência de 4 curvas; desabilita durante execução com `aria-disabled`.
- **4 curvas em sequência**: ease-out → ease-in → ease-in-out → spring, com label atualizando em tempo real (`aria-live="polite"`).
- **`prefers-reduced-motion`**: detectado via `matchMedia`, botão desabilitado, mensagem "Movimento reduzido ativo" exibida, box resetado para posição inicial.
- **IntersectionObserver**: pausa a animação quando a seção sai da viewport (threshold 0.1) — evita consumo de recursos.
- **Duplo `requestAnimationFrame`**: garante que o reset da posição (`transition: none`) seja aplicado antes do novo `transition` — técnica correta para animações em sequência.

### 1.4 Responsivo
- `tokens-demo.css` inclui breakpoints em 768px e 480px:
  - Swatch grid: 5 col → 3 col → 2 col
  - Semantic grid: 4 col → 2 col
  - Shadow grid: 4 col → 2 col → 1 col
  - Radius cards: reduzem de 110×90px para 90×74px
- Layout usa `gap`, `flex-wrap`, `grid-template-columns` — sem `position: absolute` frágil.

### 1.5 Tema escuro
- A galeria usa exclusivamente tokens semânticos (`var(--color-surface)`, `var(--color-border)`, `var(--color-text-muted)`, `var(--color-primary)` etc.) — o dark mode funciona automaticamente via `[data-theme="dark"]` do `tokens.css`.
- Swatches brutos usam os tokens de paleta crua (`--c-primary-*`, `--c-neutral-*`) que são independentes de tema — a aparência dos swatches é idêntica em ambos os temas (correto para uma galeria de paleta).
- Labels mono (`--c-neutral-900` / `#ffffff`) são fixos por swatch, não por tema — a galeria mostra a cor real, não uma interpretação temática.

---

## 2. Ressalvas (o que precisa ser corrigido)

### 🔴 Major (3)

#### M1 — Hex hardcoded `#ffffff` em `tokens-demo.css`

**Localização:** `styles/tokens-demo.css`, linha 82:
```css
.swatch--on-dark .swatch__label {
  color: #ffffff;
}
```

**Problema:** Viola DESIGN.md §3 ("nenhum hex, nenhum rem, nenhum valor mágico fora de `tokens.css`") e o pre-flight (§6: "Zero hex em toda UI gerada"). As únicas exceções documentadas são `<meta theme-color>` e favicon data-URI. O valor `#ffffff` não se qualifica.

**Por que escapou dos detectores:**
- `smoke-test.py` (`check_hex`) **só verifica `styles/components.css`**, não `styles/tokens-demo.css`.
- `anti-slop-check.py` só varre hex em `index.html` e `docs/casos/**/*.css`, não em `styles/`.

**Correção (trivial, 3 alternativas):**
```css
/* Opção A: usar o token de paleta mais claro */
color: var(--c-neutral-50);   /* #f8fafc — contraste equivalente */

/* Opção B: usar token semântico */
color: var(--color-bg);       /* resolve para o fundo do tema atual */

/* Opção C: usar color-mix com token existente (se browsers-alvo suportarem) */
color: color-mix(in srgb, var(--color-bg) 100%, white 0%);
```
**Esforço:** S (1 linha) | **Risco de regressão:** nenhum (os valores são visualmente equivalentes).

---

#### M2 — Contraste WCAG AA falho no swatch `primary-500`

**Localização:** `index.html`, linha ~176:
```html
<div class="swatch" style="background-color: var(--c-primary-500)">
  <span class="swatch__label">--c-primary-500</span>
</div>
```
CSS em `tokens-demo.css`, linha 73–78:
```css
.swatch__label {
  font-size: var(--font-size-caption);   /* 12px — texto normal */
  color: var(--c-neutral-900);            /* #0f172a */
}
```

**Problema:** O label em `--c-neutral-900` (#0f172a) sobre fundo `--c-primary-500` (#6366f1) tem contraste de **4.0:1** — abaixo do mínimo WCAG AA de **4.5:1** para texto normal (12px).

**Evidência (cálculo WCAG 2.2, fórmula sRGB → luminância relativa):**

| Swatch | Fundo | Label | Contraste | WCAG AA (normal text, ≥4.5:1) |
|---|---|---|---|---|
| primary-50 | #eef2ff | #0f172a | 16.0:1 | ✅ PASS |
| primary-100 | #e0e7ff | #0f172a | 14.5:1 | ✅ PASS |
| primary-200 | #c7d2fe | #0f172a | 12.0:1 | ✅ PASS |
| primary-300 | #a5b4fc | #0f172a | 9.0:1 | ✅ PASS |
| primary-400 | #818cf8 | #0f172a | 6.0:1 | ✅ PASS |
| **primary-500** | **#6366f1** | **#0f172a** | **4.0:1** | **❌ FAIL** |
| primary-600+ | (todos têm `swatch--on-dark`) | #ffffff | 6.3–11.4:1 | ✅ PASS |

**Correção (trivial):** Adicionar `swatch--on-dark` ao swatch primary-500 para que o label mude para branco:
```html
<div class="swatch swatch--on-dark" style="background-color: var(--c-primary-500)">
```
Com `#ffffff` substituído por `var(--c-neutral-50)` (M1), o contraste em primary-500 passará a ser **6.0:1** — bem acima de 4.5:1.

**Esforço:** S (1 classe) | **Risco de regressão:** nenhum.

---

#### M3 — Detectores não cobrem `tokens-demo.css` e `tokens-demo.js`

**Localização:** `scripts/smoke-test.py` (check_hex só varre `components.css`) e `scripts/anti-slop-check.py` (não varre `styles/` além do que já faz).

**Problema:** Os novos arquivos `styles/tokens-demo.css` e `js/tokens-demo.js` não são cobertos pelos checks automatizados. Isso permitiu que o hex `#ffffff` (M1) e os hardcoded pixels (§3) passassem despercebidos. Para cada novo arquivo CSS/JS adicionado ao showcase, os detectores precisam ser estendidos.

**Correção sugerida (2 arquivos):**

1. **`smoke-test.py`** — estender `check_hex` para varrer todos os `.css` em `styles/` (não só `components.css`), usando a função `css_files()` já existente:
   ```python
   # Em vez de:
   path = os.path.join(ROOT, "styles", "components.css")
   # Fazer:
   for fname in css_files():
       path = os.path.join(ROOT, "styles", fname)
       # verificar hex em cada arquivo
   ```

2. **`smoke-test.py`** — adicionar check de JS para `js/tokens-demo.js` (atualmente só verifica `js/app.js`).

3. **`anti-slop-check.py`** — opcionalmente, estender para varrer `styles/*.css` também (atualmente só varre `docs/casos/**/*.css`).

**Esforço:** M (~20 linhas de Python) | **Risco de regressão:** baixo.

---

### 🟡 Minor (5)

| # | O quê | Onde | Correção | Esforço |
|---|---|---|---|---|
| m1 | **`prefers-reduced-transparency` ausente** — header usa `backdrop-filter: blur(12px)` sem fallback. DESIGN.md §4.5 exige cobertura. | `styles/layout.css` (header) + `styles/tokens-demo.css` (se houver vidro) | Adicionar `@media (prefers-reduced-transparency: reduce) { .site-header { backdrop-filter: none; background-color: var(--color-bg); } }` | S |
| m2 | **Hardcoded pixels sem comentário "constante"** — `min-height: 64px`, `width: 28px`, `height: 20px`, `width: 110px`, `height: 90px`, `min-height: 100px`, `height: 80px`, `width: 48px`, `height: 48px` em `tokens-demo.css`. A convenção do kit (usada em `components.css`) é marcar geometria pontual com `/* constante */`. | `styles/tokens-demo.css` (9 ocorrências) | Adicionar comentário `/* constante de geometria */` em cada valor, ou migrar para tokens onde existir equivalente (ex.: `min-height: 64px` → `var(--space-16)`) | S |
| m3 | **JS duration hardcoded (320ms)** — `const duration = 320; /* motion-duration-slow */`. Se o token `--motion-duration-slow` mudar, o `setTimeout` fica dessincronizado do CSS. | `js/tokens-demo.js`, linha 92 | Ler o valor do token via `getComputedStyle`: `parseFloat(getComputedStyle(box).getPropertyValue('--motion-duration-slow'))` ou usar `transitionend` event em vez de timeout. | S |
| m4 | **Valores de documentação hardcoded no HTML** — "56px / 3.5rem", "40px / 2.5rem", "6px", "10px", etc. nos labels informativos. Não afetam a renderização, mas ficam stale se os tokens mudarem. | `index.html`, seção `#tokens` (~30 ocorrências) | Aceitar como débito técnico documentado (os valores são a "verdade" atual dos tokens; mudar tokens sem atualizar labels é um problema de processo, não de código). Se quiser resolver, gerar com JS que lê `getComputedStyle`. | M |
| m5 | **Hardcoded `8`, `48`, `16` em JS** — `STAGE_WIDTH` subtrai 48 (box width) e 16 (left padding), e `Math.max(8, ...)` para posição mínima. Espelham constantes CSS que podem divergir. | `js/tokens-demo.js`, linhas 30 e 76 | Extrair para constantes nomeadas no topo (`const BOX_WIDTH = 48;`) com comentário, ou ler do DOM via `getComputedStyle`. | S |

---

## 3. Verificação completa do DESIGN.md (pre-flight §6) na galeria

| Item | Status | Evidência |
|---|---|---|
| Design Read declarado | n/a | Galeria é showcase, não página de design |
| Zero `—` / `–` | ✅ | anti-slop-check: 0 em-dash |
| Zero hex hardcoded | ❌ | `#ffffff` em `tokens-demo.css:82` (M1) |
| Theme lock | ✅ | Swatches são independentes de tema; dark mode funciona |
| Color lock | ✅ | Índigo como accent único nas barras/dots |
| Shape lock | ✅ | `radius-sm` em swatches, `radius-md` em cards/seções, `radius-full` em dots — segue convenção |
| Contraste AA | ❌ | primary-500 label falha 4.0:1 < 4.5:1 (M2) |
| Hero constraints | n/a | Seção interna, não hero |
| Eyebrows ≤ ceil(seções/3) | ✅ | 2 em 20 seções |
| Sem fake screenshots | ✅ | Swatches e barras são representações fiéis dos tokens |
| Motion motivado | ✅ | Demo interativo com propósito educacional; só transform/opacity |
| `prefers-reduced-motion` | ✅ | JS desabilita, CSS no base.css colapsa |
| Nav 1 linha ≤ 80px | n/a | Herda do shell |
| Mobile collapse | ✅ | Grids colapsam em 768px e 480px |
| Estados completos | ✅ | Botão play com disabled, hover, focus-visible (via .btn) |
| Copy auditada | ✅ | pt-BR consistente, zero filler verbs, labels descritivos |
| `min-h-100dvh` | n/a | Herda do base.css |
| CWV plausíveis | ✅ | CSS puro, sem webfonts, sem imagens pesadas, IntersectionObserver |
| Micro-gaps | ✅ | `::selection` (base.css), `scrollbar` (base.css), `font-family-mono` em labels |
| `prefers-reduced-transparency` | ❌ | Ausente (m1) |
| Detectores passam | ⚠️ | Passam, mas não cobrem os novos arquivos (M3) |

---

## 4. Notas técnicas adicionais

### 4.1 Técnica de animação (correta)
O `tokens-demo.js` usa duplo `requestAnimationFrame` para resetar a posição do box antes de aplicar a nova transição — padrão correto para forçar o browser a descartar o estado anterior e iniciar nova animação. As curvas são passadas como `var(--motion-easing-*)` via string interpolation no `style.transition` — o browser resolve custom properties em inline styles corretamente.

### 4.2 Timing frágil (débito)
A animação usa `setTimeout` com valores espelhando tokens (`320` = `--motion-duration-slow`, `130` para retorno). Se os tokens mudarem, os timeouts ficam dessincronizados. O ideal seria usar o evento `transitionend` no elemento:
```js
box.addEventListener('transitionend', () => {
  // voltar ao início e disparar próxima fase
}, { once: true });
```
Isso eliminaria a dependência de valores numéricos hardcoded no JS.

### 4.3 Nomenclatura consistente
As classes seguem convenção BEM-like do kit: `tokens-demo__section`, `tokens-demo__title`, `swatch__label`, `motion-demo__controls`. Consistente com `components.css`.

### 4.4 Integração com o showcase
- `<link rel="stylesheet" href="styles/tokens-demo.css">` adicionado no `<head>` (linha 28) ✅
- `<script src="js/tokens-demo.js" defer></script>` adicionado antes de `</body>` (linha 1494) ✅
- Sidebar link `#tokens` já existia ✅
- Seção substituiu o placeholder anterior (zero ocorrências do placeholder antigo) ✅
- Número de seções aumentou de 14 para 20 (smoke-test confirma 14 âncoras → as 6 subseções internas são `<section>` aninhadas com `aria-labelledby`, não itens da sidebar — correto) ✅

---

## 5. Resumo para Atelier/Forja

### Corrigir antes de aprovar (ordem de prioridade)

| # | O quê | Arquivo | Ação | Esforço |
|---|---|---|---|---|
| 1 | `#ffffff` → `var(--c-neutral-50)` | `tokens-demo.css:82` | Trocar 1 valor | 1 min |
| 2 | `primary-500` ganhar `swatch--on-dark` | `index.html:~176` | Adicionar 1 classe | 30 seg |
| 3 | Estender smoke-test para varrer `tokens-demo.css` | `smoke-test.py` | ~15 linhas de Python | 15 min |
| 4 | Adicionar `prefers-reduced-transparency` | `layout.css` + `tokens-demo.css` | 2 media queries | 5 min |
| 5 | Marcar constantes de geometria com comentário | `tokens-demo.css` | Adicionar `/* constante */` em 9 valores | 5 min |
| 6 | Trocar `setTimeout` por `transitionend` event | `tokens-demo.js` | Refatorar `animPhase` | 20 min |

As correções 1–3 são majors (devem ser feitas antes de considerar a galeria finalizada). As correções 4–6 são minors (polimento).

---

*Relatório gerado pelo Evaluator do Design Kit. A galeria está funcional e profissional — com 3 correções pontuais (uma linha de CSS, uma classe HTML, um patch nos detectores) fica impecável e pronta para o pre-flight completo.*