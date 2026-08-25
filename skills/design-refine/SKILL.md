---
name: design-refine
description: "Refina UI existente em 3 direções: bolder (amplificar o ousado), quieter (acalmar o excessivo) e distill (reduzir à essência). Use quando o usuário disser \"deixa mais ousado/impactante\", \"está poluído, acalma\", \"simplifica, tira o excesso\", \"está sem alma\", \"muito genérico\", \"dá mais vida\", ou apontar que uma tela existente não comunica como deveria. Design refinement, bolder, louder, amplificar, ousadia, quieter, acalmar, simplificar, distill, reduzir à essência, refinar UI existente, dar vida, menos é mais. Não é para criar UI do zero (use ui-designer) nem para redesign de marca (use design-redesign)."
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → **`../design-refine/SKILL.md`** → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

**Posicionamento desta skill no fluxo:**
- **Quando a direção é REFINAMENTO (não reconstrução):** esta skill entra DEPOIS do `../design-critic/SKILL.md`. O critique aponta o que não funciona; o refine decide a direção (bolder/quieter/distill) e aplica mudanças cirúrgicas na UI EXISTENTE. **Os loops de refine voltam para cá, e não para o `../ui-designer/SKILL.md`** — o ui-designer reconstrói; o design-refine transforma o que já existe, preservando identidade, conteúdo, IA e tokens.
- **Quando o critique (ou o brief) diz que a UI está além de refinamento** (estrutura quebrada, IA confusa, linguagem visual insalvável): use `../design-redesign/SKILL.md` (preserve/overhaul) ou `../ui-designer/SKILL.md` (greenfield). Refinar uma UI que precisa ser redesenhada é o erro nº 1 desta skill.
- Saída para `../design-critic/SKILL.md` (re-critique) até o critério de parada (sem blockers, média ≥ 4, nenhuma heurística < 3; máx 2 rodadas antes de escalar ao humano).

Checkpoints humanos: ① aprovação do research/brief (ocorre antes); ② aprovação da UI refinada entre refine→a11y/handoff.

← **você está aqui:** etapa 4.5 (pós-critique). Entrada: UI existente + critique report (se houver) + brief. Saída: a MESMA página transformada, + relatório curto de direção e alavancas aplicadas.

# Design Refine

Você é o refinador do setor de design. Entrada: uma UI que já existe e foi criticada (ou que o usuário sente que "não está funcionando"). Saída: a mesma superfície, transformada em UMA das três direções — **bolder**, **quieter** ou **distill** — preservando identidade, conteúdo, IA e a regra de tokens do kit. **Refinar não é reconstruir**: cada decisão mantém o que funciona e muda só o que a direção exige.

## Como executar

0. **Leia o DESIGN.md do kit** (raiz) — a voz do produto: dials (§2), tells da IA (§4), pre-flight (§6). Ele governa todo refinamento.
1. **Leia a UI existente** (HTML/CSS/JS) e a fonte de verdade visual (`styles/tokens.css`) — nunca assuma nomes de tokens, leia o arquivo.
2. **Leia o critique report**, se existir (em `docs/casos/<nome>/critique-report*.md` ou o que o design-critic entregou). O critique é o diagnóstico; esta skill é o tratamento.
3. **Escolha a direção** (seção abaixo) — declare em uma linha por que bolder/quieter/distill, e cite os dials que vai mover.
4. **Aplique as alavancas da direção** (seções abaixo), usando SOMENTE tokens do kit. Não introduza tells.
5. **Rode a auto-verificação** e o pre-flight do DESIGN.md §6 antes de entregar.

## Como escolher a direção

Leia o critique (se houver) e o brief, e pergunte qual diagnóstico a UI tem:

| Sintoma no critique / brief | Direção | Resposta do usuário típica |
|---|---|---|
| "Falta personalidade", "sem alma", "genérica", "parece template", "bland" | **bolder** | "deixa mais ousado", "dá mais vida", "mais impacto" |
| "Poluída", "agressiva", "muito estímulo", "grita demais", "competição visual" | **quieter** | "está poluído, acalma", "muito barulho", "menos cor" |
| "Complexa demais", "não sei o que fazer", "muita coisa", "densa" | **distill** | "simplifica", "tira o excesso", "quero o essencial" |

**Regra de ouro:** se o critique aponta problema ESTRUTURAL (IA confusa, seções sem objetivo, layout quebrado), não refine — redesenhe (`design-redesign`) ou reconstrua (`ui-designer`). Refinamento muda a expressão, não a estrutura.

**Se ambíguo:** faça UMA pergunta ("Isso está sem personalidade ou está poluído demais?"). Se der para inferir do critique com confiança, não pergunte.

**Reavalie os dials (DESIGN.md §2) ao refinar** — a direção move dials, e os dials justificam as alavancas:
- **bolder**: subir `DESIGN_VARIANCE` (+1 a +3) e, quando fizer sentido, `MOTION_INTENSITY` (+1 a +2).
- **quieter**: baixar `DESIGN_VARIANCE` e `VISUAL_DENSITY` (-1 a -3); `MOTION_INTENSITY` para 3 ou menos se o estímulo era de movimento.
- **distill**: baixar `VISUAL_DENSITY` e `DESIGN_VARIANCE` (-1 a -2); remover elementos até sobrar o essencial.

---

## Comando: `bolder` — amplificar o ousado

**Quando usar:** a UI é competente mas tímida. O critique diz "segura", "genérica", "sem personalidade"; o brief pede impacto, presença, memorabilidade. O problema não é estrutura — é falta de convicção visual.

**O que NÃO fazer (em hipótese alguma):**
- NÃO adicionar gradiente roxo, glow neon, ou brilho de botão (tell do DESIGN.md §4.1).
- NÃO trocar a paleta do kit por cores saturadas aleatórias (color lock: 1 accent).
- NÃO "ousar" com em-dash, eyebrow em toda seção, fake screenshots, ou qualquer tell.
- NÃO trocar a identidade da marca — bolder amplifica o que JÁ está lá, não substitui.
- NÃO aumentar tudo ao mesmo tempo (tudo gritando = nada gritando). Uma ousadia focal.

**Alavancas concretas (tokens do kit):**
- **Assimetria real** (VARIANCE ↑): quebre um grid simétrico — hero em grid assimétrico (`grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr)`), deslocar um elemento com `margin-top: calc(-1 * var(--space-8))`, ou um elemento que "vaza" para fora do container.
- **Escala tipográfica maior no display**: `font-size: var(--font-size-display)` com `letter-spacing: var(--letter-spacing-tight)` e `font-weight: var(--font-weight-bold)` no hero — mas respeite a disciplina do hero (≤ 2 linhas, cabe no viewport; DESIGN.md §4.2).
- **Accent mais presente**: o token primário do kit (`--color-primary`) em mais superfícies estratégicas — fundo de seção com `--color-primary-soft`/`--color-primary-soft-strong`, CTA primário de verdade (não ghost), um detalhe de marca repetido com intenção. Accent único em tudo (color lock).
- **Contraste/sombras mais fortes**: `--shadow-lg`/`--shadow-xl` em vez de `--shadow-sm`/`--shadow-md` no elemento focal; bordas `--color-border-strong` para definir forma; texto `--color-text-strong` no display.
- **Motion mais vivo** (dentro do MOTION_INTENSITY escolhido): entrada escalonada com `--motion-duration-base`/`--motion-duration-slow` e `--motion-easing-spring`, hover com `translate`/`scale` em `--motion-duration-fast` — sempre com `prefers-reduced-motion` coberto e só `transform`/`opacity`.
- **Uma ousadia focal**: UMA peça que quebra o padrão do resto da página (uma palavra em itálico forte no display, um bloco invertido, um número gigante, uma linha de marca desenhada). Uma só. O resto fica consistente para ela brilhar.

---

## Comando: `quieter` — acalmar o excessivo

**Quando usar:** a UI está agressiva, estimulante demais. O critique diz "grita", "poluída", "muita competição visual"; o usuário sente cansaço. O problema é excesso de estímulo — o contrário da timidez do bolder.

**O que NÃO fazer (em hipótese alguma):**
- NÃO virar a página em branco sem vida — **quieto ≠ vazio**. Quieto é espaço com intenção, não ausência.
- NÃO remover a hierarquia (sem contraste nenhum, tudo igual, nada guia o olhar).
- NÃO manter o accent em tudo "para não perder cor" — o quieto pode manter 1 accent forte em ações.
- NÃO remover estados (hover/focus/disabled) ou acessibilidade em nome de minimalismo.

**Alavancas concretas (tokens do kit):**
- **Menos competição visual** (VARIANCE/DENSITY ↓): elimine sobreposições e deslocamentos; alinhe ao grid; uniformize paddings na escala (`--space-*`).
- **Menos cores**: accent (`--color-primary`) SÓ em ações e no elemento focal; o resto em neutros (`--color-text`, `--color-text-muted`, `--color-surface`, `--color-surface-muted`). Cores semânticas (`--color-success/warning/error/info`) só onde carregam estado.
- **Menos cards**: troque cards por espaço negativo e divisórias — `border-top: 1px solid var(--color-border)` entre blocos, `--space-12`/`--space-16` de respiro. Cards só onde elevação comunica hierarquia real (DESIGN.md §4.3).
- **Tipografia mais calma**: reduza pesos extremos (`--font-weight-bold` → `--font-weight-semibold`/`--font-weight-medium` em subtítulos), menos `letter-spacing` dramático, corpo com `--font-line-height-relaxed`.
- **Motion reduzido**: `MOTION_INTENSITY` ≤ 3 — só hover/active estáticos (via CSS), sem entradas escalonadas, sem parallax. `prefers-reduced-motion` é o default neste modo.
- **Sombras sutis**: `--shadow-sm` ou nenhuma; `--shadow-lg/xl` só no elemento que precisa flutuar (ex.: modal).

---

## Comando: `distill` — reduzir à essência

**Quando usar:** a UI está complexa demais. O critique diz "densa", "muita coisa", "não sei por onde começar"; o usuário quer o essencial. O problema é excesso de elementos, mensagens e padrões — não de decoração (isso seria quieter).

**O que NÃO fazer (em hipótese alguma):**
- NÃO remover informação funcional (estados, acessibilidade, conteúdo real do brief).
- NÃO esconder tudo em um botão "saiba mais" (distill não é enterrar conteúdo, é priorizá-lo).
- NÃO trocar densidade por "menos cards com mais texto dentro".
- NÃO perder a identidade visual (distill preserva a voz; quieto também, mas distill foca em REMOVER complexidade, não em acalmar).

**Alavancas concretas (tokens do kit):**
- **Uma mensagem por seção**: cada seção prova seu objetivo. Se uma seção não comunica hierarquia/estado/ação — sai ou é fundida na vizinha.
- **Prove cada elemento** — a pergunta é: *"Este elemento comunica hierarquia, estado ou ação? Se sair, alguém perde alguma coisa?"* Se ninguém perde, sai. Regra: **cada elemento sobrevivente tem uma razão em 1 frase.**
- **Consolidar padrões**: se 3 variações de botão fazem o mesmo papel, fica 1 (a do kit: `btn--primary`); se 2 tipos de card servem para a mesma coisa, fica 1.
- **Encurtar copy**: subtext ≤ 20 palavras (hero), parágrafos até 25 palavras (DESIGN.md §4.9 espírito), labels diretos ("Falar com o ateliê", não "Entre em contato com o nosso time para mais informações").
- **Uma CTA por intenção** (DESIGN.md §4.3): 1 CTA primária por seção de conversão; sem CTAs duplicadas com a mesma intenção na página.
- **Menos componentes, mais espaço**: longas listas viram os 3-5 destaques + link (DESIGN.md §4.3); tabelas densas viram cards ou grupos.

---

## Saída esperada

A UI refinada (mesmos arquivos, mudanças cirúrgicas) + relatório curto:
1. **Direção escolhida** (bolder/quieter/distill) e por quê (1 linha, citando critique/brief).
2. **Dials antes → depois** (VARIANCE/MOTION/DENSITY).
3. **Alavancas aplicadas** (lista curta, cada uma com o token usado).
4. **O que foi preservado** (identidade, IA, conteúdo, acessibilidade — prova de que não virou outra página).

## Exemplo

**Exemplo real (distill, direção hipotética sobre o caso Aurora, `docs/casos/aurora/`):** se o critique dissesse "a CTA final tem 2 mensagens (reservar peças + falar com o ateliê) e copy longa", o distill: mantém `#cta-titulo` ("Quer uma mesa que conte histórias?") como a ÚNICA mensagem; encurta `cta__text` de 2 frases para 1 (≤ 20 palavras); mantém UMA ação (`btn--primary btn--lg` → "Falar com o ateliê", label já direto, não quebra); remove qualquer elemento decorativo da seção; aplica `--space-*` generoso entre title/text/actions. Resultado: a CTA fica com 3 elementos (título, texto curto, 1 botão) — cada um com razão em 1 frase. Preserva `href="mailto:ola@auroracinza.com.br"`, a cor do accent terracotta do caso e o token `--radius-lg` do botão.

**Contra-exemplo (bolder errado no hero do Lumen, `docs/casos/lumen/`):** subir `font-size` do `hero__title` além do `--font-size-display` com `leading-none` quebraria a disciplina do hero (cabe no viewport, ≤ 2 linhas) e o italic com descenders (`j`, `p`) seria cortado — o bolder correto é ampliar a ASSIMETRIA do grid e reforçar o accent `--color-primary`, não estourar a tipografia.

## Auto-verificação

- [ ] Direção escolhida com razão (cite o critique/brief em 1 linha)
- [ ] Dials reavaliados e declarados (antes → depois) — não refinei sem mexer nos dials
- [ ] **Tells do DESIGN.md §4 verificados**: zero `—`/`–`, zero fake screenshots, zero gradiente roxo, zero Inter, zero nomes genéricos, zero scroll cues, zero eyebrows em excesso, zero 3 cards iguais
- [ ] Só tokens do kit — `grep` por `#hex` no CSS refinado = zero
- [ ] Identidade preservada: a página ainda é a MESMA (mesma IA, mesmo conteúdo, mesma marca) — não virou outra página
- [ ] Color lock / shape lock / theme lock mantidos (1 accent, 1 raio, 1 tema)
- [ ] Estados hover/active/focus/disabled intactos; a11y não regrediu
- [ ] Motion motivado, só `transform`/`opacity`, `prefers-reduced-motion` coberto
- [ ] Hero dentro das regras (§4.2): ≤ 2 linhas, subtext ≤ 20 palavras, CTA visível
- [ ] Pre-flight do DESIGN.md §6 rodado; smoke/anti-slop checks PASS se aplicáveis
- [ ] Se o critique pedia redesign estrutural: NÃO refinei — encaminhei para `design-redesign`/`ui-designer`

## Qualidade

- Refinamento cirúrgico: mudanças pequenas, efeito grande. Se você mudou mais de ~30% da UI, provavelmente a direção era redesign, não refine.
- Cada alavanca citada com o token real do kit — nada de "use uma cor mais forte" sem dizer qual token.
- O usuário reconhece a própria UI no resultado — só que mais ousada, mais calma ou mais essencial.
