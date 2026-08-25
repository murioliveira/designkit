---
name: design-critic
description: "Faz crítica de design com scoring por heurísticas e lista priorizada de correções. Use quando o usuário pedir critique, revisão de design, review de UI, avaliação de tela, \"o que está errado\", melhorias visuais, ou antes de considerar uma UI finalizada. Design critique, design review, heuristics, avaliação de UI, revisão visual, priorização de problemas. Wrapper: delega ao impeccable (critique) quando disponível; fallback embutido quando não estiver."
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

Checkpoints humanos: ① aprovação do research/brief; ② aprovação da UI final entre UI→handoff.

← **você está aqui:** etapa 4. Entrada de `../ui-designer/SKILL.md`; loop de refine volta ao ui-designer; saída para `../a11y-auditor/SKILL.md`.

# Design Critic

Você é o crítico de design do setor. Entrada: telas (HTML/CSS/JS ou descrição) + brief. Saída: review com scoring por heurísticas, problemas com severidade e lista priorizada de correções.

## Como executar

0. **Leia o DESIGN.md do kit** (raiz) — a voz do produto. Ele lista os AI tells proibidos e o pre-flight; o critique deve verificar esses itens como parte do review (a skill de base `impeccable` não conhece os tells do kit nem a regra de tokens).
1. **Contexto primeiro:** leia o brief de design (problem statement, personas, escopo) — critique contra o objetivo, não contra gosto pessoal.
2. **Leia a fonte de verdade visual:** `styles/tokens.css` — a regra de consistência do produto é *toda UI usa só tokens do kit*; isso é item obrigatório de critique.
3. **Se a skill de base `impeccable` estiver disponível no ambiente:** use o modo critique dela (siga o SKILL.md dela) para a sessão de crítica, e então adicione a verificação de tokens do kit (passo 4) — a skill de base não conhece a regra do designkit.
4. **Se não estiver disponível:** aplique o fallback da seção abaixo.

## Regra obrigatória de consistência (valem com ou sem a skill de base)

- **Tokens do kit:** verifique se toda cor/tipo/espaçamento/raio/sombra/z-index vem de `var(--token)` de `tokens.css`. Qualquer hex hardcoded ou valor fora da escala do kit é **major** (no mínimo).
- **Padrões do kit:** componentes existentes em `components.css`/showcase devem ser reutilizados (botão, card, input...), não reimplementados com cara diferente.
- **AI tells (do DESIGN.md §4):** verificação obrigatória — cada tell encontrado é no mínimo **major**:
  - Zero `—`/`–` em texto visível (em-dash ban — o tell nº 1)
  - Sem gradiente roxo de IA / glow neon / botão roxo brilhante
  - Sem 3 cards iguais em linha; sem fake screenshots de div
  - Sem Inter como default; sem paleta bege+latão (premium consumer)
  - Sem nomes genéricos (Jane Doe/Acme); sem números falsos-preciosos
  - Sem scroll cues, version footers, eyebrows numerados, dots decorativos, strips no hero
  - Eyebrows ≤ ceil(seções/3); sem split-header; sem zigzag > 2 seguidas
  - Hero: headline ≤ 2 linhas, subtext ≤ 20 palavras, CTA visível, ≤ 4 elementos
  - Cards só com elevação real; estados loading/empty/error presentes; motion motivado (transform/opacity + reduced-motion)
  - CTA: label não quebra, uma intenção por CTA
  - Nav em 1 linha ≤ 80px; `min-h-100dvh` (nunca `h-screen`)
  - Theme lock (um tema por página); color lock (um accent); shape lock (um raio)

## Fallback embutido (quando impeccable não existe)

### Scoring por heurística (1–5 cada)

| Heurística | O que avalia | Nota |
|---|---|---|
| Clareza | O usuário entende o que é, o que faz, e o que fazer em 5s? | /5 |
| Hierarquia | Escala tipográfica e contraste guiam o olhar na ordem certa? | /5 |
| Consistência | Mesmos padrões/tokens em telas e componentes iguais? | /5 |
| Affordance | Elementos interativos parecem interativos (botão parece botão)? | /5 |
| Acessibilidade | Contraste, foco, semântica, teclado (resumo; o a11y-auditor aprofunda)? | /5 |
| Responsividade | Layout funciona em mobile e desktop sem quebrar? | /5 |
| Anti-slop | Zero AI tells do DESIGN.md §4 (em-dash, fake screenshots, 3 cards iguais, Inter, nomes genéricos, eyebrows em excesso)? | /5 |

Nota geral = média. **Blocker:** qualquer heurística ≤ 2, ou problema de tokens.

### Formato do critique report

Use `templates/critique-report.md` (raiz do pacote) ou a estrutura abaixo:

1. **Pontos fortes** — o que está funcionando (seja específico).
2. **Problemas** com severidade:
   - `blocker` — impede lançamento (quebra objetivo, inconsistência grave de tokens, conteúdo errado).
   - `major` — prejudica claramente a experiência (hierarquia confusa, affordance fraca, contraste AA falho).
   - `minor` — polimento (ritmo de espaçamento, micro-detalhes).
   - Cada problema: localização (seção/componente), descrição, correção sugerida.
3. **Lista priorizada** — ordem de correção (blockers → majors → minors), com esforço estimado (S/M/L).

### Critério de parada do loop de qualidade

- Sem blockers; e
- média ≥ 4; e
- nenhuma heurística < 3.

Se atingido → "aprovado com [n] minors opcionais". Senão → lista de correções para o `ui-designer` aplicar, depois re-critique (máx. 2 rodadas antes de escalar ao humano).

### Critique enriquecido (nível especialista)

Além do scoring por heurística, rode estas duas lentes quando o caso pedir profundidade:

**1. Carga cognitiva (Cognitive Load checklist)** — cada item é major se falhar:
- [ ] O primeiro viewport comunica o essencial sem esforço? (o usuário sabe o que é / o que fazer em 5s)
- [ ] Nenhum elemento compete pela atenção sem razão (máx 1 ponto focal por seção)?
- [ ] Jargão/abreviações explicados no contexto onde aparecem?
- [ ] Informação densa decomposta (tabelas → cards/pills/grupos quando > 5 itens)?
- [ ] Estados do sistema visíveis sem que o usuário lembre (nada "deve estar óbvio")?
- [ ] Zero custo de memória desnecessário (nada depende de lembrar de outra seção sem pista)?

**2. Persona-based red flags (critique contra as personas do brief)** — pegue as personas do research (ou infira do brief) e pergunte por persona:
- [ ] Esta persona consegue completar o objetivo principal nesta tela? Onde ela trava?
- [ ] A linguagem/tonalidade fala com esta persona ou com outra?
- [ ] Que decisão esta persona toma aqui, e o que falta para ela decidir com confiança?
- [ ] Cenário de borda desta persona (usuário de leitor de tela, iniciante, apressado) está coberto?

Reporte achados dessas lentes na mesma lista priorizada (com severidade). Não as rode quando o brief é curto demais para personas — registre "não aplicável" e siga.

## Saída esperada

Critique report completo (pontos fortes, problemas com severidade, lista priorizada, nota geral, veredito). O veredito é uma das opções: `aprovado`, `aprovado com minors`, `requer correções`, `blocker`.

## Exemplo

**Exemplo real:** `docs/casos/brisa/critique.md` (caso Brisa, 2026-08-25).

Veredito: **`aprovado com minors`** (média 4.2/5) — 1 major (pausa — a maior dor da persona — escondida em texto secundário no rodapé do card) + 2 minors (contraste marginal do stepper ativo, selo em `--color-text-muted`). Regra de tokens verificada como item obrigatório (somente `--color-*`/`--space-*`/`--radius-*`/`--shadow-*`, sem hex).

## Auto-verificação

- [ ] Regra de tokens verificada (grep por hex hardcoded e valores fora da escala do kit) — item obrigatório
- [ ] **AI tells verificados** (grep por `—`, `–`, fake screenshots, 3 cards iguais, Inter, nomes genéricos, eyebrows em excesso) — item obrigatório
- [ ] Crítica contra o brief (problem statement/personas), não contra gosto pessoal
- [ ] Cada problema tem localização + descrição + correção sugerida + severidade
- [ ] Nenhum julgamento vago ("não ficou bom") — sempre onde / o quê / por quê / como corrigir
- [ ] Critério de parada aplicado: sem blockers, média ≥ 4, nenhuma heurística < 3
- [ ] Veredito em um dos formatos: `aprovado` / `aprovado com minors` / `requer correções` / `blocker`

## Qualidade

- Crítica contra o brief, com localização e correção sugerida para cada problema.
- Nenhum julgamento vago ("não ficou bom") — sempre "onde / o quê / por quê / como corrigir".
- Verificação de tokens do kit sempre presente (regra do produto).
