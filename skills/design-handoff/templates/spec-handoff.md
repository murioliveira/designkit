# Spec de handoff

> Template por tela — preencha um bloco por tela. Toda cor/tipo/espaçamento referencia tokens de styles/tokens.css.

## Tela: [nome] · Arquivo: [caminho] · Prioridade: [P0/P1/P2]

### Objetivo

[Tarefa do usuário que esta tela resolve — 1–2 linhas]

### Layout

- Estrutura: [blocos, ordem no fluxo]
- Container/grid: [`--container-*`, breakpoints usados]
- Responsivo: [comportamento por breakpoint: sm/md/lg/xl]

### Componentes usados

| Componente | Variante | Estados (hover/active/focus/disabled) |
|---|---|---|
| [ex.: button] | [primary/lg] | [hover: --color-primary-hover; focus: --focus-ring] |

### Tokens aplicados

| Categoria | Tokens |
|---|---|
| Cor | [`--color-bg`, `--color-primary`, ...] |
| Tipografia | [`--font-family-heading`, `--font-size-display`, ...] |
| Espaçamento | [escalas usadas] |
| Raio/Sombra | [`--radius-*`, `--shadow-*`] |
| Motion | [`--motion-duration-*`, `--motion-easing-*`] |
| Z-index | [`--z-*`] |

### Estados e bordas

| Estado | Ocorre quando | Comportamento |
|---|---|---|
| Vazio | [condição] | [o que mostra] |
| Erro | [condição] | [mensagem + token --color-error] |
| Carregando | [condição] | [skeleton/spinner] |
| Sucesso | [condição] | [confirmação] |

### Acessibilidade

- Contraste: [atendido? Níveis]
- Foco visível: [--focus-ring aplicado onde]
- ARIA/teclado: [roles, tab order, atalhos]

### Dependências

- Assets: [SVG inline, imagens, ícones]
- Dados: [mock/API]
- Integrações: [formulários, autenticação, etc.]

### Proposta de componente/token novo (se aplicável)

- **Nome:** [ex.: `--color-brand-accent` ou componente `stepper`]
- **Anatomia:** [blocos internos]
- **Variantes/estados:** [...]
- **Tokens usados:** [...]
- **Status:** `[proposta — aguardando aprovação]`

---

## Checklist de aceite (dev)

- [ ] Funcional: [fluxo principal completo]
- [ ] Estados: vazio/erro/carregando/sucesso implementados
- [ ] Visual: cores/tipos/espaçamento 100% via tokens (sem hex hardcoded)
- [ ] Responsivo: ok em [sm/md/lg/xl]
- [ ] A11y: contraste AA, foco visível, navegação por teclado, ARIA
- [ ] Motion: respeita `prefers-reduced-motion`
