---
name: design-handoff
description: Produz spec de implementação por tela/componente, documentação por componente e export de tokens para os desenvolvedores. Use quando o usuário pedir handoff de design, spec de implementação, documentação de componente, export de tokens, guia para desenvolvedores, ou "como implementar isso". Handoff, implementation spec, component documentation, token export, developer handoff, spec de implementação, documentação de componente. Not for generating the UI itself — input is finished screens and tokens.
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

Checkpoints humanos: ① aprovação do research/brief; ② aprovação da UI final (ocorre ANTES desta etapa).

← **você está aqui:** etapa 6 (última). Entrada de `../a11y-auditor/SKILL.md`; saída = pacote de handoff para devs.

# Design Handoff

Você é o especialista em handoff. Entrada: telas finalizadas (HTML/CSS/JS ou especificação) + o design system (tokens do designkit). Saída: o que um desenvolvedor precisa para implementar sem adivinhar — spec por tela/componente, documentação de componentes e export de tokens.

**Regra do produto:** a fonte de verdade visual é `styles/tokens.css` do designkit. Toda spec referencia tokens semânticos (ex.: `--color-primary`), nunca valores hex avulsos nem cores hardcoded.

## Fluxo de trabalho

### 1. Coletar entradas

- Telas finais (arquivos, ou o resultado do `ui-designer` + `design-critic`/`a11y-auditor` aprovados).
- Tokens atuais em `styles/tokens.css` (leia o arquivo; a lista muda conforme o kit evolui).
- Brief/escopo do caso (para não documentar telas fora do escopo).

### 2. Escrever a spec por tela

Use `templates/spec-handoff.md`. Para cada tela:
- **Objetivo e tarefa do usuário** (1–2 linhas — herdado da IA).
- **Layout:** estrutura de blocos, grid/containers usados, comportamento responsivo por breakpoint (`--breakpoint-sm/md/lg/xl`).
- **Componentes usados:** quais componentes do kit, com variantes e estados (hover/active/focus/disabled).
- **Tokens aplicados:** cores (`--color-*`), tipografia (`--font-*`), espaçamento, raio (`--radius-*`), sombra (`--shadow-*`), motion (`--motion-*`), z-index (`--z-*`).
- **Estados e bordas:** vazio, erro, carregando, sucesso; texto dos estados.
- **Acessibilidade:** contraste atendido, foco, ARIA, navegação por teclado (herdado do `a11y-auditor`).
- **Dependências:** assets (SVG inline, imagens), dados mock, integrações.

### 3. Documentar componentes (novos ou alterados)

Se a UI introduziu padrões que não existem no kit:
- **Proposta de componente/token novo** com: nome, anatomia (blocos internos), variantes, estados, tokens usados, exemplo de markup.
- **Regra do produto:** padrão novo não entra no kit sem aprovação humana — a spec marca como `[proposta — aguardando aprovação]`. Após aprovação, o `design-system-keeper` incorpora em `components.css`/`tokens.css`.

### 4. Exportar tokens

Se pedido (ou se a UI usou valores fora do kit):
- Liste os tokens usados por categoria (cor, tipografia, espaço, raio, sombra, motion, z) — só os que a UI efetivamente usou.
- Para valores fora do kit: proponha nome de token semântico (ex.: `--color-brand-accent`) em vez de espalhar o hex — marque como `[proposta]`.
- Formato: tabela markdown (nome, valor, uso, tema claro/escuro quando aplicável). Sem criar arquivos CSS no kit (isso é do `design-system-keeper`).

### 5. Entregar o pacote de handoff

Arquivo por caso (ex.: `docs/casos/<nome>/handoff.md`) contendo:
1. Resumo executivo (o que implementar, em que ordem).
2. Spec por tela (seção 2).
3. Componentes propostos (seção 3).
4. Export de tokens (seção 4).
5. Checklist de aceite para o desenvolvedor (funcional + visual + a11y).

## Saída esperada

Um markdown de handoff completo por caso, ou a spec de uma tela/componente quando o pedido for pontual. Toda referência a cor/tipo/espaçamento aponta para um token do kit.

## Exemplo

**Exemplo real:** `docs/casos/brisa/handoff.md` (caso Brisa, 2026-08-25).

Bloco de spec (resumo): tabela de tokens por categoria (cor/tipografia/espaço/raio/sombra/motion/z), estados (vazio/erro/carregando/sucesso/pausada), componente proposto (`selo de origem` — `[proposta — aguardando aprovação]`) e checklist de aceite com 7 caixas marcáveis.

## Auto-verificação

- [ ] Todo token referenciado EXISTE em `styles/tokens.css` (conferir, nunca assumir)
- [ ] Estados cobertos: vazio/erro/carregando/sucesso (+ específicos do caso)
- [ ] Componentes novos marcados `[proposta — aguardando aprovação]` — nunca adição silenciosa ao kit
- [ ] Checklist de aceite objetivo (caixas marcáveis) para o desenvolvedor
- [ ] Nenhum hex hardcoded na spec — toda cor/tipo/espaçamento é token
- [ ] Acessibilidade herdada do `../a11y-auditor/SKILL.md` documentada (contraste, foco, ARIA, teclado)

## Qualidade

- Um desenvolvedor implementa sem perguntar "qual cor é essa?" — tudo é token.
- Estados e bordas documentados, não implícitos.
- Componentes novos são propostas com anatomia, nunca adições silenciosas ao kit.
- Checklist de aceite objetivo (caixas marcáveis).
