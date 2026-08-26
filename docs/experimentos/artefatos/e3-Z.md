# Critique E3-a — métodoobre before.html

**Input:** docs/casos/redesign-demo/before.html (landing "Cloudly" — IA slop clássico)
**método:** o kit — o manual (tells), §5.1 (redesign audit-before-touch), scripts/smoke-test.py + anti-slop-check.py, scripts/export-tokens.py (verificação cruzada).

## Scoring por heurísticas (1-5)

| Heurística | Nota | Justificativa |
|---|---|---|
| Clareza | 2 | Hero genérico ("Transforme sua produtividade") — não nomeia público nem resultado concreto. Value prop fraca. |
| Hierarquia | 2 | 3 feature cards idênticos (layout + copy); eyebrow em TODAS as seções (count > ceil(seções/3)); headline e subtext competem por tamanho. |
| Consistência tokens | 1 | Gradiente roxo AI-typical (tell §4.1 banido); hex hardcoded (gradiente, cores de fundo); Inter explícito em font-family. |
| Affordance | 3 | Botões parecem botões; nav funciona; mas scroll cue "Scroll down" é falso affordance. |
| Acessibilidade | 2 | Skip-link ausente (divs, não landmarks); sem aria-labelledby; fake screenshot de div (não é imagem real — inaccessible); contraste AA duvidoso no gradiente. |
| Responsividade | 2 | Sem mobile-first (3 colunas fixas no hero); sem colapso explícito; sem menu hamburger. |
| Copy (anti-slop) | 1 | 4 em-dash (tell §9.G); nomes genéricos "John D."; números falsos (99.99%); scroll cue "Scroll down"; eyebrow em toda seção; version footer "v0.6". |
| **Média** | **1.7/5** | **Blocker**: consolidação de tells — não há valor de IA auditável; a UI é 100% template. |

## Tells de IA encontrados (11)

1. Em-dash (`—`) em texto visível (4 ocorrências)
2. Gradiente roxo AI-typical (hero e features)
3. Inter como font-family (global)
4. 3 feature cards idênticos (layout + copy)
5. Fake screenshot de div (painel falso de tarefas)
6. Nomename genérico "John D." (depoimento)
7. Número falso "99.99%" (uptime)
8. Scroll cue "Scroll down"
9. Eyebrow em TODAS as seções (excesso)
10. Version footer "v0.6" em landing
11. Split-header padrão ("left big headline + right small explainer")

## Veredito

**APROVADO COM RESSALVAS** (métodovaliando o alvo como audit antes de redesign): 4 em-dash (tell §9.G), 11 tells de IA catalogados, média 1.7/5. O kit capturou os mesmos padrões que o taste (9.G) e o a skill de referência (audit dimensions) — mas de forma MECHANICAL e EXAUSTIVA (grep + checklist), não por inspeção visual subjetiva. Vantagem do método: audit é executável e reprodutível.