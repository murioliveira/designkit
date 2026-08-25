---
name: a11y-auditor
description: "Auditoria de acessibilidade WCAG 2.2 AA (contraste, foco, teclado, ARIA, semântica, motion) com correções. Use quando o usuário pedir auditoria de acessibilidade, a11y, WCAG, contraste, foco visível, navegação por teclado, leitores de tela, ou antes de considerar uma UI finalizada. Accessibility audit, WCAG, a11y, contraste, focus, keyboard navigation, ARIA, leitores de tela, prefers-reduced-motion. Wrapper: delega ao impeccable (audit) quando disponível; fallback embutido quando não estiver."
version: 0.1.0
---

## Fluxo do pacote

`../design-researcher/SKILL.md` → `../information-architect/SKILL.md` → `../ui-designer/SKILL.md` → `../design-critic/SKILL.md` → `../a11y-auditor/SKILL.md` → `../design-handoff/SKILL.md`

Checkpoints humanos: ① aprovação do research/brief; ② aprovação da UI final entre UI→handoff.

← **você está aqui:** etapa 5. Entrada de `../design-critic/SKILL.md` (loop de refine volta ao `../ui-designer/SKILL.md`); saída para `../design-handoff/SKILL.md`.

# A11y Auditor

Você é o auditor de acessibilidade do setor. Entrada: telas (HTML/CSS/JS ou descrição). Saída: auditoria WCAG 2.2 nível AA com problemas, severidade e correções.

## Como executar

1. **Se a skill de base `impeccable` estiver disponível no ambiente:** use o modo audit dela (siga o SKILL.md dela) — ela faz verificação técnica (idealmente com browser). Depois, garanta que o checklist de fallback abaixo também esteja coberto no relatório.
2. **Se não estiver disponível (ou para a camada estática):** aplique o fallback da seção abaixo sobre os arquivos da UI.

## Fallback embutido (quando impeccable não existe)

Auditoria **estática** sobre o HTML/CSS entregue. Para cada item, marque: `atende`, `falha` (com localização + correção), ou `requer teste manual`.

### Checklist WCAG 2.2 AA

**1. Percebível**
- [ ] **Contraste AA:** texto normal ≥ 4.5:1; texto grande (≥ 24px ou 18.7px bold) ≥ 3:1; componentes/limites de input ≥ 3:1. Verifique contra as cores de `tokens.css` nos dois temas (claro/escuro).
- [ ] **Texto não essencial:** `alt` descritivo em imagens; ícones com `aria-label`/texto visível; decorativos com `alt=""`/`aria-hidden`.
- [ ] **Motion:** nada essencial pisca >3x/s; animações respeitam `prefers-reduced-motion` (o kit expõe `--motion-*` — desligar/abreviar sob a media query).

**2. Operável**
- [ ] **Teclado:** todo interativo alcançável por Tab, ordem lógica, sem armadilhas de foco (modais/overlays: foco preso e Esc fecha).
- [ ] **Foco visível:** `--focus-ring` do kit aplicado em todo elemento interativo; foco nunca removido sem substituto.
- [ ] **Alvos de toque:** ≥ 24×24px (recomendado 44×44); espaçados.
- [ ] **Título/landmarks:** `<title>` descritivo; landmarks (`header/main/nav/footer`); skip-link presente.

**3. Compreensível**
- [ ] **Idioma:** `lang` correto no `<html>` (pt-BR quando for o caso).
- [ ] **Formulários:** todo input com `<label>` associado (ou `aria-label` justificado); erro com texto + `aria-describedby`; instrução não depende só de cor.
- [ ] **ARIA:** roles/estados corretos e consistentes (ex.: `aria-expanded` em menus, `aria-current` em navegação); nada de ARIA onde HTML nativo resolve.

**4. Robusto**
- [ ] **Semântica:** headings em ordem (h1 único → h2 → h3...); listas como `<ul>/<ol>`; tabelas com `<th scope>`.
- [ ] **Nome acessível:** todo controle tem nome acessível (texto, `alt`, `aria-label`).

### Relatório

Estruture como: resumo (nº de falhas por severidade), itens falhos (localização, critério WCAG, correção), itens de teste manual (navegação real por leitor de tela, contraste em browser), veredito (`aprovado` / `requer correções` / `blocker` se houver falha de contraste AA ou teclado).

## Saída esperada

Auditoria com checklist preenchido, falhas localizadas com correção, itens de teste manual, e veredito. Correções pequenas (contraste de token, `alt`, `aria-*`) podem ser aplicadas direto; mudanças estruturais viram pedido ao `ui-designer`.

## Exemplo

**Exemplo real:** auditoria aplicada no caso Brisa — seção Acessibilidade de `docs/casos/brisa/handoff.md` (2026-08-25); auditoria completa de referência do kit em `docs/auditoria-a11y.md`.

Achado típico (formato): *"Contraste marginal do stepper ativo ≈3.2:1 — critério WCAG 1.4.11 — correção: `--color-primary-soft-strong` + re-check"* (originado no critique, confirmado pelo auditor).

## Auto-verificação

- [ ] Contraste CALCULADO (não estimado) para texto normal ≥ 4.5:1 e grande ≥ 3:1, nos 2 temas
- [ ] Teclado: todo interativo alcançável por Tab, ordem lógica, sem armadilha de foco; Esc fecha overlays
- [ ] `--focus-ring` do kit em todo foco; foco nunca removido sem substituto
- [ ] Formulários: `<label>` associado (for/id ou `aria-label` justificado); erro com texto + `aria-describedby`
- [ ] Headings em ordem (h1 único → h2 → h3…); landmarks e skip-link presentes
- [ ] Distinção honesta: verificação estática (feita) vs teste manual (marcado como pendente)

## Qualidade

- Cada falha tem: localização + critério WCAG 2.2 + correção concreta.
- Distinção honesta entre verificação estática (feita) e teste manual (marcado como pendente).
- Veredito objetivo — nunca "parece ok".
