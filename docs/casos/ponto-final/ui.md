# UI - Farol (descrição, não build)

> Skill: `ui-designer` · Entrada: `research.md` + `ia.md` + `DESIGN.md` · Saída: design read, dials, telas, componentes do kit, tokens. **Teste de integração: a UI é DESCRITA em markdown, não construída em HTML.**

## Design Read (1 linha)

"Lendo como: app Operate para livreiros de bairro não-técnicos, linguagem de vitrine iluminada (neutros frios + accent âmbar), tendendo aos componentes do kit com densidade média e motion contido."

## Dials (justificados)

- **DESIGN_VARIANCE: 4** - app de tarefa (Operate): layout em grid alinhado, pouca assimetria; a ousadia fica no accent âmbar e na vitrine, não na grade.
- **MOTION_INTENSITY: 3** - o livreiro não quer animação no balcão: só hover/active e transições curtas de estado. Abaixo do limiar que exigiria parallax.
- **VISUAL_DENSITY: 6** - painel com informação real (lista de títulos, pedidos, relatórios), mas com respiro entre blocos; nada de cockpit.

## Telas (lista)

1. **Visão geral** - 3 cards de resumo (títulos na vitrine, pedidos em aberto, relatório do mês) + pendências com CTA.
2. **Catálogo** - barra de busca, lista de títulos (capa, autor, editora, preço), seleção por toque, filtro por distribuidora.
3. **Importar catálogo** - upload arrastar e soltar OU link; progresso da importação; resultado com contagem.
4. **Selecionados** - lista revisável antes de publicar na vitrine.
5. **Vitrine** - grid dos títulos ativos, reordenar, editar preço inline.
6. **Pedidos** - tabela pedido x entrega com estados (pendente, chegou, parcial).
7. **Relatórios** - seleção de mês, botão "Gerar PDF", histórico de relatórios.
8. **Configurações** - dados da livraria, distribuidores, tema claro/escuro.

## Componentes do kit usados (de `styles/components.css`)

| Tela | Componentes |
|---|---|
| Visão geral | `card`, `badge` (estados), `btn` |
| Catálogo | `input` (busca), `card--interactive` (título), `badge`, `pagination`, `check` (seleção múltipla), empty state via card com CTA (padrão `.placeholder`) |
| Importar | `card`, `progress`, `alert--error`, `btn--primary` |
| Selecionados | `table` (revisão), `btn--primary`, `btn--ghost` |
| Vitrine | `card`, `dropdown` (ações do título), `toggle` (ativo/inativo) |
| Pedidos | `table--zebra`, `badge--success/warning`, `tabs` (por distribuidora) |
| Relatórios | `select` (mês), `progress`, `btn--primary`, `alert--info` |
| Configurações | `field`, `input`, `select`, `toggle`, `tabs` |

## Tokens principais

- **Cor:** `--color-bg`, `--color-surface`, `--color-surface-muted`, `--color-text`, `--color-text-muted`, `--color-text-strong`, `--color-primary` (accent âmbar da vitrine), `--color-primary-soft`, `--color-border`, `--color-success`, `--color-warning`, `--color-error`, `--color-info`.
- **Tipografia:** `--font-size-h2/h3/h4` (títulos de tela e card), `--font-size-body`, `--font-size-small`, `--font-size-caption` (badges), `--font-weight-medium/semibold/bold`, `--font-line-height-tight/body`.
- **Espaço/raio/sombra:** `--space-2/3/4/6/8/10`, `--radius-md` (inputs/cards), `--radius-full` (badges, botões pill), `--shadow-sm` (cards), `--shadow-md` (dropdown).
- **Motion/z:** `--motion-duration-fast/base`, `--z-sticky` (nav do app).
- **Breakpoints:** `--breakpoint-sm/md/lg/xl` (mobile-first: tablet no balcão, desktop para o relatório).

## Método anti-slop aplicado

- **Accent único:** o âmbar (`--color-primary`) é o ÚNICO accent da página toda; semânticos só para estado real (pedido chegou = `--color-success`, atraso = `--color-warning`).
- **Shape lock:** pills em botões/badges (`--radius-full`), `--radius-md` em cards/inputs, seguindo a regra documentada do kit.
- **Theme lock:** app inteiro no tema escolhido (claro/escuro pelo `[data-theme]` do kit), nenhuma seção inverte.
- **Zero tells:** zero em-dash na copy, zero gradiente roxo, zero 3 cards iguais (os 3 resumos da visão geral usam o MESMO padrão de card, mas com conteúdo e ícone de estado diferentes e um CTA por card), zero nomes genéricos (Otávio, Livraria Quilombo), zero scroll cues, zero eyebrows em excesso (nenhum eyebrow de seção).
- **Estados completos:** toda tela com empty/erro/carregando mapeados (ver `ia.md` fluxos); botões com hover/active/focus/disabled.
- **Hero inexistente** (é Operate, não landing): a disciplina de hero do §4.2 não se aplica; vale a disciplina de app: nav em 1 linha, densidade 6, 1 foco por tela.