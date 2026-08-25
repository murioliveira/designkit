# Distribuição — checklist de release v1.0.0

> Fase F do roadmap (docs/arquitetura-agente-design.md). Este documento é o
> checklist do que validar, como empacotar e por onde distribuir o Design Kit
> antes de declarar a versão 1.0.0. Última revisão: 2026-08-25.

## Estado atual (v0.9.0)

- ✅ Design system completo (tokens + componentes + showcase vivo)
- ✅ 6 skills empacotadas com templates
- ✅ Onboarding para pi, Claude Code e Codex
- ✅ Caso Lumen ponta a ponta (critique aprovado 4.7/5)
- ✅ Docs: arquitetura, guia de uso, componentes, este checklist
- ⏳ **Falta para o 1.0.0:** Fase E (validação multi-agente) + decisões do fundador + licença/nome

---

## 1. Antes do release — gates obrigatórios

### 1.1 Fase E: validação multi-agente (bloqueia 1.0.0)

| # | Validação | Agente | Critério de aceite |
|---|---|---|---|
| E1 | Rodar o fluxo completo (brief → research → IA → UI → critique → refine → handoff) num mini-caso novo | pi | Fluxo executa sem intervenção além dos checkpoints; artefatos completos |
| E2 | Mesmo mini-caso | Claude Code | Mesma qualidade aproximada (média de critique ≥ 4/5, sem blockers) |
| E3 | Mesmo mini-caso | Codex | Mesma qualidade aproximada |
| E4 | Skill isolada em cada agente (ex.: só critique, só a11y) | 3 agentes | Cada wrapper funciona com fallback embutido sem `impeccable`/`web-design-engineer` |

> Resultado esperado: relatório comparativo por agente em `docs/validacao-multi-agente.md`
> (a criar na Fase E), com evidência de cada execução.

### 1.2 Decisões do fundador (bloqueiam 1.0.0)

Definidas em docs/arquitetura-agente-design.md §5; precisam de resposta explícita:

1. **Agentes-alvo prioritários** — pi, Claude Code, Codex, Cursor? (define o
   README/quickstart e onde investir na Fase E).
2. **Escopo de pesquisa** — só síntese, ou também roteiros de entrevista para o
   humano conduzir? (recomendação da arquitetura: roteiros + síntese, coleta humana).
3. **Geração de imagens** — v1 sem geração externa (SVG inline + placeholders) ou
   incluir API de imagem? (recomendação: v1 sem).
4. **Open-source vs comercial** — impacta licença, vitrine e roadmap de distribuição.
5. **Nome do produto** — "Design Kit" é provisório; decidir antes do README final.
6. **Limite ético** — texto de posicionamento sobre pesquisa primária não
   substituída (já rascunhado no README; validar tom com o fundador).

### 1.3 Qualidade e licença

- [ ] Revisar o texto de licença (placeholder MIT no README) — confirmar ou trocar.
- [ ] Confirmar o nome do produto em todo o pacote (README, AGENTS.md, guia-de-uso).
- [ ] `docs/guia-de-uso.md` revisado por um não-designer (teste de legibilidade).
- [ ] Showcase aberto no navegador (duplo clique) — sem console errors, sem 404.
- [ ] `prefers-reduced-motion` e tema claro/escuro conferidos no showcase e no caso Lumen.

---

## 2. Como empacotar

O pacote é a pasta `designkit/` inteira (sem build, sem dependências — o
".zip" é só conveniência de distribuição).

### 2.1 O que entra

```
AGENTS.md, CLAUDE.md, README.md
index.html, js/, styles/
skills/          (6 skills + templates)
templates/       (3 modelos)
docs/            (arquitetura, guia-de-uso, distribuicao, componentes, casos/lumen)
.claude/skills/  (wrappers de descoberta para Claude Code)
.codex/          (instruções de portabilidade)
.gitignore
```

### 2.2 O que fica de fora (exclusões)

- `.maestri/` — configuração interna do canvas Maestri (não faz parte do produto).
- `.git/`, `node_modules/`, `*.log`, `.DS_Store` (já cobertos pelo `.gitignore`).
- Sessões/arquivos temporários de agente (`~/.pi/...` nunca entra).

### 2.3 Comando sugerido (release)

```bash
# dentro de C:/Users/muzph/projetos/designkit (ou no checkout git)
git archive --format=zip --prefix=designkit-v1.0.0/ -o designkit-v1.0.0.zip HEAD
```

> Alternativa sem git: `zip -r designkit-v1.0.0.zip . -x ".maestri/*" ".git/*"`.

### 2.4 Verificação pós-empacotamento

- [ ] Extrair o zip em pasta limpa e abrir `index.html` no navegador — showcase funcional.
- [ ] Abrir `docs/guia-de-uso.md` — links relativos resolvem (`../templates/brief.md` etc.).
- [ ] Conferir que `skills/` e `.claude/skills/` apontam para os mesmos arquivos
      (os wrappers do Claude Code referenciam `skills/<nome>/SKILL.md`).
- [ ] `grep -r "designkit"` no zip — caminhos/links consistentes com o prefixo escolhido.

---

## 3. Canais de distribuição sugeridos

| Canal | O quê | Quando |
|---|---|---|
| **GitHub (público ou privado)** | Repositório do pacote + releases (`v1.0.0` com o zip) | No 1.0.0 |
| **Vitrine do showcase** | Abrir `index.html` (GitHub Pages ou arquivo local) como "portfólio" do agente — o showcase É a demonstração do que o kit produz | Desde já |
| **Guia de uso** | `docs/guia-de-uso.md` como página de onboarding (README aponta para ela) | No 1.0.0 |
| **Caso Lumen** | `docs/casos/lumen/` como prova real de resultado | Desde já |

> Depende da decisão open-source vs comercial (§1.2). Se open-source: README +
> LICENSE + issues para o backlog público. Se comercial: vitrine + contato +
> roadmap de venda.

---

## 4. Pós-1.0.0 (backlog aberto)

- Ampliar componentes (paginação — dropdown, breadcrumb, tabela e stepper já existem).
- Nova rodada de auditoria a11y profunda no kit completo.
- Skills de visual-qa (browser) e design-system-keeper (extract de tokens).
- Validação no Cursor (`.cursor/rules`) e/ou outros agentes-alvo decididos.
- Testes de fumaça automatizados (opcional — hoje o projeto é sem build por escolha).
