# Export de Tokens — Design Kit

Export automático dos design tokens do Design Kit (`styles/tokens.css`, a
fonte de verdade) para formatos consumíveis por ferramentas, apps e outros
agentes.

## Arquivos

| Arquivo | O que é |
|---|---|
| `tokens/tokens.json` | Todos os tokens **semânticos**, estruturados por tema (`light`/`dark`) e por categoria (`color`, `typography`, `spacing`, `radius`, `shadow`, `motion`, `z`). Valores `var(--...)` **resolvidos** para o valor final onde possível. |
| `tokens/tokens.css` | Cópia nomeada de `styles/tokens.css` — import direto em projetos (sem dependências relativas). |

## Como usar

- **JSON (`tokens.json`)** — para ferramentas de design, geradores de código,
  extensões, ou consumo programático. Exemplo de leitura:

  ```python
  import json
  t = json.load(open("tokens/tokens.json", encoding="utf-8"))
  bg_claro = t["light"]["color"]["--color-bg"]      # -> "#f8fafc"
  focus_dark = t["dark"]["shadow"]["--focus-ring"]  # -> "0 0 0 3px rgb(129 140 248 / 0.6)"
  ```

  Estrutura por tema: cada `light`/`dark` tem as 7 categorias
  (`color`, `typography`, `spacing`, `radius`, `shadow`, `motion`, `z`) e a
  chave `$unresolved` (lista de tokens cujo valor manteve `var()` — vazia no
  export atual). Em cada categoria as chaves são os nomes dos tokens
  (`--color-bg`) e os valores são strings resolvidas.

- **CSS (`tokens.css`)** — para projetos CSS/HTML que querem usar os tokens
  diretamente: `@import url("tokens/tokens.css");` (ou copie o arquivo).
  Inclui paleta bruta, tipografia, escala de espaçamento, raios, sombras,
  motion, z-index, layout e os dois temas (claro em `:root`, escuro em
  `[data-theme="dark"]` + fallback `prefers-color-scheme`).

## Temas

- `light` = bloco `:root` de `styles/tokens.css`.
- `dark` = bloco `[data-theme="dark"]` — no CSS o dark **herda** os tokens
  não sobrescritos do claro (cascata); no JSON o tema `dark` lista apenas os
  tokens que o bloco define. O bloco `@media (prefers-color-scheme: dark)` é
  um fallback duplicado do dark e não é exportado.
- Tokens **fora** do export (infra do próprio CSS, não semânticos): paleta
  bruta (`--c-*`) e layout (`--container-*`, `--breakpoint-*`) — parseados
  para resolução de `var()`, mas não listados no JSON (estão no
  `tokens/tokens.css`).

## Regenerar

```bash
python scripts/export-tokens.py
```

O script lê `styles/tokens.css` (fonte de verdade), gera `tokens/tokens.json`
e `tokens/tokens.css`, e imprime as contagens (exportados / resolvidos /
não-resolvidos). Nenhuma dependência além do Python 3 stdlib.

## Integração com as skills

A skill `design-handoff` referencia este export na seção "Exportar tokens"
(etapa 4 do fluxo de handoff): quando o pacote de handoff pedir tokens, rode
o script e inclua `tokens/tokens.json` no pacote.