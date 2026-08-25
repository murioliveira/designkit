# Spec de handoff — Brisa

> Produzido pelo **design-handoff** seguindo `skills/design-handoff/SKILL.md` + template `spec-handoff.md`.
> **Regra do produto:** toda cor/tipo/espaçamento referencia tokens de `styles/tokens.css` (fonte de verdade). Tokens confirmados lendo `styles/tokens.css` (lista atual, 2026-08-25).
> **Caso:** Brisa · **Tela:** card de assinatura do café (/planos) · **Prioridade:** P0

## Tela: Card de assinatura do café · Arquivo: `ui/planos.html` (proposto) · Prioridade: P0

### Objetivo

Resolver a fase crítica da jornada de Marina (Decisão — o "aha"): entender região escolhida, preço e frequência, e **assinar com a tranquilidade de poder pausar depois** (dor nº 1 da persona). É a tela que converte o diferencial do produto (origem visível + pausa sem atrito).

### Layout

- Estrutura: card em grid — [topo: selo de origem + região + foto do produtor] → [meio: preço/entrega + seletor de frequência/quantidade] → [rodapé: CTA primário + botão secundário de pausa + link "como funciona"].
- Container/grid: `--container-sm` para o card em coluna única; grade de planos em `--container-lg` (3 cards, `--breakpoint-lg`).
- Responsivo: 1 coluna em `--breakpoint-sm/md`; 3 cards lado a lado em `--breakpoint-lg/xl`; card cresce, ordem dos blocos mantida.

### Componentes usados

| Componente | Variante | Estados (hover/active/focus/disabled) |
|---|---|---|
| button | primary/lg (CTA "Assinar Cerrado mensal") | hover: `--color-primary-hover`; active: `--color-primary-active`; focus: `--focus-ring` |
| button | secondary (Pausar quando quiser) | hover: `--color-surface-muted`; focus: `--focus-ring` |
| badge | success ("Origem verificada") | dot `--color-success` |
| stepper | quantidade/frequência (kit §stepper) | active: `--color-primary-soft-strong` (após critique) |
| card | padrão do kit | `--radius-lg`, `--shadow-md` |

### Tokens aplicados

| Categoria | Tokens |
|---|---|
| Cor | `--color-bg`, `--color-surface`, `--color-surface-muted`, `--color-primary`, `--color-primary-hover`, `--color-primary-active`, `--color-primary-soft`, `--color-primary-soft-strong`, `--color-success`, `--color-text`, `--color-text-strong`, `--color-text-muted`, `--color-border`, `--color-border-strong` |
| Tipografia | `--font-family-base`, `--font-family-heading`, `--font-size-h2` (região), `--font-size-body` (preço), `--font-size-caption` (selo), `--font-size-small` (pausa), `--font-weight-semibold`/`--font-weight-bold`, `--font-line-height-tight`/`--font-line-height-body`, `--letter-spacing-tight` |
| Espaçamento | `--space-3`, `--space-4`, `--space-5`, `--space-6`, `--space-8`, `--space-12` |
| Raio/Sombra | `--radius-lg`, `--radius-md`, `--radius-full` (badge), `--shadow-md`, `--shadow-sm` |
| Motion | `--motion-duration-fast` (hover), `--motion-easing-out` (transições) |
| Z-index | `--z-base` (conteúdo), `--z-sticky` (header do /planos) |

### Estados e bordas

| Estado | Ocorre quando | Comportamento |
|---|---|---|
| Vazio | Região sem cafés disponíveis | Card com mensagem + sugestão de região próxima; botão desabilitado |
| Erro | Falha ao assinar (pagamento) | Mensagem `--color-error` + alert do kit; card permanece preenchido |
| Carregando | Buscando planos/pagamento | Skeleton do card (kit) + botão com spinner |
| Sucesso | Assinatura confirmada | Badge "Assinatura ativa" + redirect para /conta com próximo envio |
| Pausada | Marina pausou | Badge "Pausada até [data]" + botão "Reiniciar" no lugar do CTA |

### Acessibilidade

- Contraste: pares verificados AA — texto em `--color-text` sobre `--color-surface` (≥4.5:1); selo em `--color-text` (não muted); stepper ativo com `--color-primary-soft-strong` (após critique) ≥3:1 para grafismo.
- Foco visível: `--focus-ring` em todos os botões/stepper; `:focus-visible` (não `:focus` global).
- ARIA/teclado: botões reais `<button>`; stepper com `aria-valuenow`/`aria-valuemin`/`aria-valuemax` e setas; erro com `role="alert"` + `aria-describedby`; tab order: região → preço → seletor → CTA → pausa.
- Motion: `prefers-reduced-motion` desativa transições de hover.

### Dependências

- Assets: foto do produtor/região (SVG inline ou imagem otimizada), ícones do kit (check do selo).
- Dados: mock de planos (região, preço, frequência, quantidade), endpoint futuro de assinatura.
- Integrações: checkout de pagamento (mock na v1), endpoint de pausa/reinício.

### Proposta de componente/token novo (se aplicável)

- **Nome:** `--color-*` nenhum; **componente**: selo de origem (composição de `badge` + ícone de check) — reutilizável.
- **Anatomia:** `[ícone check] [texto "Origem verificada"] [região]`.
- **Variantes/estados:** success (verificada) / neutral (pendente de verificação).
- **Tokens usados:** `--color-success`, `--color-text`, `--space-2`, `--radius-full`.
- **Status:** `[proposta — aguardando aprovação]` (não entra no kit sem aprovação humana, regra do produto).

---

## Checklist de aceite (dev)

- [ ] Funcional: assinar (região + frequência + quantidade) → confirmação em /conta
- [ ] Funcional: pausar/reiniciar assinatura em ≤2 cliques (dor nº 1 da Marina)
- [ ] Estados: vazio/erro/carregando/sucesso/pausada implementados
- [ ] Visual: cores/tipos/espaçamento 100% via tokens (sem hex hardcoded)
- [ ] Responsivo: ok em sm/md/lg/xl (1 coluna → 3 cards)
- [ ] A11y: contraste AA, foco visível, teclado (stepper), ARIA (role=alert)
- [ ] Motion: respeita `prefers-reduced-motion`
