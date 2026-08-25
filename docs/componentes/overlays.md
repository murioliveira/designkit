# Overlays e Feedback

> Grupo 8 de `styles/components.css` (fase 4C). Camadas de sobreposição e estados de carregamento: tooltip, modal, tabs, progress, skeleton e avatar.

## 1. Visão geral

- **Tooltip** (`.tooltip`): dica de contexto exibida em hover/foco, criada e posicionada pelo `app.js` (elemento `position: fixed` no `<body>`, inversão de cores para contraste AA nos dois temas).
- **Modal** (`.modal`): diálogo com backdrop, `role="dialog"` + `aria-modal`, trap de foco, Esc e devolução de foco ao gatilho — tudo orquestrado pelo `app.js`.
- **Tabs** (`.tabs`): abas WAI-ARIA (`tablist`/`tab`/`tabpanel`) com navegação por setas + Home/End e roving tabindex.
- **Progress** (`.progress`): barra determinada (largura = dado, em `style` inline) e indeterminada (animação de deslize).
- **Skeleton** (`.skeleton`): placeholder de carregamento com shimmer (estático em `prefers-reduced-motion`).
- **Avatar** (`.avatar`): círculo com imagem/iniciais, tamanhos sm/md/lg/xl e ponto de presença.

## 2. Classes e variantes

### Tooltip

| Classe / atributo | Papel |
|---|---|
| `[data-tooltip]` | Gatilho — o texto da dica vem deste atributo |
| `[data-tooltip-pos]` | Posição: `top` (padrão) \| `bottom` \| `left` \| `right` |
| `.tooltip` | Elemento criado no `<body>` (JS); `role="tooltip"`, `position: fixed`, `pointer-events: none` |
| `.tooltip.is-visible` | Revela (opacity 1) |
| `.tooltip[data-pos]` | Seta (`::after`, quadrado 8px rotacionado) alinhada à borda |

### Modal

| Classe | Papel |
|---|---|
| `.modal` | Overlay `fixed inset: 0`; **controlado por `[hidden]`** (`hidden` = fechado) |
| `.modal__backdrop` | Fundo escurecido (`rgb(2 6 23 / 0.55)` fixo proposital) + `[data-modal-close]` para fechar no clique |
| `.modal__dialog` | Caixa centralizada (`max-width: var(--container-sm)`, scroll interno, `--shadow-xl`) |
| `.modal__header` / `__title` / `__close` | Topo com título e botão X (`[data-modal-close]`) |
| `.modal__body` | Conteúdo |
| `.modal__footer` | Ações alinhadas à direita |

Gatilhos: `[data-modal-open="#id"]` abre; `[data-modal-close]` (botão, X ou backdrop), Esc e devolução de foco fecham.

### Tabs

| Classe | Papel |
|---|---|
| `.tabs__list` | `role="tablist"` (borda inferior) |
| `.tabs__tab` | `role="tab"`; ativa = `aria-selected="true"` + `tabindex="0"`; demais `tabindex="-1"`; indicador de 2px na borda inferior |
| `.tabs__panel` | `role="tabpanel"` + `aria-labelledby` + `tabindex="0"`; inativo = `hidden` |

### Progress

| Classe | Papel |
|---|---|
| `.progress` | Trilho (`--color-surface-muted`, `--radius-full`, altura `--space-2`) |
| `.progress__bar` | Preenchimento `--color-primary`; largura via `style` inline (dado) |
| `.progress--indeterminate` | Barra de 40% deslizando (`dk-progress-slide` 1.2s) |

### Skeleton

| Classe | Papel |
|---|---|
| `.skeleton` | Coluna de itens |
| `.skeleton__item` | Bloco base (`--color-surface-muted`, shimmer via `::after`) |
| `.skeleton__item--text` | Linha de texto (altura `--space-3`); largura em `style` inline |
| `.skeleton__item--rect` | Bloco de conteúdo (6rem) |
| `.skeleton__item--avatar` | Círculo 3.5rem (mesmo tamanho do `.avatar--lg`) |

### Avatar

| Classe | Papel |
|---|---|
| `.avatar` | Círculo base 2.5rem (imagem cobre, ou iniciais em `--color-primary`) |
| `.avatar--sm` / `--lg` / `--xl` | 1.5rem / 3.5rem / 5rem |
| `.avatar--primary` / `--neutral` | Fundo sólido primário / neutro |
| `.avatar__status` | Ponto de presença (borda `--color-surface` recorta o círculo) |
| `.avatar__status--away` / `--offline` | Âmbar / muted |

## 3. Exemplos de uso mínimo

```html
<!-- Tooltip: só precisa do atributo no gatilho (JS cria o resto) -->
<button type="button" class="btn btn--secondary" data-tooltip="Dica de contexto."
        data-tooltip-pos="top">Topo</button>

<!-- Modal: hidden no HTML, aberto por [data-modal-open="#demo-modal"] -->
<div class="modal" id="demo-modal" role="dialog" aria-modal="true"
     aria-labelledby="demo-modal-title" hidden>
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__dialog" role="document">
    <header class="modal__header">
      <h3 class="modal__title" id="demo-modal-title">Excluir projeto?</h3>
      <button type="button" class="modal__close" data-modal-close
              aria-label="Fechar diálogo">×</button>
    </header>
    <div class="modal__body"><p>Esta ação não pode ser desfeita.</p></div>
    <footer class="modal__footer">
      <button type="button" class="btn btn--ghost" data-modal-close>Cancelar</button>
      <button type="button" class="btn btn--danger">Excluir</button>
    </footer>
  </div>
</div>

<!-- Tabs: roving tabindex + aria-controls -->
<div class="tabs">
  <div class="tabs__list" role="tablist" aria-label="Exemplo">
    <button class="tabs__tab" id="tab-a" role="tab" aria-selected="true"
            aria-controls="panel-a">A</button>
    <button class="tabs__tab" id="tab-b" role="tab" aria-selected="false"
            aria-controls="panel-b" tabindex="-1">B</button>
  </div>
  <div class="tabs__panel" id="panel-a" role="tabpanel" aria-labelledby="tab-a" tabindex="0">
    <p>Conteúdo A.</p>
  </div>
  <div class="tabs__panel" id="panel-b" role="tabpanel" aria-labelledby="tab-b" tabindex="0" hidden>
    <p>Conteúdo B.</p>
  </div>
</div>

<!-- Progress: largura é DADO, vai no style -->
<div class="progress" role="progressbar" aria-valuenow="50" aria-valuemin="0"
     aria-valuemax="100" aria-label="Progresso: 50 por cento">
  <div class="progress__bar" style="width: 50%"></div>
</div>
<div class="progress progress--indeterminate" role="progressbar" aria-label="Carregando conteúdo">
  <div class="progress__bar"></div>
</div>

<!-- Skeleton: aria-hidden no contêiner -->
<div class="skeleton" aria-hidden="true">
  <div class="skeleton__item skeleton__item--avatar"></div>
  <div class="skeleton__item skeleton__item--text" style="width: 70%"></div>
</div>

<!-- Avatar com status -->
<span class="avatar avatar--lg">
  <img src="foto.jpg" alt="Nome da pessoa">
  <span class="avatar__status" aria-hidden="true"></span>
</span>
<span class="avatar avatar--primary">BR</span>
```

## 4. Tokens usados

- **Tooltip:** `--z-tooltip`, `--color-text-strong` (fundo), `--color-bg` (texto), `--shadow-md`, `--radius-sm`, `--space-2/3`, `--font-size-caption`, `--font-weight-medium`, `--font-line-height-tight`, `--motion-duration-fast`, `--motion-easing-out`
- **Modal:** `--z-modal`, `--container-sm`, `--shadow-xl`, `--radius-lg`, `--color-surface`, `--color-text(-muted)`, `--color-border`, `--space-2/4/6`, `--font-size-h5`, `--radius-full`, `--motion-duration-base`, `--motion-easing-out`, `--focus-ring`
- **Tabs:** `--color-border`, `--color-text(-muted/-strong)`, `--color-primary`, `--space-1/2/4`, `--font-size-small`, `--font-weight-semibold`, `--font-line-height-tight`, `--motion-duration-fast`, `--motion-easing-out`, `--focus-ring`, `--radius-sm`
- **Progress:** `--color-surface-muted`, `--color-primary`, `--radius-full`, `--space-2`, `--motion-duration-slow`, `--motion-easing-out`, `--motion-easing-in-out`
- **Skeleton:** `--color-surface-muted`, `--color-border`, `--radius-sm/full`, `--space-3`, `--motion-easing-in-out`
- **Avatar:** `--radius-full`, `--color-primary(-soft)`, `--color-on-primary`, `--color-surface(-muted)`, `--color-text-strong`, `--color-success`, `--color-warning`, `--color-text-muted`, `--font-size-small/caption/h5/h3`, `--font-weight-bold`, `--font-line-height-tight`

## 5. Acessibilidade

- **Tooltip:** nunca use tooltip como única forma de informação — conteúdo essencial deve estar no conteúdo principal. O JS liga `aria-describedby` no gatilho e usa `role="tooltip"`. Hover (mouse) e foco (teclado) acionam igualmente.
- **Modal:** o HTML precisa `role="dialog"` + `aria-modal="true"` + `aria-labelledby` (título) e opcional `aria-describedby` (descrição). O JS faz: foco no primeiro foco-ficável ao abrir, trap de Tab/Shift+Tab, Esc fecha, devolve foco ao gatilho ao fechar, `body.no-scroll` enquanto aberto.
- **Tabs:** roving tabindex (`aria-selected` refletido), setas ←/→/↑/↓ movem **e ativam** (ativação automática ao focar), Home/End vão ao primeiro/último. Painel inativo tem `hidden` — o `app.js` alterna.
- **Progress:** `role="progressbar"` + `aria-valuenow/min/max` (determinada) ou `aria-label` (indeterminada, sem valor). A largura é estilo inline (dado), não CSS.
- **Skeleton:** contêiner com `aria-hidden="true"` para leitores de tela ignorarem o placeholder; a real indicação de carregamento deve vir de `aria-busy`/`role="status"` no fluxo.
- **Avatar:** `img` com `alt` descritivo; iniciais dentro do `span`; o `.avatar__status` é `aria-hidden` (decorativo) — a presença real deve estar no texto ou `aria-label`.

## 6. Notas de implementação

1. **Tooltip e modal exigem o `app.js`:** sem JS não há tooltip (nada é renderizado) nem abertura de modal (o `hidden` persiste). O CSS sozinho não produz o comportamento — os gatilhos `[data-tooltip]`/`[data-modal-open]` só funcionam após `initTooltips()`/`initModals()` no `DOMContentLoaded`.
2. **Nunca remova o atributo `hidden` do modal no HTML** para "deixá-lo pronto": sem `hidden` o modal cobre a tela inteira e bloqueia a página desde o load. O controle é `modal.hidden = true/false` via JS.
3. **Posição do tooltip é calculada e clampa na viewport** (`GAP = 8`, `position()` no `app.js`); ao trocar o conteúdo do gatilho em runtime, o tooltip reposiciona no scroll/resize — mas se o gatilho mudar de lugar sem scroll (ex.: reflow por JS), a dica pode desalinhar até o próximo scroll.
4. **Tabs: não adicione tabs novas sem `id`s únicos** — `aria-controls` mapeia aba → painel por id; ids duplicados quebram a ativação. O `initTabs()` usa `document.getElementById`.
5. **Progress indeterminado com `aria-label` fixo:** não ponha `aria-valuenow` na indeterminada (sem valor); o leitor anuncia "progressbar, carregando". O `--progress__bar` dela tem `width: 40%` — não confunda com dado.
6. **Backdrop do modal usa cor fixa** (`rgb(2 6 23 / 0.55)`) de propósito (comentário no CSS); se precisar variar por tema, crie um token semântico novo em vez de um segundo hex.
7. **`@media (prefers-reduced-motion: reduce)`** (seção 8.7): tooltip/modal/tabs/progress param de animar; a barra indeterminada fica estática a 40% e o skeleton perde o shimmer — comportamento intencional, não regressão.
