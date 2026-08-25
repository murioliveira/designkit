# Critique Report v2 — Caso Lumen (Rodada 2 · Gate de fechamento da Fase A)

> **Caso:** Lumen (landing page de produto fictício) · **Fase:** A (gate do design-critic, re-critique pós-refine) · **Revisado por:** design-critic
> **Arquivos auditados:** `docs/casos/lumen/index.html`, `lumen.css`, `README.md` (com refine) + `styles/tokens.css`, `styles/base.css`, `index.html` raiz

## Veredito

**`APROVADO`** — sem blockers, sem majors restantes. Os 3 achados major da rodada 1 foram verificados como corrigidos (com evidência no código e cálculo de contraste). Restam 4 achados P2 (não bloqueantes), reportados para o ciclo de manutenção.

## 1. Scoring por heurísticas — atualizado

| Heurística | R1 | R2 | Comentário |
|---|---|---|---|
| Clareza de comunicação | 5/5 | **5/5** | Value prop e CTAs intactos. |
| Hierarquia visual | 5/5 | **5/5** | Sem mudanças. |
| Consistência com o kit (tokens) | 3/5 | **5/5** | Espaçamento 100% `var(--space-*)`; off-scale justificados em comentário; README corrigiu alegação falsa. |
| Affordance / interação | 4/5 | **5/5** | Nav mobile restaurada; loop de CTAs terminado em `#cadastro`. |
| Acessibilidade | 3/5 | **4/5** | Contraste AA corrigido (18.4:1 / 16.3:1 / 16.3:1 claro), skip-link, reduced-motion, toggle no paint. |
| Responsividade | 4/5 | **4/5** | Nav móvel resolvida; `var()` em media queries permanece (decisão documentada). |
| Qualidade da copy | 5/5 | **5/5** | Sem mudanças. |
| **Média** | **4.1/5** | **4.7/5** | |

## 2. Verificação dos 3 majors — CORRIGIDOS

- **Major 1 — Espaçamento tokenizado ✅**: todos os valores da escala 4px viraram `--space-*`; off-scale (1px, 6px, 12px, 88%, 24/48/20/26/9/34rem, geometria do anel) com justificativa em comentário CSS; README não afirma mais "nenhum valor mágico" (exceções tabeladas em §3.1).
- **Major 2 — Contraste AA claro ✅**: `.app-card__time` → `--color-text-strong` = **18.4:1**; `.app-card__energy-label` e `.final-cta__text` → `--color-text` = **16.3:1** (escuro 14.6:1). Todos ≥ 4.5:1 com folga.
- **Major 3 — Nav mobile colapsável ✅**: `aria-expanded`/`aria-controls` reais, Esc fecha e devolve foco, painel fecha ao navegar e ao voltar ao desktop; hambúrguer→X com matemática correta.

## 3. Minors verificados

✅ `scroll-margin-top` com `main[id]` · ✅ CTA final → `#cadastro` (placeholder real) · ✅ `prefers-reduced-motion` zerado em transforms/transitions/scroll · ✅ comentário do verde preciso.
⚠️ Foco em pills (P2-1) e bloco morto no head (P2-2) parcialmente — ver abaixo.

## 4. Achados restantes (P2 — não bloqueiam o gate)

- **P2-1 — `border-radius: inherit` não restaura o pill**: `inherit` pega o radius computed do pai (0), não o do elemento. → **Corrigido na rodada 3** (orquestrador): `var(--radius-full)`.
- **P2-2 — Bloco morto no head**: `getElementById("theme-toggle")` retorna null no parse do head (elemento ainda não existe). → **Corrigido na rodada 3**: bloco removido; script do fim do body já seta os atributos antes do primeiro paint.
- **P2-3 — Painel do menu inacessível por Tab direto**: nav antes das actions no DOM. → **Corrigido na rodada 3**: nav movido para depois de `.site-header__actions` + `order` no CSS restaura a ordem visual.
- **P2-4 — Contraste marginal do nav (4.55:1)**: → **Corrigido na rodada 3**: `--color-text` (16.3:1).

## 5. Conclusão

Gate da Fase A fechado como **APROVADO**. Correções P2 aplicadas pelo orquestrador na rodada 3 (kit e página). Próximos: a11y-auditor/visual-qa em profundidade, docs de handoff por componente, validação multi-agente (Fase E).
