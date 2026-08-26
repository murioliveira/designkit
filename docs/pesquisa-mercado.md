# Pesquisa de Mercado — Agentes de Design de IA & Open Source

> **Data:** Agosto 2026  
> **Escopo:** Concorrentes, fatores de adoção open-source, formatos de descoberta, tendências  
> **Regra perene:** Nenhuma menção à Liquid em qualquer parte deste documento.

---

## 1. Sumário Executivo

O mercado de "agentes de design de IA" explodiu entre outubro de 2025 e meados de 2026. O formato **Agent Skills** (SKILL.md), introduzido pela Anthropic como open standard em dezembro/2025, tornou-se o protocolo universal: é suportado por Claude Code, OpenAI Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf, Antigravity, VS Code e mais de 70 harnesses. O ecossistema movimenta centenas de milhares de instalações, com projetos atingindo 40–57K estrelas no GitHub em semanas.

**Achado central:** O Design Kit compete num espaço de alta velocidade onde a **portabilidade** (funcionar em qualquer agente), a **qualidade anti-slop** (design que não parece template) e a **distribuição zero-atrito** (`npx skills add`) são os três pilares de sucesso. O kit está bem posicionado com seus tokens, componentes showcase e skills, mas precisa de posicionamento competitivo claro nos três pilares.

---

## 2. Panorama Competitivo

### 2.1 Matriz de Concorrentes Diretos

| Projeto | Autor | Estrelas GitHub | Instalações | Modelo | Diferencial |
|---|---|---|---|---|---|
| **Impeccable** | Paul Bakaus | ~40K | 160K+ | 1 skill, 23 comandos, 59 regras detectoras | Vocabulário de design compartilhado humano-IA; live browser iteration; Apache 2.0 |
| **Taste-Skill** | Leonxlnx | ~46K | — | 13 skills, 3 dials (VARIANCE, MOTION, DENSITY) | Patrocinado pela Vercel; anti-slop framework; design-taste checklist; MIT |
| **Open Design** | nexu-io | ~57K (em 8 semanas) | — | 259+ skills, 142+ design systems | Local-first; alternativa open-source ao Claude Design; multi-agente; Apache 2.0 |
| **Designer Skills Collection** | Owl-Listener (Marie Claire Dean) | ~2.1K | — | 63 skills, 27 comandos, 8 plugins | Cobertura completa do processo de design (research→handoff); gratuito |
| **Anthropic frontend-design** | Anthropic (oficial) | 65K+ | 277K+ | Skill oficial no marketplace Claude | Maior base instalada; curadoria Anthropic; licença custom |
| **OpenAI frontend-skill** | OpenAI (oficial) | — | — | Skill oficial para Codex | Paralelo ao Anthropic; foco em guardrails anti-slop |
| **UI/UX Pro Max** | Comunidade | — | ~8.6K | 50 estilos, 21 paletas, 50 fontes, 20 gráficos | Maior catálogo de ativos visuais; multi-stack (React, Next.js, Vue, Svelte, SwiftUI, Flutter, Tailwind, shadcn/ui) |
| **Open CoDesign** | OpenCoworkAI | — | — | Electron desktop app, 12 módulos | UI com sliders, multi-frame preview; MIT |
| **Universal** | P Yash Jain | — | — | Art director para React com agentes | Processo de design deliberado (brief → explore → select) |
| **Design Process Pack** | Julian Oczkowski | — | — | 7 skills | Foco em processo profissional, não atalhos |
| **stop-slop** | hardikpandya | — | — | Anti-slop para prosa/texto | Complementar aos skills de design visual |

### 2.2 Análise por Camada de Valor

```
┌─────────────────────────────────────────────────────────────┐
│ CAMADA DE CRÍTICA/REFINAMENTO                               │
│ impeccable (23 comandos, 59 regras detectoras)              │
│ taste-skill (3 dials calibráveis)                            │
│ stop-slop (prosa)                                            │
├─────────────────────────────────────────────────────────────┤
│ CAMADA DE GERAÇÃO DE UI                                     │
│ Anthropic frontend-design · OpenAI frontend-skill            │
│ UI/UX Pro Max (ativos + stacks)                             │
│ SkillUI · Theme Factory                                      │
├─────────────────────────────────────────────────────────────┤
│ CAMADA DE DESIGN SYSTEMS + TOKENS                           │
│ ★ Design Kit (tokens.css ~147 tokens, components.css,       │
│   showcase index.html, skills empacotadas)                  │
│ Open Design (142+ design systems portáteis)                 │
├─────────────────────────────────────────────────────────────┤
│ CAMADA DE PROCESSO COMPLETO                                 │
│ Designer Skills Collection (research → handoff)              │
│ Design Process Pack (7 skills processuais)                  │
│ Universal (brief → explore → select)                        │
├─────────────────────────────────────────────────────────────┤
│ CAMADA DE PLATAFORMA / ECOSSISTEMA                          │
│ Vercel skills CLI (distribuição) · skills.sh (descoberta)   │
│ Composio · LobeHub · AwesomeSkills · SkillsMP                │
│ Claude Code plugin marketplace · Codex catalog              │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Onde o Design Kit se Encaixa

**Vantagens competitivas do kit:**
- **Tokens como fonte única de verdade** — 147 tokens semânticos (claro/escuro) com componentes CSS reais consumindo `var(--...)` — nenhum concorrente tem um sistema de tokens tão completo e componentizado com showcase vivo
- **Showcase index.html** — 14 seções de componentes reais renderizados no navegador, zero build — a maioria dos concorrentes são apenas skills, sem UI demonstrável
- **Skills empacotadas** — 8 papéis (researcher, IA, UI designer, redesign, critic, refine, a11y, handoff) — cobre o ciclo completo, não só geração
- **AGENTS.md de onboarding** — transforma qualquer agente-hospedeiro num setor de design — conceito único

**Vulnerabilidades:**
- **Sem presença no ecossistema `npx skills`** — não está nos diretórios de descoberta (skills.sh, AwesomeSkills, LobeHub etc.)
- **Zero estrelas no GitHub** — num mercado onde estrelas = validação social, isso é um bloqueador de adoção
- **Portabilidade parcial** — wrappers em `.claude/skills/` e `.codex/`, mas sem suporte explícito a Cursor, Copilot, Gemini CLI, Windsurf
- **Sem licença definida** — decisão do fundador pendente; sem licença aberta não há adoção open-source
- **Sem `npx`/one-command install** — instalação requer clone manual + configuração

---

## 3. O Que Atrai Desenvolvedores para Projetos Open-Source de Design

### 3.1 Os 10 Fatores de Sucesso (ordem de impacto)

| # | Fator | Evidência | Como o Design Kit está |
|---|---|---|---|
| 1 | **One-command install** | `npx skills add` domina o ecossistema; Impeccable: `npx impeccable install`; Taste-Skill: `npx skills add Leonxlnx/taste-skill` | ❌ Não tem |
| 2 | **README matador (hero section)** | 80% dos novos visitantes decidem em 10s; o README é a parte mais importante do repo | ⚠️ README em pt-BR apenas; falta hero em inglês com one-liner + comando de install + badge de stars |
| 3 | **Demo/showcase vivo** | Open Design tem sandbox preview; Taste-Skill tem projetos construídos exibidos | ✅ index.html showcase (mas não linkado de forma proeminente no README) |
| 4 | **Licença aberta clara** | MIT e Apache 2.0 dominam; sem licença = zero adoção corporativa | ❌ Pendente (decisão do fundador) |
| 5 | **Estrelas GitHub como prova social** | Ollama: 136K+; Taste-Skill: 46K+ em 4 meses; Open Design: 57K em 8 semanas | ❌ Repo privado ou sem tração |
| 6 | **Portabilidade multi-agente** | Skills que funcionam em 7+ harnesses ganham 3x mais instalações | ⚠️ Wrappers parciais (Claude + Codex); sem Cursor, Copilot, Gemini |
| 7 | **Documentação farta e em inglês** | "Documentation is not optional"; 3 buckets: quickstart, API reference, rationale | ⚠️ Docs em pt-BR; falta docs em inglês para alcance global |
| 8 | **Atualização frequente** | Commits recentes = sinal de projeto vivo; Open Design teve 10 releases em 8 semanas | ✅ Ativo (última sincronização ago/2026) |
| 9 | **Comunidade responsiva** | Issues respondidas, PRs aceitos, Discord ativo | ❌ Sem canais públicos |
| 10 | **Zero build steps** | "Abre direto no navegador" é valor real; npm overload afasta designers | ✅ HTML/CSS/JS puro |

### 3.2 O Ciclo de Adoção de um Repo de Design-Tool

```
DESCoberta          →  AVALIAÇÃO          →  INSTALAÇÃO        →  PRIMEIRO VALOR    →  RETENÇÃO
(npx skills search,   (README, stars,        (one command,       (demo em 30s,        (qualidade
 GitHub trending,     demo visual,           zero config,        resultado visível,   consistente,
 marketplace,         licença,               funciona em         "uau, funciona")     comunidade,
 YouTube/Twitter)     documentação)          qq agente)                               atualizações)
 
 ↳ 90% dos projetos morrem aqui           ↳ fricção = desistência
   se não têm: stars, demo, licença
```

---

## 4. Formatos de Descoberta & Distribuição

### 4.1 O Ecossistema `npx skills` (Vercel)

O **`npx skills add <owner>/<repo>`** é o mecanismo dominante de distribuição de Agent Skills desde janeiro/2026. Publicado pela Vercel, tornou-se o "npm dos skills":

- **Zero instalação global** — `npx` executa direto
- **Suporta 73+ harnesses** — Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode, Antigravity, Windsurf, Aider, Augment, etc.
- **Descoberta automática** — vasculha repositórios por `SKILL.md` em até 3 níveis de profundidade
- **Skill Packs** (Vercel, jun/2026) — bundling step: múltiplos skills em um pacote nomeado

**Exemplos de instalação:**  
```bash
npx skills add vercel-labs/agent-skills        # Vercel React best-practices
npx skills add nvidia/skills                    # NVIDIA-verified
npx skills add Leonxlnx/taste-skill            # Design taste
npx skills add mattpocock/skills --skill implement  # TypeScript
```

### 4.2 Diretórios de Descoberta

| Diretório | Volume | Modelo | URL |
|---|---|---|---|
| **skills.sh** | 400K+ skills | Catálogo open-source com `npx skills` | skills.sh |
| **SkillsMP** | 400K+ skills | Marketplace com crawling automático do GitHub | skillsmp.com |
| **AwesomeSkills** | Curadoria | Lista comunitária pontuada | awesomeskill.ai |
| **LobeHub Skills** | Marketplace | Catálogo com busca e categorias | lobehub.com/skills |
| **OpenAgentSkill** | 180+ skills | Biblioteca mantida por 1 pessoa | openagentskill.com |
| **Composio Skills** | Catálogo + integração | Foco em marketing/dev tools | composio.dev |
| **SkillsLLM** | Index com auditoria | Scan de segurança + prompt injection | skillsllm.com |
| **Claude Code Plugin Marketplace** | Oficial Anthropic | `/plugin marketplace` direto no terminal | — |
| **Codex Skill Catalog** | Oficial OpenAI | `$skill-installer` no CLI | — |
| **OpenDesign Plugin Library** | 16 skills | Foco em design | open-design.ai/plugins/skills |

### 4.3 Outros Formatos de Distribuição

| Formato | Quando usar | Exemplos |
|---|---|---|
| **npm package** | Componentes, tokens exportáveis, libs JS | `npm install designkit` |
| **npx comando** | Instalação de skills, scaffolds, checks | `npx impeccable install`, `npx create-designkit` |
| **GitHub Release** | Distribuição versionada com changelog | Open Design v0.9.0 (10 releases) |
| **GitHub raw/URL** | Instalação manual, agentes que leem URLs | Claude Code: "instale o skill de https://..." |
| **Marketplace nativo** | Plugins oficiais dentro dos agentes | `/plugin install frontend-design@claude-plugins-official` |
| **git clone + pasta** | Instalação manual tradicional | `.claude/skills/`, `.codex/skills/`, `.cursor/skills/` |

---

## 5. Tendências e Padrões (2025–2026)

### 5.1 Agent Skills como Novo npm

O ecossistema de Agent Skills está reproduzindo a evolução do npm:
- **Fase 1:** Instalação manual (clone + copiar pasta) → 2025
- **Fase 2:** CLI unificado (`npx skills add`) → jan/2026
- **Fase 3:** Skill Packs (bundling) → jun/2026
- **Fase 4 (emergente):** Registries com verificação, auditoria de segurança, scores de qualidade
- **Fase 5 (futura):** Monetização, skills premium, mercado de skills

**Implicação para o Design Kit:** Precisa estar no `npx skills` o quanto antes. A janela de oportunidade para ser "primeiro" num nicho está fechando.

### 5.2 A Narrativa Anti-Slop Domina

Todo skill de design de sucesso se posiciona como "anti-slop":
- Impeccable: "The missing design vocabulary for agents"
- Taste-Skill: "The Anti-Slop Frontend Framework for AI Agents"
- Anthropic frontend-design: bane Inter, Roboto, Arial, Space Grotesk, gradientes roxo-azul
- stop-slop: ataca AI tells em prosa

**O diferencial não é mais "faz design bonito" — é "faz design que não parece que uma IA fez".**

### 5.3 Portabilidade é o Novo Lock-in

O valor central do formato Agent Skills é que **um skill funciona em todos os harnesses**. Projetos que se posicionam como "para Claude Code" perdem para projetos "para qualquer agente". Open Design explicitamente auto-detecta 16 CLIs diferentes no PATH.

### 5.4 Design Systems Portáteis (não só Skills)

Open Design introduziu o conceito de **Design Systems como Markdown portátil** (esquema de 9 seções: color, typography, spacing, layout, components, motion, voice, brand, anti-patterns). Isto vai além de skills — é infraestrutura de design que viaja entre agentes.

**O Design Kit tem o embrião disso:** `DESIGN.md` + `tokens.css` + `tokens.json` + componentes. Mas não está empacotado como formato portátil interoperável.

### 5.5 GitHub Stars como Moeda

57K estrelas em 8 semanas (Open Design). 46K estrelas em 4 meses (Taste-Skill). As estrelas não são vaidade — são o principal fator de:
- Prova social para novos usuários
- Ranqueamento em diretórios (skills.sh, trending)
- Confiança para adoção corporativa
- Atração de contribuidores

### 5.6 Vercel como Ecossistema-Âncora

A Vercel emergiu como o player de infraestrutura do ecossistema de Agent Skills:
- Publicou o `skills` CLI (`npx skills add`)
- Patrocina Taste-Skill (OSS sponsorship)
- Introduziu Skill Packs
- Domina o deploy de apps geradas por skills

---

## 6. Recomendações Acionáveis para o Design Kit

### 6.1 Curto Prazo (pré-v1.0.0 — semanas)

| Ação | Impacto | Esforço |
|---|---|---|
| **Criar `npx skills add` install** — publicar o kit como um repo que o `skills` CLI detecta com `SKILL.md` no padrão | ⭐⭐⭐⭐⭐ | Baixo |
| **README em inglês** com hero section: one-liner, comando de install, badge, link para showcase | ⭐⭐⭐⭐⭐ | Baixo |
| **Listar nos 5 principais diretórios:** skills.sh, AwesomeSkills, SkillsMP, LobeHub, OpenAgentSkill | ⭐⭐⭐⭐ | Médio |
| **Resolver licença** (MIT ou Apache 2.0 recomendados) | ⭐⭐⭐⭐⭐ | Decisão do fundador |
| **Tornar repo público** e começar a acumular estrelas | ⭐⭐⭐⭐⭐ | Decisão do fundador |
| **Wrapper portátil único** — um `SKILL.md` raiz que funciona em Claude Code, Codex, Cursor, Copilot, Gemini CLI simultaneamente | ⭐⭐⭐⭐ | Médio |
| **Adicionar suporte a Cursor, Copilot, Gemini CLI** nas camadas de portabilidade | ⭐⭐⭐ | Baixo |

### 6.2 Médio Prazo (v1.0.0 — meses)

| Ação | Impacto | Esforço |
|---|---|---|
| **Posicionamento "anti-slop" explícito** — o kit já tem DESIGN.md, tokens, componentes e showcase que são anti-slop por natureza; comunicar isso | ⭐⭐⭐⭐ | Baixo |
| **Site de produto** (designkit.dev?) com showcase vivo, docs em inglês, e `npx` install | ⭐⭐⭐⭐ | Médio |
| **Design Systems como formato portátil** — exportar `DESIGN.md` + tokens no esquema de 9 seções (inspirado no Open Design) para interoperabilidade | ⭐⭐⭐⭐ | Alto |
| **Vídeos demo no YouTube** — "design kit in 60 seconds", tutoriais de cada skill | ⭐⭐⭐ | Médio |
| **Comunidade** — Discord, GitHub Discussions, responder issues rápido | ⭐⭐⭐ | Médio |

### 6.3 Diferenciação Competitiva (longo prazo)

O Design Kit tem **dois diferenciais que nenhum concorrente junta:**

1. **Tokens + Componentes + Showcase vivo** — a maioria dos concorrentes são apenas skills (instruções), sem design system implementado. O kit tem um sistema de tokens real (~147 tokens semânticos), componentes CSS consumindo `var(--...)`, e showcase HTML que abre no navegador.

2. **Ciclo completo de design como agente** — 8 papéis (researcher → handoff) cobrindo o fluxo inteiro, não só geração de UI. A Designer Skills Collection (Owl-Listener) também cobre o ciclo, mas sem tokens/componentes implementados.

**Posicionamento recomendado:**  
> "O Design Kit não é só mais um skill de design — é um **setor de design inteiro em um pacote**: design system real (tokens + componentes + showcase) + skills de processo completo (8 papéis) + onboarding (AGENTS.md). Nenhum concorrente junta os três."

### 6.4 Análise de Riscos

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Open Design domina o espaço de "alternativa open-source" com 57K estrelas, tornando muito difícil competir por atenção | Alta | Diferenciar por tokens + componentes implementados (Open Design tem 142 design systems mas são templates, não sistemas funcionais com showcase) |
| Taste-Skill e Impeccable consolidam o nicho "anti-slop" | Média | Posicionar o kit como "infraestrutura" (camada abaixo), não só "gosto" |
| Anthropic/OpenAI lançam design system oficial completo, tornando skills de terceiros redundantes | Baixa | Skills de terceiros continuam relevantes por customização e independência de vendor |
| O formato Agent Skills evolui e o kit fica desatualizado | Média | Manter compatibilidade com o open standard; usar `SKILL.md` canônico |
| Falta de decisão do fundador (licença, nome, open-source vs comercial) paralisa o lançamento | Alta | Este documento serve como base para a conversa de decisão |

---

## 7. Fontes e Referências

- **Impeccable:** github.com/pbakaus/impeccable · impeccable.style · Apache 2.0 · ~40K ★
- **Taste-Skill:** github.com/Leonxlnx/taste-skill · tasteskill.dev · MIT · ~46K ★
- **Open Design:** github.com/nexu-io/open-design · open-design.ai · Apache 2.0 · ~57K ★
- **Designer Skills Collection:** github.com/owl-listener/designer-skills · 63 skills · ~2.1K ★
- **Anthropic frontend-design:** anthropics/skills (65K ★) · 277K+ installs
- **OpenAI frontend-skill:** Codex CLI catalog
- **UI/UX Pro Max:** awesomeskill.ai · 8.6K+ installs
- **Open CoDesign:** github.com/OpenCoworkAI/open-codesign · MIT
- **Universal:** github.com/pyashjain/universal · art director para React
- **Design Process Pack:** github.com/julianoczkowski/designer-skills · 7 skills
- **stop-slop:** github.com/hardikpandya/stop-slop
- **Agent Skills spec:** platform.claude.com/docs · Open Standard (dez/2025)
- **npx skills CLI:** github.com/vercel-labs/skills · Vercel (jan/2026)
- **Diretórios:** skills.sh · skillsmp.com · awesomeskill.ai · lobehub.com · openagentskill.com · skillsllm.com
- **Ecossistema:** inference.sh/blog · agentman.ai/blog · neon.com/blog · developersdigest.tech
- **Landscape 2026:** lovart.ai/blog/ai-design-competitor-landscape-2027 · wireflow.ai/blog/best-ai-design-agent-tools-in-2026
- **Open source growth:** landbase.com/blog/fastest-growing-open-source-dev-tools · github.blog/octoverse · sonatype.com/blog
- **Adoção de design systems:** report.zeroheight.com · product.hubspot.com/blog · backlight.dev/mastery