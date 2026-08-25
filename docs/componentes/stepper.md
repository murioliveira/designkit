# Stepper (`.stepper`)

> Grupo 9.4 de `styles/components.css`. Progresso por etapas com conector visual, horizontal e vertical. Sem JS.

## 1. Visão geral

O stepper comunica em que etapa de um fluxo (checkout, inscrição, wizard) o usuário está. Estados por passo: **concluído** (check + conector preenchido), **ativo** (`aria-current="step"`) e **pendente** (upcoming). O conector entre passos é desenhado por `::after` — não existe no HTML.

## 2. Estrutura e classes

| Classe / atributo | Papel |
|---|---|
| `.stepper` | `ol` do fluxo (`aria-label` descreve o processo) |
| `.stepper__step` | `li` do passo (flex: 1 no horizontal) |
| `.stepper__step--done` | Passo concluído (marcador sólido primário + check) |
| `.stepper__step--active` | Passo atual (`aria-current="step"` no `li`) |
| `.stepper__marker` | Círculo com número (ou check quando concluído) |
| `.stepper__check` | Ícone de check dentro do marcador concluído |
| `.stepper__label` | Nome do passo (caption, forte quando done/active) |
| `.stepper--vertical` | Variante em coluna com conector à esquerda |

## 3. Exemplo de uso mínimo

```html
<ol class="stepper" aria-label="Progresso da inscrição">
  <li class="stepper__step stepper__step--done">
    <span class="stepper__marker" aria-hidden="true">
      <svg class="stepper__check" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"/>
      </svg>
    </span>
    <span class="stepper__label">Conta</span>
  </li>
  <li class="stepper__step stepper__step--active" aria-current="step">
    <span class="stepper__marker" aria-hidden="true">3</span>
    <span class="stepper__label">Pagamento</span>
  </li>
  <li class="stepper__step">
    <span class="stepper__marker" aria-hidden="true">4</span>
    <span class="stepper__label">Confirmação</span>
  </li>
</ol>
```

Vertical: `class="stepper stepper--vertical"` (mesma estrutura interna).

## 4. Tokens usados

- **Cor:** `--color-surface` (marcador), `--color-surface` + `--color-border-strong` (borda do marcador), `--color-primary` (done/active e conector preenchido), `--color-on-primary` (check), `--color-text-muted` (upcoming), `--color-text-strong` (labels done/active), `--color-border` (conector)
- **Raio:** `--radius-full` (marcador)
- **Espaçamento:** `--space-2` (gap marker↔label), `--space-10` (marcador 2.5rem), `--space-5` (metade do marcador), `--space-6` (gap vertical)
- **Tipografia:** `--font-size-small` (número), `--font-size-caption` (label), `--font-weight-bold` (número), `--font-weight-semibold` (labels done/active)

## 5. Acessibilidade

- **`aria-current="step"`** no `li` ativo comunica a posição no fluxo.
- **Marcador decorativo:** `aria-hidden="true"` no `.stepper__marker` (número/check não são lidos); o nome do passo vem do `.stepper__label`.
- **`aria-label` no `ol`** descreve o processo ("Progresso da inscrição") — o landmark list ganha um nome.
- **Estado completo via texto:** done/active/pendente são diferenciados também por texto (check, número, cor + label forte), não só por cor — o estado é compreensível em leitores de tela pelo `aria-current` + conteúdo.
- **Contraste:** marcador done usa `--color-on-primary` sobre `--color-primary` (AA nos dois temas); o conector é decorativo (não carrega informação sozinho).

## 6. Notas de implementação

1. **O conector é puramente visual:** `::after` de `.stepper__step:not(:last-child)` — se um passo for um link, o conector ainda funciona (posicionado no `li`, não no link).
2. **Geometria do conector horizontal:** `top: calc(var(--space-5) - 1px)` centraliza a linha no marcador de 2.5rem; `left: calc(50% + var(--space-5))` + `width: calc(100% - var(--space-10))` fazem a linha ir do centro deste marcador ao centro do próximo — não altere sem recalcular.
3. **Vertical com 4+ passos:** o `max-width: 16rem` evita linhas de label muito longas; labels quebram em várias linhas mantendo o conector alinhado ao marcador.
4. **Passos clicáveis:** se os passos anteriores forem navegáveis, envolva o conteúdo do `li` em `<a>` (o conector continua no `li`); adicione `:focus-visible` com o anel do kit ao link.
5. **Não use stepper para progresso contínuo** (ex.: porcentagem de upload) — para isso existe `.progress` (seção 8.4).
