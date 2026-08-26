# MAPEAMENTO SECRETO — Experimentos A/B/C (NÃO DIVULGAR AO AVALIADOR)

> **⚠️ SECRETO.** Este arquivo é para o Orquestrador e para o painel final de de-anonimização. **NÃO referencie este arquivo em `avaliacao-cega.md` nem em qualquer instrução ao avaliador cego.** Se o avaliador ler isto, a avaliação cega fica inválida.
> **Quem:** Oráculo (Pesquisador) · **Data:** 2026-08-26 · **Passo 1 do `leakage-audit.md`.**

## Como ler

- Coluna **Original** = nome antigo do arquivo (`eN-a/b/c`), que revelava o método pelo sufixo.
- Coluna **Novo** = nome anônimo aplicado (`eN-X/Y/Z`).
- Coluna **Método** = o método real por trás (A=Design Kit, B=impeccable, C=design-taste), conforme `protocolo.md`.

A permutação X/Y/Z é **diferente por experimento** para impedir que o avaliador correlacione artefatos de um mesmo método entre experimentos (ex.: se "X" fosse sempre Design Kit, ele inferiria o método por estilo recorrente).

## Tabela de mapeamento

### E1 — Landing Draftly (Persuade)

| Original | Novo | Método |
|---|---|---|
| e1-a.html | **e1-Y.html** | A (Design Kit) |
| e1-b.html | **e1-Z.html** | B (impeccable) |
| e1-c.html | **e1-X.html** | C (design-taste) |

### E2 — Dashboard NorteMetrics (Operate)

| Original | Novo | Método |
|---|---|---|
| e2-a.html | **e2-X.html** | A (Design Kit) |
| e2-b.html | **e2-Z.html** | B (impeccable) |
| e2-c.html | **e2-Y.html** | C (design-taste) |

### E3 — Critique do before.html

| Original | Novo | Método |
|---|---|---|
| e3-a.md | **e3-Z.md** | A (Design Kit) |
| e3-b.md | **e3-X.md** | B (impeccable) |
| e3-c.md | **e3-Y.md** | C (design-taste) |

### E4 — Redesign do before.html (preservar marca)

| Original | Novo | Método |
|---|---|---|
| e4-a.html | **e4-Y.html** | A (Design Kit) |
| e4-a-rel.md | **e4-Y-rel.md** | A (Design Kit) |
| e4-b.html | **e4-X.html** | B (impeccable) |
| e4-b-rel.md | **e4-X-rel.md** | B (impeccable) |
| e4-c.html | **e4-Z.html** | C (design-taste) |
| e4-c-rel.md | **e4-Z-rel.md** | C (design-taste) |

### E5 — Auditoria a11y + anti-slop

| Original | Novo | Método |
|---|---|---|
| e5-a.md | **e5-X.md** | A (Design Kit) |
| e5-b.md | **e5-Y.md** | B (impeccable) |
| e5-c.md | **e5-Z.md** | C (design-taste) |

## Verificação anti-correlação (nenhum método tem rótulo fixo)

| Método | E1 | E2 | E3 | E4 | E5 |
|---|---|---|---|---|---|
| A (Design Kit) | Y | X | Z | Y | X |
| B (impeccable) | Z | Z | X | X | Y |
| C (design-taste) | X | Y | Y | Z | Z |

Nenhuma linha é constante — o avaliador não pode inferir o método por rótulo repetido.
