# Arquitetura — Agente de IA que substitui um setor de design

> **Visão do fundador:** "um agente de IA que substitui um setor de design inteiro, assim outros humanos conseguem gerar UI, designs, critiques etc. a partir do próprio Claude, Codex e etc."
>
> **Estado atual do projeto (atualizado em 2026-08-25, pós-QA):** `designkit` tem fundação sólida — `styles/tokens.css` (~147 tokens semânticos claro/escuro), `base.css`, `layout.css` (shell do showcase), `index.html` (13 seções), `js/app.js` (tema, menu, scrollspy, demos, overlays) e `styles/components.css` (~1876 linhas com 9 seções completas: botões, badges, cards, alertas, demo, formulários, acessibilidade, overlays, dropdown/breadcrumb/tabela/stepper). Caso Lumen aprovado (critique v2 4.7/5), auditoria a11y aplicada (10 correções) e skills empacotadas.
>
> **Skills de base disponíveis no ambiente:** `impeccable` (design direction, critique, audit, polish, extract de tokens) e `web-design-engineer` (build de UI polida) — ambas em `~/.pi/agent/skills/` — e `maestri` (orquestração multi-agente no canvas).

---

## 1. Escopo do setor de design a substituir

Um setor de design típico executa 8 funções. O mapeamento para capacidades do agente:

| # | Função do setor | O que faz | Capacidade do agente | Origem da capacidade |
|---|---|---|---|---|
| 1 | Research / discovery | Entrevistas, personas, jornadas, análise de concorrência, definição de problema | **design-researcher**: transforma um brief bruto em problem statement, personas, jornadas e scan competitivo | Skill nova (prompts + templates); a coleta primária continua humana — o agente estrutura, sintetiza e transforma em artefatos |
| 2 | IA / informação | Sitemaps, fluxos, hierarquia, taxonomia | **information-architect**: deriva estrutura de navegação e fluxos de usuário do research | Skill nova (ou parte do researcher) |
| 3 | UI design | Telas, componentes, protótipos visuais | **ui-designer**: gera HTML/CSS/JS/React com a estética do designkit | `web-design-engineer` + tokens do designkit |
| 4 | Design system | Tokens, componentes, diretrizes | **design-system-keeper**: mantém e aplica `tokens.css` + componentes; extrai tokens de UI existente | `impeccable extract` + `styles/tokens.css` já existente |
| 5 | Critique / review | Sessões de crítica, heurísticas, priorização | **design-critic**: review com scoring por heurísticas e lista priorizada de correções | `impeccable critique` |
| 6 | Acessibilidade | Auditoria WCAG, contraste, foco, leitores de tela | **a11y-auditor**: auditoria técnica com correções | `impeccable audit` |
| 7 | QA visual | Pixel-check, responsividade, cross-browser | **visual-qa**: verificação em navegador, batched pass (desktop + mobile), fix em lote | `impeccable audit/polish` + workflow de browser |
| 8 | Handoff para dev | Specs, documentação, export de assets/tokens | **design-handoff**: spec de implementação, doc por componente, export de tokens | Skill nova + templates |

**Limite honesto (decisão do fundador):** pesquisa primária (entrevistas, testes com usuários reais, dados analíticos) **não é substituível** — o agente sintetiza o que recebe. O "setor substituído" é o de execução de design (2–8) + a parte de síntese de research (1). Isso precisa estar explícito no posicionamento para não gerar expectativa errada.

---

## 2. Forma do produto — recomendação: pacote de skills + AGENTS.md (não CLI, não só biblioteca)

**Recomendado: pacote de agent files/skills carregável pelos agentes-alvo (Claude, Codex, pi).**

Racional:
- O alvo é "outros humanos geram UI/designs/critiques **a partir do Claude, Codex etc.**" → o produto é algo que esses agentes **carregam**, não um app separado.
- **CLI** (ex.: `npx design-agent`) exige instalação, build e manutenção, e fica fora do fluxo natural do usuário — rejeitado como forma primária (pode existir depois como conveniência).
- **Biblioteca de componentes isolada** cobre só a função 3/4 — não faz critique, research ou handoff. Rejeitada como forma única; o designkit vira **submódulo** do pacote.
- **Skills + AGENTS.md** é o formato nativo: Claude Code (`.claude/skills` + `CLAUDE.md`), Codex (`AGENTS.md`), pi (`skills/` + `SKILL.md`), Cursor (`.cursor/rules`). Um diretório de skills é portável entre eles com adaptação mínima do arquivo de onboarding.

**Estrutura proposta do produto (a "caixa"):**

```
designkit/                      ← já é o repositório raiz
├── AGENTS.md                   ← onboarding: "você é o setor de design" + fluxo + papéis
├── docs/
│   ├── arquitetura-agente-design.md   ← este documento
│   └── guia-de-uso.md          ← como um humano carrega/usa (fase 6)
├── design-system/              ← o designkit atual (index.html + styles/ + js/)
├── skills/                     ← papéis empacotados como skills portáteis
│   ├── design-researcher/
│   ├── information-architect/
│   ├── ui-designer/            ← wrapper sobre web-design-engineer
│   ├── design-critic/          ← wrapper sobre impeccable critique
│   ├── a11y-auditor/           ← wrapper sobre impeccable audit
│   └── design-handoff/
└── templates/                  ← brief, spec, critique report, handoff (markdown)
```

Cada skill: `SKILL.md` (frontmatter + instruções) + `references/` + `templates/`. Os "wrappers" (`ui-designer`, `design-critic`, `a11y-auditor`) delegam às skills de base do ambiente quando presentes e documentam fallback (instruções embutidas) quando ausentes — assim o pacote não quebra fora do pi.

---

## 3. Arquitetura do agente

### Papéis internos

| Papel | Entrada | Saída |
|---|---|---|
| `design-researcher` | Brief cru (ideia, público, contexto) | Problem statement, personas, jornada, scan de concorrência, brief de design |
| `information-architect` | Brief de design | Sitemap, fluxos de usuário, hierarquia de conteúdo |
| `ui-designer` | Brief + IA + tokens | HTML/CSS/JS das telas, consumindo tokens do designkit |
| `design-critic` | Telas + brief | Review com scoring por heurística (clareza, hierarquia, consistência, affordance) + lista priorizada |
| `a11y-auditor` | Telas | Auditoria WCAG 2.2 AA (contraste, foco, semântica, teclado) + correções |
| `visual-qa` | Telas | Verificação em browser desktop+mobile, batched fixes |
| `design-handoff` | Telas + tokens | Spec de implementação, doc por componente, export de tokens |

### Fluxo de trabalho típico

```
brief → research → concept/IA → UI (v1) → critique → refine → a11y+QA → handoff
   │        │           │            │         │        │           │
   └────────┴───────────┴────────────┴─────────┴────────┴───────────┴──→ relatório final
```

- **Orquestração:** o AGENTS.md instrui o agente-hospedeiro a percorrer o fluxo **em fases**, com checkpoint de aprovação humana entre research→UI e UI→handoff (o humano é o diretor; o agente é o setor).
- **Loops de qualidade:** critique e a11y rodam como loops fechados — corrigir → re-revisar → seguir. Sem aprovação explícita, o ciclo para no critério do critique (ex.: sem blocker ≥ threshold).
- **Consistência:** toda UI gerada **consome apenas tokens semânticos** de `tokens.css` (regra já adotada no designkit); o `design-critic` verifica essa regra como item de critique; UIs existentes sem tokens passam por `impeccable extract` para virar tokens novos no kit.

### Como o design system é consumido

1. `tokens.css` é a **única fonte de verdade visual** — o ui-designer lê os tokens antes de gerar qualquer cor/tipo/espaçamento.
2. Componentes prontos (fases 3–5, a construir) servem como **referência de padrão**: botão, card, input etc. — o agente copia o padrão, não reinventa.
3. Qualquer nova UI que gere um padrão ausente → proposta de token/componente novo → aprovação → entra no kit (o agente mantém o próprio design system, como um setor real).

---

## 4. Roadmap de construção (ordem de dependência)

**Fase A — Prova de conceito (1 caso real, valida o conceito antes de empacotar):**
Entregáveis: AGENTS.md de onboarding mínimo; fluxo executado manualmente pelo orquestrador usando as skills existentes (impeccable + web-design-engineer) num caso real (ex.: landing page de um produto fictício do fundador); artefatos do caso (brief → telas → critique → refine → handoff) salvos em `docs/casos/`. Critério de sucesso: o fundador aprova as telas finais.

**Fase B — Skills originais (as que não existem como base):**
Entregáveis: `skills/design-researcher/`, `skills/information-architect/`, `skills/design-handoff/` com SKILL.md + templates (brief, persona, jornada, spec, critique report). Wrappers `ui-designer`, `design-critic`, `a11y-auditor` apontando para as skills de base. Critério: cada skill executável de forma isolada num mini-caso.

**Fase C — AGENTS.md completo + orquestração:**
Entregáveis: AGENTS.md final com papéis, fluxo, checkpoints humanos, regra de tokens, critérios de critique; `docs/guia-de-uso.md`. Critério: um agente (pi primeiro, depois Claude Code/Codex) executa o fluxo completo sem intervenção do orquestrador além dos checkpoints.

**Fase D — Componentes do designkit (fases 3–5 do backlog original):**
Entregáveis: componentes A (buttons/badges/cards/alerts), B (forms), C (overlays) em `components.css` + playgrounds no showcase + docs por componente. Critério: showcase completo navegável; componentes aprovados pelo critique.

**Fase E — Validação multi-agente e refinamento:**
Entregáveis: portar o pacote para Claude Code (CLAUDE.md + `.claude/skills`) e Codex (AGENTS.md); rodar o caso da Fase A nos 3 agentes; comparar e iterar. Critério: mesma qualidade aproximada em 2+ agentes-alvo.

**Fase F — Distribuição:**
Entregáveis: README do pacote, instruções de instalação por agente, versão 1.0.0.

> **Nota de paralelismo:** A e B dependem apenas das skills de base (já existentes) — começam já. C depende de A/B. D é paralela a A–C (não depende de nada além do tokens.css pronto). E/F dependem de C+D.

---

## 5. Riscos e decisões em aberto

### Decisões que precisam do fundador

1. **Agentes-alvo prioritários:** Claude Code, Codex, pi, Cursor? (Define qual formato de onboarding testar primeiro — recomendo pi primeiro por já ter as skills de base, depois Claude Code.)
2. **Escopo de pesquisa (função 1):** o agente só sintetiza (sem entrevistas reais)? Ou o produto também oferece "roteiros de entrevista + síntese" para o humano conduzir? Recomendo: roteiros + síntese, coleta humana.
3. **Geração de imagens/assets:** incluir geração de ilustrações/imagens (ex.: via API de imagem) ou restringir a UI HTML/CSS + SVG procedural? Recomendo v1 sem geração de imagem externa (SVG inline + placeholders), decidir depois.
4. **Posicionamento/comercial:** open-source com vitrine (o showcase é o "portfólio" do agente) vs. produto comercial. Impacta roadmap de distribuição.
5. **Dependência das skills de base:** usar `impeccable`/`web-design-engineer` (Apache 2.0 / livres) como dependências documentadas vs. embutir versões resumidas no pacote para portabilidade. Recomendo: dependência documentada no pi, fallback embutido resumido para outros agentes.
6. **Nome do produto** (hoje: "Design Kit" / "setor de design").
7. **Limite ético/expectativa:** como comunicar que é um setor de design aumentado por IA, sem prometer substituição de pesquisa primária nem "design validado com usuários" sem dados reais.

### Riscos técnicos

- **Portabilidade de formato de skills entre agentes** (SKILL.md vs CLAUDE.md vs AGENTS.md) — mitigado pelos wrappers com fallback embutido (Fase E valida).
- **Qualidade degradada sem humano no loop** — mitigado pelos loops fechados de critique/a11y e pelos checkpoints obrigatórios do AGENTS.md.
- **Manutenção do kit como referência de padrão** — o designkit agora tem componentes completos (9 seções em `components.css`); o risco passa a ser manter o kit em sincronia com padrões novos extraídos de casos reais (via `impeccable extract`, fluxo da arquitetura §3).
- **`impeccable` exige browser/setup** para audit — verificar disponibilidade de navegador no ambiente dos agentes-alvo; fallback = auditoria estática.

### Assunções

- O usuário final é humano não-designer, não necessariamente dev — o onboarding precisa ser "dê uma ideia, receba UI + critique + spec".
- O orquestrador (este papel) continua mantendo o designkit e o pacote de skills como código real no repositório.

---

## Resumo executivo (para o fundador)

1. **Produto:** um pacote de skills + AGENTS.md que transforma qualquer agente (Claude, Codex, pi) em um "setor de design" executável — não um CLI nem só uma biblioteca.
2. **8 funções do setor → 7 papéis do agente**, com as skills `impeccable` e `web-design-engineer` como base de UI/critique/a11y já prontas no ambiente.
3. **Fluxo:** brief → research → IA → UI → critique → refine → a11y/QA → handoff, com checkpoints humanos e loops fechados de qualidade.
4. **Consistência:** o `tokens.css` do designkit é a única fonte de verdade; toda UI gerada consome tokens; padrões novos entram no kit via extract.
5. **Roadmap:** Fase A (prova de conceito com 1 caso real) e B (skills novas) começam já; D (componentes) é paralela; C/E/F empacotam e validam multi-agente.
6. **Principais decisões do fundador:** agentes-alvo prioritários, escopo da pesquisa (síntese vs. coleta), geração de imagens, open-source vs. comercial, e o limite ético do "substituir um setor".
7. **Próximo passo imediato:** executar a Fase A — montar o AGENTS.md mínimo e rodar um caso real de ponta a ponta usando as skills existentes.
