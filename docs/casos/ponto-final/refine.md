# Refine - Farol (comando: distill)

> Skill: `design-refine` · Entrada: `critique.md` (diagnóstico) + `ui.md` · Saída: direção + dials + alavancas + preservados.

## Direção escolhida: **distill**

**Por quê (1 linha):** o critique apontou 1 major de affordance + 2 minors de clareza, e o brief diz que o livreiro tem pouco tempo e é não-técnico - o risco central é uma tela densa demais, então reduzir à essência ataca os 3 achados de uma vez.

## Dials antes → depois

| Dial | Antes | Depois |
|---|---|---|
| DESIGN_VARIANCE | 4 | 3 (uniformizar, menos variação de blocos) |
| MOTION_INTENSITY | 3 | 3 (mantido: quieto é o correto para Operate no balcão) |
| VISUAL_DENSITY | 6 | 4 (menos elementos por tela; uma tarefa em foco) |

## Alavancas aplicadas (o que mudaria na UI)

1. **Catálogo: card como alvo de seleção** (major do critique). Remove o `check` pequeno; o card-título inteiro vira o alvo (`card--interactive` com `aria-pressed`), área de toque ≥ 44px. Distill não é só tirar, é tornar a ação essencial óbvia.
2. **Visão geral: de 3 cards para 1 foco.** O livreiro entra e vê UMA coisa: "3 pedidos em aberto" com o CTA de resolução. Resumo do relatório vira link discreto, não card concorrente. Regra do distill §4: cada elemento sobrevivente tem razão em 1 frase.
3. **Importar: rótulos de resultado, não técnicos.** "Trazer catálogo" + "Escolher arquivo" substituem "importar/upload/link" como labels primários (minor 2 do critique).
4. **Pedidos: zebra por grupo, não por linha.** Mantém as `tabs` por distribuidora (já previsto); a zebra passa a separar grupos, reduzindo competição visual (minor 3).
5. **Relatórios: um botão, uma mensagem.** "Gerar PDF" é a única CTA; copy do estado vazio encurtada para ≤ 15 palavras ("Sem movimento neste mês. Gere mesmo assim ou volte depois.").
6. **Repetição de padrão revista:** a visão geral deixa de ter 3 cards iguais (regra do anti-slop do DESIGN.md); o padrão card fica para a vitrine (onde ele comunica hierarquia real), e a visão geral vira resumo + pendência focada.

## O que foi preservado (prova de que não virou outra página)

- IA intacta: sitemap e fluxos de `ia.md` não mudaram (mesma tarefa por tela).
- Tokens intactos: mesmas famílias `--color-*`/`--space-*`/`--radius-*`; o accent âmbar (`--color-primary`) continua único (color lock).
- Componentes do kit: mesmos (`card`, `btn`, `badge`, `table`, `tabs`, `dropdown`, `toggle`, `input`, `select`, `progress`, `alert`, `pagination`, `check`).
- Acessibilidade: estados hover/active/focus/disabled preservados; o major do tablet virou requisito, não regressão.
- Voz da copy: linguagem de livreiro mantida.

## Pre-flight

Zero em-dash ✓ · color/theme/shape lock ✓ · 1 foco por tela ✓ · estados completos ✓ · tokens reais ✓ · sem tells ✓.