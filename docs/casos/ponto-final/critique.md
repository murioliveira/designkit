# Critique - Farol (UI descrita)

> Skill: `design-critic` · Entrada: `ui.md` + `research.md` + `DESIGN.md` · Saída: scoring por heurística, problemas com severidade, veredito.

## Verificação de consistência (obrigatória)

- **Tokens:** todos os tokens citados em `ui.md` existem em `styles/tokens.css` (cor/tipografia/espaço/raio/sombra/motion/z/breakpoint) - verificado por grep, nenhum hex hardcoded na descrição.
- **Padrões do kit:** as classes citadas (`card`, `btn`, `badge`, `input`, `table`, `tabs`, `dropdown`, `toggle`, `select`, `progress`, `alert`, `pagination`, `check`, `field`) existem em `styles/components.css` - reuso real, não reimplementação.
- **AI tells:** zero em-dash na copy, zero gradiente roxo, accent único (âmbar), zero 3 cards iguais genéricos, zero Inter, zero nomes genéricos, zero scroll cues, zero eyebrows em excesso. Theme lock, color lock e shape lock mantidos.

## Scoring por heurística

| Heurística | Nota | Comentário |
|---|---|---|
| Clareza | 5/5 | O livreiro sabe o que é e o que fazer em 5s na visão geral |
| Hierarquia | 4/5 | Resumos + pendências guiam bem; vitrine e relatório claros |
| Consistência | 5/5 | Tokens reais, componentes do kit, locks mantidos |
| Affordance | 5/5 | Botões como botões (kit), cards interativos com hover/focus |
| Acessibilidade | 4/5 | Contraste AA, foco, estados; requer validação em browser (o a11y-auditor aprofunda) |
| Responsividade | 4/5 | Tablet no balcão e desktop para relatório; mobile-first pelo kit |
| Copy | 4/5 | Linguagem de livreiro (vitrine, pedidos), sem jargão; margem para limar frases |
| Anti-slop | 5/5 | Zero tells, método do DESIGN.md aplicado |
| **Média** | **4.5/5** | |

## Problemas

**🔴 major - catálogo busca por toque pode esconder a ação primária (affordance em tablet):** na tela Catálogo, selecionar por `check` exige um toque preciso pequeno no tablet. O livreiro trabalha no balcão, às vezes de pé. **Correção sugerida:** usar o card do título inteiro como alvo de seleção (`card--interactive` com `aria-pressed`/role check) em vez de só o `check`; área de toque ≥ 44×44 (`--space-10` ou espaçamento explícito).

**🟡 minor - barra de "importar catálogo" pode parecer técnica:** os termos "importar", "upload", "link" são técnicos para o livreiro não-técnico. **Correção sugerida:** label de ação em linguagem de resultado ("Trazer catálogo", "Escolher arquivo"), com o termo técnico como tiny secondary mas não o label primário.

**🟡 minor - tabela de pedidos com linha a linha mista:** `table--zebra` é bom, mas 5+ linhas com estados diferentes podem competir. **Correção sugerida:** agrupar pedidos por distribuidora nas `tabs` (já previsto) e reduzir a zebra a grupos, não a cada linha.

## Critério de parada

Sem blockers ✓ · média ≥ 4 (4.5) ✓ · nenhuma heurística < 3 ✓ → **aprovado com minors**.

**Veredito: `aprovado com minors`** (o major de affordance do tablet entra no refine e no handoff como requisito de alvo de toque).