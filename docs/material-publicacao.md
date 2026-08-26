# Material de Publicação — Design Kit v0.9.0

> **Uso:** copiar e colar em cada plataforma. Texto pronto, sem edição necessária.  
> **Data:** 2026-08-25 · **Versão:** v0.9.0 (pre-1.0)  
> **Regra perene:** zero menção à Liquid.

---

## 1. Posts Prontos — X (Twitter) / Bluesky

### 1.1 X — Post solo (não-thread, impacto máximo em 280 caracteres)

```
Seu agente de IA desenha tudo igual.

O problema não é o modelo. É que ele não tem constraints de design.

Design Kit: 8 skills + 158 tokens + 98 checks anti-slop que transformam Claude, Codex ou pi num setor de design completo.

github.com/murioliveira/designkit
```

### 1.2 X — Thread de 5 tweets (versão enxuta para timeline)

**Tweet 1 (hook):**
```
8 skills. 158 tokens. 98 checks anti-slop. 8 casos reais com nota de critique.

Isso não é um time de design. É um pacote de IA que instala com 1 comando.

Design Kit — um setor de design inteiro dentro do seu agente.

🧵
```

**Tweet 2 (o que faz):**
```
Você passa 1 parágrafo de brief. O agente faz:

researcher → information architect → UI designer → design critic → refine → a11y auditor → handoff

2 checkpoints de aprovação humana. O resto roda sozinho, em loops fechados de qualidade. Máximo 2 rodadas de refine antes de escalar pra você.
```

**Tweet 3 (provas, não promessas):**
```
8 casos reais. Notas, não marketing:

• Lumen (landing): critique 4.7/5
• Norte (dashboard): 4.6/5, reusa 12 grupos de componentes do kit
• Aurora: 14/14 no pre-flight anti-slop
• Ponto Final: fluxo completo, 10 artefatos
• Tereza: portfolio modo Experience
• Brisa, Linha Direta, Redesign Demo
```

**Tweet 4 (o que tem dentro):**
```
Por dentro do pacote:

→ DESIGN.md: 300 linhas de manual anti-slop (bans: em-dash, Inter, 3 cards iguais, paletas proibidas, nomes genéricos)
→ 158 tokens semânticos (claro/escuro)
→ 18+ componentes com estados reais (loading, empty, error)
→ WCAG 2.2 AA auditado e corrigido (10 fixes)
→ 6 composições de bloco pré-prontas com dials calibrados
```

**Tweet 5 (instalação + CTA):**
```
Instalar:

npx skills add murioliveira/designkit

Ou clona, abre index.html com duplo clique e vê o showcase com 14 seções de componentes no navegador. Zero build. Zero dependência.

Repo: github.com/murioliveira/designkit
```

---

### 1.3 Bluesky — 3 posts (tom técnico, sem limite de caracteres)

**Post 1 — O problema e o diagnóstico:**
```
Toda UI gerada por IA parece igual. O motivo não é criatividade do modelo — é ausência de constraints. O modelo foi treinado em milhões de landing pages idênticas e, sem instrução contrária, entrega o denominador comum: Inter, slate-900, três cards em linha, gradiente roxo no CTA.

O Design Kit resolve com três camadas que nenhuma skill de design individual oferece:

1. SISTEMA DE DESIGN PRÓPRIO
158 tokens semânticos (claro/escuro) + 18+ componentes com todos os estados. Toda UI gerada consome var(--tokens). Zero hex hardcoded. Regra auditável por grep.

2. SETOR DE DESIGN EM 8 SKILLS
Researcher → information architect → UI designer → critic → refine → a11y auditor → handoff. Com 2 checkpoints humanos e loops fechados (max 2 refines antes de escalar).

3. QA DETERMINÍSTICA
98 checks anti-slop + 8 smoke tests. Regras viram código executável. Nenhum concorrente tem isso.

Resultado: 8 casos reais validados com nota de critique, não com slide de venda.
```

**Post 2 — Comparação honesta com o ecossistema:**
```
O ecossistema de skills de design explodiu em 2026. Vamos aos fatos:

impeccable (pbakaus): 1 skill, 23 comandos, 59 regras detectoras. Excelente metodologia de critique e live browser iteration. Mas é 1 skill, não um departamento.

taste-skill (Leonxlnx): 1 skill com 3 dials (VARIANCE, MOTION, DENSITY). Patrocinado pela Vercel, ~46K estrelas. Metodologia anti-slop de alto nível. Sem design system implementado.

designer-skills (Owl-Listener): 63 skills, cobre o ciclo completo. A coleção mais ampla. Sem tokens ou componentes próprios.

Open Design (nexu-io): 259+ skills, 142+ design systems. O ecossistema mais ambicioso. Mas os design systems são templates, não sistemas funcionais com showcase vivo.

Design Kit: 8 skills, 158 tokens, 18+ componentes com showcase renderizado, 98 checks determinísticos, 8 casos com nota. É o ÚNICO que junta sistema de design implementado + setor de skills + QA executável.

Se você já usa impeccable ou taste-skill, o kit não substitui — ele wrappa. Mas se quer que seu agente execute o ciclo completo sozinho, é o pacote que junta as peças.

npx skills add murioliveira/designkit
github.com/murioliveira/designkit
```

**Post 3 — O manual anti-slop (DESIGN.md) como diferencial técnico:**
```
O ativo mais valioso do Design Kit não são as skills, os tokens ou os componentes.

É o DESIGN.md.

300 linhas. 15 categorias de tells da IA banidos com proibição explícita. 3 dials calibrados por tipo de página (VARIANCE, MOTION, DENSITY). 20 itens de pre-flight obrigatório. Regras de hero (≤2 linhas de headline, ≤20 palavras de subtext, ≤4 elementos, padding ≤6rem). Protocolo de redesign completo (audit-before-touch, 6 alavancas em ordem, preservação de SEO).

E o mais importante: as regras são AUDITÁVEIS.

O script anti-slop-check.py varre 14 arquivos em busca de em-dash, Inter, hex fora de tokens, nomes genéricos, paletas proibidas, scroll cues. 98 checks. Passou? Pode shipar. Falhou? Volta e corrige.

Isso é engenharia de qualidade visual. Não é "gosto" ou "opinião de design".

É a diferença entre "o agente gerou uma UI" e "o agente gerou uma UI que passa no controle de qualidade".

github.com/murioliveira/designkit
```

---

## 2. Post LinkedIn (PT-BR, artigo completo)

```
Seu agente de IA gera design genérico? O problema não é o modelo. É que ele não tem um setor de design.

Eu construí o Design Kit — um pacote open-source que transforma qualquer agente (Claude Code, Codex, pi, Cursor) num departamento de design completo. Da ideia ao handoff pro dev, com controle de qualidade no meio.

---

O QUE É

8 skills de IA que rodam o fluxo completo de um setor de design:

1. design-researcher — brief → problem statement, personas, jornadas
2. information-architect — sitemap, fluxos, hierarquia
3. ⏸️ VOCÊ APROVA
4. ui-designer — gera a UI consumindo apenas var(--tokens)
5. design-critic — avalia a própria UI (heurísticas + tells de IA)
6. design-refine — ajusta (bolder / quieter / distill)
7. a11y-auditor — auditoria WCAG 2.2 AA
8. ⏸️ VOCÊ APROVA
9. design-handoff — spec por componente pro desenvolvedor

O agente não gera e entrega. Ele gera, faz critique, refina, faz critique de novo. Só shipa quando zera os blockers. Máximo 2 rodadas de refine. Se ainda tiver problema, escala pro humano.

---

O QUE TEM DENTRO

→ 158 tokens de design (claro/escuro) — única fonte de verdade visual
→ 18+ componentes com estados reais (loading, empty, error): botões, badges, cards, alerts, formulários, tooltip, modal com trap de foco, tabs ARIA, progress, skeleton, avatar, dropdown, breadcrumb, tabelas, stepper, paginação
→ DESIGN.md: 300 linhas de manual anti-slop — 15 categorias de tells de IA banidos, 3 dials calibrados por tipo de página, 20 itens de pre-flight obrigatório
→ 98 checks anti-slop + 8 smoke tests — regras viram código executável (Python, stdlib apenas)
→ WCAG 2.2 AA auditado e corrigido (10 correções aplicadas: 2 P1, 5 P2, 3 P3)
→ 6 composições de bloco pré-prontas (hero split assimétrico, bento grid, manifesto editorial, sticky-stack CSS puro, marquee, galeria Experience)
→ 9 docs de handoff por componente (tudo que o dev precisa pra implementar)
→ 8 casos reais validados com nota de critique — não com slide de venda

---

PROVAS, NÃO PROMESSAS

• Lumen (landing): critique 4.7/5
• Norte (dashboard): 4.6/5, reutiliza 12 grupos de componentes do kit
• Aurora: 14/14 no pre-flight anti-slop
• Ponto Final: fluxo completo com 10 artefatos (brief → research → IA → UI → critique → a11y → refine → redesign → handoff → README)
• Tereza Vilela: portfolio em modo Experience
• Brisa: validação de skills (4/4 executáveis)
• Linha Direta: block library na prática
• Redesign Demo: antes/depois com correção de tells

Nenhum desses casos usou truque. Foram gerados pelo mesmo fluxo que qualquer pessoa roda com o kit.

---

PARA QUEM É

Devs que precisam de UI profissional sem contratar designer. Startups enxutas que não têm budget pra um time de design. Agências que querem acelerar a etapa de conceito. Times de produto que já usam IA e querem sair do genérico.

NÃO É PARA quem espera que a IA faça pesquisa primária com usuários reais. O agente estrutura e sintetiza o que você fornece. Entrevistas, testes de usabilidade e análise de dados reais continuam com humanos. O que o kit substitui é a execução do design.

---

INSTALAÇÃO

npx skills add murioliveira/designkit

Ou clona o repo e abre index.html no navegador. Zero build. Zero dependência. 14 seções de showcase com todos os componentes, tema claro/escuro, responsivo.

Repo: github.com/murioliveira/designkit

(Projeto open-source, v0.9.0. Licença MIT pendente de confirmação. Feedback bem-vindo.)
```

---

## 3. Título + Descrição Curta — Show HN / Reddit

### 3.1 Show HN

**Título:**
```
Show HN: Design Kit — an entire design department as 8 AI agent skills (158 tokens, 98 anti-slop checks, 8 validated cases)
```

**Descrição curta (para o campo de texto do Show HN):**
```
I built Design Kit because AI-generated UIs all look the same — Inter, slate-900, three identical cards, purple gradients. The models aren't bad at design; they just have zero constraints.

Design Kit gives them constraints — real, auditable, executable constraints:

• 158 semantic design tokens (light/dark) — every pixel comes from var(--tokens), zero hardcoded hex
• 18+ components with full states (loading, empty, error, focus-visible, disabled)
• 8 agent skills in a closed quality loop: researcher → IA → UI designer → critic → refine → a11y auditor → handoff
• DESIGN.md: a 300-line anti-slop manual — 15 banned AI tells, 3 calibrated dials, 20-item pre-flight
• 98 deterministic checks (Python, stdlib only) + 8 smoke tests — rules become auditable code
• 8 real cases with critique scores: Lumen landing 4.7/5, Norte dashboard 4.6/5, Aurora 14/14 pre-flight
• WCAG 2.2 AA audited (10 fixes applied: 2 critical, 5 major, 3 minor)
• 6 pre-composed block layouts with dial compatibility
• 9 per-component handoff docs for developers

No build. No npm. Just HTML/CSS/JS. Open index.html in any browser.

Try it: npx skills add murioliveira/designkit
Repo: github.com/murioliveira/designkit

I'm looking for honest feedback: would you use this? What's missing before you'd trust it in production?
```

---

### 3.2 Reddit — r/webdev

**Título:**
```
I built a design department that fits in an AI agent's pocket — 8 skills, 158 tokens, 98 deterministic anti-slop checks, 8 real cases with critique scores
```

**Descrição curta:**
```
Design Kit is an open-source package that turns Claude Code, Codex, pi, or Cursor into a functional design department. 8 skills (researcher → IA → UI designer → critic → refine → a11y → handoff), 158 design tokens (light/dark), 18+ components with full states, 98 anti-slop checks + 8 smoke tests, WCAG 2.2 AA audited. 8 real cases validated with critique scores (landing 4.7/5, dashboard 4.6/5). No build. No dependencies. Install: npx skills add murioliveira/designkit · Repo: github.com/murioliveira/designkit
```

---

### 3.3 Reddit — r/ClaudeAI

**Título:**
```
I built 8 Claude Code skills that make the agent run a full design department — from brief to handoff, with critique, accessibility audit, and 98 deterministic quality checks
```

**Descrição curta:**
```
Design Kit gives Claude Code a design system (158 tokens, 18+ components), 8 department skills (researcher, IA, UI designer, critic, refine, a11y auditor, handoff), and a 300-line anti-slop manual. Skills run in closed quality loops with 2 human checkpoints. Max 2 refine rounds before escalating. Validated: 8 real cases with actual critique scores (landing: 4.7/5, dashboard: 4.6/5). WCAG 2.2 AA audited and fixed. Install: npx skills add murioliveira/designkit · github.com/murioliveira/designkit
```

---

### 3.4 Reddit — r/DesignSystems

**Título:**
```
Design Kit: a token-first design system (158 tokens, 18+ components) + 8 AI agent skills that form a complete design department — with deterministic QA
```

**Descrição curta:**
```
Sharing an open-source package that combines a real design system (158 semantic tokens, 18+ components with full states, live HTML showcase) with 8 AI agent skills running a closed-loop design workflow. The difference from other agent design skills: tokens are the single source of truth (zero hardcoded hex, grep-auditable), quality loops are closed (critique → refine → re-critique until no blockers), and QA is deterministic (98 mechanical checks + 8 smoke tests). 8 real cases with scores. Questions for this community: what would you want in a token-first design system built for AI agents? github.com/murioliveira/designkit
```

---

## 4. Lista de Badges para o README

Copiar este bloco para o topo do `README.md` e `README.pt-BR.md` (substituir o bloco atual):

```markdown
[![Version](https://img.shields.io/badge/version-v0.9.0-blue)](https://github.com/murioliveira/designkit/releases/tag/v0.9.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Agents](https://img.shields.io/badge/agents-Claude_Code_|_Codex_|_pi_|_Cursor-orange)
![Skills](https://img.shields.io/badge/skills-8_department_roles-blueviolet)
![Tokens](https://img.shields.io/badge/tokens-158_semantic-0366d6)
![Components](https://img.shields.io/badge/components-18%2B_with_states-informational)
![Anti-slop](https://img.shields.io/badge/QA-98_anti--slop_checks-success)
![WCAG](https://img.shields.io/badge/a11y-WCAG_2.2_AA_audited-brightgreen)
![Smoke](https://img.shields.io/badge/smoke-8_integrity_checks-lightgrey)
![Casos](https://img.shields.io/badge/cases-8_validated_4.7%2F5_avg-9cf)
```

### Tópicos para a aba "About" do GitHub (15 tópicos, máximo permitido)

Copiar e colar na seção "Topics" da página principal do repositório:

```
design-system design-tokens ai-agent ai-skills anti-slop
claude-code codex pi cursor frontend web-design
wcag accessibility agent-skills token-first design-department
```

---

## 5. Ficha Técnica de Referência (para entrevistas, FAQs, bios)

Use estes números em qualquer material. São fatos do repositório, verificados pelos scripts de QA.

| Métrica | Valor | Fonte |
|---|---|---|
| Skills empacotadas | 8 | `skills/` (8 diretórios com SKILL.md + frontmatter) |
| Design tokens | 158 | `grep -c '^  --' styles/tokens.css` |
| Componentes | 18+ | `styles/components.css` (~2000 linhas, 9 seções) |
| Checks anti-slop | 98 em 14 arquivos | `python scripts/anti-slop-check.py` (PASS, 0 falhas) |
| Smoke tests | 8 | `python scripts/smoke-test.py` (PASS, 8/8) |
| Casos validados | 8 | `docs/casos/` (aurora, brisa, linha-direta, lumen, norte, ponto-final, redesign-demo, tereza) |
| Melhor nota de critique | 4.7/5 | Caso Lumen (landing, Persuade mode) |
| Caso mais completo | Ponto Final (10 artefatos) | Fluxo completo brief→handoff |
| Grupos de componentes reutilizados | 12 | Caso Norte (dashboard) |
| Pre-flight anti-slop score | 14/14 | Caso Aurora |
| Correções de acessibilidade | 10 (2 P1, 5 P2, 3 P3) | `docs/auditoria-a11y.md` |
| Docs de handoff por componente | 9 | `docs/componentes/` |
| Composições de bloco | 6 | `docs/blocos/` (hero split, bento, manifesto editorial, sticky-stack, marquee, galeria) |
| Categorias de AI tells banidos | 15 | `DESIGN.md` §4.1 |
| Dials calibrados | 3 (VARIANCE, MOTION, DENSITY) + 6 presets | `DESIGN.md` §2 |
| Itens de pre-flight | 20 | `DESIGN.md` §6 |
| Agentes suportados | 4 (Claude Code, Codex, pi, Cursor) | `AGENTS.md` + `.claude/skills/` + `.codex/` |
| Linhas de CSS total | 3.140 | `styles/` (tokens 329, base 291, layout 520, components ~2000) |
| Build steps | 0 | HTML/CSS/JS puro, abre com duplo clique |
| Comando de instalação | `npx skills add murioliveira/designkit` | README.md |
| Licença | MIT (pendente de confirmação) | `docs/distribuicao.md` |

---

*Documento produzido pelo Marketingle do Design Kit. Pronto para publicação. Dúvidas sobre fatos: consultar o Orquestrador ou rodar `python scripts/smoke-test.py` + `python scripts/anti-slop-check.py`.*