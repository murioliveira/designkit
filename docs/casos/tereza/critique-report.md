# Critique Report — Caso Tereza Vilela (modo Experience)

**Data:** 2026-08-25 · **Papel:** design-critic · **Lentes:** heurísticas + tells + tokens + cognitive-load + persona

## Veredito

**APROVADO COM RESSALVAS** (média ≈ 4.6/5, nenhuma heurística < 3, sem blockers). 1 major (color lock) para refine.

## Design Read e dials

Declarados e coerentes: VARIANCE 8 (galeria assimétrica), MOTION 4 (revelação + zoom sutil), DENSITY 2 (galeria). Coerentes com o preset "galeria" do bloco (8-10/4-8/1-3).

## Modo Experience de verdade ✅

- **Primeiro viewport = a OBRA**: ilustração SVG de capa dominando o grid 3fr/2fr; nome + lead 1 linha + CTA discreto ao lado. Sem scroll cue, sem strip decorativo.
- **Chrome mínimo**: header ≤ 64px, marca + 4 links + toggle; sem sidebar, sem CTA agressivo no header.
- **Curadoria**: 6 peças (2 capas, 2 ensaios, 1 mural, 1 retrato) com título real + editora/revista + ano, nomes contextuais (Editora Caboré, Revista Foz).
- **Bloco galeria-experience aplicado e ADAPTADO**: grid 1.1fr/1fr, flexões --livro/--ensaio/--alta/--larga/--retrato, legenda sempre visível em gradiente com fallback touch, zoom scale(1.03) só transform. Melhor que o esqueleto: SVG inline real com role="img" em vez de picsum.

## Scoring

| Heurística | Nota |
|---|---|
| Clareza | 5 |
| Hierarquia | 4 (inconsistência de accent na arte) |
| Consistência com tokens | 4 (color lock violado pela arte) |
| Affordance | 5 |
| Acessibilidade | 5 |
| Responsividade | 5 |
| Anti-slop | 4 |
| **Média** | **≈ 4.6** |

## Achados

**🔴 major — Color lock contradito pela arte**: 4 SVGs usam `var(--color-primary-soft)` (índigo/lavanda) enquanto a narrativa declara accent terracotta único ("um só vermelho"); CTAs btn--primary índigo. Fix: trocar por `--color-warning-soft`/neutro OU ajustar a narrativa para "accent de interface = índigo do kit; signature de tinta = terracotta" (decisão honesta). Sugestão: (a).

**🟡 minor**: favicon tem hex `%23b45309` além das metas theme-color (documentar a exceção no README); legenda sobre gradiente em peças claras merece verificação em browser.

## Lentes enriquecidas

- **Cognitive-load**: primeiro viewport comunica quem/o quê em 5s ✓; máx 1 foco por seção ✓; curadoria sem sobrecarga (6 peças) ✓; zero custo de memória ✓.
- **Persona (editores/diretores de arte)**: melhor trabalho primeiro ✓; manifesto sinaliza ofício + pragmatismo de prazo ("cada capa passa por três versões") ✓; gap minor: portfólio completo "sob pedido" é atrito aceitável em Experience.

## Comparação vs skills externas

As externas não têm modo Experience dedicado — tratariam o portfólio como landing genérica (hero marketing, 3 cards). Este caso prova o kit materializando Experience como disciplina de curadoria. E a detecção determinística cruzou tokens + tells + heurísticas na mesma sessão, achando a violação de color lock.

## Conclusão

Refine: corrigir o color lock (S) + documentar favicon. Rodada 2 deve fechar APROVADO limpo.
