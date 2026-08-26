# Avaliação Comparativa — Design Kit vs impeccable vs design-taste

**Data:** 2026-08-26 · **Método:** avaliação cega (avaliador independente, sem saber qual método gerou cada artefato) · **Artefatos:** 18 (5 experimentos × 3 métodos) em `docs/experimentos/artefatos/`

> **Nota de integridade:** o avaliador reportou que o painel não era 100% cego (alguns artefatos E3/E4 nomeavam métodos no corpo, apesar do saneamento). Rankings tratados como indicativos, mas os achados técnicos (contraste, a11y, tells) são verificados e confiáveis.

## Mapeamento (de-anonimização)

| Rótulo | Método |
|---|---|
| **A** | Design Kit (DESIGN.md + skills/ + scripts) |
| **B** | impeccable (skill de referência) |
| **C** | design-taste (skill de referência) |

Permutação por experimento (mapeamento-secreto.md): E1: Y=A, Z=B, X=C · E2: X=A, Z=B, Y=C · E3: Z=A, X=B, Y=C · E4: Y=A, X=B, Z=C · E5: X=A, Y=B, Z=C

---

## E1 — Landing Draftly (Persuade)

| Artefato | Método | Geral |
|---|---|---|
| e1-X | **C (design-taste)** | **4.8** 🥇 |
| e1-Z | B (impeccable) | 4.1 🥈 |
| e1-Y | A (Design Kit) | 3.7 🥉 |

**Vencedor (design-taste):** completude a11y sem falhas de contraste (teal-700 ≈ 5.4:1, muted ≈ 7.6:1, dark ≈ 8.5:1 — todos AA), skip-link visível, menu mobile com aria-expanded, prefers-reduced-motion, bento assimétrico, preview real de proposta, copy concreta, zero tells.
**3º (Design Kit):** links/eyebrow #818cf8 = 2.98:1 (falha AA, P1), skip-link com classe quebrada (P1), nav display:none no mobile sem menu (P1), typo.

## E2 — Dashboard NorteMetrics (Operate)

| Artefato | Método | Geral |
|---|---|---|
| e2-X | **A (Design Kit)** | **5.0** 🥇 |
| e2-Z | B (impeccable) | 4.2 🥈 |
| e2-Y | C (design-taste) | 4.0 🥉 |

**Vencedor (Design Kit):** densidade útil sem ruído, tabela com caption + aria-describedby + th scope + tabular-nums, tema claro/escuro com toggle + localStorage, skip-link, role=status no alerta, responsivo.
**3º (design-taste):** sem skip-link (P1), gráfico confuso, hint vs barras inconsistentes.

## E3 — Critique do before.html

| Artefato | Método | Geral |
|---|---|---|
| e3-X | **B (impeccable)** | **4.8** 🥇 |
| e3-Y | C (design-taste) | 4.3 🥈 |
| e3-Z | A (Design Kit) | 2.8 🥉 |

**Vencedor (impeccable):** exaustividade (10 heurísticas Nielsen + personas + cognitive load + scan determinístico + prioridades P0-P3 com correção por achado), honestidade metodológica, veredito quantificado.
**3º (Design Kit):** 3 erros factuais sobre o alvo (99.99% vs 99.9%, v0.6 vs v2.4.1, hero "split" vs centralizado), veredito contradiz a própria média.

## E4 — Redesign do before.html

| Artefato | Método | Geral |
|---|---|---|
| e4-X | **B (impeccable)** | **4.8** 🥇 |
| e4-Z | C (design-taste) | 4.2 🥈 |
| e4-Y | A (Design Kit) | 3.8 🥉 |

**Vencedor (impeccable):** preservação integral (marca, nav, CTAs, preços), remoção verificada de todos os tells, trilha "hoje" real no lugar do fake screenshot, linguagem papel-morno + cobalto, skip-link visível, contraste verificado, relatório com validação mecânica.
**3º (Design Kit):** "Junte-se a mais de 10 mil times" permanece no CTA (relatório afirma remoção — contradição), relatório afirma skip-link que não existe, muted 4.35:1 falha AA.

## E5 — Auditoria a11y + anti-slop (e1-Y.html)

| Artefato | Método | Geral |
|---|---|---|
| e5-X | **A (Design Kit)** | **4.8** 🥇 |
| e5-Y | B (impeccable) | 4.6 🥈 |
| e5-Z | C (design-taste) | 4.5 🥉 |

**Vencedor (Design Kit):** cobertura completa (contraste por par, foco, teclado, semântica, ARIA, scan anti-slop), tabela de priorização com severidade + localização + correção, veredito claro.
**2º (impeccable):** números de linha exatos (melhor localização). **3º (design-taste):** cenários de uso real (mais útil para priorização humana).

---

## Painel final — quem venceu onde

| Experimento | 🥇 Vencedor | Método |
|---|---|---|
| E1 Landing | e1-X | **design-taste** |
| E2 Dashboard | e2-X | **Design Kit** |
| E3 Critique | e3-X | **impeccable** |
| E4 Redesign | e4-X | **impeccable** |
| E5 Auditoria | e5-X | **Design Kit** |

**Leitura honesta:** **nenhum método domina sozinho** — cada um venceu em contextos diferentes:
- **Design Kit (A)**: venceu **Operate** (dashboard, 5.0/5) e **auditoria** (E5) — pontos fortes em densidade de dados, tabelas semânticas, dark mode e auditoria estruturada.
- **impeccable (B)**: venceu **critique** (E3) e **redesign** (E4) — pontos fortes em exaustividade de crítica (Nielsen + personas) e redesign com prova de produto real.
- **design-taste (C)**: venceu **landing** (E1) — ponto forte em persuasão, a11y completa e copy concreta.

## O que separa 1º de 2º/3º (padrão transversal)

Não é estética (todos têm linguagem visual própria e competente) — é **rigor de acabamento**:
1. Skip-link funcional e visível no foco
2. Contraste AA verificado (sem falhas de 2.98:1 / 4.35:1)
3. Zero contradição relatório ↔ artefato (o 3º do E4 afirma remoções que não fez)
4. Precisão factual sobre o alvo (o 3º do E3 errou 3 fatos)

## Anti-slop

**Zero tells residuais em todos os 15 artefatos** (em-dash, Inter, roxo, fake screenshot, scroll cue, version footer) — a disciplina anti-slop está sólida em todos os métodos avaliados.

## Recomendações

1. **Design Kit**: corrigir os pontos que o rebaixaram (contraste de links, skip-link, veracidade do relatório) — são baratos e o kit já tem os detectores para pegar (o anti-slop-check pegou em-dash, mas não contraste/skip-link; considerar estender).
2. **Combinar os 3**: o melhor produto seria usar design-taste para landing, Design Kit para dashboard/auditoria, impeccable para critique/redesign — ou o kit absorver os pontos fortes dos outros (o DESIGN.md já incorpora muito do taste; incorporar Nielsen/personas do impeccable no critique).
3. **Avaliação cega**: refazer com saneamento completo (remover TODOS os identificadores, incluindo "o kit"/"a skill de referência") para um painel 100% cego.
