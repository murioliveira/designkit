# Auditoria Comparativa — Design Kit vs impeccable + design-taste

**Data:** 2026-08-25 · **Objetivo:** mapear onde o kit supera e onde fica atrás das skills externas, e o que foi implementado para superar.

## Veredito inicial (antes da rodada de superação)

| Skill | Kit como substituto (hoje) | Com recomendações |
|---|---|---|
| impeccable | 5/10 | 8/10 |
| design-taste | 7/10 | 9/10 |

## Onde o kit já superava (evidência)

1. **Regra de tokens auditável por grep** — zero hex fora de tokens, verificada por script (`smoke-test.py`). Nem impeccable nem taste têm regra verificável.
2. **Reuso real de componentes** — Norte reusa 12 grupos de `components.css` sem redefinir classe; taste tem schema de block library vazio.
3. **Critique com tells + tokens integrados** — o design-critic cruza heurísticas + regra de tokens + AI tells na mesma sessão (as externas tratam separado).
4. **Fluxo de setor completo** — researcher → IA → UI → critic → a11y → handoff com 2 checkpoints humanos e loop máx 2 refines.
5. **Validação empírica** — Lumen 4.1→4.7, Norte 4.6, Brisa 4.2, Aurora com pre-flight 14/14.
6. **Portabilidade multi-agente** — pi/Claude Code/Codex com o mesmo método.

## Gaps identificados (alta gravidade primeiro)

- Redesign protocol completo (audit-before-touch, preserve vs overhaul, levers, SEO) — ALTA
- Performance/CWV (LCP/INP/CLS) — MÉDIA-ALTA
- Detector determinístico (varredura mecânica anti-slop) — MÉDIA
- Modos Operate/Read em profundidade + Experience — MÉDIA
- Block library com dial-compatibility — MÉDIA
- Mapa de design systems externos (quando NÃO usar o kit) — MÉDIA
- Critique enriquecido (cognitive-load, persona red flags) — MÉDIA
- Micro-gaps (browser surfaces, reduced-transparency, marquee max-1, i18n) — BAIXA

## O que foi implementado para superar (rodada 1)

1. **DESIGN.md superado** — §5.1 redesign protocol (detectar modo, audit-before-touch, preservações invioláveis, alavancas 1-6, árvore de decisão), §5.2 mapa de DS externos (GOV.UK/USWDS/Fluent/Carbon/Polaris/Atlaskit/Primer/Material + honesty rule), §5.3 detecção determinística, §1 modo Experience, §4.5 micro-gaps, §6 pre-flight com CWV + detector.
2. **skills/design-redesign** (nova skill + espelho .claude) — protocolo de redesign executável.
3. **scripts/anti-slop-check.py** — detector determinístico: 49 checks em 7 arquivos (em-dash, hex, Inter, eyebrows, nomes genéricos, paleta proibida, scroll cues); PASS no repo real, 11 falhas detectadas em caso evil de teste.
4. **docs/reference/modos.md** (193 ln) — Persuade/Operate/Read/Experience em profundidade, ancorados nos casos reais (Norte=Operate, Aurora/Lumen=Persuade).
5. **docs/blocos/** (7 arquivos, 978 ln) — block library: hero split assimétrico, hero manifesto editorial, bento grid, sticky-stack (CSS puro), marquee, galeria Experience — com dial-compatibility, esqueletos CSS puros, fallback mobile.

## Próximos passos sugeridos (rodada 2)

- Critique enriquecido: cognitive-load checklist + persona-based red flags no design-critic
- Trend de notas de critique (persistir histórico)
- Novo caso de referência usando a block library (provar o nível acima na prática)
- Re-auditar após cada rodada para medir progresso
