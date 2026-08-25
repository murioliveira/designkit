# AGENTS.md — Design Kit

> Espelhado da role Maestri "Orquestrador" e sincronizado com o estado atual do projeto.
> Última sincronização: 2026-08-25 (ver nota "Plano · Design Kit" no canvas Maestri).
> **Voz do design:** leia `DESIGN.md` antes de qualquer trabalho de UI — é o manual anti-slop do kit (método impeccable + design-taste).
> **DON'TS do fundador (nota "donts" no canvas):** NÃO usar nada da Liquid nem referenciá-la em nenhum arquivo, copy, skill ou documentação deste projeto. Regra perene.

## Papel (espelho do AGENTS.md da role)

<your_assigned_role>
Comanda o processo e subagentes como um maestro. Rode indefinidamente, só pare até um humano pedir.
</your_assigned_role>

<working_directory>
IMPORTANT: You were started in this directory to receive the above role assignment. The actual project you should be working on is located at:
C:\Users\muzph\projetos\designkit
</working_directory>

## Missão do projeto

Construir um **agente de IA que substitui um setor de design inteiro**: humanos geram UI, designs e critiques a partir do próprio Claude, Codex, pi etc. O `designkit` é o produto — um pacote de **design system (tokens + componentes)** + **skills empacotadas** + **AGENTS.md de onboarding** que transforma qualquer agente-hospedeiro em um setor de design executável.

Visão do fundador (nota "tarefas-do-humano" no canvas):
> "um agente de IA que substitui um setor de design inteiro, assim outros humanos conseguem gerar UI, designs, critiques e etc a partir do próprio Claude, Codex e etc."

## Estrutura do repositório

```
designkit/
├── AGENTS.md                        ← este arquivo (onboarding/orquestração)
├── README.md                        ← visão, stack, roadmap (pt-BR)
├── index.html                       ← showcase vivo do design system (14 seções)
├── DESIGN.md                        ← VOZ DO DESIGN: manual anti-slop (tells da IA, dials, pre-flight)
├── styles/
│   ├── tokens.css                   ← FONTE DE VERDADE visual (claro/escuro, semânticos)
│   ├── base.css                     ← reset + utilitários (.container, .sr-only, flex)
│   ├── layout.css                   ← shell (header, sidebar, scrollspy, responsivo)
│   └── components.css               ← componentes (§1-9: botões, badges, cards, alerts, forms, overlays, avançados)
├── js/app.js                        ← tema, menu mobile, scrollspy, demos, overlays
├── CLAUDE.md                        ← onboarding para Claude Code
├── .claude/skills/                  ← 8 wrappers de portabilidade (fonte única em skills/)
├── .codex/README.md                 ← notas de portabilidade para Codex
├── docs/
│   ├── arquitetura-agente-design.md ← arquitetura do agente (8 funções → 7 papéis)
│   ├── guia-de-uso.md               ← como humanos usam (onboarding)
│   ├── distribuicao.md              ← checklist de release v1.0.0
│   ├── auditoria-a11y.md            ← auditoria WCAG 2.2 AA + correções aplicadas
│   ├── auditoria-comparativa.md     ← kit vs impeccable/design-taste (superação)
│   ├── reference/modos.md           ← Persuade/Operate/Read/Experience em profundidade
│   ├── blocos/                      ← block library (6 composições com dials)
│   ├── componentes/                 ← handoff por grupo (9 docs)
│   └── casos/                       ← lumen, norte, brisa, aurora (anti-slop), linha-direta (blocos), redesign-demo (before→after)
├── skills/                          ← papéis do agente como skills portáteis
│   ├── design-researcher/           ← brief → problem statement, personas, jornadas
│   ├── information-architect/       ← sitemap, fluxos, hierarquia
│   ├── ui-designer/                 ← wrapper sobre web-design-engineer (+fallback)
│   ├── design-redesign/             ← protocolo de redesign (audit-before-touch, levers)
│   ├── design-critic/               ← wrapper sobre impeccable critique (+fallback)
│   ├── design-refine/               ← bolder / quieter / distill (refinamento pós-critique)
│   ├── a11y-auditor/                ← wrapper sobre impeccable audit (+fallback)
│   └── design-handoff/              ← spec, doc por componente, export de tokens
├── scripts/
│   ├── smoke-test.py                ← 8 checks de integridade (tokens, HTML, skills...)
│   └── anti-slop-check.py           ← detector determinístico de AI tells (49 checks)
└── templates/                       ← brief.md, critique-report.md, spec-handoff.md
```

## Regras de trabalho (obrigatórias)

1. **Tokens como única fonte de verdade**: qualquer UI/CSS gerada consome SOMENTE `var(--...)` definidos em `styles/tokens.css` — nunca valores mágicos de cor/espaçamento/raio/sombra/fonte fora do tokens. Padrões novos ausentes → propor token novo via `impeccable extract` (fluxo da arquitetura §3).
2. **Qualidade "impeccable"**: HTML semântico (landmarks, aria, skip-link, lang pt-BR), contraste WCAG AA, foco visível, teclado, mobile-first, zero lorem ipsum.
3. **Fluxo de design** (quando gerando UI): brief → research → IA/concept → UI → critique → refine → a11y/QA → handoff, com checkpoint humano entre research→UI e UI→handoff.
4. **Loops de qualidade fechados**: critique e a11y rodam até não haver blockers (máx 2 rodadas de refine antes de escalar ao humano).
5. **Um writer por arquivo**: workers paralelos não podem tocar os mesmos arquivos (escopos disjuntos); o orquestrador integra.
6. **Sem build tooling**: HTML/CSS/JS puro, sem npm — o showcase abre direto no navegador.

## Estado atual do backlog (2026-08-25, pós-QA)

- ✅ Fase 1 — Fundação: tokens.css (~147 tokens), base.css, README
- ✅ Fase 2 — Shell do showcase: index.html (14 seções), layout.css, app.js (tema/menu/scrollspy)
- ✅ Fase 3 — Arquitetura: docs/arquitetura-agente-design.md (7 papéis, roadmap A–F)
- ✅ Fase 4A — Componentes A: buttons, badges, cards, alerts
- ✅ Fase 4B — Componentes B: forms (inputs, select, checkbox, radio, toggle, validação)
- ✅ Fase 4C — Componentes C: tooltip, modal (trap de foco), tabs ARIA, progress, skeleton, avatar
- ✅ Fase 4D — Componentes avançados (§9): dropdown, breadcrumb, tabela, stepper (components.css ~1876 ln)
- ✅ Fase A — Prova de conceito: caso Lumen (landing 100% tokens) + critique v2 APROVADO (média 4.7/5); critique-report-v2.md; caso Norte (dashboard, reuso real de 12 grupos do kit) APROVADO COM RESSALVAS 4.6/5 → refine completo
- ✅ Caso Brisa — validação das skills em execução (4/4 skills executáveis) + 3 melhorias aplicadas
- ✅ Smoke test — scripts/smoke-test.py (8 checks automatizados, PASS)
- ✅ Fase B — Skills originais: researcher, information-architect, design-handoff + wrappers ui-designer/design-critic/a11y-auditor + templates
- ✅ Fase C — AGENTS.md (este arquivo) + docs/guia-de-uso.md + CLAUDE.md + .claude/skills (8 wrappers) + .codex/README
- ✅ Fase D — docs/componentes (9 docs de handoff por grupo)
- ✅ Fase E p1 — Portabilidade multi-agente (CLAUDE.md, .claude/skills, .codex)
- ✅ Fase F p1 — Distribuição pré-1.0: README reescrito + docs/distribuicao.md
- ✅ Auditoria a11y — docs/auditoria-a11y.md + 10 correções aplicadas (2 P1, 5 P2, 3 P3)
- ⬜ Fase E p2 — Validação real nos agentes-alvo (bloqueada: decisão do fundador)
- ⬜ Fase F p2 — v1.0.0 (gates: Fase E, decisões do fundador, licença, nome)

## Decisões pendentes do fundador (docs/arquitetura §5)

Agentes-alvo prioritários · escopo de pesquisa (síntese vs coleta) · geração de imagens · open-source vs comercial · nome do produto.

## Para parar o orquestrador

Interrompa a execução do agente ou edite a nota "Plano · Design Kit" no canvas Maestri pedindo parada.
