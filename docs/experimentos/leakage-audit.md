# Auditoria de Vazamento — Avaliação Cega (BLOCKED)

> **Quem:** Oráculo (Pesquisador) · **Data:** 2026-08-26
> **Tarefa (Orquestrador, Prioridade 1):** revisar os 18 artefatos em `docs/experimentos/artefatos/` e confirmar se as tríades A/B/C estão "bem montadas (sem vazamento de qual método é qual)".
> **Veredito:** ❌ **NÃO estão cegas.** Vazamento pervasivo em 3 camadas. A avaliação cega **não pode rodar como está** — qualquer avaliador identifica o método de cada artefato em segundos.

---

## 1. Veredito resumido

| Camada de vazamento | Severidade | Onde |
|---|---|---|
| 1. Nome do arquivo (`eN-a/b/c`) mapeia 1:1 para método A/B/C | **Crítica** | todos os 18 arquivos |
| 2. `<title>` / comentário HTML declara o método em texto explícito | **Crítica** | 9 HTML + todos os relatórios |
| 3. Corpo dos relatórios auto-referencia o método E compara com os rivais | **Crítica** | e3, e4-rel, e5 |
| 4. Vocabulário exclusivo de cada método (DESIGN.md, tokens.css, dials, pre-flight, /impeccable, craft-floor) | **Alta** | quase todos |
| 5. **Discrepância de input no E5** (auditaram páginas diferentes) | **Crítica** | e5-b, e5-c |

O protocolo `avaliacao-cega.md` afirma "A/B/C anônimos = X/Y/Z", mas isso é desfeito pelo próprio nome de arquivo (`a`/`b`/`c`) e pelo conteúdo. **O método A=Design Kit, B=impeccable, C=design-taste é público no `protocolo.md`**, então qualquer `a/b/c` já vaza o método mesmo sem ler o conteúdo.

---

## 2. Inventário de vazamento por artefato

### 2.1 HTML (9 arquivos)

| Arquivo | Vazamento | Trecho exato |
|---|---|---|
| `e1-a.html` | método + tokens + DESIGN.md | `<title>Draftly…</title>` + comentário CSS: *"Draftly landing - Método A (Design Kit) / Tokens consumidos de styles/tokens.css (fonte de verdade)"* + comentário `<head>`: *"exceção documentada do DESIGN.md §5"* |
| `e1-b.html` | método | comentário CSS: *"DIRECTION CONTRACT (impeccable §5)"* + *"FINISH… DESIGN.md, and every shipping raster carrying its provenance"* |
| `e1-c.html` | método + dials | comentário HTML: *"Método: design-taste (taste-skill). E1 - landing 'Draftly'. Dials: DESIGN_VARIANCE 6 · MOTION_INTENSITY 4 · VISUAL_DENSITY 3"* |
| `e2-a.html` | método + tokens | comentário CSS: *"TOKENS - espelho fiel de styles/tokens.css do Design Kit"* |
| `e2-b.html` | ✅ limpo (nenhum identificador de método) | — |
| `e2-c.html` | método + dials | comentário HTML: *"MÉTODO C (design-taste): dashboard NorteMetrics. Dials: VARIANCE 3 · MOTION 2 · DENSITY 6"* |
| `e4-a.html` | método + tokens | comentário HTML: *"Design Tokens (fonte de verdade — espelho de styles/tokens.css do kit)"* |
| `e4-b.html` | método | comentário HTML: *"FINISH… DESIGN.md, and every shipping raster carrying its provenance"* |
| `e4-c.html` | método | comentário CSS: *"Cloudly - E4 redesign (Method C: design-taste)"* |

### 2.2 Relatórios markdown (9 arquivos)

| Arquivo | Vazamento no título / 1ª linha | Vazamento no corpo |
|---|---|---|
| `e3-a.md` | *"# Critique E3-a — Método A (Design Kit)"* | *"Método A: Design Kit — DESIGN.md §4… scripts/…"* + compara rivais: *"o impeccable entrega… enquanto o Design Kit entrega…"* |
| `e3-b.md` | *"# Critique E3-b — Método B (impeccable)"* | *"Método B: skill impeccable v4.1.1…"* + 6 comandos `/impeccable …` + *"coerente com o E3-a"* |
| `e3-c.md` | *"# Critique E3-c · Método C (design-taste)"* | *"Método C: skill design-taste…"* + *"Dials (§1)…"* + *"os mesmos 11 tells do método A"* |
| `e4-a-rel.md` | *"# E4 — Redesign … · Método A (Design Kit)"* | *"Método: Design Kit — leu DESIGN.md, consumiu tokens de styles/tokens.css…"* |
| `e4-b-rel.md` | *"# E4 · Redesign … - Método B: impeccable"* | *"Método: B (impeccable v4.1.1)"* + *"craft-floor"* + *"new-work"* |
| `e4-c-rel.md` | *"# E4-c: Redesign (Método C: design-taste) · Cloudly"* | *"Método: design-taste (~/.pi/agent/skills/design-taste/SKILL.md)"* + *"Dials (skill §1)"* + *"pre-flight §14"* |
| `e5-a.md` | *"# Auditoria E5-a - Método A (Design Kit)"* | *"Alvo: …(gerada pelo Método A)"* + *"DESIGN.md do kit formaliza como 'micro-gaps' (seção §4.5)"* |
| `e5-b.md` | *"# Auditoria e5-b : Landing Draftly (método B / impeccable)"* | *"Método: impeccable : /impeccable audit…"* + *"Como artefato do método B, este E1-b é forte"* |
| `e5-c.md` | *"# Auditoria E5-c — Landing 'Draftly' (método C · design-taste)"* | *"Método: design-taste… pre-flight §14 + tells §9.G"* + *"APROVADO (método C)"* |

---

## 3. Discrepância de input no E5 (quebra a validade do experimento)

O `inputs.md` define E5 assim:

> **Input:** a mesmíssima landing gerada por **A (Design Kit)** no E1 (`e1-a.html`). Os 3 métodos auditam a mesma página.

Ou seja: A, B e C devem auditar **a mesma página** (`e1-a.html`) para que as diferenças reflitam o método, não o input.

**O que aconteceu de fato:**

| Auditor | Página auditada | Conforme protocolo? |
|---|---|---|
| e5-a.md | `e1-a.html` | ✅ correto |
| e5-b.md | `e1-b.html` | ❌ auditou o artefato do próprio método B |
| e5-c.md | `e1-c.html` | ❌ auditou o artefato do próprio método C |

**Consequência:** o E5 não compara "3 métodos auditando a mesma página" e sim "cada método auditando a própria página". Qualquer diferença de score é contaminada pela diferença de input. Além disso, cada auditor elogiou "a própria landing" — viés de auto-confirmação, não comparação cega.

---

## 4. Plano de saneamento (para desbloquear a avaliação cega)

### Passo 1 — Re-anonimizar nomes de arquivo (crítico)

Renomear `eN-a` → `eN-x`, `eN-b` → `eN-y`, `eN-c` → `eN-z` com mapeamento **aleatório** por experimento (não x=DesignKit, y=impeccable, z=taste sempre na mesma ordem). Guardar o mapeamento real num arquivo fora do alcance do avaliador (`docs/experimentos/mapeamento-secreto.md`, e.g. git-ignored ou fora da pasta de artefatos).

Exemplo de mapeamento aleatório:
- E1: a→Y, b→Z, c→X
- E2: a→Z, b→X, c→Y
- (um mapeamento diferente por experimento impede correlação cruzada)

### Passo 2 — Remover identificadores de método do conteúdo

Em todos os 18 arquivos, remover/normalizar:
- `<title>` e comentários que digam "Método A/B/C", "Design Kit", "impeccable", "design-taste", "taste-skill".
- Referências a arquivos internos: `DESIGN.md`, `styles/tokens.css`, `scripts/anti-slop-check.py`, `~/.pi/agent/skills/…`.
- Vocabulário exclusivo: `dials` (DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY), `pre-flight §14`, `DIRECTION CONTRACT`, `craft-floor`, `new-work`, comandos `/impeccable …`.
- Trechos que comparam explicitamente métodos ("o A é… o C é…", "o impeccable entrega… enquanto o Design Kit…").

**Nota de risco:** nos relatórios (e3/e5), o método está ENTRELAÇADO com o conteúdo do critique (ex.: "o método A roda grep, o método C inspeciona"). Isso exige reescrita de frases, não só deleção de rótulos. Idealmente o corridor original (Atelier) refaz esses parágrafos; o pesquisador pode pré-editar os rótulos mas não pode garantir neutralidade sem reescrever o argumento.

### Passo 3 — Corrigir o E5

- Regenerar `e5-b` e `e5-c` auditando **`e1-a.html`** (a mesma página), conforme `inputs.md`.
- Ou, alternativamente, explicitar no protocolo que E5 vira "cada método audita a própria landing" e renomear o experimento (comparação de auto-auditoria), mas isso muda o desenho — decidir com o Orquestrador.

### Passo 4 — Re-verificar pós-saneamento

Rodar de novo este mesmo grep de vazamento (termos abaixo) e exigir **zero hits** em conteúdo visível antes de liberar a avaliação cega:

```
Método|metodo|Design Kit|designkit|impeccable|design-taste|taste-skill
DESIGN\.md|tokens\.css|styles/|scripts/|~/.pi/agent/skills
dials|pre-flight|preflight|craft-floor|new-work|DIRECTION CONTRACT
DESIGN_VARIANCE|MOTION_INTENSITY|VISUAL_DENSITY
```

---

## 5. Recomendação ao Orquestrador

1. **Não rodar a avaliação cega agora** — ela produziria um ranking viesado e o painel A/B/C (prova central do fundador) nasceria contaminado.
2. **Saneamento antes de avaliar.** Passos 1 e 3 são mecânicos e podem ser feitos já. Passo 2 (reescrita de relatórios) idealmente pelo Atelier para preservar a integridade do argumento.
3. **Prioridade da minha parte:** estou disponível para executar Passo 1 (renomear + mapeamento secreto) e Passo 4 (re-verificação de vazamento) imediatamente, mediante OK do Orquestrador — pois isso edita arquivos do Atelier.
4. Em paralelo, sigo para a Prioridade 2 (benchmark dos 5 sites) e Prioridade 3 (gaps), que não conflitam com o saneamento.
