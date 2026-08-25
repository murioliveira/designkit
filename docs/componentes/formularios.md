# Formulários

> Grupo 6 de `styles/components.css` (fase 4B). Campos, controles customizados, estados e validação.

## 1. Visão geral

O kit cobre o formulário completo: **`.field`** (wrapper com label + controle + hint/erro), controles base (**`.input`**, **`.textarea`**, **`.select`**), campos com ícone/ação (**`.input-wrap`**), controles customizados sobre inputs nativos (**`.check`**, **`.radio`**, **`.toggle`**) e agrupamento (**`.fieldset`**). A validação é dirigida por estado no wrapper (`.field--error`/`.field--success`) sincronizado com `aria-invalid`.

## 2. Classes e estados

### Estrutura de campo

| Classe | Papel |
|---|---|
| `.field` | Wrapper vertical: label + controle + hint/erro |
| `.field__label` | Rótulo (forte); asterisco obrigatório em `<span class="req">` |
| `.field__hint` | Texto de ajuda (muted) |
| `.field__error` / `.field__success` | Mensagens de validação — ocultas por padrão (`display: none`), exibidas pelo estado do wrapper |
| `.field--error` / `.field--success` | Estado aplicado no `.field` (mostra a respectiva mensagem e pinta a borda do controle) |
| `.field--full` | Ocupa linha inteira em grid de 2 colunas |

### Controles base

| Classe | Estados |
|---|---|
| `.input`, `.textarea`, `.select` | `:hover` (borda `--color-text-muted`, exceto disabled/readonly), `:focus-visible` (borda `--color-primary` + `--focus-ring`), `:disabled` (fundo muted, `opacity 0.7`, `cursor: not-allowed`), `[readonly]` (borda tracejada) |
| `.textarea` | `min-height: 6rem` (3 linhas), `resize: vertical`, line-height corpo |

### Campo com ícone/ação

| Classe | Uso |
|---|---|
| `.input-wrap` | Contêiner `position: relative` |
| `.input-wrap__icon` | Ícone à esquerda (ex.: lupa de busca); `pointer-events: none` |
| `.input--with-icon` | Padding-left para o ícone (`--space-8`) |
| `.input-wrap__action` | Botão à direita (ex.: toggle de senha), 1.75rem, com focus-ring |
| `.input--with-action` | Padding-right para a ação (`--space-10`) |

### Select

| Classe | Uso |
|---|---|
| `.select-wrap` | Wrapper relativo; a seta customizada é desenhada com máscara SVG no `::after` (pinta com `--color-text-muted`, adapta ao tema) |
| `.select` | `appearance: none` + `padding-right: var(--space-8)`; `cursor: pointer` |

### Checkbox e radio customizados

| Classe | Papel |
|---|---|
| `.check` / `.radio` | Label flex com gap; `cursor: pointer` |
| `.check input` / `.radio input` | Input nativo **presente mas invisível** (1px, `opacity: 0`) — acessível, focável, nunca `display: none` |
| `.check__box` / `.radio__dot` | Controle visual (square `--radius-sm` / círculo) |
| `.check__check` / `.check__minus` | SVGs de marcado e indeterminado (opacity/scale animados) |
| `.check input:checked + .check__box` | Fundo/borda `--color-primary`, ícone visível |
| `.check input:indeterminate + .check__box` | Mostra o menos (`--color-primary`) |
| `.radio input:checked + .radio__dot` | Ponto interno `--color-on-primary` |
| `.check input:focus-visible + .check__box` | `--focus-ring` no controle customizado |
| `.check:has(input:disabled)` | `cursor: not-allowed` + conteúdo com `opacity 0.6` |

### Toggle switch

| Classe | Papel |
|---|---|
| `.toggle` | Label flex (track + texto, podendo ter `.form-note` abaixo) |
| `.toggle__track` | Trilho 40×24px (`--radius-full`, `--color-border-strong`) |
| `.toggle__track::after` | Botão deslizante 18px; quando `:checked`, `translateX(1rem)` + track `--color-primary` |
| `.toggle input` | Checkbox nativo invisível; o `app.js` (`initToggleSwitches`) adiciona `role="switch"` + `aria-checked` |

### Agrupamento e layout

| Classe | Papel |
|---|---|
| `.fieldset` / `.fieldset__legend` | Agrupamento semântico (radios, checks); legend forte |
| `.fieldset--bordered` | Borda + padding para destaque |
| `.fieldset__options` | Grid de opções |
| `.form-grid` / `.form-grid--2` | Grid 1 coluna (mobile) → 2 (≥ `--breakpoint-md`); `.field--full`/`.fieldset`/`.form-actions` cruzam a linha |
| `.form-actions` | Rodapé de ações (submit/reset) |
| `.form-note` | Texto auxiliar sob o label do toggle |
| `.form-status` | Alerta de sucesso pós-submit; `[hidden]` oculta |

## 3. Exemplo de uso mínimo

```html
<div class="field">
  <label class="field__label" for="email">E-mail <span class="req" aria-hidden="true">*</span></label>
  <input class="input" type="email" id="email" name="email" autocomplete="email" required
         aria-describedby="hint-email err-email">
  <p class="field__hint" id="hint-email">Usado para login e recuperação.</p>
  <p class="field__error" id="err-email" role="alert"></p>
</div>

<!-- Checkbox customizado -->
<label class="check" for="termos">
  <input type="checkbox" id="termos" name="termos" required>
  <span class="check__box" aria-hidden="true">
    <svg class="check__check" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
    <svg class="check__minus" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="3" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/></svg>
  </span>
  <span>Li e aceito os termos.</span>
</label>

<!-- Toggle switch -->
<label class="toggle" for="notif">
  <input type="checkbox" id="notif" name="notif" checked>
  <span class="toggle__track" aria-hidden="true"></span>
  <span>Receber novidades</span>
</label>

<!-- Estado de erro aplicado -->
<div class="field field--error">
  <label class="field__label" for="email2">E-mail</label>
  <input class="input" type="email" id="email2" value="maria@exemplo" aria-invalid="true"
         aria-describedby="err-email2">
  <p class="field__error" id="err-email2" role="alert">Formato de e-mail inválido.</p>
</div>
```

## 4. Tokens usados

- **Cor:** `--color-text(-strong/-muted)`, `--color-surface(-muted)`, `--color-border(-strong)`, `--color-primary`, `--color-error`, `--color-success`, `--color-on-primary`
- **Raio:** `--radius-sm` (checkbox), `--radius-md` (controles), `--radius-full` (radio/toggle)
- **Espaçamento:** `--space-1`…`--space-10` (gaps, paddings, posicionamento de ícones/ações)
- **Tipografia:** `--font-size-small/caption`, `--font-weight-semibold`, `--font-line-height-tight/body`
- **Motion:** `--motion-duration-fast/base`, `--motion-easing-out`
- **Foco:** `--focus-ring`

## 5. Acessibilidade

- **Inputs nativos invisíveis, nunca removidos:** `.check input`/`.radio input`/`.toggle input` ficam com 1px + `opacity: 0`. `display: none` quebraria foco e `aria` — o foco visual é pintado no controle customizado via `input:focus-visible + .check__box`.
- **Validação:** o controle recebe `aria-invalid="true"`; a mensagem usa `role="alert"` (lida no anúncio); `aria-describedby` deve listar hint **e** erro (`id="hint-x err-x"`).
- **Toggle:** o `app.js` injeta `role="switch"` + `aria-checked` sincronizado no `change`. Sem JS, continua um checkbox acessível (sem a semântica de switch) — degradação aceitável.
- **Radios/checks agrupados:** use `.fieldset` + `.fieldset__legend` (o showcase agrupa o plano de preços assim).
- **Asterisco:** `.req` é `aria-hidden` — a obrigatoriedade é dita pelo `required` + mensagens; não confie só no `*` visual.
- **Erro que some ao corrigir:** o `app.js` limpa o erro no evento `input` (não no `change`) — feedback imediato ao digitar.

## 6. Notas de implementação

1. **A validação do `app.js` é de demonstração** (`initFormValidation`, regras por `name` no form `#demo-signup`, `novalidate` no HTML). Em produção use `Constraint Validation API` ou sua lib — mas mantenha o contrato: `.field--error` no wrapper + `aria-invalid` + `role="alert"` na mensagem.
2. **`aria-describedby` duplo:** o HTML do showcase aponta para `hint-*` e `err-*`; se o erro não existir no DOM ainda, o leitor anuncia só o hint — crie os nós de erro sempre (vazios), como o kit faz.
3. **`.form-status[hidden] { display: none }`:** sem o atributo `hidden`, o alerta de sucesso fica visível sempre — o JS controla via `status.hidden`. Não remova o atributo no HTML para "testar".
4. **Select com seta por máscara:** o `::after` do `.select-wrap` pinta com `background-color: var(--color-text-muted)` + `mask` — se você trocar o `background-color` do select, a seta não acompanha (máscara é independente do `color`).
5. **`[readonly]` não cobre `select`:** os estilos de readonly são só para `.input`/`.textarea` (`.select` usa `:disabled`); um select "só leitura" não tem padrão no kit — use disabled + hint.
6. **Checkbox indeterminado precisa de JS:** `initIndeterminate()` seta `el.indeterminate = true` para o `[data-indeterminate]` do showcase; sem isso, o estado visual "menos" nunca aparece.
