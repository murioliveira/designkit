# Critique Report

> Template do design-critic — referencia rápida. Versão completa em skills/design-critic/SKILL.md.

## Caso: [nome] · Data: [data] · Revisado por: [design-critic]

## Veredito

**`aprovado` / `aprovado com minors` / `requer correções` / `blocker`**

## Scoring por heurística

| Heurística | Nota (1–5) | Comentário curto |
|---|---|---|
| Clareza | /5 | |
| Hierarquia | /5 | |
| Consistência (inclui uso de tokens do kit) | /5 | |
| Affordance | /5 | |
| Acessibilidade | /5 | |
| Responsividade | /5 | |
| **Geral** | **/5** | |

## Pontos fortes

- [específico: onde/qual elemento e por quê]

## Problemas

### Blocker
- `[localização]` — [descrição] → correção: [como]

### Major
- `[localização]` — [descrição] → correção: [como]

### Minor
- `[localização]` — [descrição] → correção: [como]

## Lista priorizada de correções

| # | Severidade | O quê | Onde | Esforço (S/M/L) |
|---|---|---|---|---|
| 1 | blocker | | | |

## Regra de tokens do kit (verificação obrigatória)

- [ ] UI usa somente `var(--token)` de `tokens.css` — hex hardcoded/valores fora da escala são major+
- [ ] Padrões existentes do kit foram reutilizados, não reimplementados

## Critério de parada atingido?

- Sem blockers: [sim/não] · Média ≥ 4: [sim/não] · Nenhuma heurística < 3: [sim/não]
- Próxima ação: [aprovar / corrigir e re-critique (máx 2 rodadas) / escalar ao humano]
