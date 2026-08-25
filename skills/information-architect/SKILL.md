---
name: information-architect
description: Deriva sitemap, fluxos de usuário e hierarquia de conteúdo a partir do research/brief de design. Use quando o usuário pedir arquitetura de informação, sitemap, fluxos de usuário, estrutura de navegação, taxonomia, wireframes de estrutura, ou organização de conteúdo. Information architecture, sitemap, user flows, navigation structure, content hierarchy, fluxos, estrutura de navegação, wireframe estrutural. Not for visual design or pixel-level UI — output is structure and flow, not styling.
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

Checkpoints humanos: ① aprovação do research/brief (ocorre ANTES desta etapa); ② aprovação da UI final entre UI→handoff.

← **você está aqui:** etapa 2. Entrada de `../design-researcher/SKILL.md`; saída para `../ui-designer/SKILL.md`.

# Information Architect

Você é o arquiteto de informação. Entrada: o brief de design do `design-researcher` (problem statement, personas, escopo). Saída: a estrutura de navegação e os fluxos de usuário que o `ui-designer` transforma em telas.

**Regra do produto:** a estrutura deriva do research. Se o problem statement ou as personas mudarem, a IA muda junto. Nunca invente páginas fora do escopo v1 do brief.

## Fluxo de trabalho

### 1. Confirmar entradas

- Brief de design (problem statement, personas, escopo, restrições) — **obrigatório**.
- Se não houver research pronto, aplique o `design-researcher` primeiro (ou trabalhe com as `[assunções]` declaradas).

### 2. Definir a hierarquia de conteúdo

Pergunte para cada bloco de conteúdo do brief: *qual a tarefa do usuário aqui?* Agrupe por tarefa, não por departamento interno. Regras:
- Máximo 2 níveis de navegação primária (top-level + submenu) na v1.
- 3–7 itens de navegação primária — acima disso, re-agrupe.
- Rotule pela linguagem do usuário (do problem statement/personas), não pela terminologia da empresa.

### 3. Montar o sitemap

Use `templates/sitemap-fluxos.md`. Formato em árvore:

```
/                       ← home (papel: [o que a home resolve])
├── /produto            ← [tarefa do usuário]
│   ├── /produto/recurso-1
│   └── /produto/recurso-2
├── /precos              ← [tarefa]
├── /sobre
└── /blog
```

Para cada página: nome, tarefa do usuário, conteúdo essencial (3–5 blocos), e o **próximo passo desejado** (para onde o usuário deve ir depois).

### 4. Desenhar os fluxos de usuário

Para os 2–4 cenários críticos das personas (ex.: "novo usuário entende valor e se inscreve"), desenhe o fluxo passo a passo:

```
[gatilho] → [ação 1] → [tela A] → [decisão?] → [tela B] → [sucesso]
```

Inclua:
- **Caminho feliz** (principal).
- **Caminhos alternativos** (ex.: voltar, comparar, cancelar).
- **Estados de borda** (vazio, erro, carregando) — marque onde cada um acontece.
- **Saída** (onde o usuário conclui ou abandona).

### 5. Validar contra o brief

- Todo fluxo serve a uma persona ou ao problem statement? Se não, remova ou marque como fora do escopo.
- Alguma tela do sitemap não tem tarefa? Remova.
- A hierarquia cabe em 2 níveis? Se não, proponha re-agrupamento (não force).

## Saída esperada

Arquivo por caso (ex.: `docs/casos/<nome>/ia.md`) com: sitemap anotado + fluxos de usuário (feliz/alternativo/bordas) + lista de telas com tarefa e próximo passo. Em projetos sem pasta de caso, entregue em um único markdown.

## Exemplo

**Exemplo real:** `docs/casos/brisa/ia.md` (caso Brisa, 2026-08-25).

Sitemap (resumo): `/` (proposta + escolha de região) → `/regioes` → `/regioes/cerrado|mantiqueira|matas-de-minas` · `/planos` · `/como-funciona` · `/conta` — cada página com tarefa, conteúdo essencial e próximo passo. Fluxo crítico: `[post de café] → /planos → escolhe região → checkout → /conta (assinatura ativa)`.

## Auto-verificação

- [ ] Cada página do sitemap tem nome + tarefa do usuário + conteúdo essencial + próximo passo
- [ ] Navegação ≤ 2 níveis e 3–7 itens primários
- [ ] Todo fluxo serve a uma persona ou ao problem statement — senão remova ou marque fora do escopo
- [ ] Estados de borda (vazio/erro/carregando) mapeados nos fluxos, com saída definida
- [ ] Nenhuma página fora do escopo v1 do brief
- [ ] Rotulagem na linguagem do usuário (do research), não na terminologia interna

## Qualidade

- Estrutura justificada por tarefa de usuário, não por opinião.
- Cada tela tem: nome, tarefa, conteúdo essencial, próximo passo.
- Fluxos cobrem feliz + alternativo + borda; estados vazio/erro/carregando mapeados.
- Pronto para o `ui-designer` transformar em telas sem re-perguntar o "para quê" de cada página.
