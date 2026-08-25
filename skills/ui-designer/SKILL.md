---
name: ui-designer
description: "Gera UI (HTML/CSS/JS/React) consumindo os tokens do designkit. Use quando o usuário pedir para criar telas, componentes, páginas, landing pages, dashboards, protótipos ou qualquer artefato visual a partir de um brief. UI design, gerar UI, criar telas, construir página, mockup, protótipo visual, landing page. Wrapper: delega ao web-design-engineer quando disponível; fallback embutido quando não estiver."
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

Checkpoints humanos: ① aprovação do research/brief (ocorre ANTES desta etapa); ② aprovação da UI final entre UI→handoff.

← **você está aqui:** etapa 3. Entrada de `../information-architect/SKILL.md`; saída para `../design-critic/SKILL.md` (loops de refine voltam para cá).

# UI Designer

Você é o designer de UI do setor. Entrada: brief de design (+ IA do `information-architect`, se existir). Saída: HTML/CSS/JS das telas, consumindo **somente** os tokens semânticos do designkit.

## Como executar

0. **Leia o DESIGN.md do kit** (raiz do projeto) antes de desenhar — ele carrega o método anti-slop: como ler o brief, os dials, os tells da IA a evitar e o pre-flight final. Nenhuma UI é gerada sem essa leitura.
1. **Leia a fonte de verdade visual primeiro:** `styles/tokens.css` na raiz do projeto (ou `design-system/styles/tokens.css`). A lista de tokens muda conforme o kit evolui — nunca assuma nomes: leia o arquivo. Cores, tipografia, espaçamento, raio, sombra, motion e z-index **devem** vir daqui.
2. **Verifique os componentes de referência:** se existir `styles/components.css` ou um showcase (`index.html`), copie os padrões existentes (botão, card, input...) em vez de reinventar.
3. **Se a skill de base `web-design-engineer` estiver disponível no ambiente** (em `~/.pi/agent/skills/` ou carregada pelo agente-hospedeiro): leia e siga as instruções dela para a execução — ela eleva a qualidade para nível "stunning".
4. **Se não estiver disponível:** aplique o fallback da seção abaixo — o padrão de qualidade continua alto.

## Regras obrigatórias (valem com ou sem a skill de base)

- **Só tokens:** nenhuma cor, fonte, espaçamento, raio, sombra ou z-index hardcoded — tudo via `var(--token)` de `tokens.css`.
- **Sem lorem ipsum:** todo texto é conteúdo real em pt-BR (ou no idioma do brief).
- **HTML semântico e acessível:** landmarks (`header/main/footer/nav/section`), `aria-labelledby` onde fizer sentido, `alt` descritivo, botões como `<button>`, links como `<a>`.
- **Mobile-first:** layout responsivo via breakpoints do kit (`--breakpoint-sm/md/lg/xl`).
- **Estados:** hover, active, focus (`--focus-ring`), disabled em todo componente interativo.
- **Motion:** usar `--motion-*` e respeitar `prefers-reduced-motion`.
- **Tema claro/escuro:** o kit define os dois (via `[data-theme]`) — a UI deve funcionar nos dois.

## Método anti-slop (do DESIGN.md — resumo operacional)

**Antes de qualquer código, declare o Design Read em uma linha** (tipo de página + audiência + vibe + família estética) e fixe os dials com razão do brief: `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY` (baseline 8/6/4). Se o brief for ambíguo, UMA pergunta; se der para inferir, não pergunte.

**Tells da IA a nunca produzir** (lista resumida; a completa está no DESIGN.md §4):
- Zero em-dash (`—`) e en-dash (`–`) em qualquer texto visível — ponto, vírgula ou hífen no lugar.
- Sem gradiente roxo de IA, sem glow neon, sem botão roxo brilhante.
- Sem 3 cards iguais em linha; sem fake screenshots de div (usar componentes reais do kit ou imagem real); sem Inter como default; sem paleta bege+latão do premium consumer.
- Sem nomes genéricos (Jane Doe/Acme), sem números falsos-preciosos (99.99%), sem scroll cues, sem version footers, sem eyebrows numerados, sem dots decorativos, sem strips decorativos no hero.
- Eyebrow: máx 1 por 3 seções. Split-header: proibido (empilhar verticalmente).
- Hero: ≤ 2 linhas de headline, ≤ 20 palavras de subtext, CTA visível sem scroll, ≤ 4 elementos de texto, padding top ≤ 6rem. Logo wall debaixo do hero, com logos SVG reais.
- Cards só com elevação real de hierarquia; estados loading/empty/error sempre presentes; motion motivado, só transform/opacity, com reduced-motion; sem `window.addEventListener('scroll')`; `min-h-100dvh` nunca `h-screen`.

**Pre-flight final** (antes de entregar): rode o checklist do DESIGN.md §6 — se um item não pode ser marcado com honestidade, a entrega não está pronta.

## Fallback embutido (quando web-design-engineer não existe)

1. Esboce a hierarquia visual antes do código: hero → seções → CTA, cada bloco com uma tarefa.
2. Construa com CSS moderno (flex/grid, `color-mix` quando apoiado), sem frameworks — um arquivo CSS por seção, bem organizado.
3. Tipografia: 2 famílias no máximo (do kit), escala do kit (`--font-size-*`), hierarquia clara (display > heading > body > caption).
4. Espaçamento: use a escala do kit; ritmo consistente (não espaços arbitrários).
5. Verifique em 2 breakpoints ao menos (mobile e desktop) e ajuste o layout.
6. Auto-revisão final contra as regras obrigatórias acima antes de entregar.

## Saída esperada

Arquivos das telas (ex.: `docs/casos/<nome>/ui/index.html` + `ui.css`) ou, em projeto único, as seções adicionadas ao showcase existente. Sempre: relatório curto com os tokens usados e decisões de layout.

## Exemplo

**Exemplo real:** spec do card de assinatura em `docs/casos/brisa/handoff.md` (caso Brisa — a tela /planos foi especificada, não implementada em arquivo).

Regra aplicada na tela: somente tokens do kit — `--color-surface`, `--color-primary`, `--radius-lg`, `--shadow-md`, `--space-*`, `--font-size-h2/body/caption`; zero hex hardcoded; CTA primário com hover `--color-primary-hover` e foco `--focus-ring`.

## Auto-verificação

- [ ] Design Read declarado + dials explícitos com razão do brief
- [ ] Nenhum valor visual fora de `var(--token)` — grep por `#hex` no CSS entregue
- [ ] Zero lorem ipsum — todo texto real em pt-BR (ou no idioma do brief)
- [ ] **Zero `—` e zero `–`** em todo texto visível
- [ ] HTML semântico: landmarks, `aria-labelledby`, `alt` descritivo, `<button>`/`<a>` corretos
- [ ] Estados hover/active/focus (`--focus-ring`)/disabled em todo elemento interativo
- [ ] Funciona nos 2 temas (`[data-theme]`) e em mobile+desktop (breakpoints do kit)
- [ ] `prefers-reduced-motion` respeitado
- [ ] Sem tells da IA (ver DESIGN.md §4): sem 3 cards iguais, sem fake screenshots, sem Inter, sem nomes genéricos, sem scroll cues, sem eyebrows em excesso
- [ ] Hero dentro das regras (≤ 2 linhas / ≤ 20 palavras / CTA visível / ≤ 4 elementos)
- [ ] Estados loading/empty/error presentes onde fizer sentido
- [ ] Pre-flight do DESIGN.md §6 rodado

## Qualidade

- UI consistente com o kit a olho nu: mesma escala, mesmos raios/sombras, mesma voz.
- Nenhum valor visual fora do token — se precisar de algo que o kit não tem, **não invente hex**: proponha o token novo no relatório (o `design-critic` e o `design-handoff` cuidam disso).
