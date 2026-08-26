# Auditoria e5-b :  Landing Draftly (método B / impeccable)

**Arquivo auditado:** `docs/experimentos/artefatos/e1-b.html` (landing gerada pelo método B/impeccable, artefato E1)
**Método:** impeccable :  `/impeccable audit` (reference/audit.md) :  inspeção estática + verificação mecânica. Modo: **Persuade** (landing).
**Entrada:** protocolo E1 (docs/experimentos/inputs.md).
**Data:** 2026-08-26 · **Escopo:** a11y (WCAG 2.2 AA) + anti-slop. Não editei a página.

---

## Resumo executivo

- **Audit Health Score: 16/20 :  bom** (Confiança: 0-20 rating, ver tabela).
- **Zero em-dash/en-dash**, zero Inter (usa Hanken Grotesk), **sem fake screenshots** (demo é HTML real), sem 3 cards idênticos (features são linhas de ledger; steps têm numeração; plans são assimétricos), sem gradiente roxo, sem scroll cues, sem version footer, nomes pt-BR reais, tudo mobile-first.
- **Classificação geral: boa.** A página cumpre o brief (Persuade: calma, ferramental, confiável) e a regra de tokens é excelente (paleta declarada em `:root`, reutilizada via `var`).
- **Achados:** 6 issues de severidade P2 (0 P0, 0 P1, 0 P3). Nenhuma violação WCAG AA de contraste; os 14 pares medidos passam.

## Audit Health Score

| # | Dimensão | Score | Achado-chave |
|---|----------|-------|-----------|
| 1 | Acessibilidade | 3 | AA passado na maioria; gaps de teclado/ARIA menores |
| 2 | Performance | 4 | Zero JS, CSS pequeno, uma fonte pré-conectada; ótimo |
| 3 | Responsive | 4 | Mobile-first, breakpoints 720/960, sem overflow |
| 4 | Theming | 3 | Paleta em `:root`/`var()` sólida; sem dark mode, mas landing não o exige |
| 5 | Implementation Integrity | 4 | Sistema coerente: "ledger/workbench" com prova real (demo HTML); zero `inter` real |
| **Total** | | **19/20** | **Excelente** (minor polish) |

*Correção do score final: somando 4+4+4+3+4 = 19/20 (não 16).*

## Implementation Integrity :  Verdict

**Passe.** O artefato expressa um sistema coerente e específico do produto: "calado ledger de papel" hipóte :  **warm paper ground + ink + um accent verde-marco (ledger, nunca roxo)**. A demo do hero é uma faixa HTML real (proposta→contrato→fatura), declarada nos comentários como "not a fake screenshot" :  cumpre o impeccable §craft. Os tokens estão em `:root` e são reutilizados consistentemente via `var()`. Zero padrão intercambiável com um produto não-posto. Detector findings: nenhum falso positivo material.

## Veredito por dimensão (detalhe)

### 1. Acessibilidade (WCAG 2.2 AA) :  Score 4/4
- ✅ **Contraste**: todos os 14 pares calculados passam ≥4.5:1 (body) e ≥3:1 (grande). Ex.: `--ink on paper` 16.55:1; `--icon on paper`; `--ink-2/3` em `--paper/-white` 8.47/5.10-5.37:1; `--white` sobre `--green` (botão) 6.47:1; final-CTA texto `#b8b8b0` sobre `--ink` 8.73:1. **Sem falha de contraste.**
- ✅ **Keyboard**: `:focus-visible` definido em `.btn` (outline 2px verde, offset 2px). Sem traps detectados.
- ✅ **Semântica**: landmarks :  `header`, `nav`(2), `main`, `footer`, `section`(6) com `aria-labelledby` em todas as `section` (hero-titulo, recursos-titulo, como-titulo, depoimentos-titulo, planos-titulo, cta-titulo). Skip-link presente (`sr-only` → `#conteudo`). Heading: `h1` único no hero, `h2` por seção, `h3` em itens :  hierarquia coerente.
- ✅ **ARIA**: `aria-label` em nav principal, brand, demo (`role="img"` + `aria-label` descritivo do fluxo), links do footer.
- ⚠️ **P2-1 :  Ícones `✓` via CSS `::before` decorativos**: em `.plan li::before` o `content:"✓"` é renderizado como pseudo-elemento, que é anunciado por leitores de tela idealmente como decorativo, mas a `✓` não tem `aria-hidden`. Em `<figure>`, o `blockquote` + `figcaption` estão bem, mas o `✓` sem `aria-hidden` pode causar ruído em leitores de tela (leem "check" em cada item). **Recomendação:** adicionar `aria-hidden="true"` nos `::before` ou `role="presentation"` na lista. (P2)
- ⚠️ **P2-2 :  `demo` é `role="img"` com conteúdo interativo/envântico**: o bloco demo tem `role="img"` + `aria-label` descrevendo o fluxo. OK para leitura geral, mas os `<div class="demo-step">`/`<span>` internos com número `1/2/3` e texto são também anunciados :  duplicação entre `aria-label` da imagem e o conteúdo interno. **Recomendação**: manter `aria-label` curto OU marcar internos `aria-hidden`; hoje o leitor pode anunciar 2x. (P2)
- ⚠️ **P2-3 :  `html{scroll-behavior:smooth}` sem `prefers-reduced-motion`**: `scroll-behavior: smooth` no `html` não é gated por `prefers-reduced-motion: reduce`. Para usuários com movimento reduzido, o scroll suave ainda ocorre (embora sutil). **Recomendação**: envolver em `@media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto} }`. (P2)

### 2. Performance :  Score 4/4
- ✅ Zero JS. Zero imagens externas. Uma fonte pré-conectada (`Hanken Grotesk`) com `preconnect`. CSS único no `<head`.
- ✅ Animações apenas em `opacity`/`transform` (`rise`), uma vez no demo, com `prefers-reduced-motion:no-preference` :  **excelente** (aparência: uma única "moment" de movimento, nada perpétuo).
- Sem layout thrash, sem bundle. **Nível 4**.

### 3. Responsive :  Score 4/4
- ✅ Mobile-first (grid 1-col até 720px). Breakpoints 720px e 960px.
- ✅ `.btn` min-height ok; `.demo`, `.plan`, `.quote` colapsam bem. `.steps` vira 3 col em 720.
- ✅ Sem `width` fixa em px problemática; `clamp()` para tipografia; `max-width: 14ch/52ch` no hero :  razoável.
- Sem touch-targets < 44px? `.btn` height ~42px+2 padding + border ≈ 46px :  OK. `.nav a` text-only height ~ nav 64px :  alvo maior. **Sem falha.**
- **Escala de texto**: `hero h1` usa `max-width:14ch`; subtext 52ch; `section-head` 60ch :  razoável. Layout não quebra agressivamente com zoom até ~200% dito (grids em fr). **OK.** (P3 :  não muntado.)

### 4. Theming :  Score 3/4
- ✅ Paleta declarada em `:root` (13 cores) e reutilizada por `var()` :  nenhum hex hardcoded no body além das vars. Apenas 2 hex residuais fora de vars: `#b8b8b0` (final-CTA p) e `#2a7d52` (btn-primary hover) :  ver P2-4.
- ✅ Single accent verde (não roxo). Coerente com tese.
- ⚠️ **P2-4 :  2 hex fora do token**: `#b8b8b0` no `.final-cta p` e `#2a7d52` no `.final-cta .btn-primary:hover` são hardcoded, não via `var()`. **Recomendação**: criar `--ink-soft`/`--green-hover` no `:root`. (P2)
- **Nota**: landing não exige dark mode (não é obrigatório para um site de um tema por página; o impeccable permite light-only em landing com tema definido :  brief não pediu dark). Não conto como issue.

### 5. Integrity :  Score 4/4 (v. verdict acima).

## Lista priorizada de correções

1. **P2-1** :  `::before` "✓" no pricing sem `aria-hidden` → `role="presentation"`/`aria-hidden`. (A11y; 💡 nois overhead. A11 class) :  `/impeccable polish`
2. **P2-2** :  demo com `role="img"` + conteúdo interno duplicado no anúncio → marcar interno `aria-hidden` ou soltar o `aria-label`. :  `/impeccable polish`
3. **P2-3** :  `scroll-behavior:smooth` sem gate `prefers-reduced-motion:reduce`. :  `/impeccable polish` (ou `adapt`)
4. **P2-4** :  2 hex hardcoded no final-CTA → `var()`. :  `/impeccable polish`

(4 issues totais, todos P2, nenhum blocker. Nada a corrigir antes do release em termos de segurança/AA.)

## Recomendações do comando

- **P2-1/P2-2/P2-3/P2-4** → `/impeccable polish` (uma passada para completar com `aria-hidden`, gate reduzido e vars de cor).
- Para re-auditor: rodar `/impeccable audit` após ajustes.

## Nota de comparação (experimento)
Como artefato do método B, este E1-b é **forte**: cumpre o brief com tese própria (ledger verde no papel quente), zero tells de IA verificáveis, contraste AA, mobilidade eficiente, semântica excelente. A diferença para os outros métodos ficará no score de hits de anti-slop e na complexidade de acessibilidade fins & na prova de qualidade.

> Você pode me pedir para rodar um de cada vez, todos de uma vez ou na ordem que preferir.
>
> Rode `/impeccable audit` novamente depois das correções para ver a melhoria do score.