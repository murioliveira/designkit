# Avaliação Inicial — Design Kit v0.9.0

> **Avaliador:** Evaluator (role ed3723c5)  
> **Data:** 2026-08-25  
> **Alcance:** repositório completo — tokens, componentes, showcase, skills, docs, casos, scripts de QA  
> **Método:** revisão do DESIGN.md, inspeção de código (CSS/JS/HTML), execução dos detectores (`smoke-test.py` + `anti-slop-check.py`), verificação estrutural do diretório e análise qualitativa das skills  

---

## Veredito: **APROVADO COM RESSALVAS**

O Design Kit está sólido, funcional e pronto para uso interno. Os detectores passam limpos (8/8 smoke, 98/98 anti-slop), o design system cobre 18+ componentes com dark mode, acessibilidade e zero build tooling, e os 8 casos validados provam que o fluxo research→UI→critique→refine→handoff funciona de ponta a ponta. As ressalvas são de maturidade de produto (pré-1.0), cobertura de portabilidade e algumas lacunas de componentes/documentação. Nenhum blocker técnico.

**Nota geral:** 4.1/5 (média das heurísticas internas de avaliação do kit, aplicadas ao próprio kit).

---

## 1. Pontos fortes (o que está excelente)

### 1.1 QA determinístico — o diferencial do kit
- **`smoke-test.py`**: 8/8 PASS. Valida tokens (109 `var()` usados, 0 faltando), hex (0 em components.css), HTML (tags balanceadas, 70 ids, 14 âncoras, aria, lang pt-BR), CSS (390 pares de chaves), JS (sintaxe válida), docs (9 referenciados, 0 faltando), skills (8 com frontmatter, espelhos .claude 1:1), casos (7 arquivos esperados, 0 faltando).
- **`anti-slop-check.py`**: 98 checks em 14 arquivos, **0 falhas reais**. As 3 falhas em `docs/casos/redesign-demo/before.html` são fixtures esperadas (em-dash, Inter, eyebrows excessivos — o arquivo *before* existe justamente para demonstrar os tells antes da correção). Nenhum em-dash, hex ilegal, Inter, nome genérico, paleta proibida ou scroll cue em arquivo de produção.

### 1.2 DESIGN.md — voz de design de classe mundial
O manual anti-slop é o ativo mais valioso do kit. Cobre:
- **3 dials** (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY) com baseline e presets por tipo de página — o agente ajusta o tom antes do primeiro pixel.
- **AI tells banidos** (§4.1): 15 categorias com proibição explícita e exemplos (em-dash, gradiente roxo, 3 cards iguais, fake screenshots, Inter, nomes genéricos, números falsos-preciosos, scroll cues, version footers, eyebrows numerados, dots decorativos, strips no hero, split-header, zigzag repetido, `window.addEventListener('scroll')`, `h-screen`).
- **Locks** (§3): 1 accent/página, shape lock (pills→botões, md→cards, sm→inputs), theme lock (1 tema/página).
- **Hero discipline** (§4.2): ≤2 linhas headline, ≤20 palavras subtext, ≤4 elementos, padding ≤6rem, CTA visível sem scroll.
- **Redesign protocol** (§5.1): audit-first, SEO preservation (risco nº1), levers em ordem (tipografia → espaçamento → cor → motion → recomposição → substituição), árvore de decisão.
- **Mapa de design systems externos** (§5.2): govuk, Fluent, Carbon, Polaris, Atlaskit, Material, Primer — com honesty rule (usar o oficial quando o brief lê como um deles).
- **Pre-flight checklist** (§6): 20 itens obrigatórios antes de shipar.

### 1.3 Tokens como única fonte de verdade
- `styles/tokens.css`: ~330 linhas, ~147 tokens semânticos. Estrutura limpa: paleta bruta → tipografia → espaçamento → raios → sombras → motion → z-index → layout → tokens semânticos claro → tokens semânticos escuro.
- Zero hex em `components.css` (1900+ linhas) — confirmado pelo smoke test e inspeção manual.
- Primária índigo + neutra slate + semânticas (success/warning/error/info) com soft backgrounds para cada tema.
- Tipografia: `system-ui` stack (zero download, zero Inter).

### 1.4 Cobertura de componentes (ampla e consistente)
`components.css` (~2000 linhas, 9 seções) cobre:
- **§1 Botões**: 4 variantes (primary/secondary/outline/ghost), 3 tamanhos (sm/md/lg), estados (:hover, :active, :focus-visible, :disabled, loading), ícone, grupo.
- **§2 Badges**: 4 semânticos + contador + tamanhos.
- **§3 Cards**: básico, header/footer, interativo (hover/focus), horizontal.
- **§4 Alertas**: 4 variantes semânticas, com ação, compacto, dismissível.
- **§5 Demo panel**: vitrine do showcase (não componente de produto).
- **§6 Formulários**: input, textarea, select, checkbox, radio, toggle switch, label, helper, erro, validação (visual + aria), grupo, fieldset/legend.
- **§7 Acessibilidade**: prefers-reduced-motion (colapsa animações), screen-reader-only.
- **§8 Overlays**: tooltip (4 posições), modal (com trap de foco em JS), tabs (role tablist/tab/tabpanel ARIA), progress bar, skeleton loader, avatar.
- **§9 Avançados**: dropdown (disclosure pattern), breadcrumb (nav + aria), tabela (responsiva com wrapper), stepper (passos numerados, estados), paginação.

### 1.5 JavaScript de qualidade
`js/app.js` (~800 linhas, vanilla ES6+):
- 12 funções de inicialização, todas com blocos de comentário próprios.
- Tema: bootstrap inline no `<head>` (zero flash) + toggle + localStorage + aria-pressed.
- Menu mobile: off-canvas com backdrop, fecha ao clicar link/Esc/backdrop/redimensionar, aria-expanded.
- Scrollspy: IntersectionObserver (sem `window scroll` listener — segue DESIGN.md §4.1).
- Modal: trap de foco completo (tab/shift+tab circula nos elementos focáveis).
- Tabs: navegação por teclado (setas left/right, home/end).
- Formulários: toggle de senha, validação inline, checkbox indeterminado, toggle switches.

### 1.6 Casos validados (7, todos com artefatos)
| Caso | Tipo | Artefatos | Nota |
|---|---|---|---|
| Lumen | Landing (Persuade) | HTML, CSS, 2 critiques (v1→v2) | 4.7/5 aprovado |
| Norte | Dashboard (Operate) | HTML, CSS, critique | 4.6/5 aprovado com ressalvas |
| Brisa | Fluxo completo | research, IA, UI, critique, handoff | 4/4 skills executáveis |
| Aurora | Anti-slop | HTML, CSS, README | 14/14 checks |
| Linha Direta | Blocos | HTML, CSS, critique, README | 6 composições |
| Redesign Demo | Before/After | before (com tells), after (corrigido), auditoria, CSS | Fixture funcional |
| Tereza | Portfólio (Experience) | HTML, CSS, critique | Modo Experience |
| Ponto Final | Fluxo completo | 10 artefatos (brief→research→IA→UI→critique→a11y→refine→redesign→handoff→README) | Cobertura total |

### 1.7 Acessibilidade aplicada
- `docs/auditoria-a11y.md`: 10 correções aplicadas (2 P1, 5 P2, 3 P3).
- Skip link funcional, landmarks (header/nav/main/footer), aria-labelledby em seções, role em componentes interativos, prefers-reduced-motion, focus-visible consistente, contraste AA nos tokens.

### 1.8 Portabilidade multi-agente
- `AGENTS.md` (raiz): onboarding universal.
- `CLAUDE.md` + `.claude/skills/` (8 wrappers): Claude Code.
- `.codex/README.md`: notas para Codex.
- `skills/`: 8 skills portáteis com SKILL.md + frontmatter.

---

## 2. Ressalvas e melhorias necessárias (lista priorizada)

### 🔴 Blocker (0)

Nenhum. O kit está funcional, os detectores passam, e todos os componentes renderizam. Não há impedimento técnico para uso.

### 🟠 Major (4)

| # | O quê | Onde | Impacto | Esforço |
|---|---|---|---|---|
| M1 | **Validação real nos agentes-alvo pendente** | Fase E p2 (AGENTS.md) | Alto: a promessa central ("funciona em Claude, Codex, pi") não foi testada em Claude Code nem Codex com as skills wrappers. Os wrappers em `.claude/skills/` delegam às skills externas (`impeccable`, `web-design-engineer`) que podem não existir nesses ambientes. | M — precisa de sessões reais em cada agente |
| M2 | **Documentação interna só em pt-BR** | `docs/arquitetura-agente-design.md`, `docs/guia-de-uso.md`, `docs/componentes/*.md`, `docs/casos/*/README.md` | Médio: limita adoção internacional. O README.md é bilíngue, mas a doc técnica (arquitetura, handoff de componentes, guia de uso) é só pt-BR. | L — tradução de ~15 docs |
| M3 | **Falta cobertura de componentes comuns** | Ausentes: data table interativa (sort/filter), date picker, file upload, combobox/autocomplete, charts/data-viz | Médio: gaps que um setor de design real cobriria. Data table com sort é especialmente esperado em dashboards (caso Norte já usa tabela estática). | L — cada componente requer HTML + CSS + JS + a11y |
| M4 | **Skills wrappers dependem de skills externas** | `skills/ui-designer/SKILL.md`, `skills/design-critic/SKILL.md`, `skills/a11y-auditor/SKILL.md` | Médio: os wrappers delegam a `impeccable` e `web-design-engineer`. O fallback embutido é razoável (design-critic tem scoring próprio), mas ui-designer e a11y-auditor são mais finos — o fallback do a11y-auditor, em particular, precisa ser robusto o suficiente para rodar sem o `impeccable audit`. | M — enriquecer fallbacks |

### 🟡 Minor (6)

| # | O quê | Onde | Impacto | Esforço |
|---|---|---|---|---|
| m1 | **components.css está grande (2000 linhas)** | `styles/components.css` | Baixo: manutenção começa a doer. Separar em `components/buttons.css`, `components/forms.css`, etc. (com @import ou concatenação) facilitaria contribuições. | S — split mecânico |
| m2 | **Sem CI/CD ou pre-commit hooks** | Raiz (ausência de `.github/workflows/`) | Baixo: smoke-test e anti-slop-check só rodam manualmente. Um GitHub Action que rode ambos em push/PR aumentaria a confiança. | S — 1 workflow YAML |
| m3 | **Showcase é single-page com 14 seções** | `index.html` (~1200 linhas) | Baixo: difícil navegar como referência rápida. Páginas isoladas por componente (ou um Storybook-like mínimo) seriam melhores para handoff. | M — requer refatoração do HTML |
| m4 | **Print stylesheet ausente** | Nenhum `@media print` nos CSS | Baixo: componentes como tabelas, alerts e forms perdem contexto na impressão. | S — um arquivo `print.css` com regras básicas |
| m5 | **Faltam testes visuais automatizados** | Nenhum (só checks textuais) | Baixo: regressão visual (ex.: Percy, BackstopJS, ou até screenshots com Puppeteer) pegaria quebras de layout que grep não detecta. | L — infra de screenshot diff |
| m6 | **Sem `prefers-reduced-transparency`** | `styles/base.css`, `styles/layout.css` | Baixo: o header usa `backdrop-filter: blur(12px)`. O DESIGN.md §4.5 exige fallback sólido sob `prefers-reduced-transparency`, mas não encontrei a media query no código. | S — adicionar media query |

### ⬜ Decisões pendentes do fundador (fora do escopo técnico)

| Decisão | Impacto | Status (AGENTS.md) |
|---|---|---|
| Agentes-alvo prioritários | Define onde validar (Fase E p2) | Bloqueada |
| Escopo de pesquisa (síntese vs coleta) | Define limite honesto do researcher | Bloqueada |
| Geração de imagens (DALL-E/Midjourney/etc.) | Afeta ui-designer e casos | Bloqueada |
| Open-source vs comercial | Define licença, nome, distribuição | Bloqueada |
| Nome do produto | Bloqueia v1.0.0 e npm package | Bloqueada |

---

## 3. Scoring interno (heurísticas do kit aplicadas ao kit)

| Heurística | Nota (1–5) | Comentário |
|---|---|---|
| Clareza | 5 | AGENTS.md + DESIGN.md + README.md comunicam o que é, como usar e por quê em minutos. |
| Hierarquia | 4 | Showcase bem organizado (14 seções com sidebar + scrollspy), mas single-page limita navegação de referência. |
| Consistência (tokens) | 5 | Zero hex em componentes, 109 var() mapeados, 0 órfãos. Perfeito. |
| Affordance | 4 | Componentes interativos têm estados completos (:hover, :active, :focus-visible, :disabled, loading). Faltam alguns (date picker, combobox). |
| Acessibilidade | 4 | Skip link, landmarks, aria, foco visível, reduced-motion, contraste AA. Falta print e reduced-transparency. |
| Responsividade | 5 | Mobile-first, off-canvas, breakpoints em tokens, testado nos casos. |
| Anti-slop | 5 | 98 checks passam, DESIGN.md cobre 15 categorias de tells, pre-flight com 20 itens. |
| Portabilidade | 3 | Estrutura existe (AGENTS.md, CLAUDE.md, .claude/skills, .codex), mas validação real pendente (Fase E p2). |
| **Geral** | **4.1** | Sólido para uso interno; falta maturidade de produto para v1.0.0. |

---

## 4. O que Atelier/Forja devem melhorar (priorizado)

Se outros agentes (Atelier = ui-designer + design-refine; Forja = engineering/integração) forem acionados para evoluir o kit, esta é a ordem:

1. **Traduzir documentação interna para EN** (M2) — desbloqueia adoção global. Começar por `docs/arquitetura-agente-design.md` e `docs/componentes/README.md`.
2. **Enriquecer fallback do a11y-auditor** (M4) — garantir que o wrapper funcione sem `impeccable audit`, com checklist WCAG 2.2 AA embutido.
3. **Adicionar data table interativa** (M3) — sort + filter + paginação JS. É o componente mais esperado para dashboards e o caso Norte já pede.
4. **Adicionar `prefers-reduced-transparency`** (m6) — o DESIGN.md §4.5 exige, mas o código não tem. Corrigir em `base.css` e `layout.css`.
5. **Criar GitHub Action de QA** (m2) — rodar `smoke-test.py` + `anti-slop-check.py` em push/PR.
6. **Adicionar print stylesheet** (m4) — `@media print` com ocultação de nav/sidebar e ajuste de cores.
7. **Dividir components.css** (m1) — separar por seção (buttons, forms, overlays, advanced) com `@import` ou concatenação.
8. **Validar em Claude Code e Codex** (M1) — depende de decisão do fundador, mas é o gate para v1.0.0.

---

## 5. Verificação das regras de ouro do DESIGN.md no próprio kit

- [x] Zero `—`/`–` em texto visível → PASS (anti-slop-check confirma)
- [x] Zero hex hardcoded em componentes → PASS (smoke-test confirma)
- [x] Zero Inter → PASS (system-ui stack)
- [x] Eyebrows ≤ ceil(seções/3) → PASS (2 em 14 seções, limite 5)
- [x] Nomes reais, não genéricos → PASS (anti-slop-check confirma)
- [x] Sem fake screenshots → PASS (showcase usa componentes reais ou placeholders marcados)
- [x] Sem scroll cues → PASS
- [x] Theme lock → PASS (1 tema por vez, toggle explícito)
- [x] Color lock → PASS (índigo como accent único)
- [x] Shape lock → PASS (pills em botões, md em cards, sm em inputs — documentado e seguido)
- [x] Motion motivado → PASS (só transform/opacity, reduced-motion coberto, IntersectionObserver sem scroll listener)
- [x] Estados completos → PASS (loading, empty, error, disabled, focus-visible em todos os componentes interativos)
- [x] `min-h-100dvh` → PASS (base.css)

---

*Relatório gerado pelo Evaluator do Design Kit. Próximo passo: entregar ao Orquestrador para priorização do backlog.*