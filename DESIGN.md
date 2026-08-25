# DESIGN.md — Design Kit

> Contexto de design durável do Design Kit. Todo agente (pi, Claude Code, Codex) que gerar UI com este kit DEVE ler este arquivo antes de desenhar. É a voz do kit: o que fazemos, o que nunca fazemos, e como lemos a sala antes de qualquer pixel.
> Fontes do método: skill `impeccable` (v4.1.1) e skill `design-taste` (taste-skill, leonxlnx) + 2 casos reais validados (Lumen 4.7/5, Norte 4.6/5).

---

## 1. Filosofia

**O Design Kit existe para gerar design que não parece feito por IA.** O padrão da IA é seguro, genérico e medido demais: gradiente roxo, hero centralizado, três cards iguais, Inter + slate-900. Nós alcançamos além disso, deliberadamente, com base na leitura do brief. O usuário (humano) é o diretor; o agente é o setor de design. Carinho de especialista significa: cada decisão tem uma razão que cabe em uma frase, e nada é shipado sem passar pelo pre-flight.

Três modos de superfície (impeccable): **Persuade** (landing, o design é o produto), **Operate** (apps, dashboards, densidade e consistência), **Read** (docs, estrutura para compreensão). O modo vem da superfície, não do produto. (Referência do 4º modo, **Experience** — portfólios, galerias, vitrines: o artefato lidera desde o primeiro viewport e a interface recua — o kit trata Experience como uma disciplina de curadoria sobre Persuade: menos chrome, mais obra, navegação mínima e discreta.)

---

## 2. Como ler o brief (antes de qualquer código)

1. **Sinais**: tipo de página (landing/portfolio/redesign/editorial), vibe words do usuário ("calmo", "Linear-style", "premium", "brutalist"), referências (URLs, produtos, concorrentes), audiência (B2B técnico vs consumidor de design), brand assets existentes, constraints silenciosas (acessibilidade, setor público, regulação) — constraints silenciosas SEMPRE vencem preferência estética.
2. **Design Read**: declare em UMA linha antes de desenhar, ex.: *"Lendo como: landing B2B para compradores técnicos, linguagem minimalista tipo Linear, tendendo a tokens do kit + motion contido."*
3. **Ambiguidade**: se o Design Read divergir genuinamente, faça UMA pergunta. Se der para inferir com confiança, não pergunte.
4. **Dials**: ajuste os três dials a partir do brief (não use o baseline em silêncio):

| Dial | 1 | 10 |
|---|---|---|
| DESIGN_VARIANCE | simetria perfeita | caos de galeria |
| MOTION_INTENSITY | estático | cinematográfico/física |
| VISUAL_DENSITY | galeria de arte | cockpit de dados |

Baseline 8/6/4. Presets: landing mainstream 7/6/4 · agência criativa 9/8/3 · premium consumer 7/6/3 · portfolio dev 6/5/4 · editorial 6/4/3 · serviço público 3/2/5 · redesign preservar = igual+1 no motion · redesign overhaul +2/+2/igual.

---

## 3. Identidade visual do kit (a fonte de verdade)

- **Tokens**: `styles/tokens.css` é a ÚNICA fonte de verdade. Nenhum hex, nenhum rem, nenhum valor mágico fora dele. Regra auditável: `grep` de `#[0-9a-fA-F]` em qualquer UI do kit = zero.
- **Primária**: índigo (ação/foco). **Neutra**: slate (frio, elegante). **Semânticas**: sucesso/alerta/erro/info. Claro + escuro via `[data-theme]` + `prefers-color-scheme` (o kit já resolve; nunca duplicar regras de tema).
- **Locks (obrigatórios)**:
  - **1 accent por página.** Escolhido uma vez, usado na página inteira. Nada de teal no footer se o accent é índigo.
  - **Shape lock.** Uma escala de raio por página (o kit: pills em botões, md em cards, sm em inputs — regra documentada, seguida em todo lugar).
  - **Theme lock.** Uma página = um tema (claro OU escuro). Seções não invertem no meio.
- **Tipografia**: system-ui (zero download). Sem Inter como default. Display com `tracking` apertado, body com `leading-relaxed` e `max-width: 65ch`. Italic em display com `y g j p q` → `leading` ≥ 1.1 + reserva de `pb`.
- **Sem serifa por default.** Só com justificativa explícita do brief (editorial/luxo/publicação), e nunca Fraunces/Instrument_Serif.

---

## 4. Regras de ouro (o que nunca fazer)

### 4.1 Os tells da IA (bans)
- **Em-dash (`—`) e en-dash (`–`): ZERO.** Em headline, eyebrow, body, quote, botão, alt. Ponto, vírgula, dois-pontos ou hífen normal. Se aparecer um `—` no output, falhou o pre-flight. (É o tell nº 1 em testes de produção.)
- **Sem gradiente roxo de IA**, sem glow neon, sem botão roxo com brilho. Accent único e saturado < 80%.
- **Sem 3 cards iguais em linha.** Layouts: 2 colunas zigzag, grid assimétrico, scroll-pinned, horizontal.
- **Sem fake screenshots de div** (UI falsa de tarefas/terminal/dashboard feita de retângulos). Usar componente real do kit, imagem real, ou nada.
- **Sem Inter como default** e sem a pilha bege+latão+oxblood do "premium consumer" (essa paleta é o tell nº 2; alternativas: luxury frio, forest, preto e tan, cobalto+creme, terracotta+slate, oliva+tijolo, monocromático+pop).
- **Sem nomes genéricos** (Jane Doe, Acme, Nexus, SmartFlow). Nomes reais, contextuais, locais.
- **Sem números falsos-preciosos** (99.99%, 4.1×). Dados reais, ou marcados `<!-- mock -->`.
- **Sem scroll cues** ("Scroll", "↓"), sem version footers em marketing (v0.6, Build 0048), sem eyebrow numerados (00/INDEX, 001·Capabilities), sem strips decorativos no rodapé do hero (BRAND. MOTION. SPATIAL.), sem dots de status decorativos, sem labels/pills sobre imagens, sem créditos de foto falsos.
- **Sem eyebrow em toda seção.** Máx 1 eyebrow por 3 seções (conta: hero = 1). Acima de ceil(seções/3) = falha.
- **Sem split-header** (headline grande à esquerda + parágrafo solto à direita como header de seção). Empilhar verticalmente.
- **Sem zigzag repetido**: máx 2 seções seguidas com o mesmo padrão imagem+texto.
- **Sem `window.addEventListener('scroll')`** para animação. IntersectionObserver, scroll-driven CSS ou Motion.
- **Sem h-screen**: sempre `min-h-100dvh`.

### 4.2 Hero (disciplina dura)
- Hero cabe no viewport inicial: headline ≤ 2 linhas, subtext ≤ 20 palavras e ≤ 4 linhas, CTA visível sem scroll.
- Máx 4 elementos de texto no hero: (eyebrow OU brand strip), headline, subtext, CTAs. Nada de tagline minúscula abaixo dos CTAs, nada de "Usado por times em..." dentro do hero.
- Top padding máx 6rem. Se precisa de mais ar, aumenta a fonte ou o asset, não o padding.
- Logo wall ("Usado por") vai DEBAIXO do hero, com logos SVG reais (Simple Icons / monograma) — nunca wordmark de texto puro, nunca labels de categoria abaixo dos logos.
- Nav em UMA linha no desktop, altura ≤ 80px (default 64-72px).

### 4.3 Componentes e estados
- Cards só quando elevação comunica hierarquia real; senão `divide-y`, `border-t` ou espaço negativo.
- Sempre estados completos: loading (skeleton no formato final, sem spinner genérico), empty (composto, indica como popular), erro (inline em forms, contextual/toast só para transitório). Feedback tátil em `:active` (translate ou scale).
- Botão: texto legível no fundo (WCAG AA 4.5:1 / 3:1 em grande), label não quebra em desktop (máx 3 palavras em CTA primário), UMA intenção por CTA ("Fale conosco" uma vez, não "Contato"+“Vamos conversar"+“Comece um projeto").
- Forms: label ACIMA do input, helper opcional no markup, erro ABAIXO do input. Nunca placeholder-como-label. Placeholder, focus ring, helper e erro todos AA contra o fundo da seção.
- Bento: exatamente N células para N conteúdos, sem célula vazia, e 2-3 células com variação visual real (imagem/gradiente de marca/padrão), não só texto.
- Longas listas (> 5 itens) usam outro componente (cards, tabs, pills horizontais, carousel), nunca `<ul>` com hairline em toda linha.

### 4.4 Motion (motivado ou ausente)
- Toda animação responde: hierarquia, storytelling, feedback ou transição de estado. "Ficou legal" não é motivo.
- Animar SÓ `transform` e `opacity`. Zero transição de `width/height/top/left`.
- `MOTION_INTENSITY > 4` exige motion real na página (se não dá para shipar, baixa o dial para 3 e entrega estático limpo).
- `prefers-reduced-motion` obrigatório para qualquer motion > 3: colapsa para estático/instantâneo (inclui paralaxe, scroll-hijack, física magnética).
- Springs com física (stiffness ~100, damping ~20), não linear easing.
- Marquee: máx 1 por página (só onde serve o conteúdo).
- "Motion claimed = motion shown": dial alto sem animação real na página é falha de pre-flight.

### 4.5 Micro-gaps (o cuidado fino que separa bom de ótimo)
- **Browser surfaces**: seleção de texto com cor coerente (`::selection`), caret visível em inputs, scrollbar discreta, underline de links com offset e espessura controlados.
- **`prefers-reduced-transparency`**: se a página usa vidro/backdrop-blur, fornecer fallback sólido também sob esta media query (não só reduced-motion).
- **Diversidade de layout**: uma página com 8 seções usa ≥ 4 famílias de layout diferentes (nunca 3-cards-iguais em tudo).
- **i18n**: texto em pt-BR ou no idioma do brief, nunca misturar; algarismos e unidades consistentes.
- **Ícones**: uma família por página, stroke consistente, sem emoji como ícone em UI de produto (emoji só em tom social/playful pedido pelo brief).

---

## 5. Como o kit gera insumos (não só UI)

- **Critique** (design-critic): scoring por heurística (clareza, hierarquia, consistência com tokens, affordance, a11y, responsividade, copy) + lista priorizada blocker/major/minor + verificação obrigatória da regra de tokens + **verificação de AI tells** (em-dash, fake screenshots, 3 cards iguais, eyebrow excessivos, Inter, nomes genéricos). Critério de parada: sem blockers, média ≥ 4, nenhuma heurística < 3. Máx 2 rodadas de refine antes de escalar ao humano.
- **Handoff** (design-handoff): spec por componente (classes exatas, tokens, estados, a11y, pegadinhas) — o que um dev ou outro agente precisa para implementar fiel.
- **Extract**: padrão novo ausente do kit → propor token/componente novo (via impeccable extract), nunca inventar valor no lugar.
- **Loops fechados**: critique e a11y rodam até não haver blockers; o humano aprova em 2 checkpoints (research→UI, UI→handoff).

## 5.1 Redesign (o kit como setor de design recebendo redesigns)

**Detectar o modo primeiro** (primeira ação, antes de tocar em qualquer coisa):
- **Greenfield**: não há site, ou overhaul aprovado. Baseline de dials normal.
- **Redesign - Preservar**: modernizar sem quebrar a marca. Auditar primeiro, extrair tokens da marca, evoluir gradualmente.
- **Redesign - Overhaul**: nova linguagem visual sobre conteúdo existente. Tratar como greenfield no visual; PRESERVAR conteúdo e IA.

**Auditar antes de tocar** (documentar antes de propor): tokens de marca (cor/tipo/logo/raios), IA (árvore de páginas, nav principal, caminhos de conversão), blocos de conteúdo (o que funciona, o que é filler), padrões a preservar (hero reconhecível, voz de copy, interações assinatura), padrões a aposentar (tells de IA, layouts quebrados, perf traps), leitura de dials do site atual (é o ponto de partida, não o baseline), SEO baseline (páginas ranqueadas, metas, OG — **migração de SEO é o risco nº 1 de redesign**).

**Preservar (nunca mudar sem aprovação):** URLs/slugs, labels da nav principal, nomes/ordem de campos de formulário (quebra analytics + autofill), logo/wordmark, copy legal/consentimento/cookies.

**Alavancas de modernização (em ordem, pare quando o brief estiver satisfeito):** 1) tipografia (maior ganho visual por unidade de risco); 2) espaçamento e ritmo; 3) recalibração de cor (dessaturar, unificar neutros, manter accent); 4) camada de motion nos componentes existentes; 5) recomposição de hero e seções-chave; 6) substituição de bloco (só quando o bloco é insalvável).

**Árvore de decisão:** IA/conteúdo/SEO sãos → evolução direcionada (alavancas 1-4, ~70% do valor a ~40% do risco); dívida visual estrutural (IA quebrada, sem design system, mobile quebrado) → redesign completo com preservação estrita de conteúdo; a marca em si está mudando → greenfield.

## 5.2 Mapa de design systems externos (quando NÃO usar o kit)

O setor de design escolhe a ferramenta certa, não empurra o kit em tudo. Se o brief lê como:
- **Setor público UK / trust-first**: usar `govuk-frontend` / `uswds` (legalmente esperado).
- **Enterprise SaaS / Microsoft-flavored**: `@fluentui/*` (tokens + a11y prontos).
- **IBM-style analytics**: `@carbon/*`.
- **Shopify apps**: `polaris` (obrigatório).
- **Atlassian/Jira-style**: `@atlaskit/*`.
- **Google-ish / Material**: `@material/web`.
- **GitHub-style devtool**: `@primer/css`.

**Honesty rule**: se o brief lê como um dos acima, use o pacote oficial — não recrie o CSS na mão, não importe os tokens para sobrescrever 90%. **Um sistema por projeto.** Quando NÃO há sistema oficial (estética pura: bento, brutalismo, editorial, dark tech), o kit manda: CSS nativo + tokens do kit + componentes reais, com comentário honesto sobre inspiração vs material oficial.

## 5.3 Detecção determinística (o diferencial do kit)

O kit tem o que nenhuma skill externa tem: **checks mecânicos executáveis**. Rode `scripts/smoke-test.py` (8 checks de integridade) e, quando aplicável, a varredura anti-slop (em-dash, hex, Inter, eyebrows) antes de shipar. O critique do kit cruza regra de tokens + tells + heurísticas na mesma sessão — as externas tratam isso como dimensões separadas. Este é o motivo pelo qual o kit é substituto viável das duas skills: o método vira código auditável.

---

## 6. Pre-flight (antes de shipar — todo item obrigatório)

- [ ] Design Read declarado e dials explícitos com razão do brief
- [ ] **Zero `—` e zero `–`** em todo texto visível
- [ ] Theme lock: um tema por página
- [ ] Color lock: um accent em tudo; Shape lock: um sistema de raio
- [ ] Contraste AA nos botões, forms (placeholder/focus/helper/erro) e body; hero em AAA
- [ ] CTA: label não quebra, uma intenção por CTA
- [ ] Hero: ≤ 2 linhas headline, ≤ 20 palavras subtext, CTA visível, ≤ 4 elementos, padding ≤ 6rem
- [ ] Eyebrows: contagem ≤ ceil(seções/3)
- [ ] Sem fake screenshots de div; imagens reais (geradas → picsum seed → slots marcados); logos reais no logo wall
- [ ] Sem scroll cues, version footers, strips decorativos, dots decorativos, eyebrows numerados
- [ ] Motion motivado, só transform/opacity, reduced-motion coberto, sem `window scroll` listener
- [ ] Nav em 1 linha ≤ 80px; zigzag ≤ 2 seguidas; bento com N células e variação visual
- [ ] Mobile collapse explícito por seção; `min-h-100dvh`
- [ ] Estados: loading/empty/error presentes
- [ ] Copy auditada: zero frases quebradas, zero "elevate/seamless/unleash", números honestos
- [ ] Dark mode definido e testado nos dois modos
- [ ] CWV plausíveis: LCP < 2.5s (hero pré-carregado ou priority), INP < 200ms, CLS < 0.1 (espaço reservado para imagens); rodar Lighthouse se houver hosting
- [ ] Micro-gaps: selection/caret/scrollbar, reduced-transparency se houver vidro, i18n coeso, 1 família de ícones
- [ ] Detector: `python scripts/smoke-test.py` PASS + varredura anti-slop (zero `—`/`–` em texto visível, zero hex fora de tokens)

Se um item não pode ser marcado com honestidade, a entrega não está pronta.

---

## 7. Referências

- Skills do kit: `skills/design-researcher`, `skills/information-architect`, `skills/ui-designer`, `skills/design-critic`, `skills/a11y-auditor`, `skills/design-handoff`
- Skills externas: `impeccable` (critique/audit/polish/extract — `~/.pi/agent/skills/impeccable/`), `design-taste` (anti-slop, dials, tells — `~/.pi/agent/skills/design-taste/`)
- Casos reais: `docs/casos/lumen/` (landing, 4.7/5), `docs/casos/norte/` (dashboard, 4.6/5), `docs/casos/brisa/` (fluxo research→handoff)
- Tokens: `styles/tokens.css` · Componentes: `styles/components.css` · Docs de handoff: `docs/componentes/`
