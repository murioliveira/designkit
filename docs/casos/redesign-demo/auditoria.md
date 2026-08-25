# Auditoria antes de tocar — Redesign "Cloudly" (modo Overhaul)

> Executada pelo papel **design-redesign** (protocolo do kit, skill `skills/design-redesign/SKILL.md` + DESIGN.md §5.1) sobre `before.html`.
> Regra do protocolo: **auditar antes de tocar, documentar o estado atual, decidir o modo com justificativa, extrair tokens da marca antes de mexer na cor.**

## 0. Modo detectado (primeira ação, antes de qualquer edição)

**Redesign - Overhaul.** Justificativa pela árvore de decisão do DESIGN.md §5.1:

- A **dívida visual é estrutural e sistêmica**: os tells de IA não são um detalhe aqui e ali, são a linguagem inteira da página (gradiente roxo, hero centralizado, 3 cards iguais, eyebrow em toda seção, fake screenshot de div). Não há "uma identidade a preservar" que valha a pena: a "marca" atual é exatamente o slop que o kit aposenta.
- **Conteúdo e IA, porém, são sãos**: a estrutura (nav → hero → recursos → preços → depoimentos → CTA final → footer), os labels de nav ("Recursos", "Preços", "Depoimentos"), as seções e a intenção dos CTAs ("Começar grátis", "Falar com vendas") cumprem seu trabalho. Isso é preservado.
- Conclusão: **overhaul no visual, preservação estrita de conteúdo e IA** (não greenfield, porque o conteúdo existe e é válido; não preserve, porque não há identidade visual a preservar).

## 1. Tokens de marca (o que existe hoje no before)

| Item | Valor atual | Veredito |
|---|---|---|
| Cor primária | roxo `#7c3aed` (botões, links, eyebrows, CTA final) | **Aposentar** — roxo genérico de IA, sem marca por trás (tell nº 1 de gradiente, DESIGN.md §4.1). Nenhum briefing ou asset de marca justifica o roxo; é default de LLM. |
| Cor de fundo | branco + `#f9fafb` + gradiente roxo claro no hero | Aposentar o gradiente; neutros são os únicos aproveitáveis (mapear para `--color-bg`/`--color-surface-muted`) |
| Tipografia | Inter (Google Fonts) | **Aposentar** — Inter como default é tell (DESIGN.md §4.1); o kit usa system-ui via `--font-family-base` |
| Raio | 8px/12px uniforme | Substituir pela escala do kit (shape lock: `--radius-full` pills em botões, `--radius-md` em cards, `--radius-sm` em inputs) |
| Logo | wordmark "Cloudly" em texto (sem SVG/marca) | Preservar o nome (é conteúdo/nav), mas ganhar uma marca simples (monograma SVG) |

**Regra da skill respeitada:** a cor da marca só sobrevive se for escolha real e articulável. O roxo do Cloudly é default de LLM, não escolha de marca. **Aposentado com justificativa documentada** (não silenciosamente).

## 2. IA (arquitetura de informação)

- Nav: 3 links (Recursos, Preços, Depoimentos) + CTA "Começar grátis". **Preservar labels.**
- Fluxo de conversão: hero (CTA primário "Começar grátis" + secundário "Ver demonstração") → recursos → preços → depoimentos → CTA final. **Preservar ordem e intenções.**
- Footer: copyright + versão. **A versão do footer é tell e sai** (DESIGN.md §4.1); o copyright fica.
- Âncoras: `#recursos`, `#precos`, `#depoimentos`. **Preservar slugs** (SEO/muscle memory).

## 3. Blocos de conteúdo (o que faz trabalho vs filler)

| Bloco | Trabalho que faz | Filler? |
|---|---|---|
| Hero (title + sub + CTAs) | Posiciona o produto | Não, mas a copy é genérica ("Transforme sua produtividade") |
| Fake screenshot (painel de divs) | Pretende mostrar o produto | **Sim, é tell estrutural** (fake screenshot de div, DESIGN.md §4.1) → substituir por visual SVG real |
| 3 cards de features | Lista capacidades | Não (conteúdo válido), mas layout é tell (3 iguais) → grid assimétrico |
| 3 cards de preços | Planos Básico/Profissional/Empresa | Não; preservar valores e nomes de plano |
| Depoimento | Prova social | Copy é tell ("aumentou 99.9%", "John D.") → persona real pt-BR, número honesto |
| CTA final | Conversão | Não; preservar intenção |

## 4. Padrões a preservar

- **Nenhum visual brilhante** (honesto): o before não tem hero reconhecível, interação assinatura ou tratamento de marca que mereça sobreviver. O que sobrevive é o esqueleto: IA, labels de nav, nomes de plano, preços, intenção de CTAs, slugs de âncora.

## 5. Padrões a aposentar (tells inventariados no before)

| Tell | Onde | DESIGN.md |
|---|---|---|
| Gradiente roxo de IA | hero bg, CTA final | §4.1 |
| Hero centralizado | hero | §4.1 ("anti-center bias") |
| 3 cards iguais em linha | features (3×) e pricing (3×) | §4.1 |
| Inter default | Google Fonts | §4.1 |
| Em-dash (`—`) | h1 ("produtividade — com Cloudly"), depoimento | §4.1 (tell nº 1) |
| Nome genérico "Cloudly" | marca | §4.1 (nomes genéricos) |
| "Transforme sua produtividade" | hero | §4.9 (filler verb "transforme") |
| Eyebrow em toda seção | 4 seções, 4 eyebrows | §4.1 (máx 1 por 3 seções) |
| Fake screenshot de div | painel de tarefas | §4.1 (ban total) |
| Scroll cue "Scroll down" | hero | §4.1 |
| Versão no footer | v2.4.1 · build 0048 | §4.1 |
| "John D." | depoimento | §4.1 (nomes genéricos) |
| Números falsos 99.9% / 10.000 times | depoimento, CTA final | §4.1 |
| Zero landmarks semânticos | sem `<header>/<main>/<footer>` reais, sem skip-link, sem `aria` | §2 do kit (qualidade) |
| `h-screen`-like hero (160px fixo) e fontes via link externo | hero, fonts | §4.4 (perf/CWV) |

## 6. Leitura de dials do site atual (ponto de partida, não baseline)

| Dial | Valor lido | Evidência |
|---|---|---|
| DESIGN_VARIANCE | **1** (simetria perfeita) | tudo centralizado, 3 colunas iguais em features e pricing |
| MOTION_INTENSITY | **2** (quase estático) | só hover de links; nada anima |
| VISUAL_DENSITY | **5** (padrão de app) | padding moderado, cards em tudo |

**Dials-alvo do after (overhaul = +2/+2/igual, conforme DESIGN.md §2):** VARIANCE **3**, MOTION **4**, DENSITY **5** (SaaS de gestão: densidade de trabalho é esperada; assimetria contida para não virar caos; motion funcional de hover/active/toggle sem scroll-jacking).

## 7. SEO baseline

- `<title>`: "Cloudly — Gestão de Tarefas Moderna" (preservar o essencial, remover o em-dash: "Cloudly: gestão de tarefas moderna").
- `<meta description>`: preservar a intenção, reescrever sem "transforma".
- Slugs de âncora (`#recursos`, `#precos`, `#depoimentos`): **invioláveis**.
- Nenhuma página ranqueada além desta landing (POC), mas a disciplina se aplica: **nada de mudar slug, título de heading ranqueado ou estrutura de URL**.
- Meta `theme-color` para claro/escuro e `lang="pt-BR"` adicionados no after.

## Resumo da decisão

Overhaul no visual (a linguagem inteira é slop), preserve total no esqueleto (IA, nav, seções, preços, CTAs, slugs). Alavancas 1-6 todas aplicáveis (dívida estrutural), aplicadas em ordem no after.html.
