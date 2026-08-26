# E4 — Redesign (preservar marca) · Método A (Design Kit)

**Corrida:** e4-a · **Data:** 2026-08-26 · **Input:** `docs/casos/redesign-demo/before.html` ("Cloudly")
**Método:** Design Kit — leu `DESIGN.md`, consumiu tokens de `styles/tokens.css` e padrões de `styles/components.css`.

## Design Read

Lendo como: landing B2B de gestão de tarefas para times pequenos e médios, linguagem calma e ferramental, tendendo aos tokens do kit (índigo/slate) com layout assimétrico e motion contido.
Dials: DESIGN_VARIANCE 6, MOTION_INTENSITY 3, VISUAL_DENSITY 3 (redesign preservar: motion = igual+1 sobre o estático original).

## O que foi PRESERVADO (conteúdo e IA)

- **IA/nav inalterada:** estrutura `nav → hero → recursos → preços → depoimentos → CTA final → footer`; labels de nav preservados (Recursos, Preços, Depoimentos); âncoras `#recursos`, `#precos`, `#depoimentos` intactas (SEO).
- **CTAs mantidos:** "Começar grátis" (nav, hero, CTA final), "Ver demonstração", "Começar" (3 planos), "Falar com vendas" (Empresa).
- **Seções preservadas:** features (Gestão de tarefas, Colaboração em tempo real, Relatórios), pricing (Básico R$0, Profissional R$29, Empresa R$99), depoimento, CTA final, rodapé.
- **Nome da marca:** "Cloudly" preservado.
- **Linguagem:** pt-BR mantida; conteúdo de tasks e depoimento reescritos apenas para remover tells (ver abaixo) e tornar os números honestos.

## O que foi APOSENTADO (tells de IA removidos)

| Tell (no before) | Onde | Correção |
|---|---|---|
| Em-dash/en-dash (`—`/`–`) | título, desc, `Transforme sua produtividade — com Cloudly` | Pontuação normal (vírgula/ponto). Zero `—` restante. |
| Inter via Google Fonts + `--ai-purple` | head, CSS | Removido; `font-family-base` system-ui do kit; tokens índigo/slate. |
| Gradiente roxo de IA (`linear-gradient` roxo) | hero/cta | Removido; fundos planos do kit (`--color-surface`/`--color-surface-muted`). |
| 3 cards de feature idênticos | `features-grid repeat(3,1fr)` + 3 `.feature-card` | Grade **assimétrica** (card 1 em destaque, grid-row span 2 no desktop); não são mais iguais. |
| Fake screenshot de div (`fake-dashboard` com retângulos) | hero | Substituído por **painel de produto real** (lista de tarefas com checkmarks SVG e texto) — conteúdo real, não barras falsas. |
| Scroll cue ("Scroll down") | hero/cta | Removido. |
| Version footer ("Cloudly v2.4.1 · build 0048") | footer | Removido (mantido só © 2026). |
| Eyebrow em toda seção (`A nova era`, `Recursos poderosos`, `Planos flexíveis`, `O que dizem`) | hero + 3 seções | Removidos; 1 badge apenas no hero e 1 no depoimento (≤ ceil(seções/3)). |
| Nome genérico "John D., Product Manager" | depoimento | "Mariana Costa, gerente de projetos no estúdio Filigrana" (nome real pt-BR). |
| Número fake-precioso "99.9%!" | depoimento | Removido; copy honesta. |
| Body copy filler ("Transforme sua produtividade", "A nova era") | hero | Copy concreta: "Menos atrito, mais entrega para o seu time". |
| Falso logo wordmark de texto "Cloudly" como logo | nav | Mantido como wordmark simples (sem inventar marca SVG — decisão: navegar com wordmark neutro). |

## Regra de tokens

- Componentes usam **apenas `var(--...)`** semânticos do kit (tipografia, espaçamento, raio, sombra, cor). **Zero hex em regra de componente.**
- O único hex mora na **camada de tokens** (seção `:root`/`[data-theme]` no `<style>`), que é a fonte de verdade permitida (espelho de `tokens.css`).
- Shape lock: botões `radius-md`, cards `radius-lg`, panel `radius-xl`, dot/tag `full` — sistema único do kit.

## Acessibilidade / anti-slop (auto-verificação)

- `aria-hidden` nos ícones decorativos; `aria-label` no panel e nav; `<blockquote>` semântico; skip de referencia `:focus-visible` com `--focus-ring`.
- Dark mode via `[data-theme="dark"]` + `prefers-color-scheme` (tokens reais).
- `prefers-reduced-motion` colapsa transições e smooth-scroll.
- Zero `—`/`–`, zero Inter, zero gradiente roxo, zero fake screenshot, zero scroll cue, zero version footer.

## Como reproduzir / verificar

- Conteúdo e IA preservados com os tells removidos; linguagem visual nova com os tokens do kit.
- Arquivos gerados: `docs/experimentos/artefatos/e4-a.html` (auto-contido, abre no navegador) e este relatório.