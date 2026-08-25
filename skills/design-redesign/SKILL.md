---
name: design-redesign
description: "Redesenha UI/site existente: moderniza preservando a marca, audita antes de tocar, distingue preserve vs overhaul. Use quando o usuário pedir redesign, modernizar, atualizar o visual do site, deixar a landing menos datada, repaginar, renovar identidade visual de um produto existente. Redesign, modernização, refresh visual, preserve, overhaul, audit antes de tocar, evolução direcionada. Wrapper: quando a skill impeccable estiver disponível, use o playbook de new-work/redesign dela como base de execução e aplique o protocolo do kit (auditoria de marca + tokens do kit + pre-flight) por cima."
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → **`../design-redesign/SKILL.md` (opcional)** → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

**Posicionamento desta skill no fluxo:**
- **Quando há UI existente e o pedido é modernizar/redesign:** esta skill entra ENTRE o `information-architect` (que pode revalidar a IA) e o `design-critic`. Ela SUBSTITUI o `../ui-designer/SKILL.md` nesse trecho do fluxo (redesign não é greenfield; o ui-designer assume quando não há UI anterior ou quando o overhaul foi aprovado e a nova linguagem já está definida).
- **Quando não há UI existente (greenfield):** ignore esta skill e use o `../ui-designer/SKILL.md` normalmente.
- Saída para `../design-critic/SKILL.md` (o critique valida o resultado do redesign contra o brief e os tokens; loops de refine voltam para cá).

Checkpoints humanos: ① aprovação do research/brief; ② aprovação do redesign ANTES do handoff. Em redesign, o checkpoint ② é obrigatório e acontece após o critique.

← **você está aqui:** etapa opcional 3.5, substituindo o ui-designer quando existe UI a modernizar. Entrada: brief de design (+ IA do `information-architect`). Saída: UI redesenhada + relatório de auditoria e decisões de preserve/levers.

# Design Redesign

Você é o redesigner do setor de design. Entrada: UI existente + brief. Saída: a mesma superfície modernizada — preservando o que a marca tem de valioso, aposentando o que a faz parecer datada ou feita por IA, e evoluindo por alavancas em ordem de risco. **O erro nº 1 de redesign é mudar o que não devia ser mudado. O erro nº 2 é fazer polish sobre uma linguagem que deveria ser substituída.** Este protocolo existe para você não errar nem para um lado nem para o outro.

## Como executar

0. **Leia o DESIGN.md do kit** (raiz) — a voz do produto: tells da IA (§4), dials (§2), pre-flight (§6). Ele governa todo redesign do kit.
1. **Detecte o modo PRIMEIRO** (antes de tocar em qualquer arquivo) — seção "Detectar o modo" abaixo.
2. **Audite antes de tocar** — seção "Auditoria" abaixo. Documente o estado atual antes de propor qualquer mudança.
3. **Extraia os tokens da marca** da UI existente (cor, tipo, raio, sombra, logo) — seção "Extração de tokens da marca" abaixo.
4. **Aplique as alavancas em ordem** (1 → 6), parando quando o brief estiver satisfeito — seção "Alavancas de modernização" abaixo.
5. **Rode o pre-flight do DESIGN.md §6** antes de entregar e reporte as decisões de preserve + levers aplicadas.

## Detectar o modo (primeira ação)

Classifique o pedido em UM destes três modos antes de qualquer edição:

| Modo | Quando | Tratamento visual | Conteúdo/IA |
|---|---|---|---|
| **Greenfield** | Não há site, ou overhaul aprovado pelo humano | Baseline de dials normal (§2 do DESIGN.md) | Novo |
| **Redesign - Preservar** | Modernizar sem quebrar a marca | Auditar → extrair tokens → evoluir gradualmente | PRESERVAR |
| **Redesign - Overhaul** | Nova linguagem visual sobre conteúdo existente | Tratar como greenfield no visual (substituir o mundo visual) | PRESERVAR conteúdo e IA |

**Se ambíguo, faça UMA pergunta, não um dump:** *"Este redesign deve preservar a identidade visual atual (cor, tipo, logo) evoluindo por partes, ou estamos começando o visual do zero sobre o mesmo conteúdo?"* Se der para inferir com confiança do brief (ex.: "deixa moderna, mas mantém as cores da marca" → Preservar; "quero outra cara, o visual atual não representa mais o produto" → Overhaul), não pergunte.

**Regra de ouro:** preserver vs overhaul nunca é decidido silenciosamente. Se o brief não deixa claro, a pergunta única acima é obrigatória. Um redesign que troca a identidade visual sem aprovação é falha grave; um preserve que só faz polish numa linguagem que deveria morrer é a falha nº 2.

## Auditoria (antes de tocar em qualquer arquivo)

Documente o estado atual em um relatório curto antes de propor mudanças. Comandos sugeridos entre parênteses.

1. **Tokens de marca** — o que é a identidade visual hoje: cor primária/accent, pilha de tipo, tratamento de logo, escala de raio, sombras. (`grep -n "color\|font-family\|border-radius" <css do site>`)
2. **IA** — árvore de páginas, nav principal, caminhos de conversão (hero → CTA, seções-chave). (`grep -n "<nav\|<header\|href=\"#" <html do site>`)
3. **Blocos de conteúdo** — o que existe, o que está fazendo trabalho, o que é filler (lorem, placeholder, texto de preenchimento).
4. **Padrões a preservar** — hero reconhecível, voz de copy, interações assinatura, acessibilidade conquistada (focus states, alt, teclado).
5. **Padrões a aposentar** — tells da IA do DESIGN.md §4 (em-dash, gradiente roxo, 3 cards iguais, Inter, nomes genéricos, fake screenshots, scroll cues, eyebrows em excesso), layouts quebrados, perf traps (scroll listener, animações de `width/height`), links mortos, imagens genéricas.
6. **Leitura de dials do site atual** — infira `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY` da UI existente. **É o seu ponto de partida, não o baseline 8/6/4.**
7. **SEO baseline** — páginas ranqueadas, meta titles, structured data, OG cards. **Migração de SEO é o risco nº 1 de redesign**: mudar slug, título ou heading de página ranqueada custa tráfego real.

## Preservações invioláveis (nunca mudar sem aprovação explícita)

- **URLs / route slugs** — quebrar links externos e bookmarks.
- **Labels da nav principal** — os usuários memorizam a navegação.
- **Nomes e ordem de campos de formulário** — quebra analytics + autofill do navegador.
- **Logo / wordmark** — identidade registrada; só com pedido explícito.
- **Copy legal / consentimento / cookies** — risco jurídico.

Se uma dessas precisar mudar, pare e peça aprovação humana ANTES (checkpoint ② do fluxo). Nunca mude em silêncio.

## Extração de tokens da marca (antes de aplicar regras de cor)

Antes de tocar na cor, extraia os tokens da marca da UI existente:

1. **Cores reais usadas** (`grep -oE "#[0-9a-fA-F]{3,8}" <css>` + `rgba`/`hsl`): identifique a primária, o accent, os neutros. **Uma marca que já é roxa continua roxa** — a regra anti-lila do DESIGN.md §4.1 só vale para escolher um accent novo em greenfield; em redesign, a cor da marca vence (override explícito documentado no DESIGN.md §5.1).
2. **Mapaie as cores para o tokens.css do kit**: cada cor de marca vira um valor para `--color-primary`, `--color-primary-hover/active/soft`, `--color-accent` (se existir accent de marca) ou um token semântico novo proposto (fluxo do `design-handoff` / impeccable extract — nunca invente hex no lugar).
3. **Tipografia da marca**: famílias, pesos, escala de display — mapeie para `--font-*` do kit ou proponha token novo.
4. **Raio e sombra da marca**: alinhe ao shape lock do kit (pills em botões, md em cards, sm em inputs) — se a marca usa outra escala consistente, documente como regra e siga em tudo.

**A cor da marca é o que sobrevive ao redesign. Os tells da IA são o que morre.** Se a marca é roxa, o redesign mantém o roxo (com intenção, paleta harmonizada, sem gradiente slop). Se a marca usa bege+latão por escolha real e articulável, mantém; se usa porque "todo site de artesanato usa", aposenta com justificativa no relatório.

## Alavancas de modernização (aplicar EM ORDEM, parar quando o brief estiver satisfeito)

| # | Alavanca | O que fazer | Risco |
|---|---|---|---|
| 1 | **Tipografia** | Maior ganho visual por unidade de risco. Reescalar display/body, apertar tracking em display, `leading-relaxed` + `max-width: 65ch` em body, remover serifa injustificada ou Inter default. Nunca Fraunces/Instrument_Serif. | Baixo |
| 2 | **Espaçamento e ritmo** | Aumentar seção em padding, corrigir ritmo vertical, unificar em `--space-*` do kit, remover valores mágicos. | Baixo |
| 3 | **Recalibração de cor** | Dessaturar, unificar neutros (uma família de cinza), manter o accent de marca, aplicar color lock (1 accent na página toda) e theme lock (1 tema por página, sem inversão no meio). | Médio |
| 4 | **Camada de motion** | Adicionar micro-interações aos componentes existentes conforme `MOTION_INTENSITY` do site atual +1 (preserve): só `transform`/`opacity`, springs com física, `prefers-reduced-motion` obrigatório, sem scroll listener. | Médio |
| 5 | **Recomposição de hero e seções-chave** | Reestruturar topo de funil: hero dentro da disciplina (§4.2: ≤ 2 linhas headline, ≤ 20 palavras subtext, CTA visível, ≤ 4 elementos), remover logo wall de dentro do hero, diversificar famílias de layout (≥ 4 em 8 seções). | Alto |
| 6 | **Substituição de bloco** | Só quando o bloco é insalvável (layout quebrado, tell estrutural). Substituir por composição nova do kit, preservando conteúdo e função. | Alto |

**Pare quando o brief estiver satisfeito.** Não aplique todas as 6 por reflexo — evolução direcionada para em 1-4 na maioria dos casos.

## Árvore de decisão

- **IA, conteúdo e SEO sãos** (problemas só visuais) → **evolução direcionada** (alavancas 1-4). ~70% do valor a ~40% do risco.
- **Dívida visual estrutural** (IA quebrada, sem design system, mobile quebrado, tells sistêmicos) → **redesign completo** com preservação estrita de conteúdo (alavancas 5-6 entram; preserver vs overhaul definido pela pergunta única).
- **A marca em si está mudando** (reposicionamento, novo público) → **greenfield** (devolva ao ui-designer com o brief revisado; não faça redesign do que vai morrer).

## Saída esperada

- **Arquivos da UI redesenhada** (ex.: `docs/casos/<nome>/ui/index.html` + `ui.css`, ou o site existente atualizado), consumindo somente tokens do kit.
- **Relatório de redesign** (obrigatório, mesmo formato de relatório do fluxo): modo detectado + resumo da auditoria (7 itens) + decisões de preserve (listadas) + levers aplicadas (quais, em qual ordem, por quê) + tokens da marca extraídos e mapeados + pré-flight rodado.
- O `design-critic` valida depois; loops de refine voltam para cá.

## Exemplo

**Exemplo real (hipotético):** modernizar a landing do Lumen (`docs/casos/lumen/`) em modo **Redesign - Preservar** (brief: "deixa moderna, mas mantém a identidade").

- **Auditoria (resumo):** tokens de marca = índigo (`--color-primary`) + slate neutro + raio full em pills; IA sã (hero → recursos → como funciona → depoimentos → CTA); padrões a preservar = mockup de produto em SVG, voz calma da copy, toggle de tema; padrões a aposentar = 2 eyebrows excedentes, 1 bloco com layout repetido; dials atuais = 8/5/4.
- **3 decisões de preserve:** ① mantém o índigo como accent (cor de marca, override documentado da regra anti-lila); ② mantém o mockup SVG do produto (é a interação assinatura e o único "ponto de produto" da página); ③ mantém a voz da copy (nada de reescrever tom calmo → marketing agressivo).
- **2 levers aplicadas:** ① Tipografia — reescala o display com tracking mais apertado e remove a serifa decorativa injustificada do eyebrow; ② Espaçamento — unifica o ritmo vertical dos 3 blocos internos em `--space-*` e remove 2 valores mágicos (`2.5rem` → `var(--space-10)`).
- **Não mudou (invioláveis):** URLs das âncoras (#recursos, #como-funciona), labels da nav, labels/form do mockup.
- **Resultado:** critique do redesign (o `design-critic` roda em seguida) contra brief + tokens; pre-flight §6 do DESIGN.md.

## Auto-verificação

- [ ] **Modo detectado e declarado** (greenfield / preserve / overhaul) antes de qualquer edição; pergunta única feita quando ambíguo
- [ ] **Auditoria documentada** (7 itens: tokens de marca, IA, conteúdo, padrões a preservar/aposentar, dials atuais, SEO baseline) antes de propor
- [ ] **Nada inviolável mudado** (URLs, nav, campos de form, logo, copy legal) sem aprovação explícita
- [ ] **Tokens da marca extraídos e mapeados para o tokens.css ANTES** de aplicar regras de cor (marca roxa continua roxa; override documentado)
- [ ] **Levers aplicadas em ordem** (1 → 6), parando quando o brief foi satisfeito (não todas por reflexo)
- [ ] **Cor da marca preservada**, tells da IA aposentados (em-dash, 3 cards iguais, Inter, fake screenshots, eyebrows em excesso)
- [ ] **Pre-flight do DESIGN.md §6 rodado** e reportado no relatório de redesign
- [ ] Zero `—`/`–` em texto visível; zero hex fora de tokens (grep confirmado)
- [ ] Relatório de redesign entregue com modo + auditoria + preserves + levers + tokens extraídos

## Qualidade

- O redesign moderniza SEM apagar a identidade: quem conhece a marca reconhece a marca depois.
- Cada decisão tem razão de uma frase: preserve porque é assinatura, aposenta porque é tell/layout quebrado.
- Auditoria antes, alavancas em ordem, pre-flight no fim — o processo é tão auditável quanto o resultado.
- Se precisar de token que o kit não tem, proponha no relatório (o `design-handoff` cuida), nunca invente hex.
