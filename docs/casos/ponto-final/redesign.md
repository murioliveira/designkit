# Redesign - Farol (cenário: site antigo da livraria)

> Skill: `design-redesign` · Entrada: cenário hipotético (o livreiro já tem um site antigo) · Saída: modo detectado + auditoria resumida + alavancas.

## Cenário

O Otávio não usa só o Farol: a Livraria Quilombo tem um site antigo (HTML de 2012, fundo bege, logo desenhado em Word, nav com 9 itens, fotos de estoque genéricas) que ele mantém por preguiça de refazer. O pedido: "moderniza o site da loja, mas mantém minha cara".

## Modo detectado

**Redesign - Preservar.** O brief pede explicitamente modernizar sem trocar a identidade ("mantém minha cara"). Não é overhaul (a marca é reconhecível e querida no bairro) nem greenfield.

## Auditoria (resumo dos 7 itens)

1. **Tokens de marca:** logo em WordArt (palavra-marca, preservar como assinatura), fundo bege atual, nav com 9 itens (encolher para 5), fotos de estoque genéricas (aposentar).
2. **IA:** página única longa (hero → sobre → catálogo → contato); nav com 9 itens fragmenta a mesma página.
3. **Blocos de conteúdo:** sobre a livraria é o melhor conteúdo (voz real do Otávio); catálogo é uma lista de imagens sem hierarquia.
4. **Padrões a preservar:** a voz do texto do "sobre", a palavra-marca, o horário de funcionamento em destaque, o email de contato.
5. **Padrões a aposentar:** fundo bege genérico, fotos de estoque, nav de 9 itens, título em Times da era Word, contador de visitas no rodapé.
6. **Dials atuais:** VARIANCE 2 (tudo centralizado), MOTION 0, DENSITY 5. Ponto de partida, não baseline.
7. **SEO:** a página "sobre" aparece no Google local como "Livraria Quilombo"; os slugs e o heading h1 não podem mudar (risco nº 1 de redesign).

## Alavancas aplicadas (em ordem, parando quando o brief satisfaz)

1. **Tipografia** (alavanca 1, baixo risco): manter a palavra-marca, mas trocar Times por `--font-*` do kit com escala editorial; sem serifa injustificada.
2. **Espaçamento e ritmo** (alavanca 2): aumentar respiro vertical em `--space-*`, unificar paddings, remover valores mágicos do CSS de 2012.
3. **Recalibração de cor** (alavanca 3): manter o âmbar da marca como accent (override documentado do anti-lila, pois é cor real da marca), aposentar o bege lavado por `--color-surface`/`--color-bg` do kit, aplicar theme lock (1 tema).
4. **Recomposição do topo** (alavanca 5, parar aqui): hero vira vitrine da livraria (foto real do balcão + headline ≤ 2 linhas), nav encolhe de 9 para 5 itens (as 5 tarefas do sitemap do Farol), catálogo vira grid de `card` do kit.

**Não mudou (invioláveis):** slug `/sobre` e o h1 "Livraria Quilombo" (SEO), o email de contato, o horário, a palavra-marca, a voz do texto.

## Conclusão

O redesign preserva a identidade (âmbar, palavra-marca, voz) e aposenta os tells de 2012 (bege genérico, Times, nav fragmentada, contador). O critique do redesign rodaria em seguida; as alavancas 4 (motion) e 6 (substituição de bloco) não foram necessárias: o brief foi satisfeito em 4 alavancas.