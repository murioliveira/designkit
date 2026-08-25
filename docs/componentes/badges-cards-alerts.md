# Badges, Cards e Alertas

> Grupos 2–4 de `styles/components.css`. Rótulos de status/contagem, superfícies de conteúdo e feedback contextual.

## 1. Visão geral

- **Badges** (`.badge`): rótulos compactos de status semântico, categoria ou contagem. O padrão de acessibilidade do kit: **a cor da variante fica no ponto** (`::before`, ícone com contraste ≥ 3:1) e o rótulo usa texto de alto contraste — legível mesmo sobre fundos "soft".
- **Cards** (`.card`): superfícies de conteúdo com hierarquia (título, eyebrow, texto, rodapé) e elevação no hover quando interativos.
- **Alertas** (`.alert`): feedback contextual (sucesso/erro/aviso/info) com barra de acento lateral, ícone colorido e fechamento animado.

## 2. Variantes e estados

### Badges

| Classe | Uso | Aparência |
|---|---|---|
| `.badge` (base) | Neutro (sem modificador) | Fundo `--color-surface-muted`, ponto `--color-text-muted`, texto `--color-text-strong` |
| `.badge--primary` | Destaque de ação/categoria | Fundo `--color-primary-soft`, ponto `--color-primary` |
| `.badge--success` | Estado positivo | Fundo `--color-success-soft`, ponto `--color-success` |
| `.badge--warning` | Atenção | Fundo `--color-warning-soft`, ponto `--color-warning` |
| `.badge--error` | Erro/falha | Fundo `--color-error-soft`, ponto `--color-error` |
| `.badge--info` | Informação | Fundo `--color-info-soft`, ponto `--color-info` |
| `.badge--counter` | Contador sólido (número, sem ponto) | Pílula `--color-primary`, texto `--color-on-primary` |
| `.badge--counter-soft` | Contador suave | Pílula `--color-primary-soft`, número `--color-primary` |

### Cards

| Classe | Uso |
|---|---|
| `.card` | Superfície básica (título + texto) |
| `.card--interactive` | Card clicável (hover eleva: `translateY(-space-1)` + `--shadow-md` + borda forte) |
| `.card__header` | Cabeçalho flex (título + badge/eyebrow lado a lado) |
| `.card__eyebrow` | Rótulo superior em caps (ex.: "Interativo") |
| `.card__title` | Título do card (`--font-size-h5`) |
| `.card__text` | Corpo (`--color-text-muted`) |
| `.card__footer` | Rodapé com ações, separado por borda superior; `margin-top: auto` ancora no fim |

### Alertas

| Classe | Uso | Acento lateral |
|---|---|---|
| `.alert` (base) | Neutro | `--color-border-strong` |
| `.alert--success` | Sucesso | `--color-success` |
| `.alert--error` | Erro | `--color-error` |
| `.alert--warning` | Aviso | `--color-warning` |
| `.alert--info` | Informação | `--color-info` |
| `.alert--closing` | Adicionado pelo `app.js` durante o fechamento (opacity 0 + translateY) | — |

Partes internas: `.alert__icon` (ícone colorido por variante), `.alert__content` (coluna), `.alert__title` (forte), `.alert__text`, `.alert__actions` (botões de ação), `.alert__close` (botão X).

## 3. Exemplos de uso mínimo

```html
<!-- Badge de status -->
<span class="badge badge--success">Ativo</span>
<span class="badge">Neutro</span>

<!-- Contador dentro de um botão -->
<button type="button" class="btn btn--secondary">
  Notificações
  <span class="badge badge--counter">3</span>
</button>

<!-- Card básico -->
<article class="card">
  <h3 class="card__title">Card simples</h3>
  <p class="card__text">Conteúdo do cartão.</p>
</article>

<!-- Card interativo: SEMPRE um <a> (ou elemento com papel de link) -->
<a class="card card--interactive" href="#detalhe">
  <p class="card__eyebrow">Interativo</p>
  <h3 class="card__title">Card clicável</h3>
  <p class="card__text">Eleva no hover.</p>
</a>

<!-- Alerta com título, texto e ação -->
<div class="alert alert--warning" role="alert">
  <svg class="alert__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" aria-hidden="true" focusable="false"><!-- triângulo --></svg>
  <div class="alert__content">
    <p class="alert__title">Sessão expirando</p>
    <p class="alert__text">Você será desconectado em 2 minutos.</p>
    <div class="alert__actions">
      <button type="button" class="btn btn--primary btn--sm">Continuar sessão</button>
    </div>
  </div>
  <button type="button" class="alert__close" aria-label="Fechar alerta">×</button>
</div>
```

## 4. Tokens usados

- **Badges:** `--color-surface-muted`, `--color-text-strong`, `--color-text-muted`, `--color-primary(-soft)`, `--color-success(-soft)`, `--color-warning(-soft)`, `--color-error(-soft)`, `--color-info(-soft)`, `--color-on-primary`, `--radius-full`, `--space-1/2`, `--font-size-caption`, `--font-weight-semibold`, `--font-line-height-tight`
- **Cards:** `--color-surface`, `--color-border(-strong)`, `--color-text(-muted)`, `--color-primary`, `--radius-lg`, `--shadow-sm/md`, `--space-2/4/6`, `--font-size-h5`, `--font-size-caption`, `--letter-spacing-wide`, `--motion-duration-base`, `--motion-easing-out`, `--focus-ring`
- **Alertas:** `--color-surface-muted`, `--color-border(-strong)`, `--color-success/error/warning/info` (+`-soft`), `--color-text(-strong/-muted)`, `--radius-md/full`, `--space-1/2/3/4`, `--font-size-small/caption`, `--font-weight-semibold`, `--motion-duration-fast`, `--motion-easing-out`, `--focus-ring`

## 5. Acessibilidade

- **Badges:** o ponto semântico é decorativo (`::before`); o texto do badge é o conteúdo real. Não use badge sozinho como única indicação de status — combine com texto ou `aria-label` quando necessário.
- **Cards interativos:** use `<a href>` (como no showcase). Se o card for clicável mas não um link (ex.: seleção), use `role="link"`/`tabindex="0"` + Enter ou um botão dentro do card — nunca `onclick` em `div` sem semântica.
- **Alertas:** escolha o papel ARIA pelo impacto — `role="alert"` (interrompe o leitor de tela, para **erro/aviso**) vs `role="status"` (anúncio polido, para **sucesso/info**). O showcase segue isso (`role="status"` em success/info, `role="alert"` em error/warning).
- **Fechar alerta:** o `.alert__close` precisa de `aria-label` ("Fechar alerta") — o conteúdo visível é só o X (SVG `aria-hidden`).
- **Contraste:** a cor semântica fica na barra/ícone (grafismo ≥ 3:1, WCAG 1.4.11); o texto usa `--color-text-strong`/`--color-text` — AA em ambos os temas.

## 6. Notas de implementação

1. **`badge--neutral` NÃO existe no CSS:** o HTML do showcase usa `class="badge badge--neutral"`, mas `components.css` não define `.badge--neutral` — o badge neutro é o `.badge` puro. A classe extra é inócua; não dependa dela em produção.
2. **O fechamento de alerta é animado e remove o nó:** `initDemoAlerts()` no `app.js` adiciona `.alert--closing` e remove o elemento após ~130ms (`--motion-duration-fast`). Em produção, se o alerta for re-exibido (ex.: erro repetido), recrie o nó em vez de reutilizar o removido.
3. **O `--danger` do alerta usa fundo "soft" + texto forte**, diferente do botão `--danger` (fundo sólido + `--color-surface`). Não generalize: são padrões propositalmente distintos (alerta = contexto passivo, botão = ação).
4. **Card `--interactive` com `border-radius` no foco:** `:focus-visible` restaura `--radius-lg` e empilha `--focus-ring, var(--shadow-md)`; se o card mudar de raio em algum ponto, o anel não acompanha (mesma pegadinha dos pills de botão — resolvida no base com `inherit` onde aplicável).
5. **`.alert__close` usa `color-mix` no hover** (`color-mix(in srgb, var(--color-text) 8%, transparent)`) — navegadores pré-2023 degradam para o fundo transparente (ainda funcional, sem hover visual).
