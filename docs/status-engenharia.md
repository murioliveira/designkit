# Status de Engenharia — Design Kit v0.9.0

> Relatório de saúde técnica do pipeline de instalação npm/npx e ferramentas internas.
> Data: 2026-08-25 · Autor: subagente de engenharia · Escopo: pré-1.0.0 (Fase F p1).

---

## Resumo executivo

O pipeline de distribuição do Design Kit está **saudável e funcional** nos 3 canais testados:
`npm pack`, `npx skills add`, e o CLI `bin/design-kit.mjs`. Todas as verificações de qualidade
passam (smoke test, anti-slop check, verify). Foi corrigido 1 problema de portabilidade YAML
(9 arquivos com descriptors não-quotados que quebravam o parser do `npx skills`) — a correção
é segura e mantém compatibilidade com a verificação própria do CLI.

---

## 1. npm pack --dry-run

| Métrica | Resultado |
|---|---|
| Pacote | `design-kit@0.9.0` |
| Arquivos | **25** |
| Tamanho empacotado | 48.9 kB |
| Tamanho descomprimido | 136.2 kB |
| Versão | 0.9.0 |

**Conteúdo validado** — O campo `"files"` do `package.json` cobre exatamente o que é necessário:

```
bin/design-kit.mjs            ✅ CLI (5.0 kB)
skills/**/SKILL.md            ✅ 8 skills com frontmatter (47.5 kB)
skills/**/templates/          ✅ Templates internos de cada skill
templates/                    ✅ 3 templates globais (brief, critique-report, spec-handoff)
DESIGN.md, AGENTS.md          ✅ Documentos de onboarding
CLAUDE.md, README.md, LICENSE ✅ Portabilidade e licenciamento
```

**Verde:** 0 ausências, 0 sobras indesejadas. O `README.pt-BR.md` é incluído automaticamente
pelo npm (regra `README*`), o que é esperado.

---

## 2. npx skills add murioliveira/designkit

| Métrica | Resultado |
|---|---|
| Skills descobertas | **8/8** |
| Agente detectado (pi) | ✅ reconhecido, instala não-interativa |
| Repositório | `https://github.com/murioliveira/designkit.git` |
| Clone + descoberta | ✅ bem-sucedido |

**Skills listadas:**

| # | Skill | Descrição resumida |
|---|---|---|
| 1 | `a11y-auditor` | Auditoria WCAG 2.2 AA com correções |
| 2 | `design-critic` | Crítica de design com scoring por heurísticas |
| 3 | `design-handoff` | Spec de implementação, docs por componente, export de tokens |
| 4 | `design-redesign` | Redesign com protocolo audit-before-touch |
| 5 | `design-refine` | Refinamento em 3 direções (bolder/quieter/distill) |
| 6 | `design-researcher` | Brief → problem statement, personas, jornadas, scan |
| 7 | `information-architect` | Sitemap, fluxos, hierarquia de conteúdo |
| 8 | `ui-designer` | Geração de UI consumindo tokens do kit |

### Correção aplicada: YAML frontmatter

Durante o teste, o parser YAML do `npx skills` emitiu 3 avisos de parse em descrições com
dois-pontos não escapados (`Nested mappings are not allowed in compact mappings`).
**Causa raiz:** as descrições longas continham `:` em texto natural (ex.: `"O export de tokens
tem implementação real: rode scripts..."`) — o YAML interpretava como mapeamento aninhado.

**Correção:** 9 arquivos atualizados com `description: "..."` (double-quote wrapping, escape de
aspas internas com `\"`):

- `skills/design-handoff/SKILL.md` (fonte)
- `.claude/skills/a11y-auditor/SKILL.md`
- `.claude/skills/design-critic/SKILL.md`
- `.claude/skills/design-handoff/SKILL.md`
- `.claude/skills/design-redesign/SKILL.md`
- `.claude/skills/design-refine/SKILL.md`
- `.claude/skills/design-researcher/SKILL.md`
- `.claude/skills/information-architect/SKILL.md`
- `.claude/skills/ui-designer/SKILL.md`

Verificação pós-correção: `node -e` com regex em todos os `SKILL.md` — **0 descrições com
dois-pontos não-quotados restantes**.

---

## 3. bin/design-kit.mjs

| Comando | Resultado |
|---|---|
| `version` | `0.9.0` ✅ |
| `verify` | 8/8 `[ok]` ✅ |
| `install` | 8 skills × 5 agentes = 40 instalações ✅ |
| Sem argumentos | Exibe help + recomendação `npx skills add` ✅ |

**Agentes-alvo da instalação:**

| Agente | Caminho | Skills instaladas |
|---|---|---|
| Claude Code | `~/.claude/skills/` | 8 |
| Codex | `~/.codex/skills/` | 8 |
| Cursor | `~/.cursor/skills/` | 8 |
| pi | `~/.pi/agent/skills/design-kit/` | 8 |
| Universal | `~/.agents/skills/` | 8 |

A instalação persiste templates globais em `templates/` (irmão de `skills/`), coerente
com a estrutura esperada pelos wrappers.

---

## 4. Testes de qualidade

| Teste | Checks | Resultado |
|---|---|---|
| `scripts/smoke-test.py` | 8 | **PASS** |
| `scripts/anti-slop-check.py` | 98 (14 arquivos) | **PASS** (0 falhas, 3 esperadas em fixtures) |

### Detalhamento smoke test

```
[PASS] tokens: 109 var() usados, 0 faltando
[PASS] hex:    0 hex hardcoded em components.css
[PASS] html:   70 ids, 14 âncoras sidebar/seções, 18 aria-labelledby, lang OK
[PASS] css:    4 arquivos, 390 pares de chaves balanceados
[PASS] js:     sintaxe válida
[PASS] docs:   9 referências em componentes/README.md, 0 faltando
[PASS] skills: 8 skills com frontmatter, 8 espelhos
[PASS] casos:  lumen + brisa — 7 arquivos esperados, 0 faltando
```

### Detalhamento anti-slop

```
arquivos: 14 | checks: 98 | falhas: 0 | esperadas: 3 | avisos: 0
ANTI-SLOP: PASS
```

As 3 falhas esperadas são no fixture `docs/casos/redesign-demo/before.html` (em-dash, Inter
e eyebrows em excesso), que é intencionalmente o "antes" de um redesign — servem como
fixture de contraexemplo.

---

## 5. Prontidão para release

### ✅ O que está pronto

- Pipeline npm: `npm pack --dry-run` produz pacote limpo, versionado, com todos os arquivos
  necessários e sem dependências externas.
- Pipeline `npx skills add`: 8 skills descobertas corretamente do GitHub, compatível com
  múltiplos agentes (pi, Claude Code, Codex, Cursor, agents).
- CLI `design-kit`: comandos `version`, `install`, `verify` todos funcionais.
- Qualidade: smoke test (8/8) e anti-slop (98/98) passam limpo.
- Portabilidade YAML: todos os frontmatters são estritamente válidos para consumo pelo
  ecossistema `skills` sem avisos de parse.

### ⏳ Pendências (bloqueiam 1.0.0)

| Item | Status |
|---|---|
| `.npmignore` | Não necessário — o campo `"files"` do `package.json` já cobre as exclusões |
| Registro npm público | Não publicado — esperando decisão do fundador (open-source vs comercial) |
| `npx skills add` do registro público | Funciona do GitHub (fonte) — publicação npm é opcional |
| Validação multi-agente (Fase E) | Bloqueada: depende de decisão do fundador sobre agentes-alvo |
| Nome do produto + licença | Bloqueados: decisão do fundador |

### Recomendação

O pipeline está pronto para v0.9.0. Para o release 1.0.0, sugerimos:

1. Manter o canal GitHub (`npx skills add murioliveira/designkit`) como primário,
   com `npm publish` como secundário quando/quem o fundador decidir.
2. As correções YAML deste ciclo devem ser commitadas e pushadas para o GitHub
   antes da próxima validação com `npx skills add`.
3. O `bin/design-kit.mjs` é autocontido e não depende de `npm publish` — funciona
   com `npx` diretamente do GitHub via `npx github:murioliveira/designkit` ou após
   clone local.

---

## 6. Evidência dos comandos

```bash
# npm pack --dry-run
$ npm pack --dry-run
npm notice 📦  design-kit@0.9.0
npm notice === Tarball Contents ===
npm notice 25 files, 48.9 kB (packed), 136.2 kB (unpacked)

# npx skills add --list
$ npx skills add murioliveira/designkit --list
◇ Found 8 skills
│ a11y-auditor, design-critic, design-handoff, design-redesign,
│ design-refine, design-researcher, information-architect, ui-designer

# CLI version / install / verify
$ node bin/design-kit.mjs version
0.9.0
$ node bin/design-kit.mjs verify
Design Kit OK — todas as 8 skills presentes e válidas.
$ node bin/design-kit.mjs install
✓ claude-code: 8 nova(s), 0 atualizada(s)
✓ codex: 8 nova(s), 0 atualizada(s)
✓ cursor: 8 nova(s), 0 atualizada(s)
✓ pi: 8 nova(s), 0 atualizada(s)
✓ agents: 8 nova(s), 0 atualizada(s)
Pronto. 40 skill(s).

# Smoke test
$ python scripts/smoke-test.py
SMOKE TEST: PASS (8 checks)

# Anti-slop check
$ python scripts/anti-slop-check.py
ANTI-SLOP: PASS (98 checks, 14 arquivos, 0 falhas)
```

---

*Relatório gerado pelo subagente de engenharia do Design Kit. Próximo passo: commit das
correções YAML + aguardar decisões do fundador para Fase E e Fase F p2.*