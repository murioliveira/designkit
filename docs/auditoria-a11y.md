# Auditoria de Acessibilidade — WCAG 2.2 AA

> **Status: 10 correções aplicadas em 2026-08-25 (2 P1, 5 P2, 3 P3)** — ver histórico
> abaixo; este documento é o registro da auditoria, não o estado atual do código.
> Correções: sidebar `visibility` (P1), anel de foco alpha 0.5/0.6 (P1), footer fora do
> `main` (P2), `tabindex` no `main` (P2), placeholder (P2), reduced-motion (P2),
> `role="document"` removido (P2), aria-label Lumen (P3), `aria-checked` mixed (P3),
> `data-modal-close` (P3).

**Auditor:** a11y-auditor (Design Kit) · **Data:** 2026-08-25 · **Modo:** read-only
**Escopo:** `index.html` (showcase) + `js/app.js` + `styles/*.css` · `docs/casos/lumen/index.html` + `lumen.css`

## Veredito por área

| Área | Veredito |
|---|---|
| 1. Semântica e landmarks | RESSALVAS (footer no main; alvo do skip link) |
| 2. Formulários | PASSA (2 notas P3) |
| 3. Overlays | RESSALVAS (`role="document"`, controle morto) |
| 4. Teclado | RESSALVAS (sidebar focável fechada — P1) |
| 5. Contraste | RESSALVAS (placeholder 4.35:1; anel de foco fraco — P1) |
| 6. Motion | RESSALVAS (lacunas no showcase) |
| 7. Lumen | RESSALVAS (2 novos, leves) |

## Lista priorizada

**Blockers:** nenhum.

**Major (P1):**
1. **Sidebar off-canvas focável quando fechada no mobile** — `styles/layout.css:176-189` + `js/app.js` (`setMenu`) + `index.html:86`. Falha 2.4.3/1.3.2 para teclado/SR no mobile. Fix: `visibility` (com transition) ou `inert` ao fechar.
2. **Anel de foco com contraste ≈1.74:1 (claro) / ≈2:1 (escuro)** — `styles/tokens.css:148-149, 226-227, 280-281, 326-327` (alpha 0.35/0.45). Fix: alpha ≥ 0.5/0.6 ou 2px sólido, ≥3:1 contra superfícies.

**Minor (P2):**
3. `tabindex="-1"` no `<main>` de ambos os arquivos (`index.html:103`; `lumen/index.html:101`) — skip link move foco. (Reavaliar `layout.css:264` `outline:none`.)
4. `.placeholder` 4.35:1 no claro — `layout.css:289-296` (usar `--color-text` ou token mais escuro).
5. Footer dentro de `<main>` — `index.html:769` (sem landmark contentinfo).
6. Reduced-motion incompleto no showcase (smooth scroll `base.css:27`, transições `layout.css:117-123, 140-144, 187-190, 243-249`).
7. `role="document"` no diálogo — `index.html:739`.

**Notas (P3):**
8. Lumen: `role="img"` omite "Pausa sugerida" — `lumen/index.html:144`.
9. `aria-checked="mixed"` no indeterminate — `index.html:576`/`app.js`.
10. Botão "Excluir projeto" sem ação — `index.html:755`.
11. Status de presença do avatar só por cor — `components.css` §8.6.

## Pontos fortes verificados

- Labels for/id em todos os 14 controles; fieldset+legend nos radios; aria-describedby + aria-invalid + role=alert + foco no primeiro inválido.
- Modal com trap de foco real, Esc, devolução de foco, aria-modal.
- Tabs com roving tabindex + arrow keys + Home/End.
- Tooltip em hover E focus, com aria-describedby dinâmico.
- Nenhum tabindex > 0; :focus-visible global; skip-link presente.
- Contraste AA passa com folga na maioria dos pares dos dois temas.
- prefers-reduced-motion coberto nos componentes e no Lumen.

## Recomendação

Rodada manual de validação em navegador (Tab pela página, leitor de tela no modal/tabs, devtools nos dois temas) antes de fechar o ciclo — sem execução de browser/axe nesta auditoria.
