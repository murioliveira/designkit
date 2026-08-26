# Design Kit — Skill Index

> Se você não sabe por onde começar, este índice organiza as skills do Design Kit **pela situação em que você se encontra**. Escolha a linha onde você está hoje.

## Instalação rápida

```bash
# Recomendado (ecossistema de skills — como o /impeccable)
npx skills add murioliveira/designkit

# Ou, dentro do Claude Code:
/plugin marketplace add murioliveira/designkit
```

Você não precisa saber programar. As skills funcionam dentro de qualquer agente de IA (Claude Code, Codex, pi, Cursor) — você conversa e o agente executa.

---

## Índice por situação

| Situação | Skill a usar | O que ela entrega |
|---|---|---|
| "Tenho só uma ideia solta" | `design-researcher` | Problem statement, persona, jornada, scan competitivo, brief de design |
| "Preciso estruturar a navegação do app" | `information-architect` | Sitemap, fluxos de usuário, hierarquia de conteúdo |
| "Quero gerar as telas da minha landing/app" | `ui-designer` | HTML/CSS/JS consumindo o design system (tokens reais) |
| "Tenho um site antigo pra modernizar" | `design-redesign` | Audit-before-touch, preservar marca vs overhaul, alavancas |
| "Será que essa tela está boa?" | `design-critic` | Critique com 8 heurísticas + cognitive-load + personas + anti-slop |
| "Deixa mais ousado / mais calmo / mais simples" | `design-refine` | bolder / quieter / distill |
| "Preciso que seja acessível" | `a11y-auditor` | Checklist WCAG 2.2 AA, contraste, foco, teclado |
| "A UI está pronta, passo pra dev" | `design-handoff` | Spec de implementação, doc por componente, export de tokens |
| "Quero o fluxo completo de ponta a ponta" | todas, em sequência | research → IA → UI → critique → refine → a11y → handoff |

## Fluxo completo (o "setor de design")

```
brief → research → IA → ⏸️ VOCÊ APROVA → UI v1 → critique → refine
→ a11y/QA → ⏸️ VOCÊ APROVA → handoff
```

O humano é o diretor: você decide o que fazer e aprova em dois checkpoints. O agente é o setor: executa, revisa o próprio trabalho e só avança quando não há blockers.

## Exemplos de prompts (copie e cole)

```
"Crie uma landing page para meu produto de assinatura de café. Público: amantes de café premium."
```
```
"Faça critique desta tela: [cole o HTML]"
```
```
"Meu site é de 2012, quero modernizar sem perder a identidade."
```
```
"Gere o handoff (spec de implementação) das telas que criei."

## Design system dentro do kit

Toda UI gerada consome **tokens reais** (`styles/tokens.css`) — nenhum hex inventado. O critique verifica a regra de tokens mecanicamente. Componentes `components.css` (10 grupos) + block library (`docs/blocos/`).

## Docs
- `DESIGN.md` — a "voz" do kit (manual anti-slop, dials, tudo)
- `README.md` / `README.pt-BR.md` — visão geral e instalação
- `docs/componentes/` — handoff por grupo de componente
- `docs/guia-de-uso.md` — como humanos usam o kit

---

**Pronto para ser usado.** Dê uma ideia, informe o público, e o agente vira o setor de design. Qualquer dúvida de "por onde começo" = pegue o `design-researcher`.