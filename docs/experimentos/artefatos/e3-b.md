# Critique E3-b — Método B (impeccable) sobre before.html

**Método B:** skill `impeccable` v4.1.1 — comando `/impeccable critique`, seguindo `reference/critique.md`.
**Input:** `docs/casos/redesign-demo/before.html` (landing "Cloudly" — estoque de AI-slop deliberado).

> **Method: DEGRADED** (single-context, sem sub-agent tool na sessão do corridor do experimento E3-b). Assessment A (design review) e Assessment B (detector) executados no mesmo contexto.

## Delphi — Deterministic scan (Assessment B)

`detect.mjs --json before.html` rodou **DEGRADED** (módulos de parser HTML não disponíveis; modo regex). Achados:

| Anti-pattern | Localização | Detalhe |
|---|---|---|
| `overused-font` (Inter) | linha 9 (`fonts.googleapis…family=Inter`) + linha 21 (`font-family: 'Inter'`) | Inter banido por ser a fonte nº1 de convergência de IA |

Complemento determinístico (grep/count, além do detector):

| Check | Contagem | Local |
|---|---|---|
| Em-dash/en-dash (`—`/`–`) | 4 | title, hero (1), meta description… |
| Inter (`Google Fonts` + `font-family`) | 2 | linha 9, linha 21 |
| AI-purple (hex `#7c3aed/#6d28d9/#ede9fe`) | 3 | `--ai-purple`, `--ai-purple-dark`, `--ai-purple-light` |
| Fake screenshot (divs/spans vazios) | 20 (`fake-dashboard*`) | `.fake-dashboard` com 3 rows de spans vazios |
| 3 feature cards idênticos | 12 (3× icon+title+text) | `#recursos` |
| Scroll cue ("Scroll down") | 2 | `.scroll-cue` |
| Version footer | 2 (`v2.4.1`, `build 0048`) | `.footer__version` |
| Nome genérico "John D." | 1 | depoimento |
| Número falso-precioso "99.9%" | 1 | depoimento |
| Eyebrow em toda seção | 6 | hero + 3 seções |

> **Nota de método:** o detector em modo regex **subestima** (não avalia computed contrast, nem selector matching). O gap real de a11y (fake screenshot vazio, sem contraste calculado) foi coberto por inspeção manual (Assessment A).

## Assessment A — Design Review (11 heurísticas Nielsen)

**Design Specificity Verdict:** Categoria-intercambiável em grau máximo — esta landing poderia ser de qualquer SaaS de produtividade/tarefas (Todoist, Asana, Monday…) sem trocar uma palavra. Não há uma decisão de design pertencente ao "Cloudly": o gradiente roxo, as 3 feature cards simétricas, a preview de div falsa e o Inter são o "default de IA", não uma identidade. Não é "ruim por falta de talento" — é "STA sample assinado por nenhuma marca".

### Nielsen 10 Heuristics

| # | Heurística | Score | Problema-chave |
|---|-----------|-------|----------------|
| 1 | Visibility of System Status | n/a | Landing estática, sem operações; não se aplica |
| 2 | Match System / Real World | 2 | Subtext genérico ("a ferramenta que sua equipe merece") não nomeia resultado concreto |
| 3 | User Control and Freedom | n/a | Sem há flows de entrada de dado; não se aplica |
| 4 | Consistency and Standards | 1 | Inter + purple + 3 cards = "padrão de IA", não um padrão de produto |
| 5 | Error Prevention | 1 | "Ver demonstração" é botão `<button>` sem ação real; CTA sem destino confirmável |
| 6 | Recognition Rather Than Recall | 1 | Fake dashboard não reconhece produto real; ícones (feature-card__icon) são divs vazios sem semântica |
| 7 | Flexibility and Efficiency | n/a | Sem navegação/especialização; não se aplica |
| 8 | Aesthetic and Minimalist Design | 1 | Gradiente roxo, 6 eyebrows, 3 cards idênticos: ruído visual uniforme |
| 9 | Error Recovery | 1 | Scroll cue "Scroll down" falso (tudo visível); sem mitigação de erro |
| 10 | Help and Documentation | n/a | Landing; não se aplica |

**Total:** **8/24** (6 heurísticas aplicáveis × 4) → **33% → faixa "Poor"** (30–50% Poor). Em base 40 seria ~10-11/40 → **Poor**.

### Cognitive Load Checklist

- ❌ Single focus: 6 eyebrows + 2 CTAs + preview + 3 seções competem
- ❌ Chunking: feature cards e pricing têm sempre 3, mas o conteúdo é idêntico (sem chunk real)
- ⚠️ Visual hierarchy: eyebrow em tudo apaga hierarquia (tudo parece igual)
- ⚠️ Minimal choices: 2 CTAs repetidos em 4 pontos diferentes (Começar grátis repetido 4×: nav, hero, CTA final)
- ❌ Working memory: "começar grátis" aparece em nav/hero/pricing/cta — usuário não distingue intenções
- **Resultado: 4+ falhas → alta carga cognitiva**

### Persona Red Flags

- **Jordan (First-Timer):** botão "Ver demonstração" não abre demonstração nenhuma; fake dashboard (spans vazios) não mostra um produto real; termo "build 0048" (footer) é jargão de dev, não de landing. Abandona em 5s.
- **Casey (Mobile):** nav é `<ul>` sem menu mobile/hamburger; 3 colunas fixas em `features-grid` e `pricing-grid` (sem media query) — quebram em <768px; touch-targets 0px reais (cards não-clicáveis). Não há layout mobile.
- **Sam (A11y):** fake dashboard usa `<span>` vazios sem `role`/`alt`/texto — leitor de tela lê nada; feature-card__icon é div vazia; o único aria-label está no fake-dashboard. Sem contraste calculado (degraded), mas o `--ai-purple-light #ede9fe` com texto roxo `#7c3aed` é suspeito para texto pequeno.

## Priority Issues (P0–P3)

**P0 — Fake screenshot de div apresentado como "Prévia do produto"**: `.fake-dashboard` é 3 linhas de spans vazios sem conteúdo real ou texto alternativo. É o tell nº1 de IA e quebra a confiança e a acessibilidade. *Fix:* usar screenshot real, componente real, ou remover. *Sugestão:* `/impeccable polish` + `/impeccable audit`.

**P1 — Identidade genérica (Inter + purple + 3 cards + 6 eyebrows)**: sem caractere de marca; tudo "template de IA". *Fix:* trocar AI-purple por accent próprio, fonte não-Inter, layouts assimétricos. *Sugestão:* `/impeccable typeset` + `/impeccable colorize` + `/impeccable layout`.

**P1 — Zero responsividade mobile**: `features-grid` e `pricing-grid` fixas em 3 colunas, sem `@media`. *Fix:* mobile-first com breakpoints e colapso. *Sugestão:* `/impeccable adapt`.

**P2 — CTA sem ação real + scroll cue falso**: "Ver demonstração" e "Começar grátis" não acionam nada; "Scroll down" é fingido. *Sugestão:* `/impeccable harden`.

**P2 — 4 em-dash visíveis + "Scroll down" + version footer "build 0048"**: tells de tipografia/copy que um leitor atento flagra. *Sugestão:* `/impeccable clarify`.

**P2 — Nome genérico "John D." e número falso "99.9%"**: destroem a credibilidade do depoimento. *Sugestão:* `/impeccable clarify`.

## Minor Observations

- Nav sem estado ativo/aria-current; sem `aria-expanded` (crosshair — inexistente aqui, mas o padrão de nav fixa está ok).
- `section__eyebrow` repetido em todas as seções viola a disciplina de "eyebrow ≥ 1 por 3 seções".
- Pricing repete "Começar" em 3 cards + nav "Começar grátis" + hero + CTA final = mesma intenção espalhada.
- Fonte Inter em dois pontos (preconnect + family).

## Resumo (comparável ao E3-a)

**Média heurísticas:** 8/24 (33%, Poor) — coerente com o E3-a (média 1.7/5 ≈ 34%). Os dois métodos chegaram à mesma faixa de reprovação com fundamentos sintéticos parecidos, mas o impeccable entrega isso como **10 heurísticas Nielsen + personas + cognitive load + detector**, enquanto o Design Kit entrega **checklist mecânico + tells** + tokens. O detector impeccable (degraded aqui) achou só 2 (Inter), pois o parser não carregou; o Design Kit achou 11 tells via grep. Em ambiente completo (parser OK), o detector impeccable daria mais — não foi possível validar aqui.