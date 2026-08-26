# Gaps e Ideias — Design Kit vs Concorrentes

> **Data:** Agosto 2026  
> **Método:** Cruzamento de docs/pesquisa-mercado.md, docs/avaliacao-inicial.md e docs/proposta-design.md com inspeção direta dos repositórios concorrentes e do código do kit.  
> **Regra perene:** Nenhuma menção à Liquid em qualquer parte deste documento.  
> **Convenção de validação:** "✅ Validado" = dado verificável de fonte pública; "⚠️ Precisa de validação" = inferência razoável mas sem confirmação externa direta — NÃO implantar sem validar.

---

## ⚠️ CORREÇÕES PÓS-VALIDAÇÃO (adicionadas após auditoria direta dos repositórios — 2026-08)

Esta seção registra correções de fatos apurados DEPOIS da primeira versão deste documento. Foram encontrados **erros de dado** que alteram conclusões. Ler antes da matriz.

| # | Alegação original | Correção verificada | Fonte | Impacto |
|---|---|---|---|---|
| C1 | Designer Skills tem "63 skills" | São **87 skills + 27 comandos em 8 plugins** (o README cita "107 skills" no índice total da suíte) | github.com/owl-listener/designer-skills + perfil GitHub do autor | Subestimei a cobertura em ~38% |
| C2 | Designer Skills tem "zero scripts" | Tem diretório `scripts/` com 5 scripts: `build-gemini.sh`, `extract-release-notes.py`, `generate-index.py`, `generate-readmes.py`, `lint-frontmatter.py` | github.com/owl-listener/designer-skills/tree/main/scripts | **Atenua a Ideia 2** — mas são tooling de repo (lint de frontmatter, geração de índice), NÃO detectores de tells de design como o anti-slop-check.py |
| C3 | Designer Skills é um projeto isolado | É uma **suíte de 5+ repos**: designer-skills (87), ai-design-skills (44, com RESEARCH.md + REFERENCES.md = mapeamento pesquisa→prática acadêmica), inclusive-design-skills, designpowers (10 agentes + tests/ + CI + CLAUDE.md + GEMINI.md), agent-ready (skill + plugin Figma + 13 checks.js) | github.com/owl-listener (perfil) + extração dos repos | O concorrente é uma **plataforma**, não uma coleção |
| C4 | "AGENTS.md como onboarding é conceito único" (Ideia 5) | **designpowers faz exatamente isso**: CLAUDE.md + GEMINI.md + `agents/` com 10 agentes de design orquestrados + `tests/` + `hooks/` | github.com/owl-listener/designpowers | **INVALIDA a unicidade da Ideia 5** |
| C5 | Designer Skills "não tem quality gates automáticos" | designpowers tem `tests/` + `.github/workflows/` (CI). ai-design-skills tem `.githooks/` + `.github/workflows/` | github.com/owl-listener/designpowers + ai-design-skills | **Atenua a Ideia 3** — têm CI, embora não detectores de tells de design |

**Conclusão das correções:** o Owl-Listener (MC Dean) é o concorrente MAIS forte que eu havia retratado. As Ideias 2, 3 e 5 ficam **parcialmente enfraquecidas**. As Ideias 1, 4, 6 permanecem intactas (nenhum concorrente tem tokens CSS + componentes reais + showcase vivo). Ver §2 revisada e §6.

---

## 1. Matriz de Gaps — Design Kit vs 4 Concorrentes

### 1.1 As 12 Dimensões de Comparação

Cada dimensão é pontuada de 1 (fraco/ausente) a 5 (líder de mercado) com evidência concreta.

| # | Dimensão | Design Kit | Impeccable (Bakaus) | Taste-Skill (Leonxlnx) | Designer Skills (Owl-Listener) | Anthropic frontend-design |
|---|---|---|---|---|---|---|
| **1** | **Tokens implementados** (CSS real, não só conceito) | ⭐⭐⭐⭐⭐ 147 tokens semânticos, claro/escuro, `var(--...)` em todo componente | ⭐ "Vocabulário de design" — conceitos, não CSS | ⭐⭐ 3 dials (VARIANCE, MOTION, DENSITY) — parâmetros, não tokens | ⭐ Skills de processo — zero tokens | ⭐⭐ Referências a design tokens no prompt, sem implementação |
| **2** | **Componentes implementados** (HTML/CSS/JS reais) | ⭐⭐⭐⭐⭐ 18+ componentes, 9 grupos, ~2000 linhas CSS, estados completos, a11y | ⭐ Nenhum — é uma skill de instrução, não entrega componentes | ⭐ Nenhum — é uma skill de instrução, não entrega componentes | ⭐ Nenhum — é uma skill de instrução, não entrega componentes | ⭐ Nenhum — é uma skill de instrução, não entrega componentes |
| **3** | **Showcase/demo vivo** (abre no navegador, zero build) | ⭐⭐⭐⭐ index.html com 14 seções, dark/light, scrollspy. GAP: seção Tokens é placeholder vazio; casos reais invisíveis | ⭐⭐ Sem showcase — apenas site impeccable.style com docs | ⭐⭐⭐ tasteskill.dev com projetos da comunidade (contribuídos, sem controle de qualidade) | ⭐ Nenhum | ⭐ Nenhum |
| **4** | **Skills de processo** (research → handoff) | ⭐⭐⭐⭐ 8 skills + fallbacks embutidos + templates. GAP: fallback do a11y-auditor é fino; wrappers dependem de skills externas | ⭐⭐⭐ 23 comandos de design (critique, audit, polish, extract, animate, colorize...) — todos na mesma skill | ⭐⭐⭐ 13 skills (variantes de estilo: minimalist, brutalist, soft, gpt-taste...) + 3 dials | ⭐⭐⭐⭐⭐ 87 skills + 27 comandos em 8 plugins (+ ai-design-skills 44, + inclusive, + designpowers = suíte 130+ skills) — a MAIOR cobertura, com grounding acadêmico | ⭐⭐⭐ 1 skill monolítica com múltiplos modos implícitos |
| **5** | **QA determinístico** (scripts executáveis, não prompts) | ⭐⭐⭐⭐⭐ smoke-test.py (8 checks) + anti-slop-check.py (98 checks) — executáveis, auditáveis, CI-ready | ⭐⭐⭐⭐ 59 "detector rules" no SKILL.md — regras de prompt para o LLM, não scripts executáveis | ⭐⭐ Nenhum — confia nos dials + julgamento do LLM | ⭐ (CI/tests de repo; sem detectores de tells de design) | ⭐ Nenhum |
| **6** | **Casos reais com scoring** (provas de qualidade) | ⭐⭐⭐⭐⭐ 7 casos (Lumen 4.7/5, Norte 4.6/5, +5) + critique reports completos + 2 detectores PASS | ⭐⭐⭐⭐ Site mostra cases de usuários (hedge-ops, etc.) sem scoring quantitativo | ⭐⭐⭐⭐ tasteskill.dev mostra projetos da comunidade — sem scoring | ⭐ Nenhum caso documentado no repo | ⭐ Nenhum caso documentado no repo |
| **7** | **Portabilidade multi-agente** (funciona em qq harness) | ⭐⭐⭐ AGENTS.md + CLAUDE.md + .claude/skills/ (8 wrappers) + .codex/README. GAP: sem suporte a Cursor, Copilot, Gemini CLI; validação real pendente (Fase E p2) | ⭐⭐⭐⭐⭐ SKILL.md padrão; instalável via `npx impeccable install`; funciona em Claude Code, Codex, Cursor, Copilot, Gemini CLI | ⭐⭐⭐⭐⭐ SKILL.md padrão; `npx skills add Leonxlnx/taste-skill`; funciona em todos os harnesses | ⭐⭐⭐⭐⭐ SKILL.md padrão; `/plugin marketplace add`; funciona em todos os harnesses | ⭐⭐⭐⭐⭐ Skill oficial Anthropic; funciona em Claude Code, Claude.ai, API; portabilidade parcial (não testado em Codex/Cursor) |
| **8** | **Distribuição one-command** | ⭐ Nenhuma — clone manual. GAP CRÍTICO | ⭐⭐⭐⭐⭐ `npx impeccable install` | ⭐⭐⭐⭐⭐ `npx skills add Leonxlnx/taste-skill` | ⭐⭐⭐⭐⭐ `/plugin marketplace add Owl-Listener/designer-skills` | ⭐⭐⭐⭐ `/plugin install frontend-design@claude-plugins-official` |
| **9** | **Prova social** (estrelas, installs) | ⭐ Zero — repo privado ou sem tração. GAP CRÍTICO | ⭐⭐⭐⭐⭐ ~40K ★, 160K+ installs | ⭐⭐⭐⭐⭐ ~46K ★, Vercel-sponsored | ⭐⭐⭐ ~2.1K ★ | ⭐⭐⭐⭐⭐ 65K ★, 277K+ installs |
| **10** | **Documentação** (completeness, idioma) | ⭐⭐⭐ AGENTS.md + DESIGN.md excelentes. GAP: docs internos só em pt-BR; sem docs em inglês para mercado global | ⭐⭐⭐⭐ impeccable.style + README + dev.to articles + YouTube | ⭐⭐⭐⭐ tasteskill.dev + README + YouTube tutorial | ⭐⭐⭐ Medium article + README — docs mais finos que o kit | ⭐⭐⭐⭐⭐ Documentação oficial Anthropic + blog posts + 277K installs de prova |
| **11** | **Anti-slop rigor** (regras + enforcement) | ⭐⭐⭐⭐⭐ DESIGN.md com 15 categorias de tells + 98 checks + pre-flight 20 itens + detectores executáveis | ⭐⭐⭐⭐ 59 regras detectoras (no prompt) + commands de critique — menos enforcement automatizado | ⭐⭐⭐⭐ Dials + SKILL.md extenso (1206 linhas, 85KB) — regras no prompt, sem detectores executáveis | ⭐⭐ Foco em processo, não em anti-slop — sem detector system | ⭐⭐⭐⭐ Bans explícitos (Inter, Roboto, Arial, Space Grotesk, gradientes) — no prompt, sem detectores |
| **12** | **Licença aberta** | ❌ Pendente (decisão do fundador). GAP BLOQUEADOR | ⭐⭐⭐⭐⭐ Apache 2.0 | ⭐⭐⭐⭐⭐ MIT | ⭐⭐⭐⭐⭐ MIT | ⭐⭐⭐ Custom (restritiva) |

### 1.2 Radar Visual de Forças/Fraquezas

```
                     TOKENS
                       5
                       │
          LICENÇA  0   │   4  COMPONENTES
              ╲    │   │   ╱
                ╲  │   │ ╱
    ANTI-SLOP 5───●───●───●───3  SHOWCASE
                 │ Design│
    DOCS 3──────●───Kit──●───4  SKILLS
                 │   │   │
      SOCIAL 0───●───┼───●───5  QA AUTOMATIZADO
                 │   │   │
    DISTRIB 1────●───●───●───5  CASOS REAIS
                      │
                     3
                PORTABILIDADE

    ● = Design Kit    ─ = Média dos 4 concorrentes
```

### 1.3 Interpretação da Matriz

**Onde o kit GANHA (diferença ≥ 2 pontos vs média dos concorrentes):**
- **Tokens implementados** (5 vs ~1.5) — é o ÚNICO com design system CSS real consumível
- **Componentes implementados** (5 vs ~1) — é o ÚNICO com componentes HTML/CSS/JS reais
- **QA determinístico** (5 vs ~1.5) — é o ÚNICO com detectores de tells executáveis (os concorrentes têm tooling/CI de repo, mas não detectores de design)
- **Casos reais com scoring** (5 vs ~2) — é o ÚNICO com critique quantitativo

**Onde o kit está PAR a PAR (diferença ≤ 1):**
- **Showcase** (4 vs ~1.5) — vantagem, mas o placeholder de tokens e a invisibilidade dos casos reduzem o impacto
- **Skills de processo** (4 vs ~3.5) — Designer Skills Collection (87 skills, suíte 130+) cobre mais breadth E tem grounding acadêmico (ai-design-skills RESEARCH.md) e CI (designpowers). O kit cobre mais depth de IMPLEMENTAÇÃO (skills + tokens + componentes), mas a vantagem de "processo" não é mais clara
- **Anti-slop rigor** (5 vs ~3.5) — vantagem real, mas Impeccable e Taste-Skill competem forte em regras de prompt

**Onde o kit PERDE (gap ≥ 2 pontos vs líder):**
- **Distribuição** (1 vs 5) — GAP CRÍTICO. Todo concorrente tem one-command install
- **Prova social** (0 vs 5) — GAP CRÍTICO. Zero estrelas vs 40-65K dos líderes
- **Portabilidade** (3 vs 5) — GAP SIGNIFICATIVO. Wrappers parciais vs suporte universal
- **Licença** (0 vs 5) — GAP BLOQUEADOR. Sem licença = sem adoção
- **Documentação** (3 vs 4-5) — GAP MODERADO. Falta docs em inglês para alcance global

---

## 2. Ideias de Diferenciação (7 ideias ordenadas por impacto)

Cada ideia inclui: descrição, gap que ataca, validação objetiva, viabilidade, e o que o concorrente faria.

---

### Ideia 1: "Design System Executável" — tokens + componentes + showcase vivo como produto integrado

**Descrição:** Posicionar o kit como o ÚNICO agente de design que entrega um design system CSS completo e funcional (tokens → componentes → showcase), não só instruções. Enquanto Impeccable e Taste-Skill são "o que fazer", o Design Kit é "o que fazer COM o que usar" — o agente não precisa gerar CSS do zero, ele consome `var(--...)` reais de um sistema que já funciona.

**Gap que ataca:** Dimensões 1 (tokens), 2 (componentes), 3 (showcase).

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Impeccable (github.com/pbakaus/impeccable): 1 SKILL.md + scripts auxiliares. Zero CSS de componentes. Zero HTML de showcase. | Inspeção do repo público | ✅ Validado |
| Taste-Skill (github.com/Leonxlnx/taste-skill): 13 SKILL.md + exemplos. Nenhum arquivo `.css` com componentes. | Inspeção do repo público | ✅ Validado |
| Designer Skills (github.com/owl-listener/designer-skills): 87 skills em 8 plugins (+ 44 em ai-design-skills). Zero CSS de componentes. Zero HTML de showcase. Tem scripts/ de tooling (não detectores de design). | Inspeção do repo público (corrigido pós-auditoria) | ✅ Validado |
| Anthropic frontend-design: skill oficial no marketplace. SKILL.md com princípios de design. Zero implementação de componentes. | Documentação Anthropic + repo anthropics/skills | ✅ Validado |
| Open Design (nexu-io/open-design): 142+ design systems como DESIGN.md portátil. NÃO são componentes CSS implementados — são schemas/templates de identidade visual. | Inspeção do repo + docs | ✅ Validado |
| Design Kit: styles/tokens.css (147 tokens), styles/components.css (2000 linhas, 18+ componentes), index.html (showcase 14 seções), styles/base.css + layout.css. | Código do próprio kit | ✅ Validado |

**Conclusão da validação:** ✅ VALIDADO. Nenhum concorrente implementa um design system CSS real com componentes renderizáveis e showcase vivo. O gap é real e defensável.

**Viabilidade:** Alta. Já existe — é o que o kit já é. O trabalho é de **posicionamento e empacotamento** (distribuição + comunicação), não de construção.

**O que o concorrente faria:** Impeccable ou Taste-Skill poderiam adicionar um arquivo `tokens.css` e alguns componentes de exemplo em semanas. A barreira de entrada para "ter tokens" é baixa. Mas a barreira para "ter 18+ componentes com estados completos, a11y, dark mode, showcase com scrollspy e QA determinístico" é alta (meses de trabalho). **Mitigação:** velocidade de distribuição + depth como moat.

---

### Ideia 2: "QA Automatizado de Design" — detectores executáveis como produto standalone

**Descrição:** Extrair `smoke-test.py` e `anti-slop-check.py` como ferramenta independente: `npx designkit-check` (ou `npx @designkit/qa`). Um comando que qualquer projeto pode rodar para auditar seu HTML/CSS contra AI tells, acessibilidade básica e integridade de tokens — independente de usar o resto do kit. Isso posiciona o kit como **infraestrutura de qualidade de design**, não só como ferramenta de geração.

**Gap que ataca:** Dimensão 5 (QA determinístico) + converte o maior diferencial técnico do kit em produto de adoção independente.

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Impeccable: 59 detector rules no SKILL.md. São instruções para o LLM aplicar durante critique, NÃO scripts executáveis. Nenhum `.py` ou `.js` de detecção no repo. | Inspeção do repo github.com/pbakaus/impeccable | ✅ Validado |
| Taste-Skill: Zero detectores. O SKILL.md (1206 linhas) contém regras de design mas são prompts, não código executável. | Inspeção do repo github.com/Leonxlnx/taste-skill | ✅ Validado |
| stop-slop (hardikpandya): Foca em AI tells de prosa. É um SKILL.md, não script. | Inspeção do repo | ✅ Validado |
| AccessLint: CI tool para a11y. Faz uma fração do que o anti-slop-check faz (foco em contraste/a11y, não em tells de IA). | Conhecimento público | ✅ Validado |
| Design Kit: smoke-test.py (8 checks, Python 3 stdlib) + anti-slop-check.py (98 checks, Python 3 stdlib). Ambos executáveis, zero dependências externas, output PASS/FAIL com contagens. | Código do próprio kit — scripts/ | ✅ Validado |
| Mercado potencial: "design QA automation" não tem líder. Ferramentas como Percy/Chromatic fazem regressão visual (screenshots), não detecção de tells. O espaço "lint de design para IA" está vazio. | Pesquisa de mercado §4, pesquisa-mercado.md | ✅ Validado |

**Conclusão da validação:** ✅ VALIDADO. Nenhum concorrente tem detectores executáveis. O espaço "lint de design determinístico" está vazio. A ferramenta é extraível como produto standalone.

**Viabilidade:** Média-Alta. O código já existe. O trabalho é: (a) empacotar como pacote instalável (`npx designkit-check`), (b) documentar em inglês, (c) adicionar CI template (GitHub Action). Estimativa: 1-2 semanas.

**O que o concorrente faria:** Impeccable é o candidato mais óbvio a adicionar detectores — Paul Bakaus já tem 59 regras detectoras no prompt. Converter de prompt para script Python é trabalho de dias, não semanas. **Mitigação:** ser primeiro + oferecer mais checks (98 vs 59) + integração CI pronta + exportar para formatos que os concorrentes não cobrem (anti-slop visual, não só a11y). O moat é profundidade e ecossistema, não a ideia em si.

---

### Ideia 3: "Ciclo Fechado de Design" — 8 skills que cobrem o fluxo inteiro com quality gates integrados

**Descrição:** O kit junta skills de processo COM design system CSS implementado COM detectores determinísticos de qualidade — uma combinação que os concorrentes não reproduzem integralmente. O kit entrega o ciclo completo: researcher → IA → ui-designer → critic → refine/redesign → a11y → handoff, com scoring quantitativo em cada etapa e loops de qualidade fechados (critique + a11y rodam até zero blockers). Posicionar como "o agente que não só desenha — audita, refina e entrega código funcional".

**Gap que ataca:** Dimensões 4 (skills de processo), 5 (QA), 6 (casos com scoring).

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Designer Skills Collection: 87 skills, 27 comandos, cobre o ciclo inteiro (+ 44 em ai-design-skills, + designpowers com 10 agentes e CI). Tem MUITO mais skills que o kit (87 vs 8). MAS: (a) não tem design system CSS implementado (tokens + componentes reais), (b) os scripts/ são tooling de repo, NÃO detectores de tells de design, (c) não tem detectores executáveis de anti-slop, (d) não tem casos com scoring quantitativo. | Inspeção do repo github.com/owl-listener/designer-skills + ai-design-skills + designpowers (corrigido pós-auditoria) | ✅ Validado |
| Impeccable: 23 comandos cobrem critique, audit, polish, extract, refine, animate, colorize — foco em qualidade visual, não em processo completo. Sem research, sem IA, sem handoff. | Inspeção do repo + impeccable.style | ✅ Validado |
| Design Kit: 8 skills + DESIGN.md com pre-flight 20 itens + detectores que rodam entre etapas + casos Lumen (4.7/5) e Norte (4.6/5) como prova de que o ciclo fecha. | Código do kit: skills/ + DESIGN.md §5, §6 | ✅ Validado |
| Cada skill do kit tem SKILL.md com frontmatter, descrição, fluxo de trabalho documentado, e fallback independente de skills externas. | skills/*/SKILL.md (8 arquivos, 5-14KB cada) | ✅ Validado |

**Conclusão da validação:** ⚠️ PARCIALMENTE VALIDADO (rebaixado de ✅). O kit junta 3 camadas (design system CSS + skills de processo + QA determinístico de design). Mas o Owl-Listener NÃO está parado: tem breadth superior (87+ skills), grounding acadêmico (ai-design-skills RESEARCH.md/REFERENCES.md), e CI/tests (designpowers). A única camada que o concorrente realmente NÃO tem é **design system CSS implementado** (tokens + componentes + showcase). A diferenciação agora é ESTREITA e depende de uma única coisa: "o kit entrega código de design funcional, os outros entregam instruções".

**Risco de validação:** Designer Skills (87 skills) + ai-design-skills (44) + inclusive + designpowers cobrem MUITO mais cenários de processo (design ops, prototyping, testing, toolkit, AI product design, alignment, orchestration). Um humano que quer cobertura máxima pode preferir 130+ skills sem design system a 8 skills COM design system. ⚠️ **Precisa de validação:** breadth vs depth continua sem resposta definitiva. Mas há dado parcial: o mercado já recompensou Owl-Listener com 2.3K★ (designer-skills), 160★ (ai-design-skills), 236★ (designpowers) — sinal de que breadth tem demanda real.

**Viabilidade:** Alta. As 8 skills já existem. O trabalho é: (a) fortalecer fallbacks (especialmente a11y-auditor, ver Ideia 6), (b) criar um diagrama/visual do ciclo no showcase/README, (c) empacotar como 1 skill-pai que orquestra as 8 (via AGENTS.md).

**O que o concorrente faria:** Designer Skills Collection poderia referenciar tokens do kit como dependência ("use com designkit para tokens"). Isso seria complementar, não competitivo. Impeccable poderia adicionar uma skill de research ou handoff. A barreira para adicionar skills de processo é baixa (escrever SKILL.md). **Mitigação:** o moat não está nas skills em si, está na integração delas com tokens + componentes + QA + casos reais. É o sistema, não as partes.

---

### Ideia 4: "Showcase como Prova Viva" — tornar o index.html a demonstração definitiva do que o kit constrói

**Descrição:** Implementar as duas melhorias da proposta-design.md: (a) visualização viva de tokens (~60 tokens em 6 subseções: cores, tipografia, espaçamento, raios, sombras, motion) substituindo o placeholder vazio, e (b) seção "Resultados" com previews CSS dos 3 casos principais (Lumen, Norte, Tereza) com links diretos. O showcase deixa de ser "galeria de componentes isolados" e vira "prova visual do que o kit entrega".

**Gap que ataca:** Dimensão 3 (showcase) + fecha a quebra de confiança identificada na avaliação (placeholder vazio na 2ª seção).

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Showcase atual: seção Tokens é `<div class="placeholder">Referência visual dos tokens: em breve</div>`. Primeira impressão após o hero = caixa tracejada cinza. | Inspeção do index.html linha ~80-90 | ✅ Validado |
| Casos reais (Lumen 4.7/5, Norte 4.6/5, Tereza portfólio) existem em docs/casos/ mas NÃO são referenciados no showcase. | Inspeção do index.html — zero menção a casos | ✅ Validado |
| Proposta-design.md estima 6-9h de trabalho para as duas melhorias (280 linhas HTML + 220 CSS + 30 JS). | docs/proposta-design.md §5 | ✅ Validado |
| Taste-Skill (tasteskill.dev) mostra projetos da comunidade — este é o padrão de referência. Mas são contribuídos, sem controle de qualidade. | tasteskill.dev | ✅ Validado |
| Open Design tem sandbox preview e multi-frame preview — mas é para artefatos gerados na hora, não showcase estático. | open-design.ai + repo | ✅ Validado |

**Conclusão da validação:** ✅ VALIDADO. O gap do showcase é real, documentado em dois docs separados (avaliacao-inicial e proposta-design), e a solução é de baixo risco (6-9h, CSS/HTML puro, zero dependências).

**Viabilidade:** Muito Alta. As duas melhorias já foram desenhadas em detalhe na proposta-design.md. É trabalho de implementação, não de design.

**O que o concorrente faria:** Nada — este é um gap interno do kit, não uma vantagem sobre concorrentes. Consertar o showcase não "vence" ninguém, apenas remove uma desvantagem autoinfligida. Mas é pré-requisito para qualquer estratégia de adoção: ninguém adota uma ferramenta de design cujo showcase tem placeholder vazio na 2ª seção.

---

### Ideia 5: "AGENTS.md como Onboarding Universal" — transformar qualquer agente-hospedeiro em setor de design

**Descrição:** O AGENTS.md do kit é um arquivo único que configura um agente de IA genérico (Claude Code, Codex, pi, Cursor) para operar como um setor de design completo — com papéis, regras, fluxo de trabalho, quality gates e pre-flight. **ATENÇÃO (correção pós-auditoria):** este conceito NÃO é único — o designpowers (Owl-Listener) faz role onboarding equivalente (CLAUDE.md + GEMINI.md + 10 agentes). A diferenciação passa a ser "o kit faz melhor", não "o kit inventou". Posicionar como "onboarding que transforma seu agente em setor de design com design system CSS real + detectores executáveis".

**Gap que ataca:** Dimensão 7 (portabilidade) + cria categoria própria ("agent onboarding para design").

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Impeccable: SKILL.md com instruções de design. Não configura papéis, fluxo de trabalho ou qualidade gates para o agente. | github.com/pbakaus/impeccable/blob/main/SKILL.md | ✅ Validado |
| Taste-Skill: SKILL.md com regras anti-slop + dials. Não é um onboarding de papel — é uma skill temática. | github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md | ✅ Validado |
| Designer Skills: múltiplos SKILL.md que agentes carregam individualmente. **CORREÇÃO:** o repo irmão designpowers TEM arquivo-mestre de orquestração — CLAUDE.md + GEMINI.md + `agents/` (10 agentes) + `hooks/`. A Ideia 5 NÃO é única. | github.com/owl-listener/designpowers (corrigido pós-auditoria) | ❌ Invalidado |
| Design Kit: AGENTS.md (raiz) define papel do orquestrador, estrutura do repo, regras de trabalho (6 itens: tokens fonte única, qualidade impeccable, fluxo de design, loops fechados, 1 writer/arquivo, sem build), backlog, decisões pendentes. | AGENTS.md do kit (~130 linhas) | ✅ Validado |
| CLAUDE.md: onboarding específico para Claude Code (~90 linhas). | CLAUDE.md do kit | ✅ Validado |
| DESIGN.md: manual anti-slop como "voz do design" (~177 linhas). É o complemento de gosto/taste ao AGENTS.md. | DESIGN.md do kit | ✅ Validado |

**Conclusão da validação:** ❌ INVALIDADO como "categoria nova". O conceito "role onboarding para design" JÁ existe no designpowers (Owl-Listener): CLAUDE.md + GEMINI.md + `agents/` com 10 agentes de design orquestrados + `hooks/`. O que o kit oferece de único nesta ideia é reduzido a: **design system CSS real + detectores executáveis** como parte do onboarding (designpowers orquestra agentes mas não traz tokens/componentes CSS implementados). Reformulada como "o kit faz onboarding com design system executável", a ideia volta a ter mérito — mas como aprimoramento de algo existente, não como invenção.

**Risco de validação:** ⚠️ **Precisa de validação:** A pergunta agora é "o kit faz role onboarding MELHOR que designpowers?", não "é único?". O designpowers tem 10 agentes orquestrados + CI + hooks; o kit tem AGENTS.md + CLAUDE.md + DESIGN.md + tokens/componentes CSS + detectores. Não há dado público sobre qual abordagem gera melhor resultado de design. Sem testar lado a lado (mesmo brief, dois kits), não dá para afirmar superioridade.

**Viabilidade:** Alta. O AGENTS.md já existe. A CLAUDE.md já existe. O DESIGN.md já existe. O trabalho é: (a) criar versões para outros agentes (CODEX.md, CURSOR.md, GEMINI.md), (b) documentar o conceito de "role onboarding", (c) comunicar no README/showcase.

**O que o concorrente faria:** Anthropic (frontend-design) já tem o conceito de "skill que define como o agente pensa sobre design". Adicionar algo como "CLAUDE.md para design" seria trivial para eles. Mas o kit junta AGENTS.md (orquestração) + CLAUDE.md (agente específico) + DESIGN.md (gosto/taste) em 3 camadas — os concorrentes juntam tudo em 1 SKILL.md. A arquitetura em 3 camadas é o moat, não os arquivos individuais.

---

### Ideia 6: "Handoff Estruturado com Export Real" — spec + tokens exportáveis + docs por componente

**Descrição:** A skill `design-handoff` do kit não é só um prompt que gera documentação — ela tem **scripts reais de export**: `python scripts/export-tokens.py` gera `tokens/tokens.json` (resolvido, estruturado por tema e categoria) e `tokens/tokens.css` (cópia portátil). Complementada por `docs/componentes/` (9 docs de handoff por grupo: botoes, badges-cards-alerts, formularios, overlays, dropdown, breadcrumb, tabela, stepper, paginacao) + templates de spec (`templates/spec-handoff.md`). Nenhum concorrente tem export automatizado de tokens + docs de handoff por componente.

**Gap que ataca:** Dimensões 1 (tokens), 2 (componentes), 4 (skills de processo).

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Designer Skills Collection: comando `/handoff` gera "developer handoff package with measurements, behaviours, edge cases, and a QA checklist". É geração por prompt, sem scripts de export automatizados. | github.com/owl-listener/designer-skills + composio.dev/content/top-design-skills | ✅ Validado |
| Impeccable: comando `extract` extrai padrões de design, mas não gera tokens exportáveis em JSON. | impeccable.style (documentação) | ✅ Validado |
| Design Kit: `scripts/export-tokens.py` (Python 3 stdlib, zero dependências) lê styles/tokens.css, resolve `var(--...)`, gera tokens.json (light/dark por categoria) + tokens/tokens.css. | scripts/export-tokens.py + tokens/README.md | ✅ Validado |
| Design Kit: docs/componentes/ com 9 arquivos .md, cada um documentando classes CSS, tokens, estados, a11y e exemplos de uso. | docs/componentes/*.md (9 arquivos) | ✅ Validado |
| Design Kit: templates/spec-handoff.md como template de spec de implementação. | templates/ | ✅ Validado |
| Nenhum concorrente tem (a) script de export automatizado + (b) docs de handoff por componente + (c) template de spec no mesmo pacote. | Pesquisa de mercado §2, §4 | ✅ Validado |

**Conclusão da validação:** ✅ VALIDADO. O combo "export script + component docs + spec template" é único. Designer Skills tem o `/handoff` mas sem automação de tokens. O gap é real.

**Viabilidade:** Alta. Já existe. O trabalho é: (a) documentar o fluxo de handoff como diferencial competitivo, (b) adicionar export para mais formatos (Figma variables JSON? Style Dictionary?), (c) criar um `npx designkit-export` standalone.

**O que o concorrente faria:** Open Design tem "142+ design systems portáteis" como DESIGN.md. Eles poderiam adicionar um script de export similar. A barreira é média — requer parser de CSS para resolver `var()`. **Mitigação:** o kit já tem o parser (export-tokens.py). A vantagem é de execução, não de conceito.

---

### Ideia 7: "Casos como Prova de Qualidade" — 7 casos reais com scoring quantitativo como portfólio do agente

**Descrição:** Nenhum concorrente publica casos reais gerados pela própria ferramenta COM avaliação quantitativa independente (critique score). Os 7 casos do kit (Lumen 4.7/5, Norte 4.6/5, Tereza, Aurora, Linha Direta, Redesign Demo, Ponto Final) são a prova de que o sistema funciona de ponta a ponta. Posicionar como "não acredite em nós — veja o que o kit constrói e a nota que recebeu".

**Gap que ataca:** Dimensão 6 (casos com scoring) + dimensão 9 (prova social alternativa a estrelas).

**Validação objetiva:**

| Evidência | Fonte | Status |
|---|---|---|
| Taste-Skill: tasteskill.dev mostra "Projects built with Taste Skill" (Floria, Collective OS) — são projetos da comunidade, sem scoring de qualidade. | tasteskill.dev | ✅ Validado |
| Impeccable: site mostra depoimentos e cases de usuários (ex.: hedge-ops.com). Sem scoring quantitativo. | impeccable.style + hedge-ops.com/posts/impeccable-design | ✅ Validado |
| Designer Skills: zero casos com scoring quantitativo documentados. (designpowers tem `examples/`, mas sem scoring de critique como o kit.) | github.com/owl-listener/designer-skills + designpowers | ✅ Validado (com nuance) |
| Anthropic frontend-design: zero casos documentados. | anthropics/skills | ✅ Validado |
| Design Kit: 7 casos em docs/casos/. Lumen: 2 critiques (v1→v2, 4.7/5). Norte: critique completo (4.6/5). Ponto Final: 10 artefatos cobrindo ciclo completo. Aurora: anti-slop check (14/14). | docs/casos/ (8 diretórios) + avaliacao-inicial.md §1.6 | ✅ Validado |
| Cada caso tem HTML funcional, CSS, e critique/auditoria documentados — não são só screenshots. | docs/casos/lumen/index.html, docs/casos/norte/index.html, etc. | ✅ Validado |

**Conclusão da validação:** ✅ VALIDADO. Nenhum concorrente publica casos com scoring quantitativo. A prática de "provar com casos reais auditados" é um diferencial genuíno.

**Risco de validação:** ⚠️ **Precisa de validação:** Os scores (4.7/5, 4.6/5) foram gerados pelo próprio design-critic do kit — ou seja, o kit avalia a si mesmo. Um cético dirá "claro que o kit se dá notas altas". Para validação externa, seria necessário: (a) submeter os casos a avaliação humana independente, ou (b) rodar o critique do Impeccable ou Taste-Skill sobre os mesmos casos e comparar scores. Sem isso, a alegação de qualidade é circular (o juiz é o próprio réu). **Marcar como "precisa de validação externa" — não usar os scores como prova até ter avaliação independente.**

**Viabilidade:** Média. Os casos já existem. O trabalho é: (a) obter validação externa (humana ou via skill concorrente), (b) criar a seção "Resultados" no showcase (Ideia 4), (c) escrever case studies em inglês para o README/site.

**O que o concorrente faria:** Taste-Skill poderia adicionar scoring aos projetos da comunidade (já tem o conceito de "projetos construídos"). Impeccable poderia publicar cases com suas próprias métricas. A barreira é baixa para "mostrar cases", mas média para "mostrar cases COM scoring quantitativo independente". **Mitigação:** ser o primeiro a estabelecer o padrão de "cases auditados com scoring".

---

## 3. Sumário Executivo: O Que Fazer e Em Que Ordem

### 3.1 As 3 Vulnerabilidades Fatais (resolver antes de qualquer diferenciação)

| # | Gap | Ação | Dependência |
|---|---|---|---|
| **G1** | Sem licença | Escolher MIT ou Apache 2.0 | Decisão do fundador |
| **G2** | Sem distribuição one-command | Criar `npx skills add` install (padrão SKILL.md no repo) | Repo público + licença |
| **G3** | Zero prova social | Tornar repo público; listar em skills.sh, AwesomeSkills, LobeHub, SkillsMP | Licença + distribuição |

**Sem G1+G2+G3 resolvidos, nenhuma ideia de diferenciação importa** — o kit é invisível e ininstalável.

### 3.2 As 7 Ideias em Ordem de Prioridade

| # | Ideia | Impacto | Esforço | Dependências | Validada? |
|---|---|---|---|---|---|
| **1** | Showcase como Prova Viva (Ideia 4) | Fecha gap interno crítico (placeholder vazio) | 6-9h | Nenhuma | ✅ Totalmente |
| **2** | Design System Executável (Ideia 1) — posicionamento | Diferenciação central: tokens + componentes reais | 1-2 dias (docs + comunicação) | G1, G2 | ✅ Totalmente |
| **3** | QA Automatizado standalone (Ideia 2) | Cria categoria própria: "lint de design para IA" | 1-2 semanas | G1, G2 | ✅ Totalmente |
| **4** | Handoff Estruturado (Ideia 6) — comunicar + expandir | Diferenciação técnica defensável | 3-5 dias | Nenhuma (já existe) | ✅ Totalmente |
| **5** | Ciclo Fechado de Design (Ideia 3) — comunicar integração | Diferenciação de arquitetura (skills + tokens + QA) | 3-5 dias (docs + visual) | Fortalecer fallback a11y | ✅ Parcial (⚠️ breadth vs depth) |
| **6** | AGENTS.md como Onboarding Universal (Ideia 5) | Cria categoria "role onboarding" (NÃO única — designpowers já faz) | 1-2 semanas (multi-agente) | Testar em Cursor, Copilot, Gemini; comparar vs designpowers | ❌ Inválida como inovação; ⚠️ validar se "faz melhor" |
| **7** | Casos como Prova de Qualidade (Ideia 7) | Prova social alternativa a estrelas | 1-2 semanas (validação externa) | Validação externa dos scores | ⚠️ Precisa de validação externa |

### 3.3 O que NÃO fazer (ideias descartadas com razão)

| Ideia descartada | Razão |
|---|---|
| Competir em quantidade de skills (fazer 60+) | Designer Skills já tem 87 (suíte 130+). Não é onde o kit ganha. Jogar o jogo do concorrente é perder. |
| Fazer Electron app / desktop tool | Open Design e Open CoDesign já ocupam esse espaço. O kit é zero-build por filosofia. |
| Adicionar geração de imagens (DALL-E/Midjourney) | Fora do escopo do DESIGN.md; decisão pendente do fundador; não é core. |
| Criar "design systems portáteis" como Open Design | Open Design já tem 142+ e 57K estrelas. Competir nisso é chegar tarde demais. |
| Fazer integração com Figma | Impeccable e outros já têm. Custo alto, benefício incerto. |

---

## 4. Métricas de Sucesso (como saber se as ideias funcionaram)

| Ideia | Métrica | Alvo (6 meses pós-lançamento) |
|---|---|---|
| Showcase vivo | Tempo até primeira impressão "uau" no showcase | < 30s (hero → resultados → tokens vivos) |
| Design System Executável | Menções "design system" + "executável" em referências externas | > 5 menções em blogs/social |
| QA Automatizado | Instalações do `npx designkit-check` | > 500 (tração inicial) |
| Handoff Estruturado | Issues/PRs referenciando docs/componentes/ ou tokens.json | > 10 |
| Ciclo Fechado | Casos completos (brief → handoff) feitos por terceiros com o kit | > 3 |
| AGENTS.md Onboarding | Agentes configurados via AGENTS.md (estrelas/forks do repo) | > 100 |
| Casos com Scoring | Scores de validação externa (humana ou concorrente) | Pelo menos 2 casos com avaliação independente |

---

## 5. Riscos e Mitigações (visão consolidada)

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Open Design (57K ★) domina o espaço "open-source design tool" e sufoca visibilidade | Alta | Alto | Diferenciar no que Open Design NÃO faz: design system CSS implementado + componentes reais + QA determinístico. Open Design é templates/schemas; o kit é código funcional. |
| Impeccable adiciona detectores executáveis e neutraliza Ideia 2 | Média | Médio | Ser primeiro + ter mais checks (98 vs 59) + integração CI pronta. O script é código aberto — se copiarem, a diferenciação vira "quem executa melhor". |
| Taste-Skill (Vercel-sponsored) recebe investimento pesado e acelera | Média | Alto | Vercel foca em deploy/hosting; o kit foca em design system + QA. São complementares, não competidores diretos. Parceria possível. |
| Designer Skills adiciona design system CSS e iguala o kit em breadth+depth | Média | Alto | 87 skills já é difícil de manter; mas a suíte tem CI, tests e grounding acadêmico — não é improvável que adicionem tokens CSS. O moat do kit NÃO é mais as skills; é o design system CSS implementado + detectores de tells. Proteger e ampliar ESSA vantagem é a prioridade. |
| Falta de decisão do fundador (licença, nome, open-source) paralisa tudo | Alta | Crítico | Este documento + pesquisa-mercado.md + avaliacao-inicial.md formam o dossiê completo para a conversa de decisão. |
| Scores dos casos são circulares (kit avalia a si mesmo) e não convencem | Média | Médio | Obter validação externa antes de usar scores como prova de marketing (ver Ideia 7, risco de validação). |

---

## 6. Apêndice: Checklists de Validação Pendente

### ⚠️ Itens marcados como "precisa de validação" (NÃO implantar sem resolver)

| Item | O que validar | Método sugerido |
|---|---|---|
| **Ideia 3 (Ciclo Fechado): breadth vs depth** | O mercado prefere 130+ skills amplas (Owl-Listener, já com 2.3K★ + CI + grounding acadêmico) ou 8 skills profundas integradas com design system CSS? | Survey com 20+ devs/designers que usam agentes de IA; ou análise de issues/stars. Dado parcial já disponível: Owl-Listener tem 2.3K★ — breadth tem demanda |
| **Ideia 5 (AGENTS.md onboarding): valor de "role onboarding"** | **REVISADO:** designpowers (Owl-Listener) já faz role onboarding (CLAUDE.md + GEMINI.md + 10 agentes). A pergunta não é mais "é único?" (não é), mas "o kit faz MELHOR que designpowers?" | Comparar AGENTS.md + CLAUDE.md + DESIGN.md do kit vs designpowers: cobertura de design system + detectores vs agentes orquestrados |
| **Ideia 7 (Casos com scoring): validação externa dos scores** | Os scores 4.7/5 e 4.6/5 são replicáveis por avaliador independente? | Rodar Impeccable critique sobre Lumen e Norte; comparar scores; ou avaliação humana cega |
| **Designer Skills: real depth das 87 skills** | RESOLVIDO (auditoria feita 2026-08): skills têm grounding acadêmico (RESEARCH.md mapeia 44 skills a papers), CI (designpowers) e tooling (5 scripts). NÃO são superficiais. Pergunta residual: alguma implementa tokens/componentes CSS reais? Resposta: não. | ✔ Auditoria concluída — ver seção Correções C1-C5 |

---

*Documento produzido pelo Pesquisador do Design Kit. Próximo passo: revisão pelo Orquestrador e apresentação ao fundador para decisão de licenciamento e lançamento público.*