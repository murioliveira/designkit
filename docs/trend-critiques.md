# Trend de Critiques — Memória do Setor de Design

> Histórico consolidado de todas as rodadas de critique do Design Kit. Cada linha
> é um ciclo completo (crítica → refine → re-crítica). Este arquivo é a memória
> do setor: o que cada caso ensinou ao kit, para o método evoluir (não só a tela).
> Última atualização: 2026-08-25.

| Caso | Veredito | Média | Data | Achados principais | Report | Aprendizado para o kit |
|---|---|---|---|---|---|---|
| Lumen (v1) | APROVADO COM RESSALVAS | 4.1/5 | 2026-08-25 | 3 majors: espaçamento não tokenizado (~15 valores mágicos), contraste AA claro 4.34:1 (text-muted sobre surface-muted), nav some no mobile; 6 minors (skip-link sob header, foco pill, loop de CTA, toggle estático) | `docs/casos/lumen/critique-report.md` | **Tokenização de espaçamento é regra auditável** — a partir daqui, `grep` de hex/valores mágicos virou check obrigatório; contraste claro precisa de folga (não borda de 4.5:1) |
| Lumen (v2) | APROVADO | 4.7/5 | 2026-08-25 | 3 majors verificados corrigidos (18.4:1/16.3:1 claro); restam 4 P2 não bloqueantes | `docs/casos/lumen/critique-report-v2.md` | P2s viraram ciclos de manutenção (foco pill, tab order do nav, contraste do nav) — **kit e página são refinados juntos** |
| Norte | APROVADO COM RESSALVAS | 4.6/5 | 2026-08-25 | 1 P1 (modal com dados fixos errados), 6 P2 (quirk de setas do dropdown, legenda de gráfico, contrastes na fronteira, `[hidden]` dependente de regra UA, README superestima) | `docs/casos/norte/critique-report.md` | **Reuso real de 12 grupos do kit sem conflito** (prova do PoC) + **bug de setas do dropdown corrigido no kit** (`js/app.js`) — casos reais alimentam o kit |
| Brisa | aprovado com minors | 4.2/5 | 2026-08-25 | 1 major (pausa — maior dor da persona — escondida em texto secundário), 2 minors (contraste do stepper ativo, selo em muted) | `docs/casos/brisa/critique.md` | **Critique contra persona, não contra gosto** — a necessidade nº 1 da persona define prioridade dos achados |
| Linha Direta | APROVADO COM RESSALVAS | 4.71/5 | 2026-08-25 | 3 P1: célula vazia no bento (auto-placement do Grid), color lock violado (índigo vs âmbar), marquee com costura visível (matemática do transform) | `docs/casos/linha-direta/critique-report.md` | **Bugs do marquee e do bento corrigidos no bloco-fonte** (`docs/blocos/marquee.md`) — block library é validada por caso real; color lock virou check (1 accent por página) |
| Tereza (Experience) | em aberto (a pontuar) | — | 2026-08-25 | Chrome mínimo, obra no primeiro viewport, galeria assimétrica, terracotta único; anti-slop 98 checks | `docs/casos/tereza/` | **4º modo materializado** — Experience como curadoria (menos chrome, obra lidera); valida o bloco galeria-experience |
| Redesign Demo | (demo before→after, não pontuado) | — | 2026-08-25 | Auditoria do "antes": 16 tells de IA (4 em-dash, Inter, gradiente roxo, fake screenshot, eyebrows em excesso) → "depois" limpo (split assimétrico, accent único, SVG real) | `docs/casos/redesign-demo/auditoria.md` | **before.html é a fixture negativa do detector** — `scripts/anti-slop-check.py` a marca como falha esperada (3 checks: em-dash, inter, eyebrows); prova que o detector pega o que a skill externa não pega |

## Leitura da tendência

1. **A média subiu e estabilizou**: 4.1 → 4.7 (Lumen), 4.6 (Norte), 4.71 (Linha Direta). O piso de qualidade subiu com o método anti-slop (DESIGN.md).
2. **Cada caso gerou correção no kit, não só na página**: dropdown (Norte), marquee/bento (Linha Direta), tokenização (Lumen) — o ciclo critique→refine é o motor do design system.
3. **O critique evoluiu**: heurísticas → + regra de tokens → + AI tells → + cognitive-load/persona (Rodada 2 de superação). A severidade dos achados subiu com o rigor do crítico.

## Como registrar um novo critique

1. Salve o report em `docs/casos/<nome>/critique-report[-vN].md`.
2. Adicione a linha nesta tabela (veredito, média, achados, aprendizado).
3. Se o caso gerou correção no kit, registre o aprendizado na coluna correspondente — essa coluna é o que transforma caso em método.
