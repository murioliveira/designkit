# Dropdown (`.dropdown`)

> Grupo 9.1 de `styles/components.css`. Menus de ações e seleção em popup, com navegação por teclado completa.

## 1. Visão geral

O dropdown é um popup sobreposto ancorado a um gatilho. O kit oferece dois usos:

1. **Menu de ações** — lista de ações sobre um item (renomear, duplicar, excluir…), com item destrutivo e separador.
2. **Select-like** — escolha de uma opção entre várias, com checkmark no item selecionado (atualiza o valor no gatilho).

O comportamento de teclado e foco fica no `js/app.js` (`initDropdowns()`): o HTML declara a estrutura acessível (ARIA) e o JS a anima.

## 2. Estrutura e classes

| Classe / atributo | Papel |
|---|---|
| `.dropdown` | Wrapper posicionado (ancoragem do menu) |
| `[data-dropdown]` | Gatilho (botão); recebe `aria-haspopup="menu"`, `aria-expanded`, `aria-controls` |
| `.dropdown__trigger` | Estilo do gatilho aberto (estado pressionado) |
| `.dropdown__chevron` | Seta do gatilho (gira 180° quando aberto) |
| `.dropdown__menu` | Popup `role="menu"`, oculto via `[hidden]` |
| `.dropdown--align-end` | Variante: menu alinhado à direita (menus de ação) |
| `.dropdown__item` | Item `role="menuitem"` (botão) |
| `.dropdown__item--danger` | Item destrutivo (cor `--color-error`) |
| `.dropdown__check` | Check do select-like (visível com `aria-current="true"`) |
| `.dropdown__separator` | Divisor visual entre grupos de itens (`role="separator"`) |
| `[data-select-like]` | Marca o menu como select-like no JS |

## 3. Exemplo de uso mínimo

```html
<div class="dropdown">
  <button type="button" class="btn btn--secondary dropdown__trigger" data-dropdown
          aria-haspopup="menu" aria-expanded="false" aria-controls="menu-acoes">
    Ações
    <svg class="dropdown__chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <polyline points="6 9 12 15 18 9"/>
    </svg>
  </button>
  <div class="dropdown__menu" id="menu-acoes" role="menu" aria-label="Ações do projeto" hidden>
    <button type="button" class="dropdown__item" role="menuitem" tabindex="0">Renomear</button>
    <div class="dropdown__separator" role="separator"></div>
    <button type="button" class="dropdown__item dropdown__item--danger" role="menuitem" tabindex="-1">Excluir</button>
  </div>
</div>
```

Select-like com check:

```html
<div class="dropdown__menu" id="menu-plano" role="menu" aria-label="Escolha o plano" data-select-like hidden>
  <button type="button" class="dropdown__item" role="menuitem" tabindex="0" aria-current="true">
    Starter
    <svg class="dropdown__check" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <polyline points="20 6 9 17 4 12"/>
    </svg>
  </button>
</div>
```

> O `tabindex` inicial (0 no primeiro item, −1 nos demais) é redefinido pelo JS ao abrir — o HTML só precisa estar correto no estado inicial.

## 4. Tokens usados

- **Cor:** `--color-surface` (menu), `--color-surface-muted` (hover), `--color-border` (borda/separador), `--color-text` / `--color-text-strong` (itens), `--color-primary` (selecionado, gatilho aberto), `--color-error` (item perigo)
- **Raio:** `--radius-md` (menu), `--radius-sm` (itens)
- **Sombra:** `--shadow-md`
- **Espaçamento:** `--space-1`…`--space-3` (padding/gaps)
- **Tipografia:** `--font-size-small`, `--font-weight-semibold`, `--font-line-height-tight`
- **z-index:** `--z-dropdown`
- **Motion:** `--motion-duration-fast` + `--motion-easing-out`

## 5. Acessibilidade

- **Padrão WAI-ARIA Menu Button:** gatilho com `aria-haspopup="menu"` + `aria-expanded` + `aria-controls`; menu com `role="menu"` e itens `role="menuitem"`.
- **Teclado:** Enter/Espaço/↑/↓ abrem o menu (↑/↓ focam o último/primeiro item); dentro do menu, ↑/↓ circulam, Home/End vão ao primeiro/último, Esc fecha devolvendo o foco ao gatilho, Tab fecha e segue a ordem natural.
- **Foco:** `:focus-visible` com `--focus-ring`; roving tabindex (só o item ativo entra na ordem de Tab).
- **Gatilho de ícone:** precisa de `aria-label` (ex.: "Mais opções") — o ícone é `aria-hidden`.
- **Fechamento:** Esc, clique fora, escolha de item ou Tab. O estado é refletido em `aria-expanded`.

## 6. Notas de implementação

1. **`[hidden]` é o estado fechado:** o menu começa com `hidden` no HTML e o JS só alterna o atributo — não use `display:none` via classe em paralelo (o CSS usa `[hidden] { display: none }`).
2. **Clique fora usa delegação no documento:** o handler ignora cliques dentro de `.dropdown`; se você aninhar dropdowns, o `closest(".dropdown")` do evento mais interno resolve primeiro.
3. **Select-like requer `.dropdown__value` no gatilho:** sem esse span, o JS troca o `aria-current` mas não atualiza o rótulo visível.
4. **Itens desabilitados são pulados:** `:disabled` filtra `itemsOf()` na navegação e na contagem de Tab.
5. **Não use `<a role="menuitem">` para ações destrutivas sem confirmação** — menu de ação não substitui diálogo de confirmação (ver `.modal`).
