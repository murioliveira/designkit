# Revisão de Especialista — Experiência Real de Uso

**Alvo:** `docs/experimentos/artefatos/e1-Y.html` — landing "Draftly" (pt-BR, 501 linhas)
**Estilo:** leitura crítica com foco em quem usa a página de verdade (leitor de tela, usuário idoso, teclado), achados priorizados, checklist anti-slop com contagens.

---

## Como esta página se comporta para quem realmente a usa

### Cenário 1 — Usuária de leitor de tela (NVDA, navegando por headings)

A navegação por headings funciona: h1 "Draftly" → h2 "Recursos" → h2 "Como funciona" → h2 "Depoimentos" → h2 "Preços" → h2 "Comece agora". A ordem é limpa e sem saltos. **Porém:** ao chegar no conteúdo, a usuária ouve os links da nav primeiro — e não há atalho para pular para o conteúdo. Ela tabula 4 links da nav antes de qualquer conteúdo útil. Em uma página de 501 linhas, isso é atrito diário, não exceção.

**Achado 1 (bloqueador):** sem skip-link. A usuária de teclado/SR perde tempo em toda visita.

### Cenário 2 — Usuário idoso com baixa visão (contraste)

O texto principal (slate-800 sobre branco, 14.63:1) é excelente. Mas os **links** são o problema: `#818cf8` sobre branco dá **2.98:1**. Para um usuário com catarata ou presbiopia, links quase invisíveis = navegação quebrada. Ele não sabe o que é clicável. O subtexto (`#64748b`, 4.34:1) também é fraco — parágrafos de features e o subtexto do hero exigem esforço.

**Achado 2 (bloqueador):** links com contraste 2.98:1 — o mecanismo de navegação mais importante da página é o mais difícil de ver.

**Achado 3 (major):** subtexto 4.34:1 — leitura cansativa em parágrafos de features.

### Cenário 3 — Usuária de teclado (sem mouse)

Ela tabula: logo (link) → 4 links da nav → CTA → ... O `:focus-visible` existe (3 ocorrências), então o anel de foco aparece. **Mas** o anel usa a mesma cor primária clara (`#818cf8`), que sobre fundo branco tem 2.98:1 — o anel de foco pode não ser distinguível o suficiente para ela saber onde está.

**Achado 4 (major):** anel de foco com contraste não verificado (mesma cor fraca dos links).

### Cenário 4 — Usuária que lê o status do documento

O status "Pago/Pendente" (`#16a34a`, 3.15:1 em fonte 12px) é informação funcional. Para uma usuária com baixa visão, distinguir "Pago" (verde) de "Pendente" (âmbar) exige esforço — e o verde não passa AA.

**Achado 5 (major):** status com contraste 3.15:1.

---

## Checklist anti-slop — contagens reais

| Tell | Contagem | Status |
|---|---|---|
| Em-dash (`—`) | 0 | ✅ |
| En-dash (`–`) | 0 | ✅ |
| Inter (font-family) | 0 | ✅ |
| Google Fonts `<link>` | 0 | ✅ |
| Hex hardcoded em uso | 0 (só em definição de tokens) | ✅ |
| Fake screenshot de div | 0 | ✅ |
| Nomes genéricos (John/Jane/Acme/Lorem) | 0 | ✅ |
| Scroll cue | 0 | ✅ |
| Version footer | 0 | ✅ |
| Eyebrow (uppercase tracking) | 1 (hero) | ✅ (limite: 1 por 3 seções) |
| `prefers-reduced-motion` | 2 | ✅ |
| `:focus-visible` | 3 | ✅ |
| `lang` | pt-BR | ✅ |
| `<title>` descritivo | sim | ✅ |
| Landmarks | header/main/footer/2 nav | ✅ |
| Seções com `aria-labelledby` | 6 | ✅ |
| `<img>` sem `alt` | 0 | ✅ |
| Skip-link | **0** | ❌ |

**Anti-slop: 16/17 checks limpos.** A única falha estrutural é o skip-link (que é a11y, não anti-slop). A página é genuinamente limpa de tells de IA — o que é raro e digno de nota.

---

## Achados priorizados

| # | Sev. | Achado | Localização | Impacto real |
|---|---|---|---|---|
| 1 | 🔴 Blocker | Links/eyebrow `#818cf8` = 2.98:1 | `a`, `.hero__eyebrow`, `.feature__icon` | usuário de baixa visão não vê o que é clicável |
| 2 | 🔴 Blocker | Sem skip-link | `<body>` | usuário de teclado/SR tabula a nav toda |
| 3 | 🟠 Major | Subtexto `#64748b` = 4.34:1 | `.hero__sub`, `.section-head p`, `.feature p` | leitura cansativa |
| 4 | 🟠 Major | Status `#16a34a` = 3.15:1 | `.draft-row__status` | informação funcional ilegível |
| 5 | 🟡 Minor | Anel de foco com cor fraca | `:focus-visible` | foco pouco visível |
| 6 | 🟡 Minor | 10 h3 | features/how/pricing | hierarquia pesada |

---

## Veredito

**REPROVADO com 2 bloqueadores** — mas por razões cirúrgicas, não estruturais. A página é anti-slop impecável (16/17), semântica correta, e o texto principal tem contraste excelente. Os bloqueadores são: links com 2.98:1 (a cor primária clara usada como texto) e a ausência de skip-link. Trocar 2-3 tokens de cor e adicionar um skip-link eleva a página a WCAG 2.2 AA. Para uma landing de conversão, corrigir os links é prioridade absoluta — é o que o usuário clica.
