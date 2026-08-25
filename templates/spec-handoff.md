# Spec de Handoff (referência rápida)

> Template compacto do design-handoff — versão completa em skills/design-handoff/templates/spec-handoff.md.

## Tela: [nome] · Arquivo: [caminho] · Prioridade: [P0/P1/P2]

**Objetivo:** [tarefa do usuário]

**Layout:** [blocos; containers `--container-*`; comportamento por breakpoint sm/md/lg/xl]

**Componentes usados:**

| Componente | Variante | Estados |
|---|---|---|
| [ex.: button] | [primary] | hover `--color-primary-hover` · focus `--focus-ring` · disabled |

**Tokens aplicados:**

| Categoria | Tokens |
|---|---|
| Cor | [`--color-*`] |
| Tipografia | [`--font-*`] |
| Espaço/raio/sombra | [`--radius-*`, `--shadow-*`] |
| Motion/z | [`--motion-*`, `--z-*`] |

**Estados:** vazio [quando/como] · erro [mensagem + `--color-error`] · carregando [skeleton] · sucesso [confirmação]

**A11y:** contraste AA [sim/não] · foco `--focus-ring` [onde] · ARIA/teclado [detalhes]

**Dependências:** [assets, dados mock, integrações]

**Proposta nova (se aplicável):** [nome · anatomia · variantes · status: aguardando aprovação]

## Checklist de aceite (dev)

- [ ] Funcional: fluxo principal completo
- [ ] Estados: vazio/erro/carregando/sucesso
- [ ] Visual: 100% tokens (sem hex hardcoded)
- [ ] Responsivo: sm/md/lg/xl
- [ ] A11y: AA, foco, teclado, ARIA
- [ ] Motion: respeita `prefers-reduced-motion`
