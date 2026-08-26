# Inputs Compartilhados dos Experimentos

> Mesmo input para os 3 métodos (A=Design Kit, B=impeccable, C=design-taste). Os corridores NÃO podem alterar este arquivo.

## E1 — Landing page (Persuade)

**Brief (idêntico para A, B, C):**

Produto: **Draftly** — SaaS de gestão de freelancers (propostas, contratos, faturamento e onboarding de clientes em um lugar).

- Público: freelancers de design, dev e escrita (individual, não a agências).
- Proposta: "fecha proposta, assina contrato e cobra sem sair do fluxo de trabalho".
- Tom: calmo, ferramental, confiável. Não-babar; não-empresarial-corporativo.
- Seções: hero, features (3-4), como funciona (3 passos), depoimentos (2-3), pricing (3 planos), CTA final + footer.
- Idioma: pt-BR (comente que é pt-BR). Nomes de pessoas reais pt-BR.
- Zero lorem ipsum; números coerentes (preços em R$).
- O artefato deve ser HTML+CSS auto-contido (1 arquivo) que abre no navegador. Sem build.
- Restrições anti-slop (valem igual p/ os 3): zero em-dash/en-dash visível; zero Inter como fonte; sem gradiente roxo de IA; sem 3 cards idênticos; sem fake screenshot de div; contraste AA; mobile-first; sem scroll cues; sem version footer; pessoas/nomes reais.

## E2 — Dashboard (Operate)

**Brief (idêntico):**

Produto: **NorteMetrics** — dashboard financeiro para PMEs.

- Público: dono de pequena empresa não-técnico.
- Telas: visão geral com 4 KPIs (receita, despesas, a receber, margem), gráfico de fluxo de caixa (6 meses), tabela de transações recentes (10 linhas, dados fictícios coerentes em R$), alerta de 1 item (fatura vencendo), um filtro por período.
- Idioma pt-BR. Números coerentes (totais batem).
- Artefato HTML+CSS auto-contido. Sem build.
- Restrições anti-slop idênticas ao E1 + tabela acessível (caption/aria), estados (vazio/loading opcional), alinhamento numérico.

## E3 — Critique de UI

**Input:** a mesma UI para os 3 — `docs/casos/redesign-demo/before.html` (landing "Cloudly" com tells de IA: em-dash, Inter, gradiente roxo, 3 cards iguais, fake screenshot, nomes genéricos, scroll cue, version footer, eyebrow em toda seção).

**Entregar:** critique report em pt-BR com: heurísticas pontuadas (1-5), problemas com severidade e localização, verificação de tells de IA (listar quais achou). Não editar a UI. Não salvar além do report.

## E4 — Redesign (preservar marca)

**Input:** a mesmíssima `docs/casos/redesign-demo/before.html` do E3.

**Brief:** redesenhar preservando conteúdo/IA (mesmas seções, nav, CTA labels), mas removendo os tells; nova linguagem visual; identidade de marca "Cloudly" (nome preservado). Entregar `after.html` + `redesign.css` (auto-contido) + 1 relatório curto do que mudou e o que preservou. pt-BR.

## E5 — Auditoria a11y + anti-slop

**Input:** a mesmíssima landing gerada por **A (Design Kit)** no E1 (`e1-a.html`). Os 3 métodos auditam a mesma página.

**Entregar:** relatório a11y (WCAG 2.2 AA: contraste, foco, teclado, semântica, ARIA) + scan anti-slop (em-dash, hex, Inter, fake screenshots, nomes genéricos, eyebrows) com localização e severidade. NÃO editar a página. Não rodar o kit (sem acesso aos scripts) — inspeção estática.