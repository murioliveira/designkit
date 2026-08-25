# Critique Report — Caso Linha Direta (nível enriquecido do kit)

**Data:** 2026-08-25 · **Papel:** design-critic · **Lentes:** heurísticas + tells + tokens + cognitive-load + persona-based

## Veredito

**APROVADO COM RESSALVAS** (média 4.71/5, nenhuma heurística < 3, sem blockers). 3 P1 para refine antes de fechar.

## Design Read e dials

Declarados e coerentes: VARIANCE 9 (hero 1.4fr/1fr com peça deslocada, bento com pesos), MOTION 6 (marquee + pin do sticky-stack), DENSITY 3 (editorial). P2: "hero reveal" citado no README mas sem keyframe correspondente (só `marquee-scroll`).

## Uso dos blocos

| Bloco | Status |
|---|---|
| hero-split-assimetrico | ✅ aplicado de verdade (grid + SVG real com role=img, adaptado à identidade) |
| marquee | ⚠️ estrutura ok, loop com costura visível (P1-3) |
| bento-grid | ⚠️ 5 artigos vs "6 células" do README; 1 célula vazia no desktop (P1-1) |
| sticky-stack | ✅ position: sticky real (CSS puro), fallbacks corretos |

## Scoring

| Heurística | Nota |
|---|---|
| Clareza | 5 |
| Hierarquia | 4 (dois accents diluem o código visual) |
| Consistência com tokens | 4 (color lock violado) |
| Affordance | 5 |
| Acessibilidade | 5 |
| Responsividade | 5 |
| Anti-slop | 5 |
| **Média** | **4.71** |

## Achados priorizados

**P1-1 — Bento com célula vazia no desktop**: 5 artigos + span wide não fecham a grade 1.4fr/1fr (buraco em r3c2). Correção: 6ª célula ou re-espanar.
**P1-2 — Color lock violado**: CTA do header (btn--primary = índigo) e ghost buttons índigo vs accent declarado âmbar. Correção: `.ld-btn-accent` no header + ghost em âmbar/slate.
**P1-3 — Marquee com costura visível (22s)**: `translateX(-50%)` relativo a 1 lista (largura W) em vez do track (2W). Correção: -100% no list ou -50% no track. **Corrigir também `docs/blocos/marquee.md` (mesmo bug no esqueleto).**

P2: README superdeclara (hero reveal, marquee mobile), subtext 14 palavras não 17, em-dash no README (2x), casos fictícios sem selo de "ilustrativos".

## O que o critique enriquecido pegou que as externas não pegariam

1. **Célula vazia do bento** — artefato de auto-placement do CSS Grid; critique por screenshot não vê.
2. **Costura do marquee** — matemática de transform (base do percentual ≠ largura do track); expõe bug no bloco-fonte do kit.
3. **Color lock** — regra de produto do kit ("1 accent por página"); nenhuma skill externa conhece a regra nem o token como accent candidato.

## Conclusão

O caso prova o valor do loop do kit (critique enriquecido > skills externas nos 3 itens acima), mas mostra que a block library exige critique antes de ser citada como prova. Refine dos 3 P1 + correção do bloco marquee.md.
