# Tabela (`.table`)

> Grupo 9.3 de `styles/components.css`. Dados tabulares com zebra, alinhamento numérico, header fixo e estado vazio. Sem JS.

## 1. Visão geral

Tabela de dados com três necessidades cobertas:

1. **Responsividade** — `.table-wrap` rola horizontalmente em telas estreitas (sem quebrar o layout da página).
2. **Legibilidade** — zebra opcional, alinhamento numérico tabular e header fixo em containers com rolagem vertical.
3. **Estados** — linha de "vazio" com `colspan` para resultados ausentes.

Acessibilidade é responsabilidade do HTML: `<caption>` (visível ou `sr-only`) ou `aria-label` na tabela, `scope` em todos os cabeçalhos.

## 2. Estrutura e classes

| Classe / atributo | Papel |
|---|---|
| `.table-wrap` | Container com `overflow-x: auto` (rolagem horizontal no mobile) |
| `.table-wrap--sticky` | Container com altura máxima e rolagem vertical; header fixo |
| `.table` | Tabela base (largura total, bordas discretas) |
| `.table--zebra` | Linhas alternadas com `--color-surface-muted` |
| `.table__caption` | `caption` visível estilizada |
| `.table__num` | Alinhamento à direita + `font-variant-numeric: tabular-nums` |
| `.table__empty` | Célula do estado vazio (com `colspan`) |
| `thead th` | Cabeçalhos com `scope="col"`; sticky dentro do container |

## 3. Exemplo de uso mínimo

```html
<div class="table-wrap">
  <table class="table table--zebra">
    <caption class="table__caption">Projetos ativos — horas por semana</caption>
    <thead>
      <tr>
        <th scope="col">Projeto</th>
        <th scope="col" class="table__num">Horas</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Lumen</th>
        <td class="table__num">128</td>
      </tr>
    </tbody>
  </table>
</div>
```

Header fixo e estado vazio:

```html
<div class="table-wrap table-wrap--sticky">
  <table class="table" aria-label="Registros de auditoria">
    <thead>…</thead>
    <tbody>…linhas…</tbody>
  </table>
</div>

<!-- Estado vazio -->
<tr>
  <td class="table__empty" colspan="4">Nenhum projeto encontrado para os filtros aplicados.</td>
</tr>
```

## 4. Tokens usados

- **Cor:** `--color-surface` (fundo do header fixo), `--color-surface-muted` (zebra), `--color-border` (linhas), `--color-border-strong` (linha do thead), `--color-text-strong` (cabeçalho), `--color-text-muted` (caption/vazio)
- **Espaçamento:** `--space-2` / `--space-3` (padding das células), `--space-8` (padding do vazio)
- **Tipografia:** `--font-size-small` (células), `--font-size-caption` (caption), `--font-weight-semibold` (thead), `--font-line-height-tight`

## 5. Acessibilidade

- **Nome da tabela:** `<caption>` visível (recomendado) ou `aria-label` — nunca os dois ao mesmo tempo; caption `sr-only` quando o título já está na página.
- **`scope` em todos os cabeçalhos:** `scope="col"` no thead e `scope="row"` na primeira célula de cada linha (dados hierárquicos).
- **Números tabulares:** `font-variant-numeric: tabular-nums` impede que os dígitos "dançem" ao atualizar — melhor para leitura de colunas numéricas.
- **Estado vazio:** a célula com `colspan` (número total de colunas) mantém o alinhamento da tabela e anuncia "nenhum resultado" no fluxo natural.
- **Rolagem horizontal:** o container `overflow-x: auto` é acessível por teclado/mouse; para tabelas muito largas considere uma versão empilhada em cards no mobile (fora do escopo deste componente).

## 6. Notas de implementação

1. **Sticky header exige o container com altura:** `.table-wrap--sticky` define `max-height` + `overflow-y: auto`; sem container com rolagem o `position: sticky` não tem efeito.
2. **`z-index: 1` no thead sticky** garante que as linhas zebradas rolem sob o cabeçalho; o fundo do thead é `--color-surface` (sólido nos dois temas).
3. **Não use `colspan` mágico:** o valor precisa ser exatamente o número de colunas do thead, senão a linha vazia desalinha.
4. **Zebra + sticky:** a zebra (`nth-child(odd)`) aplica-se às linhas do corpo; o cabeçalho permanece com fundo sólido — comportamento correto por construção.
5. **Tabelas de dados vs. layout:** este componente é só para dados tabulares; layout de página deve usar grid/flex (nunca tabela).
