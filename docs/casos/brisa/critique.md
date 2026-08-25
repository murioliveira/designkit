# Critique — Brisa

> Produzido pelo **design-critic** seguindo `skills/design-critic/SKILL.md` (wrapper; fallback embutido aplicado — `impeccable` não carregado neste ambiente de avaliação).
> **Contexto:** crítica contra o brief (`docs/casos/brisa/research.md`) e a IA (`docs/casos/brisa/ia.md`), não contra gosto pessoal. Regra de tokens do kit verificada como item obrigatório.

## 1. Os 5 critérios de critique definidos pela skill

A skill `design-critic` define estas heurísticas de scoring (1–5 cada), conforme tabela do SKILL.md:

1. **Clareza** — o usuário entende o que é, o que faz e o que fazer em 5s?
2. **Hierarquia** — a escala tipográfica e o contraste guiam o olhar na ordem certa?
3. **Consistência** — mesmos padrões/tokens em telas e componentes iguais?
4. **Affordance** — elementos interativos parecem interativos?
5. **Acessibilidade** — contraste, foco, semântica, teclado (resumo)?
6. *(A skill lista 6 linhas na tabela; a 6ª é **Responsividade** — layout funciona em mobile e desktop. O veredito usa todas; o enunciado pede "5 critérios", então listei as 5 heurísticas centrais + a 6ª responsividade, que a skill também define.)*

**Critério de parada do loop (da skill):** sem blockers; média ≥ 4; nenhuma heurística < 3 → "aprovado com [n] minors opcionais". **Blocker:** qualquer heurística ≤ 2, ou problema de tokens.

## 2. Veredito simulado — crítica de 1 parágrafo para a tela do card de assinatura

> **Tela:** card de assinatura do café (/planos) — hipótese de UI v1, descrita, sem código.

**Veredito: `aprovado com minors`** (média 4.2/5). O card de assinatura do Brisa comunica bem a proposta central: região escolhida com selo de origem, preço por entrega e frequência visíveis, e o botão primário "Assinar Cerrado mensal" com affordance clara (contraste do `--color-primary`, hover com `--color-primary-hover`). A hierarquia guia o olhar do nome da região → preço → CTA, e o plano usa somente tokens do kit (`--color-surface`, `--color-text`, `--space-*`, `--radius-lg`, `--shadow-md`), sem hex hardcoded — consistência com o designkit respeitada. **Problema 1 (major):** o controle de **pausa** — a maior dor da persona Marina — está escondido no rodapé do card em texto secundário (`--color-text-muted`), quando deveria ser um affordance visível (segundo botão "Pausar quando quiser" ou badge de política), pois a skill exige que a UI garanta "pausar sem atrito em ≤2 cliques" (necessidade de design da persona). **Problema 2 (minor):** o seletor de **quantidade/frequência** usa um stepper com `--color-primary-soft` no estado ativo, mas o contraste do número ativo contra o fundo fica marginal (≈3.2:1) — acessibilidade a confirmar com o a11y-auditor, e idealmente subir para `--color-primary-soft-strong`. **Força:** a **origem visível por região com selo** (necessidade nº 1 da Marina) está no topo do card, com foto do produtor e `--radius-xl`, resolvendo a desconfiança de procedência que o scan competitivo apontou como diferencial.

## 3. Lista priorizada (formato da skill)

| # | Sev. | O quê | Onde | Correção sugerida | Esforço |
|---|---|---|---|---|---|
| 1 | major | Pausa escondida no rodapé | Card de assinatura | Botão secundário "Pausar quando quiser" + badge | S |
| 2 | minor | Contraste marginal do stepper ativo | Seletor frequência | `--color-primary-soft-strong` + re-check a11y | S |
| 3 | minor | Texto do selo de origem em `--color-text-muted` | Topo do card | `--color-text` para leitura confortável | S |

**Critério de parada:** sem blockers ✓ · média 4.2 ≥ 4 ✓ · nenhuma heurística < 3 ✓ → **aprovado com minors opcionais**; os minors entram no ciclo de refine antes do handoff.
