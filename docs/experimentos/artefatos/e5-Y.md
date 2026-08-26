# Auditoria Dupla — Acessibilidade (WCAG 2.2 AA) + Anti-slop

**Alvo:** `docs/experimentos/artefatos/e1-Y.html` — landing "Draftly" (pt-BR, 501 linhas)
**Estilo:** auditoria dupla em texto corrido, severidade por seção, localização exata.

---

## Resumo executivo

A página é estruturalmente sólida: landmarks corretos, `lang="pt-BR"`, título descritivo, seções com `aria-labelledby`, zero tells de IA (sem em-dash, sem Inter, sem fake screenshots, sem nomes genéricos). O problema concentra-se em **contraste de texto de interface** (4 pares falham AA) e na **ausência de skip-link**. Nenhum blocker de semântica; 2 blockers de contraste.

---

## 1. Acessibilidade — ponto a ponto

### 1.1 Contraste (WCAG 1.4.3) — 🔴 2 blockers, 🟠 1 major

**Blocker 1 — Links e eyebrow com contraste insuficiente.**
`a { color: var(--color-primary) }` (linha 145) e `.hero__eyebrow` (linha 183) usam `--color-primary` = `#818cf8`. Sobre o fundo branco `#ffffff`, o contraste é **2.98:1** — abaixo de 4.5:1 (texto normal) e até abaixo de 3:1 (AA-large). Links são o principal mecanismo de navegação da página; um usuário com baixa visão não os distingue do texto. **Correção:** usar `--color-primary-600` (`#4f46e5`, 6.29:1) para texto de link/eyebrow, reservando o tom claro para decoração.

**Blocker 2 — Subtexto e parágrafos de seção com contraste insuficiente.**
`.hero__sub` (linha 185), `.section-head p` (linha 205), `.feature p` (linha 210) e `.draft-row__meta` (linha 199) usam `--color-text-muted` = `#64748b`. Sobre `--color-surface-muted` (`#f1f5f9`), o contraste é **4.34:1** — abaixo de 4.5:1. É texto de leitura (subtexto do hero, descrições de features), não decoração. **Correção:** usar `--color-text` (`#334155`, 9.90:1) ou escurecer o token muted para ≥4.5:1.

**Major — Status com contraste insuficiente.**
`.draft-row__status` (linha 195) usa `--color-success` = `#16a34a` em fonte caption (12px). Sobre `#f8fafc`, o contraste é **3.15:1** — falha AA para texto normal. É um status informativo ("Pago", "Pendente") que o usuário precisa ler. **Correção:** usar um verde mais escuro (ex.: `#15803d`, ~4.6:1) ou texto em `--color-text` com ícone verde decorativo.

### 1.2 Bypass Blocks (WCAG 2.4.1) — 🟠 Major

**Sem skip-link.** Não há `<a class="skip-link" href="#main">` no início do `<body>`. Usuários de teclado/leitor de tela precisam tabular por toda a nav (4 links) antes de chegar ao conteúdo. **Correção:** adicionar skip-link com `:focus` visível, alvo `#main`.

### 1.3 Semântica e landmarks — ✅

- `lang="pt-BR"` no `<html>` ✅
- `<title>` descritivo: "Draftly: proposta, contrato e cobrança para freelancers" ✅
- Landmarks: `<header>`, `<main id="main">`, `<footer>`, 2 `<nav>` com `aria-label` ✅
- 6 seções com `aria-labelledby` apontando para headings ✅
- Hierarquia h1→h2→h3 ordenada (1 h1, 5 h2, 10 h3) — ⚠️ 10 h3 é pesado, mas sem saltos ✅

### 1.4 Foco e teclado — ⚠️ parcial

- `:focus-visible` definido (3 ocorrências) ✅
- Ordem de tabulação lógica (DOM) ✅
- Anel de foco sem contraste verificado contra o fundo — ⚠️ (não é possível confirmar ≥3:1 sem inspeção em browser)
- Sem dropdowns/menus complexos — navegação simples ✅

### 1.5 Imagens e mídia — ✅

- Nenhum `<img>` sem `alt`; nenhuma imagem decorativa sem `aria-hidden` explícito (mas sem imagens problemáticas)

---

## 2. Anti-slop — varredura completa

| Tell | Resultado |
|---|---|
| Em-dash/en-dash (`—`/`–`) | **0** ✅ |
| Inter como fonte | **0** ✅ (usa `var(--font-family-base)`) |
| Google Fonts via `<link>` | **0** ✅ |
| Hex hardcoded em uso | **0** ✅ (hex só em definição de tokens `--c-*` no `<style>`) |
| Fake screenshot de div | **0** ✅ |
| Nomes genéricos (John/Acme/Lorem/Nexus) | **0** ✅ |
| Scroll cue ("Scroll down") | **0** ✅ |
| Version footer (v0.x) | **0** ✅ |
| Eyebrow em excesso | 1 (hero) — dentro do limite ✅ |
| `prefers-reduced-motion` | 2 ocorrências ✅ |
| `:focus-visible` | 3 ocorrências ✅ |

**Veredito anti-slop: LIMPO.** Nenhum tell de IA detectado. A página usa um sistema de tokens inline (`--c-*` → `--color-*` semânticos), o que é boa prática.

---

## 3. Priorização final

| Sev. | Achado | Localização | Esforço |
|---|---|---|---|
| 🔴 Blocker | Contraste link/eyebrow 2.98:1 | `a` (145), `.hero__eyebrow` (183), `.feature__icon` (208) | S |
| 🔴 Blocker | Contraste subtexto 4.34:1 | `.hero__sub` (185), `.section-head p` (205), `.feature p` (210) | S |
| 🟠 Major | Contraste status 3.15:1 | `.draft-row__status` (195) | S |
| 🟠 Major | Sem skip-link | `<body>` | S |
| 🟡 Minor | 10 h3 | features/how/pricing | M |
| 🟡 Minor | Anel de foco sem verificação | `:focus-visible` | S |

---

## Veredito

**REPROVADO** — 2 blockers de contraste (links e subtexto), 2 majors (status e skip-link). Anti-slop impecável (zero tells). A correção é barata (trocar 3 tokens de cor + adicionar skip-link) e elevaria a página a AA em minutos.
