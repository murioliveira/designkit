# Demonstração da skill design-redesign: "Cloudly" (before → after)

> **Objetivo do caso:** provar a skill `skills/design-redesign/SKILL.md` em execução real, de forma não-destrutiva: pegar uma landing GENÉRICA DE IA ("Cloudly", SaaS de tarefas) e redesenhar pelo protocolo do kit, preservando o esqueleto de conteúdo e aposentando os tells.
> **Papel executado:** design-redesign · **Local:** `docs/casos/redesign-demo/` · **Não tocou em nenhum outro arquivo.**

## Arquivos

- `before.html` — o "AI slop" típico (o estado a redesenhar): hero centralizado com gradiente roxo, 3 cards iguais, Inter, em-dashes, nome genérico "Cloudly", "Transforme sua produtividade", eyebrow em toda seção, fake screenshot de div, scroll cue "Scroll down", versão no footer, depoimento "John D.", número falso "99.9%".
- `auditoria.md` — o audit-before-touch completo (7 itens do protocolo) + árvore de decisão.
- `after.html` + `redesign.css` — o redesign final, consumindo somente tokens do kit.
- este `README.md` — o relato.

## 1. Modo detectado

**Redesign - Overhaul** (com preservação estrita de conteúdo/IA). Justificativa (árvore de decisão do DESIGN.md §5.1): a dívida visual é **estrutural e sistêmica** (os tells são a linguagem inteira da página, não detalhes), mas **IA e conteúdo são sãos** (estrutura, labels de nav, preços e intenção de CTAs cumprem trabalho). Não é greenfield (o conteúdo existe e vale) e não é preserve (não há identidade visual a preservar: o roxo é default de LLM, não marca).

## 2. Auditoria resumida (detalhe em auditoria.md)

- **Tokens de marca extraídos:** roxo `#7c3aed` → **aposentado com justificativa** (default de LLM, sem marca por trás; a regra da skill diz que a cor da marca só sobrevive se é escolha real e articulável). Neutros `#f9fafb`/`#fff` mapeados para `--color-bg`/`--color-surface-muted`.
- **IA preservada:** nav (Recursos, Preços, Depoimentos), seções, ordem de conversão, slugs (`#recursos`, `#precos`, `#depoimentos`), nomes/valores de plano (Básico R$0, Profissional R$29, Empresa R$99), intenção de CTAs (Começar grátis, Ver demonstração, Falar com vendas).
- **Padrões a aposentar (16 inventariados):** gradiente roxo, hero centralizado, 3 cards iguais, Inter, em-dash, nome genérico, "Transforme sua produtividade", eyebrow em toda seção, fake screenshot de div, scroll cue, versão no footer, "John D.", "99.9%"/"10.000 times", ausência de landmarks, hero de 160px.
- **Dials lidos do before:** VARIANCE 1, MOTION 2, DENSITY 5. **Dials-alvo (overhaul +2/+2/igual):** 3/4/5.

## 3. Alavancas aplicadas (em ordem, parando quando o brief foi satisfeito)

| # | Alavanca | O que mudou |
|---|---|---|
| 1 | Tipografia | Inter (Google Fonts) → system-ui do kit (`--font-family-base`); display com `--letter-spacing-tight` + `--font-line-height-tight`; body com `--font-line-height-relaxed` e `max-width: 52ch` |
| 2 | Espaçamento e ritmo | Valores mágicos (`24px`, `48px`, `160px`, `32px`) → escala `--space-*` do kit; seções com ritmo `--space-16/20`; removido o hero de 160px (agora `padding-block` via tokens) |
| 3 | Recalibração de cor | Roxo + gradiente → neutros slate do kit + **um único accent** (`--color-primary` índigo) em CTAs, eyebrows, marca e destaque do plano; color lock na página inteira; theme lock (claro/escuro via `[data-theme]` do kit) |
| 4 | Camada de motion | Hover com spring (`--motion-easing-spring`) e `translateY(-2px)` + sombra em cards; `:active` com scale; hambúrguer que vira X; **só transform/opacity**, `prefers-reduced-motion` zerando tudo; sem scroll listener |
| 5 | Hero recomposição | Centralizado → **split assimétrico** (texto | mockup SVG real); headline 1 linha ("Clareza no que cada um faz, hoje."), subtext 17 palavras, 2 CTAs, 4 elementos de texto (eyebrow + título + sub + CTAs), sem scroll cue, sem logo wall |
| 6 | Substituição de blocos | Fake screenshot de div → **mockup de produto real em SVG** (checklist com estados done/pendente, progresso 66% honesto, `role="img"` + `aria-label`); 3 cards iguais → **grid assimétrico 2+1** (feature wide + 2 normais) |

**Não aplicadas por reflexo:** nada além das 6 (o brief "modernize sem quebrar o esqueleto" foi satisfeito na 6).

## 4. O que foi PRESERVADO (invioláveis da auditoria)

Nav labels e ordem (Recursos, Preços, Depoimentos) · slugs de âncora (`#recursos`, `#precos`, `#depoimentos`) · nomes e valores dos planos (Básico 0, Profissional 29, Empresa 99) · intenções de CTA (Começar grátis, Ver demonstração, Falar com vendas) · o nome "Cloudly" (conteúdo; ganhou monograma SVG como marca, sem trocar o wordmark) · seções e fluxo de conversão · copyright no rodapé.

## 5. Auto-avaliação contra o pre-flight (DESIGN.md §6)

- [x] Design Read declarado e dials explícitos (3/4/5, razão: overhaul de SaaS de gestão com densidade de trabalho, assimetria contida, motion funcional)
- [x] **Zero `—` e zero `–`** em `after.html` (grep: 0 ocorrências)
- [x] Theme lock (um tema por página, via `[data-theme]` do kit); Color lock (accent único `--color-primary` em tudo); Shape lock (raio do kit: full em pills, lg em mockup/cards, md em itens/inputs)
- [x] Contraste AA: texto `--color-text` sobre `--color-bg` (~13:1), muted só em metadados, CTA primário com `--color-on-primary`
- [x] CTA: labels não quebram ("Começar grátis", "Ver recursos", "Falar com vendas"), uma intenção por CTA (signup / browse / contact)
- [x] Hero: headline 1 linha, subtext 17 palavras, CTA visível sem scroll, 4 elementos, padding top `--space-16` (4rem ≤ 6rem)
- [x] Eyebrows: 1 (hero) ≤ ceil(5 seções/3) = 2
- [x] Sem fake screenshots (SVG real de produto); sem scroll cues, version footer, strips, dots, eyebrows numerados
- [x] Motion motivado (feedback de hover/active, transição de estado do menu), só transform/opacity, reduced-motion coberto, sem `window scroll` listener
- [x] Nav em 1 linha no desktop (altura `--space-16` = 4rem ≤ 80px); zigzag 0; grids com variação real (2+1)
- [x] Mobile collapse explícito (nav colapsável com aria-expanded/aria-controls, Esc fecha, grids 1 coluna)
- [x] Estados: landing sem forms (N/A loading/error); hover/active/focus presentes
- [x] Copy auditada: persona real pt-BR (Mariana Duarte, gerente de produto na Plena), quote sem número falso, zero "transforme/elevate/seamless"
- [x] Dark mode definido (herdado do kit) e funcionando nos dois modos
- [x] Detector: `python scripts/smoke-test.py` PASS (caso não quebra o repo) + varredura anti-slop (0 em-dash, 0 hex fora de tokens no after)

## 6. Decisão de design documentada (uma frase cada)

- **Overhaul, não preserve**: a "marca" atual é o slop inteiro; preservar seria polish sobre linguagem que deveria morrer (erro nº 2 do protocolo).
- **Roxo aposentado, não mantido**: sem asset de marca que o justifique; é o tell nº 1. O kit fornece o accent (índigo) como identidade.
- **Nome "Cloudly" preservado**: é conteúdo de IA; o redesign não é pretexto para rebranding silencioso.
- **Mockup SVG real, não imagem**: landing sem build, sem assets externos; SVG inline é o padrão do kit (casos Aurora/Lumen/Norte) e comunica o produto sem fake screenshot.

## 7. Como abrir

Abra `after.html` direto no navegador (tema segue `dk-theme`/sistema; toggle alterna e persiste). Compare com `before.html` para ver a transformação. Depois do critique, o `design-critic` valida o after contra brief + tokens (loop de refine volta para esta skill).
