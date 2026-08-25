# Ponto Final - Teste de Integração de Ponta a Ponta

> **Objetivo:** prova de que o fluxo completo das 8 skills do Design Kit funciona de ponta a ponta num mini-brief real.
> **Produto fictício:** Farol, app de assinatura de livros para pequenas livrarias independentes.
> **Regra:** os artefatos são DESCRITOS em markdown (integração das skills, não build de UI).

## Mapa do fluxo (skill → artefato → o que provou)

| Skill | Artefato | O que provou |
|---|---|---|
| brief (input) | `brief.md` | Problema definido, público (livreiro não-técnico), critério de sucesso, escopo v1, restrição de tokens |
| `design-researcher` | `research.md` | Problem statement canônico + persona Otávio + jornada com aha + scan competitivo (assunções marcadas) |
| `information-architect` | `ia.md` | Sitemap 5 itens + 2 fluxos (cadastrar livro, relatório) com feliz/alternativo/borda |
| `ui-designer` | `ui.md` | Design read + dials justificados + telas + componentes do kit + tokens + anti-slop aplicado |
| `design-critic` | `critique.md` | Scoring 8 heurísticas + 1 major (alvo de toque) + 2 minors + veredito (aprovado com minors) |
| `design-refine` | `refine.md` | Direção distill + dials antes/depois + 6 alavancas com tokens + preservados |
| `design-redesign` | `redesign.md` | Cenário site antigo: modo Preservar + auditoria + 4 alavancas em ordem + invioláveis |
| `a11y-auditor` | `a11y.md` | 3 checks WCAG AA (contraste/foco+teclado/semântica) + 1 risco (motion da barra) |
| `design-handoff` | `handoff.md` | Spec do card de livro: tokens reais, componentes do kit, estados, a11y, checklist de aceite |

## Leitura da prova

1. **O fluxo encadeia:** cada artefato consome o anterior (research → IA → UI → critique → refine → a11y → handoff) e nenhuma skill re-pergunta o que a anterior já respondeu.
2. **Tokens reais e verificáveis:** todos os `--var(--...)` citados em `ui.md` e `handoff.md` existem em `styles/tokens.css` (grep confirmado); nenhum hex inventado.
3. **Componentes do kit reusados:** todas as classes citadas existem em `styles/components.css` - reuso real, não reimplementação.
4. **Método anti-slop presente:** design read + dials com razão (ui-designer), tells verificados no critique, direção com razão e preservados no refine, override de marca no redesign (accent âmbar como cor real da marca), contraste calculado no a11y.
5. **O loop critique → refine funciona:** o major do critique (alvo de toque no tablet) virou requisito P0 no handoff, e o refine atacou os 3 achados com distill.

**Resultado: o fluxo de ponta a ponta das 8 skills FUNCIONOU.**