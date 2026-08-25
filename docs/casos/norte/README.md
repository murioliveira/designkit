# Caso Norte — Dashboard de gestão financeira (Fase A, prova de conceito 2)

> **Objetivo da prova:** validar o reuso dos componentes avançados do kit (dropdown, breadcrumb, tabela, paginação, stepper, tabs, modal) num caso real de UI densa — um dashboard — e verificar que `components.css` é consumível de fora do showcase sem depender de `js/app.js` da raiz.
> **Produto fictício:** Norte — gestão financeira para pequenas empresas (contas a pagar/receber, fluxo de caixa).
> **Arquivos:** `index.html` + `dashboard.css` + este relatório, em `docs/casos/norte/`.

---

## 1. Brief

Dashboard de fluxo de caixa para pequenas empresas. O usuário precisa ver, em uma tela:

1. **Situação imediata** — saldo disponível, a receber, a pagar e inadimplência (cards de métrica).
2. **Tendência** — gráfico do fluxo de caixa com granularidade variável (Semana/Mês/Trimestre).
3. **Lançamentos** — tabela de transações com status, valores em BRL e paginação (5 páginas, 28 transações).
4. **Ações de contexto** — menu de ações do relatório (exportar/imprimir/arquivar) e detalhe de transação em modal.
5. **Estado vazio real** — filtro de busca que demonstra a linha `.table__empty`.
6. **Progresso** — stepper de onboarding (ativação do plano anual).

Requisitos de qualidade: pt-BR, zero lorem ipsum, contraste AA nos dois temas, teclado completo (tabs com setas, dropdown com Esc/clique fora, modal com trap de foco), responsivo (tabela com `overflow-x`).

## 2. Decisões (10 linhas)

1. **Auto-contido, reusando o kit via `<link>`:** `index.html` carrega `tokens.css` + `base.css` + `components.css` (da raiz) e só o layout do caso em `dashboard.css` — prova que o kit é consumível fora do showcase.
2. **Não carrega `layout.css` nem `app.js` da raiz:** header, theme-toggle, skip-link e footer foram replicados em `dashboard.css` com os mesmos padrões (mecanismo `dk-theme`, `sr-only-focusable`), mantendo o caso portátil.
3. **Interações reescritas num script auto-contido pequeno** com os MESMOS padrões ARIA do `app.js` do kit (dropdown `aria-expanded/controls`, tabs roving tabindex + setas + Home/End, modal `role=dialog` + `aria-modal` + trap de foco + Esc + devolução de foco ao gatilho) — para o caso funcionar sem o app da raiz.
4. **Gráfico em SVG puro** com `role="img"` + `aria-label` descritivo por período; `aria-hidden="true"` nos elementos decorativos; cores só via `var(--...)` (inclusive dentro do SVG).
5. **Tabela** reusa `.table`/`.table--zebra`/`.table__num` (dígitos tabulares) com `aria-describedby` apontando para o `caption`; estado vazio = `<tbody hidden>` alternado com `.table__empty` (colspan 6) via filtro JS.
6. **Paginação** reusa `.pagination` com `aria-current="page"` na página 1 e `aria-disabled="true"` na seta anterior; links apontam para `#transacoes` (demo estática, sem recarregar dados).
7. **Breadcrumb** reusa `.breadcrumb__list` com `aria-current="page"` no item atual; separador `/` vem do CSS (não é texto no HTML).
8. **Stepper** reusa `.stepper--vertical` com `aria-current="step"` no passo ativo; check SVG nos passos concluídos; nota de valor (R$ 588,00 anual) em texto real.
9. **Modal de detalhe** usa o padrão estrutural do kit (`[hidden]`, backdrop com `data-modal-close`, `aria-labelledby` + `aria-describedby`) e `body.no-scroll` durante a abertura.
10. **Números realistas em BRL** (R$ 48.230,00 saldo, R$ 312,00 fatura vencida, R$ 2.140,00 inadimplência) com datas de agosto/2026; alerta de erro (fatura #4817) e alerta de info (importação concluída).

## 3. Critique simulado (design-critic)

| Heurística | Nota | Observação |
|---|---|---|
| Clareza de comunicação | 4/5 | Painéis legíveis de imediato; modal de detalhe exibia dados da primeira linha para todas as transações (P1 — corrigido neste refine). |
| Hierarquia visual | 5/5 | Métricas primeiro (situação), depois tendência, depois lançamentos — ordem natural de leitura; `table__num` alinha valores. |
| Consistência com o kit | 5/5 | Todos os componentes reusados por classe do kit; zero hex/valor mágico fora do dashboard.css (valores fora de escala documentados em comentário). |
| Affordance / interação | 4/5 | Dropdown com teclado completo, tabs com setas, modal com trap de foco, estado vazio com "Limpar filtro"; setas do dropdown com menu aberto no gatilho focavam item errado (P2 — corrigido). |
| Acessibilidade | 4/5 | Landmarks, skip-link, `aria-labelledby`, `role=alert`/`role=status`; contrastes na fronteira do AA no claro (ver abaixo). |
| Responsividade | 5/5 | Métricas 4→2→1 colunas (`--breakpoint-lg/md`), tabela com `overflow-x` (`.table-wrap` do kit), header com wrap. |
| Qualidade da copy | 5/5 | Zero lorem ipsum; rótulos com verbo de ação ("Pagar agora", "Continuar para pagamento"). |
| **Média** | **4.6/5** | **APROVADO COM RESSALVAS** — critique real em `critique-report.md`; P1 e P2 corrigidos no refine. |

### Verificações do critique

- **Tokens:** todos os `var(--...)` usados em `index.html` + `dashboard.css` existem em `tokens.css` (verificação automatizada em `scripts/smoke-test.py`).
- **Contraste AA (tema claro, pares críticos):** `--color-success` (#16a34a) sobre `--color-surface` — usado só em badges com texto `--color-text-strong`; badge Pago tem fundo `--color-success-soft` + texto `--color-text-strong` (≥ 7:1). `--color-error` (#dc2626) em texto sobre superfície = **4.5:1** (limite AA, usado em rótulos grandes/títulos). `--color-text-muted` (#64748b) sobre `--color-surface` = **4.55:1** ✓ (texto pequeno aceito, ≥ 4.5:1). Seta de paginação `aria-disabled` com `--color-text-muted` sobre `--color-surface-muted` = **4.34:1** ✓ (elemento gráfico, critério 1.4.11 exige ≥ 3:1). Dot do badge success ≈ **3.0:1** (gráfico, ≥ 3:1 ✓). No tema escuro todos os pares sobem (superfície #0f172a, textos claros).
- **Teclado:** dropdown abre com Enter/Espaço/↑/↓, navega com setas/Home/End, fecha com Esc (devolve foco) e clique fora; tabs com setas + Home/End (roving tabindex); modal com trap de foco + Esc + devolução de foco ao gatilho; skip-link com `tabindex="-1"` no `main`.
- **Semântica:** `role="dialog" aria-modal="true"` no modal; `role="tablist/tab/tabpanel"`; `role="menu/menuitem"`; `role="separator"` no divisor do dropdown; badges como texto (não `aria-hidden`).

## 4. Handoff

### Componentes do kit reutilizados (via `../../../styles/components.css`)

| Componente | Classes usadas | Como | Seção do components.css |
|---|---|---|---|
| Botões | `.btn`, `.btn--primary`, `.btn--ghost`, `.btn--danger`, `.btn--sm` | Ações, ferramentas, alertas, modal | §1 (29–190) |
| Badges | `.badge`, `.badge--success`, `.badge--warning`, `.badge--error` | Status da tabela + métricas | §2 (199–291) |
| Cards | `.card` | Métricas (4 cards) | §3 (299–366) |
| Alertas | `.alert`, `.alert--error`, `.alert--info`, `.alert__icon`, `.alert__title`, `.alert__text`, `.alert__actions` | 2 alertas da página | §4 (375–484) |
| Forms (ícone) | `.input-wrap`, `.input-wrap__icon`, `.input`, `.input--with-icon` | Busca da tabela | §7 (667–724) |
| Overlays — modal | `.modal`, `.modal__backdrop`, `.modal__dialog`, `.modal__header`, `.modal__title`, `.modal__close`, `.modal__body`, `.modal__footer` | Detalhe da transação | §8.2 (1153–1267) |
| Overlays — tabs | `.tabs__list`, `.tabs__tab`, `.tabs__panel` | Período do gráfico | §8.3 (1275–1319) |
| Dropdown | `.dropdown`, `.dropdown--align-end`, `.dropdown__trigger`, `.dropdown__chevron`, `.dropdown__menu`, `.dropdown__item`, `.dropdown__item--danger`, `.dropdown__check`, `.dropdown__separator` | Ações do relatório | §9.1 (1538–1641) |
| Breadcrumb | `.breadcrumb__list`, `.breadcrumb__item`, `.breadcrumb__link`, `.breadcrumb__current` | Trilha da página | §9.2 (1651–1695) |
| Tabela | `.table-wrap`, `.table`, `.table--zebra`, `.table__caption`, `.table__num`, `.table__empty` | Transações + estado vazio | §9.3 (1709–1774) |
| Stepper | `.stepper`, `.stepper--vertical`, `.stepper__step`, `.stepper__step--done`, `.stepper__step--active`, `.stepper__marker`, `.stepper__check`, `.stepper__label` | Onboarding do plano | §9.4 (1785–1886) |
| Paginação | `.pagination`, `.pagination--sm`, `.pagination__list`, `.pagination__link`, `.pagination__arrow` | 5 páginas da tabela | §9.5 (1897–1988) |

**12 grupos de componentes do kit reutilizados** — o dashboard não define nenhuma classe de componente, só layout de página (`.dash*`, `.metric*`, `.panel*`, `.chart*`, `.det*`, `.table-tools`, `.stepper__note`) e o shell mínimo (header/toggle/footer/skip-link) replicado do padrão do kit.

### Tokens usados (amostra)

Cores `--color-primary/-soft/-soft-strong/-on-primary`, `--color-success/-warning/-error/-info` + `-soft`, `--color-bg/surface/surface-muted`, `--color-text/-strong/-muted`, `--color-border/-strong` · Tipografia `--font-size-*`, `--font-weight-*`, `--font-line-height-*`, `--letter-spacing-*`, `--font-family-*` · Espaçamento `--space-1..16` · Raios `--radius-md/lg/full` · Sombras `--shadow-md/xl` (via componentes) · Motion `--motion-duration-*`, `--motion-easing-*` · Z `--z-sticky/-dropdown/-modal/-toast` · Layout `--container-xl`, `--breakpoint-md/lg`.

### Melhor componente no reuso

**Dropdown (§9.1)** — funcionou melhor: com o CSS do kit e ~40 linhas de script replicando os padrões ARIA do `app.js` (abrir no clique/Enter/Espaço/↑/↓, navegar com setas/Home/End, fechar com Esc/clique fora/Tab, devolver foco ao gatilho), o menu de ações ficou completo e acessível sem tocar no kit. A estrutura `[data-dropdown]` + `aria-controls` + `[hidden]` do kit torna o componente plug-and-play: o JS do caso só orquestra ARIA, o visual é 100% do CSS do kit. Em segundo lugar, a **tabela + paginação** — `table--zebra`/`table__num`/`table__empty` cobriram estado denso, vazio e numérico sem override nenhum.
