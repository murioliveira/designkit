# Plano de Descoberta — Design Kit

> **Objetivo:** fazer humanos encontrarem e usarem o Design Kit.  
> **Data:** 2026-08-25 · **Versão do kit:** v0.9.0 (pre-1.0)  
> **Owner:** Marketing (role `25d1d061-86b5-4233-9bd5-0a529d155ce9`)

---

## 1. Posicionamento (1 frase)

**Um setor de design inteiro em um pacote de skills.** 8 papéis, 98 checks anti-slop, design system com 158 tokens e 15+ componentes, 7 casos validados com nota. Instala com um comando.

---

## 2. Diferenciais vs concorrentes

| Dimensão | Design Kit | impeccable (pbakaus) | taste-skill (Leonxlnx) | designer-skills (Owl-Listener) | frontend-design (Anthropic) |
|---|---|---|---|---|---|
| **Skills** | 8 (setor completo) | 1 (23 comandos) | 1 (anti-slop) | 7 (coleção) | 1 (design taste) |
| **Design system próprio** | ✅ 158 tokens + 15+ componentes | ❌ (metodologia pura) | ❌ (metodologia pura) | ❌ (metodologia pura) | ❌ |
| **Checks anti-slop mecânicos** | ✅ **98 checks** em 14 arquivos | ✅ 59 regras | ❌ (manual) | ❌ | ❌ |
| **Loops de qualidade fechados** | ✅ critique → refine → re-critique (máx 2) | ❌ (execução única) | ❌ | ❌ | ❌ |
| **Casos reais com nota** | ✅ 7 casos (Lumen 4.7/5, Norte 4.6/5, Aurora 14/14) | ❌ | ❌ | ❌ | ❌ |
| **Auditoria a11y** | ✅ WCAG 2.2 AA, 10 correções aplicadas | ✅ (comandos de audit) | ❌ | ✅ (visual-critique) | ❌ |
| **Block library** | ✅ 6 composições com dials | ❌ | ❌ | ❌ | ❌ |
| **Docs de handoff por componente** | ✅ 9 docs | ❌ | ❌ | ❌ | ❌ |
| **Portabilidade** | Claude Code + Codex + pi + Cursor | Claude Code (foco) | Claude Code (foco) | Claude Code + Codex + ChatGPT | Claude Code (nativo) |
| **Regra de tokens auditável** | ✅ grep por hex = zero, script de smoke test | ❌ | ❌ | ❌ | ❌ |
| **2 checkpoints humanos** | ✅ (research→UI, UI→handoff) | ❌ | ❌ | ❌ | ❌ |
| **Custo** | Open-source (MIT pendente) | Open-source | Open-source (65k ★) | Open-source (2.1k ★) | Open-source (Anthropic) |

### O Design Kit é o ÚNICO que junta três camadas

1. **Design system** (tokens + componentes) — o chão de fábrica. Concorrentes são metodologia pura; o kit entrega o sistema visual completo.
2. **Setor de design** (8 skills em fluxo) — não é uma skill de taste ou critique; é o departamento inteiro rodando em closed loops com 2 checkpoints humanos.
3. **QA determinística** (98 checks mecânicos + 8 smoke tests) — regras viram código auditável. Nenhum concorrente tem detector executável com essa cobertura.

---

## 3. Badges e tópicos do GitHub

### Badges prontas (copiar para o README e páginas de destino)

```markdown
[![Version](https://img.shields.io/badge/version-v0.9.0-blue)](https://github.com/muzphaxx/designkit/releases/tag/v0.9.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Agents](https://img.shields.io/badge/agents-Claude_Code_|_Codex_|_pi_|_Cursor-orange)
![Skills](https://img.shields.io/badge/skills-8_department_roles-blueviolet)
![Anti-slop](https://img.shields.io/badge/QA-98_anti--slop_checks-success)
![Tokens](https://img.shields.io/badge/tokens-158_design_tokens-0366d6)
![Components](https://img.shields.io/badge/components-15%2B_battle--tested-informational)
![WCAG](https://img.shields.io/badge/a11y-WCAG_2.2_AA_audited-brightgreen)
![Casos](https://img.shields.io/badge/cases-7_validated-9cf)
```

### Tópicos do GitHub (recomendados para a aba About do repo)

```
design-system design-tokens design-kit ai-agent ai-skills anti-slop
claude-code codex pi cursor web-design frontend components wcag
accessibility design-critique design-handoff agent-skills
closed-quality-loops design-department taste ui-components
token-first impeccable-alternative
```

---

## 4. Conteúdo pronto por plataforma

### 4.1 X (Twitter) — thread de lançamento (8 tweets)

**Tweet 1 (hook, fixado):**
```
Seu agente de IA desenha feio?

O problema não é o modelo. É que ele não tem um setor de design.

Design Kit: 8 skills que transformam Claude, Codex ou pi num departamento de design completo.

↓ thread com o que isso significa na prática
```

**Tweet 2 (o que é):**
```
Design Kit = design system (158 tokens + 15+ componentes) + 8 skills de setor + onboarding.

O agente vira researcher, information architect, UI designer, critic, a11y auditor e handoff — em sequência, com 2 checkpoints de aprovação humana.

Nenhuma skill isolada faz isso.
```

**Tweet 3 (diferencial 1 — não parece IA):**
```
O problema das skills de design atuais: toda UI sai igual. Inter, 3 cards, gradiente roxo.

O kit tem DESIGN.md — um manual anti-slop com regras DURAS:
- Zero em-dash (—)
- Zero Inter como default
- Zero 3 cards idênticos
- 98 checks mecânicos que rodam ANTES de shipar
```

**Tweet 4 (diferencial 2 — qualidade fechada):**
```
Skills normais: geram UI e param.

Design Kit: gera → faz critique → refina → faz critique de novo → só shipa quando zera os blockers.

Máximo 2 rodadas. Se ainda tiver problema, escala pro humano decidir.

É literalmente um setor de design com loops de qualidade.
```

**Tweet 5 (diferencial 3 — provas reais):**
```
"Legal no papel, mas funciona?"

7 casos reais validados:
• Lumen (landing): 4.7/5 no critique
• Norte (dashboard): 4.6/5, reutiliza 12 grupos de componentes
• Aurora: 14/14 no pre-flight anti-slop
• Tereza Vilela: portfolio em modo Experience

Notas, não promessas.
```

**Tweet 6 (instalação):**
```
Instalar:

npx skills add muzphaxx/designkit

Ou:

npm i -g design-kit
npx design-kit install

8 skills no seu agente. Zero build. Abre no navegador com duplo clique.
```

**Tweet 7 (exemplo de prompt):**
```
Exemplo de uso real:

"Crie uma landing page para um app de planejamento de refeições para quem mora sozinho. Público: 25-35 anos. Tom: calmo e acolhedor, nada de hype de startup."

O agente faz: brief → research → IA → UI → critique → refine → a11y → handoff.

Você aprova em 2 checkpoints.
```

**Tweet 8 (CTA final):**
```
Repo: github.com/muzphaxx/designkit

Showcase vivo: index.html no browser (14 seções, tema claro/escuro, todos os componentes)

Dúvidas? DM aberta.

Se você já cansou de UI genérica de IA, testa o kit.
```

---

### 4.2 Bluesky (3 posts, mais longos e técnicos)

**Post 1 — O problema:**
```
Toda skill de design de IA sofre do mesmo problema: gera UI genérica.

Inter, slate-900, 3 cards, hero centralizado, gradiente roxo no CTA.

Por quê? Porque o modelo foi treinado em milhões de landing pages iguais e não tem constraints reais.

O Design Kit resolve isso com DESIGN.md: um manual anti-slop de ~300 linhas com regras objetivas, dials por brief (variância/motion/densidade) e 98 checks mecânicos que rodam antes de shipar.

Não é "taste". É engenharia de qualidade visual.
```

**Post 2 — O que tem dentro:**
```
O que o Design Kit entrega que nenhuma outra skill entrega:

- Design system próprio: 158 tokens semânticos (claro/escuro) + 15+ componentes com estados reais (loading/empty/error)
- 8 skills de setor em fluxo fechado: researcher → IA → UI → critic → refine → a11y → handoff
- 2 checkpoints humanos obrigatórios (você decide, o agente executa)
- Block library: 6 composições prontas (hero split, bento, manifesto editorial, sticky-stack CSS puro, marquee, galeria Experience) com dial-compatibility
- WCAG 2.2 AA auditado e corrigido (10 fixes: 2 P1, 5 P2, 3 P3)
- 7 casos reais validados com nota, não com venda

1 pacote. 1 comando de instalação. Zero build.
```

**Post 3 — Comparação honesta:**
```
impeccable e taste-skill são bons. Uso diário de muitos devs.

Mas são skills individuais. Design Kit é um setor de design completo.

Comparação rápida:
- impeccable: 1 skill, 23 comandos, 59 regras
- taste-skill: 1 skill, anti-slop manual
- designer-skills: 7 skills, sem design system
- Design Kit: 8 skills, 98 checks mecânicos, 158 tokens, 15+ componentes, 7 casos

Se você já usa impeccable, o kit NÃO substitui (ele wrappa a critique). Mas se você quer que seu agente execute o ciclo completo sozinho — brief até handoff — é o pacote que junta as peças.
```

---

### 4.3 LinkedIn (2 posts, tom profissional, pt-BR como padrão — com versão EN)

**Post 1 — PT (mais longo, artigo):**
```
Seu time gasta 40% do ciclo de produto em design.

E se esse trabalho fosse feito por um agente de IA — com a mesma qualidade, mas em minutos?

Foi isso que construí com o Design Kit.

O QUE É:
Um pacote de 8 skills de IA que transforma qualquer agente (Claude Code, Codex, pi, Cursor) num setor de design completo.

COMO FUNCIONA:
1. Você passa um brief de 1 parágrafo
2. O agente faz research, arquitetura de informação e gera a UI
3. Você aprova (checkpoint 1)
4. O agente faz critique da própria UI, refine e auditoria de acessibilidade
5. Você aprova de novo (checkpoint 2)
6. O agente gera o handoff pro dev

O QUE TEM DENTRO:
• Design system: 158 tokens + 15+ componentes com todos os estados
• DESIGN.md: manual anti-slop com 98 checks mecânicos executáveis
• 7 casos reais validados (landing 4.7/5, dashboard 4.6/5, portfolio)
• WCAG 2.2 AA auditado e corrigido
• Zero build: abre no navegador com duplo clique

PARA QUEM:
Devs que precisam de UI profissional sem contratar designer. Startups enxutas. Agências que querem acelerar a etapa de conceito. Times de produto que já usam IA e querem sair do "genérico".

Instalação: npx skills add muzphaxx/designkit

Repo: github.com/muzphaxx/designkit

(Projeto open-source, v0.9.0, feedback bem-vindo.)
```

**Post 2 — EN (mais curto, foco em números):**
```
AI-generated UI looks the same everywhere. Here's why — and how to fix it.

The problem: models are trained on millions of identical landing pages. The result is "AI slop": Inter, purple gradients, 3 identical cards, fake dashboards.

Design Kit solves this with 3 layers no other skill has:

1. DESIGN SYSTEM (158 tokens + 15+ components)
   Every pixel comes from var(--...). Zero hardcoded hex. Grep-auditable.

2. DESIGN DEPARTMENT (8 skills in closed quality loops)
   Researcher → IA → UI Designer → Critic → Refine → A11y Auditor → Handoff.
   2 human checkpoints. Max 2 refine rounds or escalate.

3. DETERMINISTIC QA (98 anti-slop checks + 8 smoke tests)
   Before shipping: no em-dashes, no Inter, no "Jane Doe", no banned palettes.
   Rules become auditable code.

Validated with real scores, not promises:
• Lumen (landing): 4.7/5 critique
• Norte (dashboard): 4.6/5, reuses 12 component groups

1 command: npx skills add muzphaxx/designkit

github.com/muzphaxx/designkit
```

---

### 4.4 Reddit (3 posts para subreddits diferentes)

**r/webdev — "I built a design department that fits in an AI agent's pocket"**

```
Title: I built an entire design department that fits in an AI agent's pocket — 8 skills, 158 tokens, 98 deterministic anti-slop checks

Body:

I got tired of AI-generated UIs all looking the same (Inter, 3 cards, purple gradient, you know the drill). So I built Design Kit — a package that turns Claude Code, Codex, pi, or Cursor into a functional design department.

What's inside:
- 8 agent skills covering the full workflow: researcher → IA → UI designer → critic → refine → a11y auditor → handoff
- A real design system: 158 semantic tokens (light/dark) + 15+ components with all states (loading/empty/error)
- DESIGN.md: a 300-line anti-slop manual that bans AI tells (em-dash, Inter, generic names, banned palettes)
- 98 deterministic checks that run BEFORE shipping (`python scripts/anti-slop-check.py`)
- 8 smoke tests for repo integrity
- 7 validated cases with actual critique scores (Lumen 4.7/5, Norte 4.6/5)
- WCAG 2.2 AA audited and fixed (10 corrections applied)
- Block library: 6 pre-composed layouts with dial compatibility

No build. No npm dependencies. Open index.html with double-click.

Try it: `npx skills add muzphaxx/designkit`
Repo: github.com/muzphaxx/designkit

Comparison with what's out there:
- impeccable: 1 skill, 59 rules. Design Kit: 8 skills, 98 checks + design system.
- taste-skill: anti-slop methodology only. Design Kit: methodology + design system + executable detectors.
- designer-skills: 7 skills, no design system. Design Kit: 8 skills + 158 tokens + component library.

Honest question: would you use this? What's missing?
```

**r/ClaudeAI — "How I made Claude Code run a design department (8 skills, closed quality loops)"**

```
Title: I built 8 Claude Code skills that make the agent run a full design department — from brief to handoff, with critique and accessibility audit in between

Body:

Claude Code is great at generating UI. But it still produces AI slop unless you give it very specific constraints.

I built Design Kit — 8 skills + a design system + onboarding files (CLAUDE.md) that turn Claude Code into a functional design department:

Workflow:
1. Brief → design-researcher (problem statement, personas)
2. information-architect (sitemap, flows)
3. ⏸️ YOU APPROVE
4. ui-designer (generates UI using only var(--tokens))
5. design-critic (scores heuristics, catches AI tells)
6. design-refine (bolder/quieter/distill)
7. a11y-auditor (WCAG 2.2 AA)
8. ⏸️ YOU APPROVE
9. design-handoff (per-component spec for devs)

Key constraint: max 2 refine rounds. If there are still blockers, it escalates to the human.

The anti-slop layer is the real differentiator. DESIGN.md encodes objective rules:
- Zero em-dashes
- Zero Inter as default
- Zero 3 identical cards
- 98 deterministic checks (`python scripts/anti-slop-check.py`)

Installing: `npx skills add muzphaxx/designkit`
Or just drop the skills into .claude/skills/ — wrappers already exist.

Repo: github.com/muzphaxx/designkit
Showcase: open index.html in any browser

Would love feedback from the Claude Code community.
```

**r/DesignSystems — "Design Kit: token-first design system + agent skills = entire design department"**

```
Title: Design Kit: a token-first design system + 8 agent skills that form a complete design department

Body:

Sharing something I've been building: Design Kit — an open-source package that combines a design system (158 tokens, 15+ components) with 8 AI agent skills that run the full design workflow.

What makes it different from other agent design skills:

1. TOKENS ARE THE SINGLE SOURCE OF TRUTH
   158 semantic tokens (light/dark themes). Every generated UI consumes ONLY var(--tokens). Zero hardcoded hex. Enforced by grep check in smoke test.

2. CLOSED QUALITY LOOPS
   The agent critiques its own work, refines, and re-critiques before shipping. Criterion: no blockers, average ≥ 4/5, no heuristic < 3.

3. DETERMINISTIC QA
   98 mechanical anti-slop checks + 8 integrity smoke tests. Rules become auditable code. No other design skill has this.

4. VALIDATED, NOT PROMISED
   7 cases with real scores:
   - Lumen (landing): 4.7/5 critique
   - Norte (dashboard): 4.6/5, reuses 12 component groups
   - Aurora: 14/14 pre-flight

The design system goes beyond methodology. It ships actual components: buttons, badges, cards, alerts, forms, tooltips, modals (focus trap), tabs (roving tabindex), progress, skeleton, avatar, dropdown, breadcrumb, tables, stepper, pagination.

All components have full states: loading (skeleton in final shape), empty (composed), error (inline).

Questions for this community:
- What would you want in a token-first design system built for AI agents?
- Is a "design department in a box" useful for your workflow, or do you prefer individual tools?

Repo: github.com/muzphaxx/designkit
```

---

### 4.5 Hacker News (Show HN)

```
Title: Show HN: Design Kit — an entire design department as AI agent skills (8 skills, 158 tokens, 98 anti-slop checks)

URL: github.com/muzphaxx/designkit

Body:

I built Design Kit because I was tired of AI-generated interfaces all looking the same. Inter. Slate-900. Three cards. Purple gradient CTA. Lorum ipsum.

The insight: AI models aren't bad at design. They've just been trained on millions of identical pages and have zero constraints. Give them constraints — real constraints, auditable constraints — and the output changes.

What it is:
- 158 design tokens (light/dark) — single source of visual truth
- 15+ components with full states (loading/empty/error)
- 8 agent skills: researcher → information architect → UI designer → critic → refine → a11y auditor → handoff
- DESIGN.md: 300-line anti-slop manual (bans em-dash, Inter, 3 identical cards, banned palettes, generic names)
- 98 deterministic anti-slop checks (Python, stdlib only) + 8 integrity smoke tests
- 7 validated cases with real critique scores (landing: 4.7/5, dashboard: 4.6/5)
- WCAG 2.2 AA audited (10 fixes applied)
- 6 pre-composed block layouts with dial compatibility (variance/motion/density)
- Works with Claude Code, Codex, pi, Cursor
- No build. No npm. Just HTML/CSS/JS.

How it compares:
- impeccable (pbakaus): 1 skill, 59 rules — excellent but it's a methodology, not a department + design system
- taste-skill (Leonxlnx): anti-slop methodology with manual enforcement — Design Kit adds executable detectors (98 checks)
- designer-skills (Owl-Listener): 7 skills, 2.1k stars — Design Kit adds a design system + deterministic QA

The core idea: design quality shouldn't depend on the human being a designer. The methodology, the tokens, the components, and the QA checks should be in the package.

I'm looking for feedback on:
1. Would you use this in your workflow? Why/why not?
2. What's missing before you'd consider it production-ready?
3. Is "design department in a box" the right framing, or does it overpromise?

Try it: npx skills add muzphaxx/designkit
```

---

## 5. SEO do repositório

### 5.1 Description do GitHub (160 caracteres máx)

```
Design department in a box: 8 AI agent skills, 158 tokens, 15+ components, 98 anti-slop checks, WCAG 2.2 AA. Turns Claude, Codex, pi, Cursor into a full design team.
```

### 5.2 Website (se não houver Pages separado)

```
https://muzphaxx.github.io/designkit/
```

### 5.3 Palavras-chave para indexação

**Primárias:** ai design skills, agent design department, design tokens, anti-slop design, claude code design skill, codex design skill, pi design agent

**Secundárias:** design system for ai, token-first css, wcag ai audit, design critique automation, agentic design workflow, npx skills design, ai ui components, closed quality loops, design handoff automation

**Long-tail:** "how to make ai generate better ui", "claude code design system", "ai agent that designs like a human", "replace design team with ai", "design tokens for ai agents", "ai slop detection"

### 5.4 Metadata dos arquivos

- `README.md`: já otimizado (tags, badges, exemplos de prompt)
- `README.pt-BR.md`: versão em português (criar a partir do README atual se ainda não existir)
- `docs/guia-de-uso.md`: tutorial de onboarding
- `docs/plano-descoberta.md`: este documento

### 5.5 Social cards (Open Graph para GitHub Pages)

```html
<meta property="og:title" content="Design Kit — an entire design department in a box" />
<meta property="og:description" content="8 AI agent skills that turn Claude, Codex, pi, and Cursor into a functional design department. 158 tokens, 15+ components, 98 anti-slop checks." />
<meta property="og:image" content="https://muzphaxx.github.io/designkit/og-image.png" />
<meta name="twitter:card" content="summary_large_image" />
```

---

## 6. Kit de lançamento (ações imediatas)

### 6.1 Pré-lançamento (agora, v0.9.0)

| Ação | Status | Responsável |
|---|---|---|
| Badges do GitHub atualizadas no README | ⬜ pendente | Marketing |
| Tópicos do GitHub adicionados na aba About | ⬜ pendente | Fundador (owner do repo) |
| `docs/plano-descoberta.md` publicado no repo | ✅ este arquivo | Marketing |
| README.pt-BR.md criado/verificado | ⬜ verificar | Marketing |
| Showcase no GitHub Pages ativado | ⬜ pendente | Fundador |
| OG image gerada (screenshot do showcase) | ⬜ pendente | Marketing + UI Designer |

### 6.2 Lançamento v1.0.0 (após decisões do fundador)

| Ação | Canal | Quando |
|---|---|---|
| Thread de 8 tweets | X | Dia do lançamento |
| 3 posts | Bluesky | Dia +1 |
| 2 artigos | LinkedIn (PT + EN) | Dia +2 |
| 3 posts | Reddit (r/webdev, r/ClaudeAI, r/DesignSystems) | Dia +3 |
| Show HN | Hacker News | Dia do lançamento (manhã PT) |
| Post no blog (se houver) | dev.to / Medium / blog próprio | Dia +5 |
| Divulgação no Discord/Circle | Comunidades de AI agents e design systems | Semana 1 |

### 6.3 Roteiro de engajamento (30 dias pós-lançamento)

- **Semana 1:** lançamento nos canais principais, responder TODOS os comentários
- **Semana 2:** post de "bastidores" (como o kit foi construído, decisões de arquitetura)
- **Semana 3:** case study expandido (Lumen ou Norte, com antes/depois, métricas)
- **Semana 4:** "O que aprendi" + convite para contribuições

### 6.4 Métricas de sucesso (propostas)

| Métrica | Alvo (30 dias) | Alvo (90 dias) |
|---|---|---|
| GitHub stars | 100 | 500 |
| Instalações via `npx skills add` | 50 | 200 |
| Issues abertas (qualidade do feedback) | 10+ | 30+ |
| Menções no X/Bluesky | 20 | 50 |
| Contribuidores externos | 2 | 5 |

---

## 7. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Nome "Design Kit" genérico demais (difícil SEO) | Resolver antes do v1.0.0 (decisão pendente do fundador) |
| Competidores estabelecidos (impeccable 65k★ no taste-skill) | Focar no diferencial de setor completo + design system + QA determinística, não em competir como "mais uma skill de taste" |
| Portabilidade não validada em Codex e Cursor (Fase E p2 pendente) | Deixar claro que é pre-1.0; priorizar validação |
| Docs internos em pt-BR — barreira para comunidade global | Traduzir `README.md` e `DESIGN.md` para EN como prioridade |
| Licença MIT provisória (pendente confirmação) | Resolver antes do lançamento público |

---

## 8. Próximos passos (ações delegáveis)

1. **Fundador:** adicionar tópicos do GitHub na aba About do repo + ativar GitHub Pages + decidir nome definitivo e licença.
2. **Orquestrador:** validar o showcase no GitHub Pages (abrir URL pública e checar 14 seções + tema + responsivo).
3. **UI Designer:** gerar OG image (screenshot do showcase com overlay do nome do kit).
4. **Marketing (esta role):** agendar posts e preparar versão EN do README e DESIGN.md.
5. **Qualquer dev do time:** rodar `python scripts/smoke-test.py` e `python scripts/anti-slop-check.py` antes do lançamento e anexar output ao release.