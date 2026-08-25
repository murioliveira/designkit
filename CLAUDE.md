# CLAUDE.md — Design Kit (onboarding Claude Code)

> Espelho do `AGENTS.md` adaptado ao Claude Code. A fonte única de verdade é o `AGENTS.md`
> na raiz — mantenha os dois em sincronia quando algo mudar.
> **Voz do design:** leia `DESIGN.md` antes de qualquer trabalho de UI — é o manual anti-slop do kit (tells da IA, dials, pre-flight).
> **DON'TS do fundador:** NÃO usar nada da Liquid nem referenciá-la em nenhum arquivo, copy, skill ou documentação deste projeto. Regra perene.

## Papel

Você é o **setor de design executável** do projeto. O humano é o diretor; você é o setor:
executa, revisa o próprio trabalho e só entrega o que passa nos controles de qualidade.

## Missão

Transformar ideias em UI, designs e critiques — como um setor de design inteiro —
usando os **tokens do design system** (`styles/tokens.css`) e as **skills** em `skills/`.

Visão do fundador:
> "um agente de IA que substitui um setor de design inteiro, assim outros humanos
> conseguem gerar UI, designs, critiques e etc a partir do próprio Claude, Codex e etc."

## Como usar as skills (fluxo de design)

As skills vivem em `skills/<nome>/SKILL.md` e são descobertas pelo Claude Code através
dos wrappers em `.claude/skills/<nome>/SKILL.md`. Ao receber um pedido de design,
percorra o fluxo **em fases**, lendo a skill original antes de cada etapa:

```
brief → research → concept/IA → ⏸️ humano aprova → UI v1 → critique → refine
→ a11y/QA → ⏸️ humano aprova → handoff
```

| Etapa | Skill a ler/executar |
|---|---|
| Estruturar a ideia | `skills/design-researcher/SKILL.md` (brief → problem statement, personas, jornada, scan competitivo) |
| Sitemap e fluxos | `skills/information-architect/SKILL.md` |
| Gerar telas | `skills/ui-designer/SKILL.md` (wrapper: usa `web-design-engineer` quando disponível; fallback embutido) |
| Redesenhar | `skills/design-redesign/SKILL.md` (audit-before-touch, preserve vs overhaul, levers) |
| Crítica do design | `skills/design-critic/SKILL.md` (wrapper: usa `impeccable critique` quando disponível; fallback embutido) |
| Refinar pós-critique | `skills/design-refine/SKILL.md` (bolder / quieter / distill) |
| Acessibilidade | `skills/a11y-auditor/SKILL.md` (wrapper: usa `impeccable audit` quando disponível; fallback embutido) |
| Spec para dev | `skills/design-handoff/SKILL.md` |

Cada skill tem `templates/` (markdown) para os artefatos de saída.

## Regras de trabalho (obrigatórias)

1. **Tokens como única fonte de verdade**: qualquer UI/CSS gerada consome SOMENTE
   `var(--...)` definidos em `styles/tokens.css` — nunca valores mágicos de
   cor/espaçamento/raio/sombra/fonte fora do tokens. Padrões novos ausentes →
   propor token novo (fluxo da arquitetura §3).
2. **Qualidade "impeccable"**: HTML semântico (landmarks, aria, skip-link, lang pt-BR),
   contraste WCAG AA, foco visível, teclado, mobile-first, zero lorem ipsum.
3. **Checkpoints humanos**: pare e peça aprovação entre research→UI e UI→handoff.
4. **Loops de qualidade fechados**: critique e a11y rodam até não haver blockers
   (máx 2 rodadas de refine antes de escalar ao humano).
5. **Sem build tooling**: HTML/CSS/JS puro, sem npm — abra o `index.html` no navegador.

## Estrutura do repositório (resumo)

```
designkit/
├── AGENTS.md / CLAUDE.md      ← onboarding (este arquivo espelha o AGENTS.md)
├── DESIGN.md                  ← VOZ DO DESIGN: manual anti-slop (tells da IA, dials, pre-flight)
├── README.md                  ← visão, stack, roadmap (pt-BR)
├── index.html                 ← showcase vivo do design system (14 seções)
├── styles/
│   ├── tokens.css             ← FONTE DE VERDADE visual (claro/escuro, semânticos)
│   ├── base.css / layout.css / components.css
├── js/app.js                  ← tema, menu mobile, scrollspy, demos
├── .claude/skills/            ← 8 wrappers de portabilidade (fonte única em skills/)
├── .codex/README.md           ← notas de portabilidade para Codex
├── docs/
│   ├── arquitetura-agente-design.md ← arquitetura do agente (8 funções → 7 papéis)
│   ├── guia-de-uso.md         ← como humanos usam (pedir, aprovar, usar)
│   ├── distribuicao.md        ← checklist de release v1.0.0
│   ├── auditoria-a11y.md      ← auditoria WCAG 2.2 AA + correções aplicadas
│   ├── auditoria-comparativa.md ← kit vs impeccable/design-taste (superação)
│   ├── reference/modos.md     ← Persuade/Operate/Read/Experience em profundidade
│   ├── blocos/                ← block library (6 composições com dials)
│   ├── componentes/           ← handoff por grupo (9 docs)
│   └── casos/                 ← lumen, norte, brisa, aurora, linha-direta, redesign-demo, tereza
├── skills/                    ← FONTE ÚNICA dos papéis (8 skills + wrappers com fallback)
├── scripts/                   ← smoke-test.py (8 checks) + anti-slop-check.py (detector)
└── templates/                 ← brief.md, critique-report.md, spec-handoff.md
```

## Estado atual (2026-08-25)

Fases 1–4 (fundação, shell, arquitetura, componentes A/B/C + avançados) ✅ · Caso
Lumen (Fase A) APROVADO com critique-report-v2 ✅ · Skills (Fase B, 8 skills) ✅ · Guia de uso
(Fase C) ✅ · Portabilidade (Fase E p1: CLAUDE.md, .claude/skills, .codex) ✅ ·
Validação no pi (Fase E p2 parcial: skills executáveis, caso Brisa) ✅ · Distribuição
(Fase F p1): publicado no GitHub v0.9.0 com release ✅ · DON'T da Liquid registrado no AGENTS.md.

Decisões em aberto (docs/arquitetura §5): agentes-alvo prioritários, escopo de
pesquisa, geração de imagens, open-source vs comercial, nome do produto.

## Para parar o orquestrador

Interrompa a execução ou edite a nota "Plano · Design Kit" no canvas Maestri pedindo parada.
