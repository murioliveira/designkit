# E4-c: Redesign (Método C: design-taste) · Cloudly

**Input:** `docs/casos/redesign-demo/before.html` (landing "Cloudly" com tells de IA)
**Método:** design-taste (`~/.pi/agent/skills/design-taste/SKILL.md`)
**Artefato:** `docs/experimentos/artefatos/e4-c.html` (auto-contido, HTML+CSS)
**Data:** 2026-08-26

---

## 1. Design Read (skill §0.B)

> "Reading this as: B2B SaaS landing for small teams, with a calm, ferramental language, leaning toward an asymmetric editorial layout with warm neutrals and a single emerald accent, native CSS."

Página: landing SaaS · Audiência: equipes pequenas (não-técnicas) · Vibe: calmo/ferramental · Família: editorial assimétrica + neutros quentes + accent único.

## 2. Dials (skill §1)

| Dial | Valor | Razão |
|---|---|---|
| DESIGN_VARIANCE | 6 | Redesign-preserve puxa para simetria original; elevo +=3 para quebrar o "centrismo padrão" (skill §1.A). Anti-center bias (§4.3). |
| MOTION_INTENSITY | 4 | Micro-interações (hover/press) apenas; respeita `prefers-reduced-motion`. |
| VISUAL_DENSITY | 3 | Ar respirável, galeria/editorial. |

## 3. Modo e audit (skill §11)

**Modo:** Redesign - Preserve (marca "Cloudly" preservada; conteúdo e IA preservados; alavancas de modernização, §11.D).

**Audit antes de tocar (§11.B):** tells inventariados no `before.html`: em-dash (4+), Inter, gradiente roxo AI-typical, 3 cards iguais, fake-screenshot de div, nomes genéricos ("John D."), número falso (99.9%), scroll cue, version footer (v2.4.1/build 0048), eyebrow em toda seção.

**Preservado (§11.C):** brand name "Cloudly" · nav labels (Recursos, Preços, Depoimentos) + "Começar grátis" · CTA intents iguais ao before (Começar grátis / Ver demonstração / Começar / Falar com vendas) · copy voice (calmo, voltado a times) · seções: hero, recursos, precos, depoimentos, cta-final, footer · ids: #recursos, #precos, #depoimentos.

**Levers aplicadas (§11.D):** (1) tipografia (system-ui no lugar de Inter), (2) spacing/rhythm (padrão respirável), (3) recalibração de cor (neutros quentes + emerald, zero roxo), (4) motion (hover/press autoresp), (5) recomposição do hero (split screen), (6) substituição do fake-screenshot por preview real de componente.

## 4. Tells removidos: evidência por check

| Tell (skill §9) | Antes | Agora | Check |
|---|---|---|---|
| Em-dash/en-dash (§9.G) | título/test-dash/CTA | substituído por ponto e vírgula | `grep` 0 |
| Inter (§4.1 / §9.B) | font-family Inter + Google Fonts link | system-ui (sem link externo) | 0 (só em comentário) |
| Gradiente roxo AI-typical (§9.A / §0.D) | `linear-gradient` roxo no hero e cta-final | neutros quentes sólidos | 0 |
| 3 cards iguais (§4.7) | `.features-grid` 3 col iguais | grid assimétrico `1.4fr/1fr` com 1 feature larga | divergente |
| Fake screenshot de div (§4.8 / §9.F) | `.fake-dashboard` de retângulos | preview real com texto significativo | real |
| Nomes genéricos (§9.D) | "John D., Product Manager" | Marina Duarte / Ricardo Nogueira (pt-BR) | 0 |
| Número falso (99.9%) (§4.9) | "aumentou 99.9%" | depoimento qualitativo | removido |
| Scroll cue (§9.F) | "Scroll down" | removido | 0 |
| Version footer (§9.F) | "v2.4.1 · build 0048" | removido (© 2026 somente) | 0 |
| Eyebrow em toda seção (§4.7) | eyebrow em hero+recursos+precos+depo | apenas 1 (hero) | 1 ≤ ceil(5/3)=2 |
| Split-header banido (§4.7) | centrado | split screen legítimo (1 lado copy, 1 lado preview real) | ok |

## 5. Pre-flight: checklist final (skill §14)

- [x] Design Read declarado + dials explícitos com razão
- [x] Zero `—` / `–` em texto visível (grep = 0)
- [x] Color lock: um accent (emerald) em tudo; Shape lock: raios consistentes (14px cards, pills botões)
- [x] Theme lock: claro consistente (landing, sem inversão por seção)
- [x] Contraste AA: todos os pares 5.47:1 a 17.88:1
- [x] CTA: labels curtos, uma intenção por CTA
- [x] Hero: headline ≤ 2 linhas, subtext ≤ 20 palavras, CTA visível, ≤ 4 elementos de texto; padding top 88px (≤ 6rem); split assíncrono; sem tagline sob CTAs
- [x] Eyebrow: contagem 1 ≤ ceil(5/3)=2
- [x] Sem fake screenshots (preview real), sem scroll cues, sem version footers, sem eyebrow numerados
- [x] Motion motivado e contido (hover/press), só transform/opacity, reduzido-motion coberto
- [x] Nav em 1 linha, altura 64px (≤ 80px)
- [x] Zigzag: nenhuma repetição (grid assimétrico + steps + testimonials diferentes)
- [x] Estados: `:active` com feedback tátil; `prefers-reduced-motion`
- [x] Mobile: colapso explícito (nav links ocultos, grids viram 1 col) em <=860px
- [x] Zero `#3c3c` etc fora de tokens (CSS usa :root vars)

**Nota honestidade (§2.B):** estética própria em CSS nativo; nenhum design system externo importado; inspiração editorial-assimétrica documentada.

## 6. Contraste (verificação numérica)

| Par | Razão |
|---|---|
| accent #0f766e / branco | 5.47:1 |
| accent-strong #0b5d56 / branco | 7.74:1 |
| ink #191715 / paper #fbfaf8 | 17.14:1 |
| ink-muted #57544f / paper #fbfaf8 | 7.23:1 |
| CTA ink / white | 17.88:1 |
| CTA muted #c9c6c0 / ink | 10.49:1 |

Todos ≥ WCAG AA (4.5:1 p/ texto normal).

## 7. Conclusão

Redesign-preserve do Cloudly aplicado com o método design-taste: IA e conteúdo preservados, marca intacta, 10+ tells removidos com evidência por grep, pre-flight §14 passado, contraste AA. Artefato auto-contido `e4-c.html` abre direto no navegador, sem build.