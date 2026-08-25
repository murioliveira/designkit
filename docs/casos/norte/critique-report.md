# Critique Report — Caso Norte (Dashboard Financeiro) — Fase A, PoC 2

**Data:** 2026-08-25 · **Crítico:** design-critic (revisão independente, read-only) · **Arquivos auditados:** `docs/casos/norte/index.html`, `dashboard.css`, `README.md`

## Veredito

**APROVADO COM RESSALVAS** — o objetivo central do PoC (provar que `components.css` é consumível fora do showcase, sem `layout.css`/`app.js`) está **plenamente comprovado**: regra de tokens rigorosa, zero conflito de CSS, todas as classes do kit presentes, padrões ARIA de dropdown/tabs/modal/tabela/paginação/stepper corretos. Nenhum P0. Um P1 (dados incorretos no modal) e seis P2.

## 1. Regra de tokens e reuso via `<link>` — APROVADO

- `dashboard.css`: **zero** hex/rgb mágicos; valores de design 100% `var(--...)`; literais documentados (34rem leitura, 16rem gráfico, blur 12px, alpha 88%).
- Ordem de `<link>` correta: tokens → base → components → dashboard. Nenhuma classe de componente sobrescrita (dashboard.css cobre só layout de página + shell replicado de layout.css, que não é carregado).

## 2. Classes do HTML × components.css — todas existem

12 grupos reusados: botões, badges, cards, alertas, forms, modal, tabs, dropdown, breadcrumb, tabela, stepper, paginação — todos ✅.

## 3. Scoring por heurísticas — média 4.6/5

| Heurística | Nota |
|---|---|
| Clareza | 4/5 (modal com dados de outra transação) |
| Hierarquia visual | 5/5 |
| Consistência com o kit | 5/5 |
| Affordance / interação | 4/5 (quirk de setas; aria-disabled clicável) |
| Acessibilidade | 4/5 (contrastes na fronteira do AA) |
| Responsividade | 5/5 |
| Qualidade da copy | 5/5 |

## 4. Achados

**P1 (corrigir antes do handoff):**
1. **Modal exibe dados errados para 5 de 6 linhas** — `index.html:358-398` (gatilhos `data-modal-open`) vs conteúdo fixo `:513-519` (#4821 · Aurora · R$ 3.240,00). Script (680-706) só abre/fecha sem popular. Correção: `data-*` no gatilho + preenchimento do `<dl>` no open, ou desabilitar gatilhos das demais linhas.

**P2:**
2. Quirk de setas no dropdown com menu aberto por clique (`index.html:582-600`; também `js/app.js:653,689` do kit): ArrowDown do gatilho foca o último item. Correção: `delta=1` quando `from === trigger`.
3. Legenda do gráfico semanal anuncia 2 séries mas só desenha 1, cores diferentes das barras (`index.html:230-254`; trimestral 290-307 idem; mensal correto).
4. Contrastes na fronteira AA: text-muted sobre bg 4.55:1 (`dashboard.css:162-167`); seta aria-disabled sobre surface-muted 4.34:1; dot do badge success ≈3.0:1. Passam, mas README (4.76:1) impreciso.
5. `[hidden]` em `.btn`/`tbody` depende da regra UA — kit protege explicitamente; sugerir `[hidden]{display:none}` no base.css.
6. README autocrítico superestima (5.0/5 sem blockers vs P1-1); referência a "seção 5" inexistente.

## 5. Conclusão

Gate do caso Norte: **APROVADO COM RESSALVAS**. Refine: corrigir P1 + P2-2 (também no kit), P2-3, P2-4 (docs), P2-6 (README). Objetivo do PoC comprovado.
