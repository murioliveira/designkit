# Pesquisa de Mercado 2026-08-26 (2ª edição) — Validação & Novas Frentes

> **Quem:** Oráculo (Pesquisador) · **Data:** 2026-08-26
> **Base:** complementa `docs/pesquisa-mercado.md` (1ª edição). Aqui eu VALIDO métricas com web atual (ago/2026) e flagro novidades de ecossistema que mudam o posicionamento.
> **Regra perene:** nenhuma menção à Liquid em qualquer parte deste documento.

---

## 1. O que mudou desde a 1ª edição (resumo executivo)

As métricas de mercado CONFIRMARAM as tendências e aceleraram para cima. Nenhum número-chave caiu; vários concorrentes **mais que dobraram** em estrelas e instalações. O espaço está mais quente, mais disputado, e o Design Kit precisava de decisões do fundador (licença, repo público, nome) — **cada dia sem repo público pública aberto é atenção indo para os incumbentes.**

| Projeto | 1ª edição (ago/2026) | 2ª edição (26/ago/2026) | Δ |
|---|---|---|---|
| **impeccable** (pbakaus) | ~40K★ · 160K+ installs | **62.3K★ · 248K installs** (Skillselion) | ★ ▲ ~55% · installs ▲ |
| **taste-skill** (Leonxlnx) | ~46K★ | **78.5K★** (78.372 em 20/ago) · Vercel OSS | ★ ▲ ~70% |
| **open-design** (nexu-io) | ~57K★ | **57.4K★** · 6.5K forks · v0.9.0 (10º release) | estável, amadurece |
| **anthropics/skills** (frontend-design) | 65K★ · 277K+ installs | **148–170K★** · **583K–792K installs** | ★ ▲ 2.5x+ |
| **designer-skills** (Owl-Listener) | 63 skills | **97–107 skills · 9 plugins** (cresceu) | ▲ |
| open-design (SkillsLLM) | — | 8.9K★ (índice) vs 57K★ (GitHub oficial) | — |

**Mensagem central:** o crescimento não desacelerou. O incumbente (Anthropic) está a ordinária de 3–4x dos demais, e os "anti-slop" proprietários (impeccable/taste) consolidaram a categoria. O Design Kit ainda não está no jogo público.

---

## 2. Validação de métricas (fontes de ago/2026)

### 2.1 impeccable — pbakaus/impeccable
- **62.3K★ GitHub · 248K installs** (Skillseli.on, atualizado 25/ago/2026).
- O artigo **a16z "Impeccable by Design"** (Paul Bakaus) confirma: 40K+★ e 160K+ installs só via skills.sh (uma fração — também instala por `npx impeccable install` e marketplace Claude nativo). → **Prova social + infra de ecossistema = a16z fez case do unrinnable skill.** Design é tema "infraestrutura" agora.
- Video de iteração: impeccable "supera 37 anti-patterns" — os 98 checks do kit seguem na frente em cobertura mecânica.

### 2.2 taste-skill — Leonxlnx/taste-skill
- **78.5K★** (78.372 em 20/ago/2026). **Patrocinado pelo Vercel OSS Program.**
- **9 skill packages** (v2 experimental desde meados 2026, v1 pinable). 3 dials: DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY (1–10).
- Compatíveis: Cursor, Claude Code, Codex, Antigravity, Windsurf, Copilot.
- Stack default: React/Next + Tailwind + Framer Motion (≠ kit: HTML/CSS/JS puro).
- Passou scan de segurança do SkillsLLM (sem issues high-severity) → **auditoria de segurança virou fator de adoção.**
- Nota: `tasteskill/tasteskill` (151★) é repo diferente do canônico `Leonxlnx/taste-skill` (78.5K★). Cuidado com homônimos ao citar.

### 2.3 Open Design — nexu-io/open-design
- **57.4K★ · 6.5K forks · v0.1.0 (Jan) → v0.9.0 (02/jun/2026)**, 10º release. Commit ~a cada 3 dias.
- Posição: alternativa local-first ao Anthropic Claude Design; 19–20 skills, 71–142 design systems, sandbox preview, export HTML/PDF/PPTX.
- Expansão do autor: **nexu-io/html-anything** (75 skills × 9 surfaces, 8.4K★ apache) e **nexu-io/looper** (run AI agents as dev team) → o vencedor de stars agora é multi-produto.
- Issue #2378 de usuário: "os design systems são todos iguais" → **pain point de produção: adicionar qualidade/customização de design systems, não quantidade.** Zhão vindicado do kit (tokens + componentes reais).

### 2.4 Anthropic frontend-design (anthropics/skills)
- Install: `npx skills add anthropics/frontend-design`.
- **148–170K★** repo anthropics/skills · **583K–792K instalações** (fontes divergem: Skillselion 583K · claudemarketplaces 792K).
- v1.3.0 (ago/2026). É o "S-rank" da categoria.
- 45K+ skills públicas Claude agora **OpenCode-compatible** (Reddit) → portabilidade universal acelerando.
- Inclui em "AI image generation" (b) a geração de design systems.

### 2.5 designer-skills (Owl-Listener / Marie Claire Dean)
- Cresceu: agora **97–107 skills, 30+ comandos, 9 plugins** (designer-skills + ai-design-skills de 44 skills + inclusive-design-skills).
- Install: `/plugin marketplace add Owl-Listener/designer-skills`.
- **Comparação (2ª edição) atualizada:** o kit ainda é o único com **design system próprio + QA determinística**; designer-skills cobre research→handoff mas pura plataforma/methodology, sem tokens/componentes executáveis.

---

## 3. Novidades de ecossistema (não na 1ª edição)

1. **a16z perfilou impeccable** — "Impeccable by Design" mostra que skills de design são lidos como **infraestrutura/padrão de mercado**, não "curiosidade de nicho". O Design Kit precisa de uns case público idêntico (a16z só deu pra quem já tem tração).
2. **Vercel patrocinou taste-skill** — ecossistema-âncora investe no concorrente de critica/refine mais próximo do kit.
3. **Pompa >10 skills fix count** — Marketplaces e Skill Packs consolidam a descoberta. /plugin add é o "npm install" de Claude agora.
4. **Security scan virou barreira de entrada** — SkillsLLM audita segurança e prompt-injection; novos pitches precisam passar scan. O kit pode adotar "passou auditoria" como hardening.
5. **Monetiz/infra-estrutura de review** — "Taste skills are turning agent review into infrastructure" (developers digest). O "foundation loop de qualidade" do kit (critique→refine→re-critique) é recriado pela comunidade como infra — o kit está à frente no mérito conceitual.
6. **Nova entrada relevante:** `google-labs-code/design.md` (16K★, 22 fit) e `anthropics brand-guidelines` (171K★) em rankings — exemplos de design/creative com alto apetite.
7. **Geração de imagem virou categoria própria** (Nano Banana Pro 77.2K signal). Decisão pendente do fundador (geração de imagens) conflita aqui: skills de imagem viram; kit pode integrar ou se manter focado em UI.

---

## 4. Implicações acionáveis para o Design Kit (prioridade)

| Prioridade | Ação | Razão (evidência) |
|---|---|---|
| **CRÍTICO** | **Corrigir nome do repo no docs** — `docs/plano-descoberta.md` todo usa `murioliveira/designkit`, mas README/INDEX/`.skills.json`/package.json usam **`murioliveira/designkit`**. Decidir o definitivo e padronizar ANTES do lançamento. | Repo errado em posts/tweets = link quebrado no day-1 do launch. |
| **CRÍTICO** | **Resolver licença + ir público** — gate determinante. | Sem repo público + licença MIT, zero estrelas impossíveis; todos os canais (X/Reddit/HN) dependem de URL pública (kit-de-lancamento). |
| **ALTO** | **Fechar decisão de nome** ("Design Kit" genérico p/ SEO). | risco já mapeado (plano-descoberta §7). |
| **ALTO** | Posicionar com números de cobertura mecânica superior: **98 checks vs impeccable 37 anti-patterns**; único com `detector executável` em 14 arquivos. | impeccable 26 "37 anti-patterns", o kit supera em cobertura (auditoria-comparativa-v2). |
| **ALTO** | Aproveitar o pane-point de produção do Open Design n. 9. | Issue #981: "149 design systems todos iguais" → kit oferece tokens + componentes reais (não templates). |
| **MÉDIO** | Passar scan de segurança de skills (SkillsLLM/devtools) e exibir badge "security audited". | taste-skill usa como moeda de confiança; feito passou. |
| **MÉDIO** | Publicar "a16z-style" -- Não esperar a16z; publicar case-study próprio (dev.to/HN) sobre "design department as infra". | A categoria ganha visibilidade de infra. |
| **MÉDIO** | Considerar porta-fejição de imagem quando fundador decidir geração de imagens. | Categoria em alta (+77K signal). |
| **BAIXO** | Investor OpenCode compatibility (45K skills já) | Portabilidade "Em att" p/ novos harnesses. |

---

## 5. Riscos atualizados

| Risco | Δ vs 1ª ed | Mitigação |
|---|---|---|
| Impeccable consolidou-se (62.3K★ + a16z) fatalmente como o "padrão de critique" | ↑ | Kit não compete como critique isolada: **é complementa (wrapper)** e compete como setor completo + design system. |
| Taste-skill patrocinado pela Vercel consolida o nicho anti-slop | ↑ | Diferenciar: o kit É infra (tokens + QA determinístico), não "gosto a mais". |
| Open design amadurecido (57K★ multi-produto), pain point de custom/corporate exposto | = | Falar com esse pain: "a maioria são templates iguais; o kit entrega tokens reais + componentes". |
| Anthropic 3–4x os demais em base instalada | = | Aceitar: a maior base instalada = marketplace. Kit como skill de terceiro continua valido p/ independência de vendor. |
| Sem repo público = zero tração; janela fecha | **ALTO hoje** | Priorizar decisões do fundador (licença, nome, público). |

---

## 5b. Validação de copy — reforços p/ o Mural (plano-descoberta + material-publicacao)

Pedido do Orquestrador: conferir se os 2 ativos de lançamento exploram bem (a) o pain-point "design systems todos iguais" e (b) o diferencial de QA. **Veredito: ambos conversam sobre, mas NÃO usam o golpe mais forte nem têm números consistentes.**

### CJ nº1 — Pain-point mal mirado (o golpe está na mão e não é usado)
- Estado atual: material-publicacao (Post 2, Bluesky) diz só que Open Design tem "design systems são templates, não sistemas funcionais". Fraco — e contradiz a própria evidência (o pain real é QUALIDADE, não formato).
- **Evidência forte não usada:** usuários do próprio open-design reclamam (issue): "149 design systems são todos iguais"; open-design = 142–149 THEMES/MULTIDADOS mas todos parecen templates.
- **Reforço de título/copy para o Mural (uma frase):**
  > "Open Design chegou a **149 design systems — e seus próprios usuários pedem qualidade no lugar de quantidade** ("they are all the same"). Seu agente não precisa de mais templates; precisa de um sistema com tokens reais + enforcement. O Design Kit: 1 sistema de 158 tokens, auditorável por grep, zero hex hardcoded."
- **Título (Show HN) sugerido:** re-enganá-lo para INVERTER a métrica de quantidade em argumento de qualidade:
  > `Show HN: Design Kit — not 149 templates. 158 auditable design tokens + 98 anti-slop checks inside an 8-skill design department.`

### CJ nº2 — QA como diferencial confrontável (98 vs 37)
- Estado atual: material diz "98 checks, nenhum concorrente tem isso" — mas nunca cita o número do adversário na veia.
- **Evidência:** impeccable (o skill de critique mais instalado) expõe em vídeo oficial "37 anti-patterns" por página. Isso permite comparação auditável: 37 (detecções/página) vs 98 (checks determinísticos/14 arquivos).
- **Reforço de copy:**
  > "O padrão de critique mais usado (impeccable) fala em **37 anti-patterns por página**. O Design Kit roda **98 checks determinísticos** em 14 arquivos — e passa antes de shipar (ou o agente não avança). Qualidade não é promessa, é gate."

### CJ nº3 — Consistência numérica (crédito queimado no day-1)
- Casos: plano-descoberta = **7 casos**; material-publicacao = **8 casos**; repo real (docs/casos) = 8 (aurora, brisa, linha-direta, lumen, norte, ponto-final, redesign-demo, tereza).
- Componentes: plano = **15+**; material = **18+**. Só um número é verdade; verificar README/componentes.css mais recente.
- **Licença MIT JÁ decidida** (LICENSE presente) mas material ainda diz "MIT pendente de confirmação".
- taste-skill estrelas: material diz ~46K; pesquisa 2ª ed confirma **78.5K**.
- Open Design: material diz 259+/142+; pesquisa atualizada mostra 19–20 skills/71–142 DS (SkillsLLM) vs 57K★ na conta oficial — re-balançar antes de lançar.
- **Ação:** o Mural precisa de UMA única fonte de verdade de números — a Ficha Técnica do material-publicacao §5 (já tem 8 casos). Alinhar plano-descoberta a ela e remover o já resolvido "pendente de confirmação" (licença já no repositório).

## 6. Fontes (ago/2026)
- a16z News: "Impeccable by Design" (Paul Bakaus) — 40K★/160K installs de skills.sh
- tasteskill.dev · github.com/Leonxlnx/taste-skill (78.5K★) · andrew.ooo review (20/08)
- github.com/nexu-io/open-design (57.4K★) · tecn examplos · nexu-io/html-anything · nexu-io/looper
- claudemarketplaces.com: anthropics/skills frontend-design (792K installs, 170.2K★)
- SkillsLLM: open-design, taste-skill (security scan), designer-skills
- composio.dev/top-design-skills (designer-skills #5 · 63 skills/8 plugins)
- github.com/Owl-Listener/designer-skills (97–107 skills · ai-design-skills · inclusive-design-skills)
- developersdigest.tech: taste skills → agent review as infrastructure
- OpenAgentSkill rankings: google-labs design.md (16K★) · anthropics brand-guidelines (171K★)
- aiskill.market: Nano Banana Pro (77.2K signal image-gen)
- Reddit r/opencodeCLI: 45K+ skills OpenCode-compatible