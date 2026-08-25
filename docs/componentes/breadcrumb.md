# Breadcrumb (`.breadcrumb`)

> Grupo 9.2 de `styles/components.css`. Trilha de navegação com separador via CSS e item atual destacado. Sem JS.

## 1. Visão geral

O breadcrumb mostra a posição do usuário na hierarquia do site. É **CSS puro** (zero JS): o HTML declara a trilha em um `ol` semântico e o CSS desenha o separador tipográfico (`/`) via `::after` — ele **não existe no HTML**, então leitores de tela não anunciam separadores.

## 2. Estrutura e classes

| Classe / atributo | Papel |
|---|---|
| `nav.breadcrumb` | Landmark de navegação (com `aria-label`) |
| `.breadcrumb__list` | `ol` da trilha (flex, quebra em mobile) |
| `.breadcrumb__item` | `li` — o separador `::after` é aplicado exceto no último |
| `.breadcrumb__link` | Link de nível intermediário (cor atenuada) |
| `.breadcrumb__link--truncated` | Link longo com ellipsis (texto completo no `title`) |
| `.breadcrumb__current` | Item atual (`aria-current="page"`, texto forte) |

## 3. Exemplo de uso mínimo

```html
<nav class="breadcrumb" aria-label="Trilha de navegação">
  <ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a class="breadcrumb__link" href="/">Início</a></li>
    <li class="breadcrumb__item"><a class="breadcrumb__link" href="/docs">Documentação</a></li>
    <li class="breadcrumb__item"><span class="breadcrumb__current" aria-current="page">Botões</span></li>
  </ol>
</nav>
```

Link truncado:

```html
<li class="breadcrumb__item">
  <a class="breadcrumb__link breadcrumb__link--truncated" href="/" title="Design Kit — Showcase e Documentação">
    Design Kit — Showcase e Documentação
  </a>
</li>
```

## 4. Tokens usados

- **Cor:** `--color-text-muted` (links/separador), `--color-text-strong` (item atual e hover), `--color-primary` (link padrão do base)
- **Espaçamento:** `--space-1` / `--space-2` (gap entre itens e separador)
- **Tipografia:** `--font-size-small`, `--font-weight-semibold` (atual)
- **Motion:** `--motion-duration-fast` + `--motion-easing-out` (transição do link)

## 5. Acessibilidade

- **Landmark:** `nav` com `aria-label` distinto dos demais landmarks de navegação.
- **`aria-current="page"`** no item atual (no elemento que representa a página atual, `span` ou `a`).
- **Separador não textual:** o `/` é `::after` com `content` — não é lido por leitores de tela (evita "Início barra Documentação barra Botões").
- **Truncamento:** o texto completo fica no `title` do link (hover) e o conteúdo visível é o início do nome.

## 6. Notas de implementação

1. **Último item não é link** quando é a página atual: use `span.breadcrumb__current` em vez de `a` — a página atual não precisa (nem deve) linkar para si mesma.
2. **`vertical-align: bottom` no link truncado** evita o corte da descendente (ex.: "p") dentro do `inline-block`.
3. **Nível único é válido:** breadcrumb com só o item atual comunica "você está aqui" sem hierarquia; use `aria-label` que deixe isso claro.
4. **Mobile:** a trilha quebra em múltiplas linhas (`flex-wrap`) em vez de rolar — para trilhas longas, considere ocultar o nível mais antigo (padrão "collapse") em telas pequenas.
