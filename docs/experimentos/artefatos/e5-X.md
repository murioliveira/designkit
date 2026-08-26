# Auditoria de Acessibilidade e Anti-slop — Checklist Estruturado

**Alvo:** `docs/experimentos/artefatos/e1-Y.html` (landing "Draftly", pt-BR, 501 linhas)
**Abordagem:** checklist estruturado — contraste calculado por par, foco, teclado, semântica, ARIA + scan anti-slop com severidades e localizações.

---

## 1. Contraste WCAG 2.2 AA — calculado por par

| Par (texto sobre fundo) | Onde | Ratio | Veredito |
|---|---|---|---|
| `#818cf8` sobre `#ffffff` | links (`a`), eyebrow do hero, ícones de feature | **2.98:1** | ❌ **FAIL** (AA texto normal ≥4.5; AA-large ≥3.0) |
| `#818cf8` sobre `#eef2ff` | ícone de feature sobre `--color-primary-soft` | **2.67:1** | ❌ **FAIL** |
| `#64748b` sobre `#f1f5f9` | `hero__sub`, `section-head p`, `feature p`, `draft-row__meta` | **4.34:1** | ❌ **FAIL** (AA texto normal ≥4.5) |
| `#16a34a` sobre `#f8fafc` | `.draft-row__status` (caption 12px) | **3.15:1** | ❌ **FAIL** (AA texto normal ≥4.5) |
| `#4f46e5` sobre `#ffffff` | `--color-primary-600` (CTA hover) | 6.29:1 | ✅ AA |
| `#1e293b` sobre `#ffffff` | texto principal | 14.63:1 | ✅ AA |
| `#020617` sobre `#ffffff` | `--color-text-strong` | 20.17:1 | ✅ AA |
| `#b45309` sobre `#ffffff` | `--color-warning` | 5.02:1 | ✅ AA |
| `#334155` sobre `#f8fafc` | `--color-text` sobre `--color-bg` | 9.90:1 | ✅ AA |

**Resumo contraste:** 4 pares falham AA (2.98, 2.67, 4.34, 3.15) — todos em texto de interface (links, subtexto, status). O texto principal passa com folga.

---

## 2. Foco e teclado

| Check | Status | Localização |
|---|---|---|
| `:focus-visible` definido | ✅ | 3 ocorrências no CSS |
| Ordem de tabulação lógica (DOM) | ✅ | header → nav → main → footer |
| Skip-link presente | ❌ **FAIL** | ausente (falha 2.4.1 Bypass Blocks) |
| `:focus` em todos os interativos | ⚠️ parcial | links e botões têm, mas sem verificação de contraste do anel de foco |
| Teclado em nav (menu) | ✅ | nav simples de links, sem dropdown |

---

## 3. Semântica e ARIA

| Check | Status | Localização |
|---|---|---|
| `lang="pt-BR"` | ✅ | `<html>` |
| `<title>` descritivo | ✅ | "Draftly: proposta, contrato e cobrança para freelancers" |
| Landmarks (`header/main/footer/nav`) | ✅ | header, main, footer, 2 navs |
| Seções com `aria-labelledby` | ✅ | hero, recursos, como-funciona, depoimentos, precos, final-cta |
| Hierarquia de headings | ⚠️ | 1 h1, 5 h2, **10 h3** (features 4 + how 3 + pricing 3) — h3 em excesso, mas ordem h1→h2→h3 correta |
| `alt` em imagens | ✅ | nenhum `<img>` sem `alt` |
| Formulários | ✅ | nenhum form na página (landing) |

---

## 4. Scan anti-slop

| Tell | Contagem | Veredito |
|---|---|---|
| Em-dash (`—`) / en-dash (`–`) | 0 | ✅ limpo |
| Inter como fonte | 0 | ✅ limpo (usa `var(--font-family-base)`) |
| Google Fonts | 0 | ✅ limpo |
| Hex hardcoded em uso | 0 (hex só em definição de tokens `--c-*`) | ✅ limpo |
| Fake screenshot de div | 0 | ✅ limpo |
| Nomes genéricos (John/Acme/Lorem) | 0 | ✅ limpo |
| Scroll cue ("scroll down") | 0 | ✅ limpo |
| Version footer | 0 | ✅ limpo |
| Eyebrow em excesso | 1 (hero) | ✅ dentro do limite |
| `prefers-reduced-motion` | 2 | ✅ presente |

---

## 5. Priorização

| Sev. | Achado | Localização | Correção |
|---|---|---|---|
| 🔴 Blocker | Contraste do link/eyebrow `#818cf8` = 2.98:1 | `a`, `.hero__eyebrow`, `.feature__icon` | usar `--color-primary-600` (#4f46e5, 6.29:1) para texto |
| 🔴 Blocker | Contraste do subtexto `#64748b` = 4.34:1 | `.hero__sub`, `.section-head p`, `.feature p` | usar `--color-text` (#334155) ou escurecer muted |
| 🟠 Major | Contraste do status `#16a34a` = 3.15:1 | `.draft-row__status` | usar `--color-success-700` ou texto mais escuro |
| 🟠 Major | Sem skip-link | `<body>` | adicionar `<a class="skip-link" href="#main">` |
| 🟡 Minor | 10 h3 (hierarquia pesada) | features/how/pricing | reduzir para h3 só onde há sub-bloco real |
| 🟡 Minor | Anel de foco sem contraste verificado | `:focus-visible` | garantir ≥3:1 contra fundo |

---

## Veredito

**REPROVADO com 2 blockers de contraste + 2 majors.** A página é limpa em anti-slop (zero tells) e tem boa semântica, mas falha WCAG 2.2 AA em 4 pares de contraste de texto de interface e não tem skip-link. Correções são pontuais (trocar 3 tokens de cor + adicionar skip-link).
