> 🌐 English version available: [README.md](README.md)

# Design Kit — o setor de design em uma caixa

> **v0.9.0** (pré-1.0) · pt-BR · Um pacote que transforma qualquer agente de IA
> (Claude, Codex, pi) em um setor de design executável: pesquisa, arquitetura de
> informação, UI, critique, acessibilidade e handoff — sem contratar um setor.

**Tagline:** você dá a ideia; o agente faz o design, critica o próprio trabalho
e só entrega o que passa no controle de qualidade.

---

## O que é

O **Design Kit** é um pacote de **design system** (tokens + componentes) +
**skills empacotadas** + **arquivos de onboarding** (`AGENTS.md` / `CLAUDE.md`)
que transforma qualquer agente-hospedeiro — Claude, Codex, pi, Cursor — em um
**setor de design inteiro**. Em vez de contratar (ou ser) o designer, o
programador e o revisor, você conversa com o seu agente e ele executa o ciclo
completo: de uma ideia em uma frase até telas prontas para desenvolvimento, com
crítica e auditoria de acessibilidade no meio.

O **humano é o diretor**: você decide o que fazer e aprova em dois checkpoints
obrigatórios (antes das telas e antes do handoff). O **agente é o setor**:
executa, revisa o próprio trabalho em loops fechados e só avança quando não há
bloqueadores.

Um **limite honesto**: pesquisa primária com pessoas reais (entrevistas, testes
de usabilidade, dados analíticos) **não é substituída**. O agente estrutura,
sintetiza e transforma o que você fornece — e marca o que faltar como
`[assunção]`. O que ele substitui é a *execução* de design.

## Como funciona

O agente percorre o fluxo de um setor de design, em fases, com dois checkpoints
de aprovação humana:

```
brief → research → concept/IA → ⏸️ VOCÊ APROVA → UI v1 → critique → refine
→ a11y/QA → ⏸️ VOCÊ APROVA → handoff
```

- **Loops fechados de qualidade:** critique e a11y corrigem → re-revisam → seguem
  (máx. 2 rodadas de refine antes de escalar a você).
- **Consistência por tokens:** toda UI gerada consome **somente** `var(--...)`
  de `styles/tokens.css` — nunca cores/espaçamentos/raios mágicos. Padrões novos
  viram tokens novos no kit.
- **Qualidade "impeccable":** HTML semântico, contraste WCAG AA, foco visível,
  teclado, mobile-first, zero lorem ipsum.

## O que tem dentro

| Camada | Conteúdo | Onde |
|---|---|---|
| **Design system** | 130+ tokens (cor, tipografia, espaçamento, raio, sombra, motion, z-index) claro/escuro; componentes: botões, badges, cards, alerts, formulários, tooltip, modal, tabs, progress, skeleton, avatar, dropdown, breadcrumb, tabela, stepper | `styles/`, `index.html` (showcase vivo com 14 seções) |
| **8 skills** | `design-researcher`, `information-architect`, `ui-designer`, `design-redesign`, `design-critic`, `design-refine`, `a11y-auditor`, `design-handoff` — originais com SKILL.md + templates/; wrappers com fallback embutido | `skills/` |
| **Voz do design** | Manual anti-slop do kit: tells da IA, dials, locks e pre-flight (método impeccable + design-taste) | `DESIGN.md` |
| **QA determinístico** | `smoke-test.py` (8 checks de integridade) · `anti-slop-check.py` (98 checks mecânicos em 14 arquivos) | `scripts/` |
| **3 templates** | `brief.md`, `critique-report.md`, `spec-handoff.md` | `templates/` |
| **Casos validados** | Lumen (critique 4.7/5) · Norte (4.6/5, reusa 12 grupos do kit) · Brisa · Aurora (anti-slop) · Linha Direta (block library) · Redesign Demo · Tereza (Experience) | `docs/casos/` |
| **Docs** | Arquitetura do agente, guia de uso (para humanos), docs por grupo de componentes, checklist de distribuição | `docs/` |
| **Portabilidade** | `CLAUDE.md` + `.claude/skills/` (Claude Code), `.codex/README.md` (Codex) | raiz, `.claude/`, `.codex/` |

## Quickstart

O pacote é um diretório de skills + um arquivo de onboarding. Você o entrega ao
seu agente e ele passa a agir como o setor de design. Sem build, sem npm, sem
instalação.

### No pi (recomendado para começar)

```bash
# 1. Copie as skills para onde o pi as descobre
cp -r skills/ ~/.pi/agent/skills/designkit/
# 2. Rode o pi dentro do diretório do designkit (ele lê AGENTS.md)
pi
```

### No Claude Code

```bash
# Abra o Claude Code na raiz do designkit — ele lê CLAUDE.md e
# descobre as skills em .claude/skills/ automaticamente
claude
```

### No Codex (OpenAI)

```bash
# Abra o Codex na raiz do designkit — ele lê AGENTS.md (formato nativo).
# As skills ficam em skills/ e são lidas nas etapas do fluxo (ver .codex/README.md)
codex
```

> **Portabilidade:** o mesmo diretório de skills funciona nos três agentes; a
> única adaptação é o arquivo de onboarding (`AGENTS.md` ↔ `CLAUDE.md`). Veja
> `docs/guia-de-uso.md` para o passo a passo completo.

## Exemplos de prompts

```text
Crie uma landing page para meu produto: um app de organização de refeições
para quem mora sozinho. Público: jovens adultos (25–35), que cozinham pouco
e comem comida entregue. Tom: calmo, acolhedor, nada de "startup hype".
```

```text
Faça critique da minha tela abaixo. Quero saber o que está confuso, o que
está bom, e uma lista do que corrigir primeiro.

[cole aqui o HTML/CSS ou uma descrição detalhada da tela]
```

```text
Audite a acessibilidade deste formulário de cadastro e corrija o que estiver
em nível AA do WCAG.
```

```text
Gere o spec de handoff da landing page que aprovamos: o que o dev precisa
para implementar, componente por componente, usando os tokens do designkit.
```

## Roadmap

| Fase | Estado |
|---|---|
| **1–2. Fundação + shell** — tokens, base, showcase | ✅ |
| **3. Arquitetura do agente** — 8 funções do setor → papéis do agente, roadmap A–F | ✅ |
| **4. Componentes** — A/B/C + avançados (dropdown, breadcrumb, tabela, stepper, paginação) | ✅ |
| **A. Prova de conceito** — caso Lumen ponta a ponta, critique aprovado | ✅ |
| **B. Skills originais** — researcher, IA, redesign, refine, handoff + wrappers | ✅ |
| **C. Onboarding + orquestração** — AGENTS.md, DESIGN.md, CLAUDE.md, .codex, guia de uso | ✅ |
| **D. Docs de componentes + block library** | ✅ |
| **E p1/p2. Portabilidade multi-agente** — estática + executada no pi | ✅ |
| **F. Distribuição** — publicado no GitHub, tag v0.9.0 | ✅ |
| **E p3. Validação runtime** no Claude Code e Codex | ⬜ (bloqueia 1.0.0) |
| **Decisões do fundador** — agentes-alvo, escopo de pesquisa, imagens, licença, nome | ⬜ (bloqueiam 1.0.0) |

## Vitrine ao vivo

O showcase do design system (tokens, componentes e demonstrações) roda em:
- **Portal de design cases resolvidos:** https://murioliveira.github.io/designkit/portal/
- **Showcase do design system:** https://murioliveira.github.io/designkit/
- **Local:** abra `index.html` ou `portal/index.html` no navegador (sem build, sem dependências)

## Como contribuir / estrutura do repo

```
designkit/
├── AGENTS.md / CLAUDE.md      ← onboarding do agente (setor de design)
├── DESIGN.md                  ← voz do design: manual anti-slop
├── index.html                 ← showcase vivo do design system (14 seções)
├── styles/
│   ├── tokens.css             ← FONTE DE VERDADE visual (claro/escuro)
│   ├── base.css               ← reset + utilitários
│   ├── layout.css             ← shell do showcase
│   └── components.css         ← componentes (9 grupos CSS)
├── js/app.js                  ← tema, menu mobile, scrollspy, demos
├── scripts/
│   ├── smoke-test.py          ← 8 checks de integridade
│   └── anti-slop-check.py     ← detector determinístico de tells (98 checks)
├── docs/
│   ├── arquitetura-agente-design.md
│   ├── guia-de-uso.md
│   ├── distribuicao.md        ← checklist de release v1.0.0
│   ├── blocos/                ← block library (composições + dials)
│   ├── componentes/           ← handoff por grupo
│   ├── casos/                 ← 7 casos reais validados
│   └── trend-critiques.md     ← histórico de critiques (memória do setor)
├── skills/                    ← papéis do setor (SKILL.md + templates)
├── templates/                 ← brief, critique-report, spec-handoff
├── .claude/skills/            ← wrappers de descoberta (Claude Code)
└── .codex/                    ← instruções de portabilidade (Codex)
```

Regras de trabalho (detalhe no `AGENTS.md`): tokens como única fonte de verdade;
um writer por arquivo; sem build tooling; loops de qualidade fechados.

## Licença

**MIT** — placeholder, a confirmar pelo fundador antes do v1.0.0 (ver
`docs/distribuicao.md`).

---

🌐 This project also exists in English: [README.md](README.md)
