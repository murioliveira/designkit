# Protocolo — 5 Experimentos: Design Kit vs impeccable vs design-taste

**Data:** 2026-08-26 · **Objetivo:** comparar empiricamente os 3 métodos de design para agentes (mesmo input, método diferente, avaliação por critérios fixos).

## Desenho

- **5 experimentos controlados.** Cada um: mesmo brief/input, executado 3x — uma vez com cada método.
- **Critérios fixos** (independentes do método): mecânicos (anti-slop, contraste, em-dash, tokens) + 7 heurísticas (clareza, hierarquia, consistência, affordance, a11y, responsividade, copy).
- **Artefatos:** cada corrida salva o HTML/CSS produzido (experimentos de geração) ou o relatório (crítica/auditoria).

## Os 5 experimentos

| # | Tipo | Input (mesmo p/ os 3) | Saída avaliada |
|---|---|---|---|
| E1 | Landing page (Persuade) | Brief: SaaS de gestão de freelancers "Draftly" | HTML/CSS da landing |
| E2 | Dashboard (Operate) | Brief: dashboard financeiro "NorteMetrics" | HTML/CSS do dashboard |
| E3 | Critique de UI | Uma mesma UI (before.html do redesign-demo, cheio de tells) | Critique report (problemas achados, veracidade) |
| E4 | Redesign | A mesma UI antiga do E3, preservar marca | Rede de E4: after.html (preservação) |
| E5 | Auditoria a11y + anti-slop | A mesma landing gerada no E1 | Relatório a11y (achados reais) |

## Métodos (3 corridores por experimento)

- **A = Design Kit**: lê `DESIGN.md` + usa `skills/` do repo (ui-designer/design-critic/etc) + `scripts/`. Roda os detectores.
- **B = impeccable**: lê `~/.pi/agent/skills/impeccable/SKILL.md` + references (new-work, critique, audit, craft-floor) e segue.
- **C = design-taste**: lê `~/.pi/agent/skills/design-taste/SKILL.md` (dials, tells, pre-flight) e segue.

## Avaliação

1. **Mecânica** (script): zero em-dash? hex fora de tokens? Inter? contraste AA (pares chave)? anti-slop checks?
2. **Heurísticas** (avaliador cego): pontua 1-5 nas 7 heurísticas, sem saber qual método produziu (anônimo).
3. **Painel final**: tabela por experimento (A/B/C) + ranking + "o que cada método fez melhor/pior" + veredito por perfil de uso.

## Saída

- `docs/experimentos/artefatos/` — outputs anônimos (e1-a.html, e1-b.html, e1-c.html...)
- `docs/experimentos/avaliacao.md` — scoring, rankings, painel, veredito
- `docs/experimentos/README.md` — resumo de 10 linhas + recomendações