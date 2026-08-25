# Re-Auditoria Comparativa v2 — Design Kit vs impeccable + design-taste

**Data:** 2026-08-25 (rodada 2) · **Baseline:** auditoria-comparativa.md (5/10 impeccable, 7/10 taste)

## Checklist das 8 recomendações

| # | Recomendação | Status | Evidência |
|---|---|---|---|
| 1 | Redesign protocol | ✅ | DESIGN.md §5.1 + skills/design-redesign + docs/casos/redesign-demo/ (auditoria 16 tells, levers em ordem) |
| 2 | Performance/CWV | ✅ | DESIGN.md §6 (plausível, sem gate automatizado) |
| 3 | Detector determinístico | ✅ | scripts/anti-slop-check.py (7 checks, exit code) |
| 4 | Modos em profundidade + Experience | ✅ | docs/reference/modos.md (193 ln, ancorado em casos reais) |
| 5 | Block library | ✅ + validada | docs/blocos/ (6 blocos) + docs/casos/linha-direta/ (4 blocos aplicados) |
| 6 | Mapa de DS externos | ✅ | DESIGN.md §5.2 + honesty rule |
| 7 | Critique enriquecido | ✅ + provado | design-critic (cognitive-load + persona) + linha-direta (3 P1 que externas não pegam) |
| 8 | Micro-gaps | ✅ | DESIGN.md §4.5 (browser surfaces, reduced-transparency, i18n, ícones) |

## Notas atualizadas

| Skill | Antes | Agora |
|---|---|---|
| impeccable (substituto) | 5/10 | **8.5/10** |
| design-taste (substituto) | 7/10 | **9/10** |

## Gaps residuais (para 10/10)

**P1:** detector sem hook automático pós-edição (estilo detect.mjs); trend de notas de critique não implementado.
**P2:** after.html do redesign-demo fora da varredura automática (corrigir target_files); contagem "49 checks" defasada (hoje 70); critique do redesign-demo em aberto; caso Experience puro (portfólio) ausente.
**P2/P3:** comandos bolder/quieter/distill; i18n profundo; CWV só plausível; dual-agent A/B.

## Veredito

**Substituto superior** para: método anti-slop + design system de tokens + fluxo de setor executável com detecção mecânica e validação empírica.
**Ainda não** para: detector-com-hooks + trend de notas + comandos de refinamento + i18n profundo (esses 4 separam 8.5/9 de 10).
