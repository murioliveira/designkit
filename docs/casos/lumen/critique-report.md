# Critique Report — Caso Lumen

> **Caso:** Lumen (landing page de produto fictício) · **Fase:** A (gate do design-critic) · **Revisado por:** design-critic
> **Arquivos auditados:** `docs/casos/lumen/index.html`, `docs/casos/lumen/lumen.css`, `docs/casos/lumen/README.md`
> **Contexto:** `docs/arquitetura-agente-design.md` §3, `styles/tokens.css`, `styles/base.css`, `index.html` (raiz)

## Veredito

**`APROVADO COM RESSALVAS`** — sem blockers; 3 achados major alimentam o próximo ciclo de refine (regra de tokens na categoria espaçamento, contraste AA em tema claro, navegação mobile ausente).

## 1. Scoring por heurísticas (1–5)

| Heurística | Nota | Comentário |
|---|---|---|
| Clareza de comunicação | **5/5** | Value prop inequívoca no hero ("Foco profundo. Energia medida. Distrações em silêncio."), CTAs com verbo de ação claro; sem ruído entre mensagens. |
| Hierarquia visual | **5/5** | H1 display no desktop, eyebrow + lead em escala decrescente, ritmo vertical em `--space-*` consistente, CTA primário domina sem concorrência; anel de progresso como único "ponto de produto". |
| Consistência com o kit (tokens) | **3/5** | Cor/raio/sombra/fonte: 100% tokens ✓. Espaçamento/geometria: ~15 valores literais (ver §4) — contradiz a regra do kit e a alegação do README ("nenhum valor mágico"). |
| Affordance / interação | **4/5** | Hover/active ricos em botões e cards, `cursor: pointer`, toggle de tema com `aria-pressed`; perde pontos pela nav principal ausente no mobile e pelo loop circular de CTAs. |
| Acessibilidade | **3/5** | Skip-link, landmarks, `aria-labelledby` em todas as seções, teclado nativo, `prefers-reduced-motion` ✓. Falhas: contraste AA 4.34:1 em 3 pontos do tema claro; skip-link aterrissa sob header sticky; anel de foco retangular em botões pill (efeito do base.css). |
| Responsividade | **4/5** | Mobile-first, breakpoints via tokens (`var(--breakpoint-md/lg)`), grids `minmax(0,1fr)`, fluidas; perde ponto pela nav que desaparece em <768px sem substituto e pela degradação em navegadores antigos com `var()` em media query. |
| Qualidade da copy | **5/5** | Zero lorem ipsum; pt-BR correto, tom "calmo/premium" sustentado do hero ao rodapé; depoimentos com voz realista por persona; microcopy do mockup coerente com o produto. |
| **Média** | **4.1/5** | |

## 2. Pontos fortes

- **Disciplina de tokens nas categorias críticas:** nenhum hex hardcoded em `lumen.css` — cor, raio, sombra e fonte são 100% `var(--...)`. Verificação independente confirmou (grep em `lumen.css`).
- **Mockup de produto em SVG puro** (`index.html:127-190`, `lumen.css:285-457`) com anel de progresso matematicamente correto (circunferência 2π·52 = 326.7; offset 173 ≈ 47% de 42/90 min — comentário em `lumen.css:348-350`) e `role="img"` + `aria-label` descritivo (`index.html:127-128`).
- **Decisão de contraste documentada no CSS** (`lumen.css:412-415`): texto do rodapé do mockup em `--color-text-strong` porque `--color-success` (#16a34a) tem 3.30:1 sobre branco — verde reservado a ícones decorativos (≥3:1 para grafismo, WCAG 1.4.11). Raciocínio correto.
- **Acessibilidade estrutural de alto padrão:** skip-link (`index.html:30`), seções com `aria-labelledby`, 2 navs com `aria-label`, ícones `aria-hidden`/`focusable="false"`, estrelas com `aria-label` (`index.html:243-246`).
- **Theming herdado sem JS do kit:** bootstrap de tema inline idêntico ao da raiz (`index.html:20-27`), zero dependência de `js/app.js`; fallback `@supports not (color-mix...)` em `lumen.css:100-104` correto.
- **Contraste das estrelas confirmado AA** (dúvida aberta do README resolvida): `--color-warning` #b45309 sobre branco = **5.0:1** (claro) e #fbbf24 sobre #0f172a = **10.7:1** (escuro) — ambos ≥4.5:1.

## 3. Problemas

### Blocker
- Nenhum.

### Major

1. **Regra de tokens violada na categoria espaçamento/geometria** — `lumen.css` (inventário completo no §4). A regra do kit ("Componentes consomem APENAS os tokens semânticos"; "Nunca usar valores mágicos fora deste arquivo" — `tokens.css:22-26`) e a alegação do README §3.2 ("nenhum valor mágico") não se sustentam: há ~15 valores literais. **Correção:** substituir pelos equivalentes de escala existentes (`1.25rem→var(--space-5)`, `1.5rem→var(--space-6)`, `2.5rem→var(--space-10)`, `3rem→var(--space-12)`, `4rem→var(--space-16)`, `-1.25rem/-0.75rem→calc(-1 * var(--space-5/3))`); para os off-scale (9rem, 24rem, 26rem, 34rem, 48rem, 20rem, 12px, 88%, 1px), documentar justificativa ou propor tokens novos via `impeccable extract` (fluxo previsto na arquitetura §3).
2. **Falha de contraste AA (WCAG 1.4.3) no tema claro** — `--color-text-muted` (#64748b) sobre `--color-surface-muted` (#f1f5f9) = **4.34:1** < 4.5:1 em 3 pontos com texto normal/pequeno:
   - `lumen.css:315-322` `.app-card__time` (12px) — chip "09:00 – 10:30".
   - `lumen.css:389-391` `.app-card__energy-label` (14px) — "Energia agora".
   - `lumen.css:671-674` `.final-cta__text` (16px).
   (Tema escuro passa: 5.70:1.) **Correção:** nesses três seletores usar `var(--color-text)` (ou `--color-text-strong` no chip) em vez de `--color-text-muted`; ou o design-system-keeper escurecer `--color-text-muted` do tema claro (afeta o kit todo).
3. **Navegação principal some no mobile** — `lumen.css:136-139` `.site-nav { display: none }` sem hambúrguer ou substituto em <768px (reaparece só em `lumen.css:737-739`). Usuário mobile perde as âncoras Recursos/Como funciona/Depoimentos. **Correção:** adicionar menu colapsável (padrão do kit é o `menu-toggle` com `aria-expanded`/`aria-controls` da raiz) ou manter uma nav compacta em telas pequenas.

### Minor

- **Skip-link aterrissa sob o header sticky** — `scroll-margin-top` em `lumen.css:14-15` cobre `section[id]`/`footer[id]`, mas não `#main` (alvo do skip-link em `index.html:30`); ao pular para o conteúdo, o topo fica oculto sob os ~5rem do header. **Correção:** incluir `main[id]` no seletor.
- **Anel de foco retangular em botões pill** — `base.css:117-121` aplica `border-radius: var(--radius-sm)` (6px) no `:focus-visible`, deformando o `--radius-full` dos `.btn` e do `.theme-toggle`. É efeito do kit, mas visível nesta página. **Correção (kit):** remover o `border-radius` da regra de foco do base.css ou usar `inherit`.
- **Loop circular de CTAs** — hero "Planejar meu primeiro bloco" → `#cta-final` (`index.html:99`) e CTA final "Começar grátis" → `#main` (`index.html:416`), que devolve ao topo. Sem destino de conversão real (aceitável em POC, mas o padrão `href="#main"` para "Começar grátis" é confuso). **Correção:** apontar para um placeholder de cadastro ou usar `#` documentado.
- **Estado inicial do toggle antes do JS** — `aria-pressed="false"`/`aria-label="Ativar tema escuro"` estáticos (`index.html:57-58`) divergem do tema real até o script do fim do body rodar (um frame de anúncio errado para leitores de tela em sistema dark). **Correção:** inicializar atributos no bootstrap do `<head>`.
- **Comentário CSS impreciso** — `lumen.css:412-415` diz que "o verde fica só no ícone decorativo" do `.app-card__foot`, mas o ícone herda `color: var(--color-text-strong)`; o verde (`--color-success`) está nos checks do `hero__points` (`lumen.css:279-281`). **Correção:** ajustar o comentário ou aplicar `--color-success` ao ícone.
- **`var()` dentro de media queries** (`lumen.css:737`, `753`) — navegadores sem suporte (pré-2023) invalidam os breakpoints e perdem os layouts md/lg; degrada graciosamente para mobile, mas vale nota de compatibilidade. **Correção (opcional):** breakpoints literais com comentário, ou aceitar como decisão.
- **`prefers-reduced-motion` parcial** — desativa só a animação do badge (`lumen.css:463-467`); `transform` de hover/active (`lumen.css:48`, `511`) e o `scroll-behavior: smooth` do base.css permanecem. **Correção:** estender o bloco `@media (prefers-reduced-motion: reduce)` para zerar transforms.
- **Valores literais toleráveis (fora das categorias auditadas, mas a documentar):** `1px` de borda (sem token de border-width no kit — consistente com base.css) e `transparent` (`lumen.css:28`, `95`, `216`), `blur(12px)` (`lumen.css:96-97`), alpha `88%` do `color-mix` (`lumen.css:95`), `stroke-width: 8` e `dasharray/dashoffset` do anel (`lumen.css:340`, `346`, `349-350`). Sugerir ao keeper tokens `--border-width-*` e documentar o 88% como intencional.

## 4. Verificação obrigatória da regra de tokens

**Pergunta:** todos os valores de cor/espaçamento/raio/sombra/fonte em `lumen.css` vêm de `var(--...)` definidos em `tokens.css`?

- **Cor:** ✅ 100% `var(--color-*)` ou `color-mix()` sobre `var(--color-bg)` — nenhum hex em `lumen.css`. (Os hexes `#f8fafc`/`#020617` estão apenas nas metas `theme-color` do `index.html:8-9`, mesmo padrão do `index.html` raiz — nota, não violação.)
- **Raio:** ✅ 100% `var(--radius-*)`.
- **Sombra:** ✅ 100% `var(--shadow-*)`.
- **Fonte:** ✅ 100% `var(--font-*)` / `var(--letter-spacing-*)` / `var(--font-line-height-*)`.
- **Espaçamento/geometria:** ❌ valores mágicos encontrados (inventário):

| Valor | Onde (`lumen.css`) | Equivalente na escala |
|---|---|---|
| `1px` (translateY do press) | :48 `.btn:active` | fora da escala (escala é 4px) |
| `4rem` (min-height header) | :112 `.site-header__inner` | `var(--space-16)` |
| `1.5rem` (marca/ícones) | :131-132, :403, :441-442, :541-542 | `var(--space-6)` |
| `2.5rem` (toggle/step/avatar) | :163-164, :575-576, :633-634 | `var(--space-10)` |
| `1.25rem` (ícones pequenos) | :182-183, :279-280, :420-421, :707-708 | `var(--space-5)` |
| `3rem` (icon feature) | :532-533 | `var(--space-12)` |
| `-1.25rem` / `-0.75rem` (badge flutuante) | :426-427 | `calc(-1 * var(--space-5/3))` |
| `9rem` (anel 144px) | :327-328 | fora da escala (propor token) |
| `24rem` (altura do glow) | :212 | fora da escala |
| `48rem 20rem` (raio do gradiente) | :214 | fora da escala |
| `26rem` (largura do mockup) | :287, :759 | fora da escala (416px) |
| `34rem` (texto do CTA final) | :672 | fora da escala (544px) |
| `40rem` (max-width hero/head) | :229, :482 | `var(--container-sm)` ✓ |
| `12px` (blur) | :96-97 | fora da escala |
| `88%` (alpha do color-mix) | :95 | fora da escala |
| `8` (stroke-width) + `326.7`/`173` | :340, :346, :349-350 | documentados via comentário |

**Conclusão:** a regra está **satisfeita nas categorias cor/raio/sombra/fonte** e **violada na categoria espaçamento** (major §3.1). O README §3.2 ("nenhum valor mágico") está factualmente incorreto e deve ser corrigido no próximo ciclo.

## 5. Lista priorizada de correções

| # | Sev. | O quê | Onde | Esforço |
|---|---|---|---|---|
| 1 | major | Tokenizar/justificar os valores de espaçamento (usar `--space-*`; propor tokens novos ou documentar off-scale) | `lumen.css` (15 ocorrências) | M |
| 2 | major | Trocar `--color-text-muted` por `--color-text` nos 3 pontos sobre `surface-muted` (4.34:1 → ≥4.5:1) | `lumen.css:318`, `:391`, `:673` | S |
| 3 | major | Restaurar navegação no mobile (menu colapsável ou nav compacta) | `lumen.css:136-139` + HTML | M |
| 4 | minor | `scroll-margin-top` para `#main` (skip-link sob header) | `lumen.css:14-15` | S |
| 5 | minor | Foco em botões pill (corrigir `border-radius` do base.css ou override local) | `base.css:117-121` | S |
| 6 | minor | Destino do CTA final + estado inicial do toggle | `index.html:416`, `:57-58` | S |
| 7 | minor | Estender `prefers-reduced-motion` a transforms; corrigir comentário verde | `lumen.css:463-467`, `:412-415` | S |

**Critério de parada:** sem blockers ✓ · média ≥ 4 (4.1) ✓ · nenhuma heurística < 3 ✓ → **próxima ação: refine dos 3 majors e re-critique (máx 2 rodadas).**

---

## Resumo (10 linhas)

1. **Veredito: APROVADO COM RESSALVAS** — sem blockers, média 4.1/5, 3 majors para o ciclo de refine.
2. **Top 1 (major):** regra de tokens violada na categoria espaçamento — ~15 valores literais (1px, 4rem, 9rem, 26rem, 34rem, 88%…), contradizendo o README que afirma "nenhum valor mágico"; cor/raio/sombra/fonte estão 100% tokenizados.
3. **Top 2 (major):** contraste AA falha no tema claro — `text-muted` sobre `surface-muted` = 4.34:1 < 4.5:1 no chip de tempo, label de energia e texto do CTA final (tema escuro passa).
4. **Top 3 (major):** navegação principal some em <768px (`display:none` sem hambúrguer), quebrando o acesso às âncoras no mobile.
5. Pontos fortes: mockup SVG com anel matematicamente correto, decisões de contraste documentadas, acessibilidade estrutural de alto padrão, theming herdado sem JS do kit.
6. Estrelas de depoimento verificadas: 5.0:1 (claro) e 10.7:1 (escuro) — AA ✓, dúvida do README resolvida.
7. Minors: skip-link sob header sticky, foco retangular em pills (efeito do base.css), loop circular de CTAs, toggle com estado inicial estático.
8. Nota de compatibilidade: `var()` em media queries degrada para mobile em navegadores antigos (aceitável).
9. Correções priorizadas: tokenizar espaçamento (M), trocar muted→text em 3 pontos (S), restaurar nav mobile (M).
10. Próxima ação: refine dos 3 majors → re-critique → a11y-auditor/visual-qa → handoff.
