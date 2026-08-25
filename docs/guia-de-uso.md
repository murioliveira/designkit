# Guia de Uso — seu setor de design em uma caixa

> Para humanos — não-designer, possivelmente não-dev. Este guia mostra como
> usar o **designkit** para gerar UI, designs e critiques a partir do seu
> agente de IA (Claude, Codex, pi ou outro).

## Índice

- [O que é](#o-que-é)
- [O que você pode pedir](#o-que-você-pode-pedir)
- [Como carregar o agente](#como-carregar-o-agente)
- [Fluxo típico passo a passo](#fluxo-típico-passo-a-passo)
- [Como dar um bom brief](#como-dar-um-bom-brief)
- [Perguntas frequentes (FAQ)](#perguntas-frequentes-faq)
- [Glossário](#glossário)

---

## O que é

O **designkit** é um pacote que transforma qualquer agente de IA em um
**setor de design executável**. Em vez de contratar — ou ser — o designer,
o programador e o revisor, você conversa com o seu agente e ele executa o
trabalho de design: pesquisa, arquitetura de informação, telas, crítica,
acessibilidade e o repasse para desenvolvimento.

O humano continua sendo o **diretor**: você decide o que fazer, aprova nos
pontos importantes e dá o rumo. O agente é o **setor**: executa, revisa o
próprio trabalho e só entrega o que passa nos controles de qualidade.

Um limite honesto: pesquisa primária com pessoas reais (entrevistas, testes
de usabilidade, dados analíticos) **não é substituída**. O agente estrutura,
sintetiza e transforma o que você fornece — ele não inventa entrevistas nem
números. O que ele substitui é a *execução* de design: transformar ideia em
brief, brief em telas, telas em critique, e critique em spec pronta para
implementar.

## O que você pode pedir

Você não precisa de jargão. Diga o que quer em linguagem natural. Exemplos
reais, um por papel do setor:

| Papel | Você pede | O que recebe |
|---|---|---|
| **Pesquisa** | "Quero criar um app de organização de refeições para quem mora sozinho. Me ajuda a pensar?" | Problem statement, personas, jornada, scan de concorrência e um brief de design |
| **Arquitetura de informação** | "Com base nesse brief, monte o sitemap e os fluxos do app." | Estrutura de navegação, fluxos de usuário, hierarquia de conteúdo |
| **UI** | "Crie uma landing page para meu produto: um app de organização de refeições. Público: jovens adultos que moram sozinhos." | HTML/CSS/JS das telas, usando os tokens do design system |
| **Crítica** | "Faça critique da minha tela: [cole o HTML ou descreva]." | Review com notas por heurística (clareza, hierarquia, consistência) e lista priorizada de correções |
| **Acessibilidade** | "Audite a acessibilidade deste formulário." | Auditoria WCAG 2.2 AA (contraste, foco, teclado, leitores de tela) com correções |
| **Handoff** | "Gere o spec de implementação dessas telas para o dev." | Spec por tela/componente, documentação e export dos tokens |

Exemplos prontos de prompt:

```text
Crie uma landing page para meu produto: um app de organização de refeições
para quem mora sozinho. Público: jovens adultos (25–35), que cozinham pouco
e comem comida entregue. Tom: calmo, acolhedor, nada de "startup hype".
```

```text
Faça critique da minha tela abaixo. Eu quero saber o que está confuso, o que
está bom, e uma lista do que corrigir primeiro.

[cole aqui o HTML/CSS ou uma descrição detalhada da tela]
```

```text
Audite a acessibilidade deste formulário de cadastro e corrija o que estiver
em nível AA do WCAG.
```

```text
Gere o spec de handoff da landing page que aprovamos: o que o dev precisa
para implementar, componente por componente, usando os tokens do designkit.
```

## Como carregar o agente

O designkit é um diretório de **skills** + um arquivo de **onboarding**
(`AGENTS.md`). Você o entrega ao seu agente de IA e ele passa a agir como o
setor de design.

### No pi (recomendado para começar)

```bash
# 1. Coloque as skills do designkit onde o pi as descobre
#    (ex.: copie a pasta skills/ para ~/.pi/agent/skills/designkit/ )
# 2. Rode o pi dentro do diretório do designkit (ele lê AGENTS.md)
pi
```

Pronto. A partir daí, o `pi` sabe usar `design-researcher`,
`information-architect`, `ui-designer`, `design-redesign`, `design-critic`,
`design-refine`, `a11y-auditor` e `design-handoff`.

### No Claude Code

O pacote já traz `CLAUDE.md` (onboarding) e `.claude/skills/` (wrappers de
descoberta apontando para as skills originais em `skills/`).

1. Abra o Claude Code no diretório do projeto — ele lê `CLAUDE.md` e descobre
   as skills em `.claude/skills/` automaticamente.
2. Peça o que quiser (veja a seção *O que você pode pedir*).

> **Portabilidade:** os wrappers em `.claude/skills/` não duplicam conteúdo —
> apontam para `skills/<nome>/SKILL.md`, a fonte única. Se você copiar o
> designkit para outro projeto, leve `CLAUDE.md`, `.claude/skills/`, `skills/`
> e `templates/` juntos.

### No Codex (OpenAI)

O pacote já traz `AGENTS.md` (formato nativo do Codex) e `.codex/README.md`
com as instruções de portabilidade.

1. Abra o Codex no diretório do projeto — ele lê `AGENTS.md` automaticamente.
2. As skills ficam em `skills/` e são lidas sob orientação do `AGENTS.md` na
   etapa correspondente do fluxo. Veja `.codex/README.md` para detalhes (e para
   o caminho opcional de skills nativas do Codex).
3. Use os prompts da seção anterior.

> **Portabilidade:** o mesmo diretório de skills funciona nos três. A única
> adaptação é o arquivo de onboarding (`AGENTS.md` → `CLAUDE.md` no Claude
> Code). Cursor usa `.cursor/rules`; a adaptação é equivalente.

## Fluxo típico passo a passo

Para um projeto de tela (ex.: landing page, app), o agente percorre o fluxo
em fases. Você aprova em dois pontos importantes:

```
1. BRIEF → 2. RESEARCH → 3. CONCEPT/IA → ⏸️ VOCÊ APROVA → 4. UI v1
→ 5. CRITIQUE → 6. REFINE → 7. A11Y/QA → ⏸️ VOCÊ APROVA → 8. HANDOFF
```

1. **Brief** — você conta a ideia (pode ser uma frase). Use o modelo
   [`templates/brief.md`](../templates/brief.md) se quiser.
2. **Research** — o `design-researcher` devolve problem statement, personas,
   jornada e scan de concorrência. Dados que faltam viram `[assunção]`
   explícita.
3. **Concept / Arquitetura de informação** — o `information-architect` monta
   sitemap e fluxos.
4. **⏸️ Checkpoint 1** — *você* aprova o rumo antes de qualquer tela. Mudou
   algo? Ajuste aqui (é mais barato do que depois).
5. **UI v1** — o `ui-designer` gera as telas consumindo **somente** os tokens
   do design system.
6. **Critique** — o `design-critic` revisa com notas e lista priorizada.
   Loops fechados: corrigir → re-revisar → seguir (no máximo 2 rodadas antes
   de te consultar).
7. **A11y/QA** — o `a11y-auditor` audita contraste, foco, teclado e
   semântica; o QA visual confere responsividade.
8. **⏸️ Checkpoint 2** — *você* aprova as telas finais.
9. **Handoff** — o `design-handoff` produz o spec de implementação e a
   documentação por componente.

Você pode pular etapas: já tem telas e só quer critique? Vá direto ao passo 6.
Só quer a UI a partir de um brief? Os passos 2–3 são curtos e melhoram o
resultado — vale a pena na primeira vez.

## Como dar um bom brief

Quanto melhor o brief, melhor (e mais rápido) o resultado. O essencial:

- **Ideia em uma frase** — o que é, do jeito que um amigo entenderia.
- **Para quem** — o público principal (idade, contexto, o que ele quer fazer).
- **O problema** — o que está ruim hoje / o que falta para esse público.
- **O que já existe** — concorrentes ou referências que você admira.
- **Restrições** — plataforma (web/mobile), prazo, tecnologia, marca/cores se
  já definidos.
- **Sucesso** — como você saberá que funcionou.
- **Fora de escopo** — o que NÃO deve entrar na primeira versão.

O que você não souber pode ficar em branco: o agente marca como `[assunção]`
e te pergunta ou propõe como validar — ele não inventa.

## Perguntas frequentes (FAQ)

**Preciso saber programar?**
Não. O agente gera o código (HTML/CSS/JS) e você abre no navegador. Para ver
o resultado, peça o arquivo e abra com duplo clique — sem instalar nada.

**Posso usar sem o design system?**
Sim, mas perde consistência. O design system (tokens + componentes) é o que
garante que todas as telas pareçam do mesmo produto — cores, espaçamentos,
tipografia e raios padronizados. Sem ele, cada tela vira um "design novo".

**E se eu não gostar do resultado?**
Peça refine com feedback específico: "o título está muito grande", "quero
mais espaço entre os cards", "essa cor não combina com o resto". O agente
itera e o critique roda de novo até não haver problemas.

**O agente roda sozinho?**
Não — ele precisa de um agente-hospedeiro (Claude, Codex, pi). O designkit é
o que você *carrega* nesse agente. E mesmo dentro do fluxo, há dois
checkpoints seus antes de avançar: o agente não entrega telas finais sem a
sua aprovação.

**O agente substitui pesquisas com usuários reais?**
Não. Entrevistas, testes e dados de uso continuam sendo coletados por
pessoas. O agente sintetiza e estrutura o que você trouxer — e marca o que
faltar como `[assunção]`.

**Posso pedir apenas uma parte?**
Sim — critique de uma tela, auditoria de acessibilidade de um formulário,
spec de handoff de telas prontas. Cada skill funciona isolada.

**Isso gera imagens/ilustrações?**
Na v1, não: as telas usam HTML/CSS e SVG procedurais. Ilustrações e fotos
reais ficam de fora (decisão em aberto no roadmap).

**Qual a diferença entre este guia e o AGENTS.md?**
O `AGENTS.md` é o manual *do agente* — instrui o agente-hospedeiro a agir
como o setor de design. Este guia é o manual *seu* — como pedir, aprovar e
usar o que ele entrega.

## Glossário

| Termo | Significado |
|---|---|
| **Tokens** | Variáveis de design (`--color-primary`, `--space-4`…) que centralizam cor, espaçamento, tipografia e raios. São a "fonte de verdade" visual do kit. |
| **Design system** | O conjunto tokens + componentes + regras que mantém todas as telas consistentes entre si. |
| **Critique** | Revisão crítica de um design com notas por heurística e lista priorizada de correções — o "olhar de designer sênior" no seu resultado. |
| **Handoff** | O repasse do design para desenvolvimento: spec por tela/componente, documentação e export de tokens — o que o dev precisa para implementar sem adivinhar. |
| **WCAG** | Web Content Accessibility Guidelines — diretrizes de acessibilidade web. Nível **AA** é o padrão de referência (contraste, foco, teclado, leitores de tela). |
| **Persona** | Perfil fictício e realista de um usuário-tipo do produto, usado para guiar decisões de design. |
| **Jornada** | Sequência de passos que o usuário percorre para completar uma tarefa no produto. |
| **Sitemap** | Mapa das páginas/telas do produto e como se conectam. |
| **Problem statement** | Declaração clara do problema que o produto resolve e para quem. |
| **Brief** | O pedido inicial: ideia, público, contexto e restrições do que você quer criar. |
| **[assunção]** | Marcação usada pelo agente quando um dado necessário não foi informado — ele sinaliza em vez de inventar. |
