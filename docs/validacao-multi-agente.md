# Validação de Portabilidade Multi-Agente (Fase E p3)

**Data:** 2026-08-25 · **Método:** validação estática da correção de portabilidade (sem executar Claude Code/Codex — não instalados). Fonte única: `skills/`. Verificação: leitura dos 8 wrappers `.claude/skills/*/SKILL.md`, comparação `CLAUDE.md` ↔ `AGENTS.md`, leitura `.codex/README.md`, `docs/guia-de-uso.md` §3, regras de descoberta do pi (docs do pi, v0.84.3).

---

## 1. Claude Code

### 1.1 Wrappers `.claude/skills/` — CORRETOS

Verificação mecânica dos 8 wrappers (por leitura):

| Wrapper | Caminho apontado | Frontmatter | Veredito |
|---|---|---|---|
| a11y-auditor | `../../skills/a11y-auditor/SKILL.md` ✅ | name=a11y-auditor (válido) ✅ | OK |
| design-critic | `../../skills/design-critic/SKILL.md` ✅ | name=design-critic ✅ | OK |
| design-handoff | `../../skills/design-handoff/SKILL.md` ✅ | name=design-handoff ✅ | OK |
| design-redesign | `../../skills/design-redesign/SKILL.md` ✅ | name=design-redesign ✅ | OK |
| design-refine | `../../skills/design-refine/SKILL.md` ✅ | name=design-refine ✅ | OK |
| design-researcher | `../../skills/design-researcher/SKILL.md` ✅ | name=design-researcher ✅ | OK |
| information-architect | `../../skills/information-architect/SKILL.md` ✅ | name=information-architect ✅ | OK |
| ui-designer | `../../skills/ui-designer/SKILL.md` ✅ | name=ui-designer ✅ | OK |

- Caminho `../../skills/<nome>/SKILL.md` resolve de `.claude/skills/<nome>/` → `skills/<nome>/SKILL.md` no repo. **8/8 corretos.**
- Formato Claude Code válido: frontmatter `name` (minúsculo, hífens, = nome do diretório) + `description`; sem caracteres inválidos. **8/8 válidos.**
- Espelho 1:1 confirmado pelo `smoke-test.py` ("8 skills com frontmatter, 8 espelhos" — PASS).

### 1.2 CLAUDE.md ↔ AGENTS.md — DIVERGÊNCIAS (CLAUDE.md defasado)

| # | Local | Divergência | Correção sugerida |
|---|---|---|---|
| D1 | CLAUDE.md:62 | "index.html (13 seções)" — o index.html tem 14 seções (paginação adicionada) | atualizar para "14 seções" |
| D2 | CLAUDE.md tabela de fluxo | lista 6 skills (researcher, IA, ui-designer, critic, a11y, handoff) — **omite design-redesign e design-refine** (existem em skills/ e .claude/skills/) | adicionar as 2 linhas na tabela |
| D3 | CLAUDE.md:56-66 estrutura | estrutura resumida omite DESIGN.md, scripts/, docs/blocos/, docs/reference/, docs/auditoria-comparativa*, casos novos (aurora, linha-direta, redesign-demo), .codex/README | espelhar estrutura atual do AGENTS.md |
| D4 | CLAUDE.md "Estado atual" | diz "Fases 1–4 ✅ · Lumen ✅ · Skills (B) ✅ · Guia (C) ✅ · Portabilidade (E p1) ✅ · E p2 pendente · Distribuição (F) pendente" — **E p2 já validado no pi (4/4 skills, caso Brisa)**; kit publicado no GitHub (v0.9.0) | atualizar estado: E p2 ✅ parcial, F p1 ✅, publicações |
| D5 | CLAUDE.md | **não menciona DESIGN.md** (voz de design obrigatória no AGENTS.md) nem o DON'T da Liquid | adicionar referência ao DESIGN.md e ao DON'T |
| D6 | AGENTS.md:32 vs :80 | AGENTS.md internamente inconsistente: estrutura diz "14 seções" (linha 32), backlog Fase 2 diz "13 seções" (linha 80) | alinhar para 14 seções |

Nota: AGENTS.md:41 e :90 ainda dizem "6 wrappers" — hoje são 8. (correção menor)

### 1.3 Passos de carregamento (guia-de-uso §3 "No Claude Code")

- "Abra o Claude Code no diretório do projeto — ele lê CLAUDE.md e descobre as skills em .claude/skills/ automaticamente." **FACTÍVEL e correto** (Claude Code descobre `.claude/skills/*/SKILL.md`).
- "Leve CLAUDE.md, .claude/skills/, skills/ e templates/ juntos" — **correto** (wrappers apontam para skills/ relativo).

## 2. Codex

### 2.1 Formato AGENTS.md

- `AGENTS.md` na raiz é o formato nativo de onboarding do Codex ✅. `.codex/README.md` documenta o acesso às skills.
- **Caminho A (recomendado, documentado):** AGENTS.md instrui o agente a ler `skills/<nome>/SKILL.md` na etapa do fluxo; skills auto-contidas (sem dependência de web-design-engineer/impeccable — fallback embutido). **FACTÍVEL.**
- **Caminho B (opcional):** copiar `skills/<nome>/SKILL.md` para `.codex/skills/<nome>.md`. **Sugestão de ajuste:** o `.codex/README.md` diz "o diretório que a versão atual do Codex usar para skills" — vago; citar o caminho canônico atual (config-codex: `~/.codex/skills/` ou `.codex/skills/` do projeto) para factibilidade imediata.

### 2.2 Passos concretos para um usuário Codex

1. Clone o repo / copie o diretório do designkit.
2. Abra o Codex no diretório (lê AGENTS.md; pronto para atuar como setor de design).
3. Peça em linguagem natural ("faça critique dessa tela"); o AGENTS.md guia a leitura da skill certa.
4. (Opcional, Caminho B) copie as skills para `.codex/skills/` para descoberta nativa.

## 3. pi

- pi lê `AGENTS.md` + `DESIGN.md` (+ `CLAUDE.md`) quando roda no diretório do projeto (contexto).
- **Descoberta de skills no pi** (docs pi v0.84.3 §Skill Locations): global `~/.pi/agent/skills/`, `~/.agents/skills/`; projeto (após trust) `.pi/skills/`, `.agents/skills/` no cwd e ancestrais; packages `skills/` + `pi.skills` em package.json. **O diretório raiz `skills/` do projeto NÃO é local de descoberta automática do pi** (só `.pi/skills/`/`.agents/skills/` ou global).
- **Na prática (Caminho A, igual Codex):** AGENTS.md instrui a ler `skills/<nome>/SKILL.md` como markdown — funciona sem registro formal. Guia-de-uso §3 "No pi" orienta "copie skills/ para ~/.pi/agent/skills/designkit/" — esse caminho (global) É descoberto pelo pi ✅ (factível e correto).
- Ajuste menor: com a cópia global, as skills viram `/skill:nome`; sem cópia, funcionam via instrução do AGENTS.md. Ambos válidos; documentar a distinção.

## 4. Checklist final de portabilidade

| Hospedeiro | O que carrega | Como descobre | O que falta | Veredito |
|---|---|---|---|---|
| **pi** | AGENTS.md, DESIGN.md (contexto); skills/ (via cópia global `~/.pi/agent/skills/designkit/` ou leitura sob orientação do AGENTS.md) | Global `~/.pi/agent/skills/`; contexto de projeto | Nenhum (cópia opcional para /skill:nome) | **PRONTO** |
| **Claude Code** | CLAUDE.md (onboarding), .claude/skills/ (8 wrappers), skills/ (fonte) | `.claude/skills/*/SKILL.md` automático | CLAUDE.md defasado (D1–D5) | **PRECISA DE AJUSTE** (docs, não estrutura) |
| **Codex** | AGENTS.md (onboarding), skills/ (leitura sob orientação) | Não há skill-discovery nativo documentado; Caminho A via AGENTS.md | Citar caminho canônico de skills do Codex (Caminho B) | **PRONTO** |

## 5. Achados consolidados

- **Blocker:** nenhum — toda a estrutura de portabilidade (wrappers, caminhos relativos, frontmatter) está correta e verificada por smoke-test.
- **Maior (docs):** CLAUDE.md defasado vs AGENTS.md (D1–D5): 13→14 seções, 6→8 skills na tabela, estrutura omissa, estado desatualizado, sem DESIGN.md/DON'T. Não quebra o funcionamento (wrappers apontam certo), mas o onboarding do Claude Code fica incompleto/incorreto.
- **Menor:** AGENTS.md inconsistência interna (13 vs 14 seções; "6 wrappers" → 8); .codex/README.md com caminho vago para Caminho B; guia-de-uso lista 6 skills no fluxo do pi (idem D2).

## Resumo (10 linhas)

1. Portabilidade estrutural íntegra: 8 wrappers `.claude/skills/` apontam para o caminho relativo correto `../../skills/<nome>/SKILL.md` com frontmatter válido; smoke-test confirma espelho 1:1.
2. pi: PRONTO — AGENTS.md/DESIGN.md no contexto do projeto; cópia global opcional para `/skill:nome`.
3. Codex: PRONTO — AGENTS.md nativo + `.codex/README.md` com Caminho A factível; Caminho B com caminho vago a especificar.
4. Claude Code: PRECISA DE AJUSTE (somente documental) — CLAUDE.md defasado em 5 pontos vs AGENTS.md (seções, skills na tabela, estrutura, estado, DESIGN.md/DON'T).
5. Divergência mais visível: CLAUDE.md omite design-redesign e design-refine da tabela de fluxo — 2 das 8 skills ficam invisíveis no onboarding.
6. Nenhuma correção aplicada (escopo: reportar ao orquestrador). Divergências com localização e correção na seção 1.2.
7. Sem execução de Claude Code/Codex (não instalados) — validação estática; a execução real permanece Fase E p3-runtime.
8. Risco residual: se o orquestrador decidir aplicar, as edições são textuais em CLAUDE.md/AGENTS.md/.codex/README/guia-de-uso.
9. Check adicional: DESIGN.md é a "voz" obrigatória — sua ausência no CLAUDE.md é o gap funcional mais relevante para qualidade do output.
10. Veredito por hospedeiro: **pi PRONTO · Claude Code PRECISA DE AJUSTE (docs) · Codex PRONTO**.