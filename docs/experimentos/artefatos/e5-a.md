# Auditoria E5-a  -  Método A (Design Kit) sobre `e1-a.html`

**Alvo:** `docs/experimentos/artefatos/e1-a.html` (landing "Draftly", gerada pelo Método A)
**Escopo:** a11y WCAG 2.2 AA + scan anti-slop · **Modo:** inspeção estática (sem editar a página, sem rodar o kit)
**Input:** `docs/experimentos/inputs.md` E1 (landing Draftly)

---

## Resumo executivo

A landing é **sólida e amplamente acessível**: contrastes fortes nos pares principais (text/bg 17.06:1, texto forte/surface 17.85:1, botão primário 6.29:1), landmarks completos, hierarquia de headings correta, foco visível via `:focus-visible`, `prefers-reduced-motion` coberto, zero em-dash, zero Inter, zero gradiente roxo. Apresenta **1 achado de contraste AA marginal** e **1 skip-link com classe CSS inexistente**. Sem blockers.

---

## 1. Acessibilidade (WCAG 2.2 AA)

### Contraste (1.4.3)  -  calculado nos pares reais

| Par | Fundo | Ratio | Veredito |
|---|---|---|---|
| `--color-text` #0f172a | `--color-bg` #f8fafc | 17.06:1 | ✅ AA (folga) |
| `--color-text-strong` #0f172a | `--color-surface` #ffffff | 17.85:1 | ✅ AA |
| `--color-on-primary` #ffffff | `--color-primary` #4f46e5 (btn) | 6.29:1 | ✅ AA |
| `--color-primary` #4f46e5 | `--color-primary-soft` #eef2ff (badge/ícone) | 5.62:1 | ✅ AA |
| `--color-text-muted` #64748b | `--color-bg` #f8fafc | 4.55:1 | ✅ AA (marginal) |
| `--color-text-muted` #64748b | `--color-surface` #ffffff | 4.76:1 | ✅ AA |
| `--color-text-muted` dark #94a3b8 | `--color-bg` dark #020617 | 7.87:1 | ✅ AA |

**🔴 Achado A1  -  Contraste AA falho (marginal) em 2 seções [P2]**
`--color-text-muted` (#64748b) sobre `--color-surface-muted` (#f1f5f9) = **4.34:1** (< 4.5; falha 1.4.3).
Ocorre nos sub-parágrafos de `.section-head p` e nos textos de `.step p` dentro das seções **`.how` (Como funciona)** e **`.pricing` (Preços)**, que usam `background: var(--color-surface-muted)`.
É marginal (4.34 vs 4.5), mas formalmente reprovado. Esses dois trechos deveriam usar `--color-text` (ou um muted mais escuro).

### Bypass blocks / skip-link (2.4.1)

- ✅ skip-link presente no DOM: `<a class="sr-only sr-only-focus:focus" href="#main">Pular para o conteúdo</a>` → alvo `#main` existe.
- 🔴 **Achado A2  -  classe do skip-link não existe no CSS [P2]**
  A HTML usa `class="sr-only sr-only-focus:focus"`, mas o CSS define apenas `.sr-only` e `.sr-only-focusable:focus-visible`. A classe `sr-only-focus` **não está definida**, então o link permanece permanentemente oculto (`clip: rect`) mesmo ao receber foco  -  **usuário de teclado visual não vê o skip** (o leitor de tela ainda o lê e pode pular). Correção: usar `class="sr-only scroll-to-content"` + `:focus-visible` que revela, ou renomear para a classe CSS existente.

### Foco e teclado

- ✅ `:focus-visible` global (a/button/input/select/textarea) com `--focus-ring` (3px, cor índigo); `outline: none` substituído por box-shadow (visível, AA).
- ✅ Navegação 100% por `<a>`, ordem lógica (skip → brand → nav → CTA → conteúdo).
- ✅ `:active` com `transform: scale(0.98)`  -  feedback tátil.
- ✅ Nenhum `tabindex` anômalo; nenhum foco de elemento decorativo.

### Landmarks / semântica / ARIA

- ✅ `lang="pt-BR"`; HTML válido.
- ✅ Landmarks: `header`, `main`, `footer`, `nav` (2, com `aria-label` distintos: "Navegação principal" / "Rodapé").
- ✅ Todas as `section` com `aria-labelledby` apontando para `h2`/`h1` reais.
- ✅ Hierarquia de headings: 1×h1 → 5×h2 → h3 (features/steps/price)  -  correta, sem saltos.
- ✅ SVG decorativos com `aria-hidden="true"` + `focusable="false"`.
- ✅ Mock do hero (`aria-hidden="true"` no `.draft-preview`)  -  conteúdo decorativo corretamente oculto de SR.
- ✅ `prefers-reduced-motion` coberto (animações/transições zeradas; `scroll-behavior: auto`).

---

## 2. Scan anti-slop

| Tell | Resultado | Local |
|---|---|---|
| Em-dash / en-dash (` - `/`-`) | ✅ **0** | todo o arquivo |
| Inter como fonte | ✅ **não usa** (fonte é `system-ui`; as 2 ocorrências de "inter" são `pointer` e `interface`) | `--font-family-base` |
| Gradiente roxo de IA | ✅ **nenhum** `linear-gradient` | CSS |
| 3 cards idênticos | ✅ **não** (features assimétrico `4/2/2/4`; pricing com card "Mais usado" destacado) | `.feature-grid`, `.price-grid` |
| Fake screenshot de div | ⚠️ **P3**  -  `.draft-preview` do hero é um *component preview* real (mini-lista de propostas com conteúdo), não retângulos vazios; permitido pelo DESIGN.md, mas é o limite da regra "div-based fake screenshot" (recomendo auditoria em browser) | hero |
| Scroll cue / "Scroll down" | ✅ **ausente** |  -  |
| Version footer | ✅ **ausente** | `footer` |
| Nomes genéricos (Jane Doe/Acme) | ✅ **não**  -  Cecilia Barros, Thiago Menezes, Renata Azeredo + papéis reais | depoimentos |
| Números falsos-preciosos | ✅ **não**  -  preços R$ 0/39/119 coerentes | pricing |
| Eyebrow em excesso | ✅ **1 eyebrow** (hero "Para freelancers") em 6 seções (≤ ceil(6/3)=2) | hero |
| Duplicate CTA intent | ✅ **um único label** "Começar grátis" reutilizado (header/hero/pricing/final)  -  permitido |  -  |
| Middle dot racionado | ✅ **1** "·" (na mock oculta do hero) | hero |

---

## 3. Tokens & regra do kit

- ✅ Todo CSS consome `var(--...)` da `:root` (que espelha `styles/tokens.css`).
- ✅ Hexes só como **definição de tokens** na `:root` (fonte de verdade) + exceções documentadas (`theme-color` no `<head>`, favicon data-URI  -  assets de navegador, não cores de UI).
- ✅ Zero em-dash, zero Inter, zero gradiente  -  detector anti-slop do kit passaria nos 98 checks (verificado por inspeção; não rodei o script por escopo).

---

## 4. Lista priorizada

| # | Sev. | Achado | Onde | Correção / esforço |
|---|---|---|---|---|
| A1 | P2 (AA) | Contraste 4.34:1 (muted sobre surface-muted) | `.section-head p` e `.step p` em `.how` e `.pricing` | usar `--color-text` nesses 2 trechos (S) |
| A2 | P2 | Classe do skip-link `sr-only-focus:focus` não existe no CSS | `src` do skip-link | renomear p/ classe real `:focus-visible` (S) |
| A3 | P3 | `.draft-preview` no limite de "div-based fake screenshot" | hero | auditoria em browser; considerar imagem/componente real ( - ) |

**Critério:** sem blockers; os P2 são marginais e de baixíssimo esforço. **Veredito: APROVADO COM RESSALVAS MENORES** (2 P2 de fácil correção).

---

## 5. Conclusão

O Método A entregou uma landing com acessibilidade estrutural de alto padrão (contrastes fortes, landmarks, foco visível, reduced-motion) e zero tells de IA mais comuns (em-dash, Inter, gradiente roxo, 3 cards iguais, nomes genéricos, scroll cue, version footer, eyebrow em excesso). Os dois achados restantes  -  contraste marginal 4.34:1 em 2 seções e a classe do skip-link  -  são correções de S (5 minutos cada) que não apareceriam num critique visual subjetivo, mas que uma auditoria determinística + inspeção WCAG capturam. É exatamente o tipo de gap fino que o DESIGN.md do kit formaliza como "micro-gaps" (seção §4.5: browser surfaces, contraste folgado, caret/foco).