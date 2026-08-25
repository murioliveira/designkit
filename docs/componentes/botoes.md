# Botões (`.btn`)

> Grupo 1 de `styles/components.css`. Botões de ação com variantes, tamanhos, estados, ícone e loading.
> Vale para `<button>` **e** `<a class="btn">` (links com aparência de botão).

## 1. Visão geral

O botão é o gatilho de ação primário do kit. Um único elemento base (`.btn`) recebe modificadores de **variante** (ênfase), **tamanho** e **estado**. O contraste de cor on/off vem dos tokens semânticos de cada tema — nenhuma cor é hardcoded.

## 2. Variantes, tamanhos e estados

### Variantes

| Classe | Quando usar | Aparência |
|---|---|---|
| `.btn` (base) | Sem modificador = botão "fantasma neutro" (transparente, texto normal) | Sem fundo, `--color-text` |
| `.btn--primary` | **Ação principal da tela** (uma por view) | Fundo `--color-primary`, texto `--color-on-primary`, `--shadow-sm` |
| `.btn--secondary` | Ação alternativa com superfície | Fundo `--color-surface`, borda `--color-border-strong` |
| `.btn--ghost` | Ação de baixa ênfase (ex.: "Cancelar", links) | Sem fundo até hover; texto `--color-primary` |
| `.btn--danger` | Ação destrutiva/irreversível | Fundo `--color-error`, texto `--color-surface` (contraste AA nos 2 temas) |

### Tamanhos

| Classe | Padding | Fonte |
|---|---|---|
| `.btn--sm` | `--space-1` `--space-3` | `--font-size-caption` (12px) |
| `.btn` (médio) | `--space-2` `--space-4` | `--font-size-small` (14px) |
| `.btn--lg` | `--space-3` `--space-6` | `--font-size-h6` (16px) |

### Estados (pseudo-classes e atributos)

| Estado | Seletores | Comportamento |
|---|---|---|
| Hover | `.btn:hover` | Remove sublinhado (herdado de link); variantes trocam fundo (`--color-primary-hover`, `--color-surface-muted`, `--color-primary-soft`); `--danger` usa `filter: brightness(0.92)` |
| Pressionado | `.btn:active` | `transform: translateY(1px)` (constante de geometria); `--danger` → `brightness(0.85)`; variantes trocam para `--color-primary-active`/`--color-border`/`--color-primary-soft-strong` |
| Foco | `.btn:focus-visible` | `outline: none` + `box-shadow: var(--focus-ring)`; `border-radius: var(--radius-md)` preservado |
| Desabilitado | `.btn:disabled` | `opacity: 0.5`, `cursor: not-allowed`, `pointer-events: none`, sem sombra/transform |
| Carregando | `.btn--loading` (+ `:disabled`) | Spinner visível, `opacity: 1`, `cursor: wait`, `pointer-events: auto` — mantém as cores da variante |

### Ícone e spinner

| Classe | Uso |
|---|---|
| `.btn__icon` | Ícone inline (SVG) dentro do botão; `1.25em` (escala com a fonte) |
| `.btn__spinner` | Spinner CSS puro (borda `currentColor` + `border-right-color: transparent`, animação `dk-spin` 0.8s); oculto até `.btn--loading` |
| `.btn__label` | Texto do botão (usado pelo demo de loading para trocar "Salvar alterações" → "Salvando…") |

## 3. Exemplo de uso mínimo

```html
<!-- Ação principal -->
<button type="button" class="btn btn--primary">Salvar alterações</button>

<!-- Alternativa -->
<button type="button" class="btn btn--secondary">Cancelar</button>

<!-- Link com aparência de botão -->
<a class="btn btn--ghost" href="/continuar">Continuar</a>

<!-- Destrutiva -->
<button type="button" class="btn btn--danger">Excluir projeto</button>

<!-- Com ícone (SVG inline, aria-hidden) -->
<button type="button" class="btn btn--primary">
  <svg class="btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" aria-hidden="true" focusable="false">
    <polyline points="7 10 12 15 17 10"/>
    <line x1="12" y1="15" x2="12" y2="3"/>
  </svg>
  Baixar
</button>

<!-- Loading (JS do showcase: [data-demo-loading]) -->
<button type="button" class="btn btn--primary" aria-busy="true" disabled>
  <span class="btn__spinner" aria-hidden="true"></span>
  <span class="btn__label">Salvando…</span>
</button>
```

## 4. Tokens usados

- **Cor:** `--color-primary` / `--color-primary-hover` / `--color-primary-active` / `--color-on-primary` / `--color-primary-soft` / `--color-primary-soft-strong` / `--color-surface` / `--color-surface-muted` / `--color-border-strong` / `--color-text` / `--color-error`
- **Raio:** `--radius-md` (corpo), `--radius-full` (spinner)
- **Sombra:** `--shadow-sm` (primário e danger)
- **Espaçamento:** `--space-1`…`--space-6` (paddings e gap interno)
- **Tipografia:** `--font-size-small` / `--font-size-caption` / `--font-size-h6`, `--font-weight-semibold`, `--font-line-height-tight`
- **Motion:** `--motion-duration-fast` + `--motion-easing-out` (transições)
- **Foco:** `--focus-ring` (definido no tokens, sobrescrito por tema)

## 5. Acessibilidade

- **Foco visível:** `:focus-visible` com `--focus-ring` (anel 3px) — nunca remova o outline sem substituir pelo anel.
- **Ícones:** SVG com `aria-hidden="true"` + `focusable="false"`; o rótulo de texto fica no conteúdo.
- **Loading:** use `aria-busy="true"` no botão e troque o rótulo por verbo progressivo ("Salvando…"); o spinner é `aria-hidden` (decorativo).
- **Desabilitado:** `:disabled` cobre botões nativos; para `<a class="btn">` desabilitado não existe `:disabled` — aplique `aria-disabled="true"` e trate o clique (não basta CSS).
- **Link vs botão:** use `<a>` para navegação e `<button>` para ações; o kit estiliza ambos, mas o papel semântico não muda.

## 6. Notas de implementação

1. **Não `display: none` o spinner em produção:** o `.btn__spinner` usa `display: none` por padrão e `display: inline-block` em `.btn--loading` — se você precisar animar a entrada, troque para `visibility`/`opacity` com `aria-hidden` para não perder o layout.
2. **`translateY(1px)` no `:active` compõe com transforms:** se a variante adicionar outro `transform` (ex.: elevação), o estado ativo sobrescreve; para combinar, use `translateY(calc(1px + var(--offset)))`.
3. **O demo de loading é só do showcase:** `[data-demo-loading]` (2.2s, `initDemoLoading()` no `app.js`) simula o fluxo; em produção, controle `disabled`/`aria-busy`/classe pelo estado real da sua requisição e reaplique `aria-label` no label ao concluir.
4. **`.btn:disabled` usa `pointer-events: none`:** o loading reabilita via `.btn--loading:disabled { pointer-events: auto }` — não remova isso ou o `cursor: wait` para de funcionar.
5. **Um `--primary` por tela:** a hierarquia visual depende disso; dois primários lado a lado competem e o critique do kit reprova.
