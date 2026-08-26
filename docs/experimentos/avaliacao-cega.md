# Avaliação Comparativa Cega — instruções ao avaliador

> ⛔ **STATUS: BLOQUEADA (2026-08-26, Oráculo).** Os artefatos atuais NÃO são cegos — vazam o método em nome de arquivo, título e corpo (ver `leakage-audit.md`). **Não rodar esta avaliação até o saneamento dos Passos 1–4 do `leakage-audit.md`.** O painel A/B/C nasceria contaminado se avaliado agora.

Você é um avaliador independente e CEGO. Não vai saber qual método gerou cada artefato (X/Y/Z é anônimo). Julgue APENAS pela qualidade observável, sem procurar "assinaturas" de ferramenta.

## Experimentos × Tríades (leia os 3 de cada, pontue e compare)

| Exp | O que é | Artefatos (3 anônimos por experimento: X, Y, Z) | Critério de julgamento |
|---|---|---|---|
| E1 | Landing Draftly | e1-X.html · e1-Y.html · e1-Z.html | persuasão, clareza, hierarquia, anti-slop, contraste, copy |
| E2 | Dashboard NorteMetrics | e2-X.html · e2-Y.html · e2-Z.html | densidade de dados, scanability, consistência, a11y (tabela), alinhamento numérico |
| E3 | Critique do before.html (mesma UI) | e3-X.md · e3-Y.md · e3-Z.md | precisão dos achados, severidade, quão exaustivo, quão útil p/ corrigir |
| E4 | Redesign do before.html | e4-X.html (+rel) · e4-Y.html (+rel) · e4-Z.html (+rel) | preservação de conteúdo/IA, remoção de tells, qualidade da nova linguagem |
| E5 | Auditoria a11y+anti-slop do e1 | e5-X.md · e5-Y.md · e5-Z.md | cobertura (contraste, foco, teclado, semântica, ARIA, tells), localização precisa, severidade |

## Escala

Cada artefato em cada experimento: nota 1-5 por heurística relevante (mobile-first, anti-slop, contraste AA, hierarquia, clareza, a11y, copy/consistência) + nota geral 1-5.

Não olhe/rode nada além dos arquivos. Não tente adivinhar X/Y/Z = qual ferramenta. Depois de pontuar, rankeie em cada experimento (1º/2º/3º) e anote, sem julgamento de método: "o 1º lugar nesse experimento se destacou por...".

## Saída

Grave em `docs/experimentos/avaliacao.md`:
1. Tabela por experimento (X/Y/Z × heurísticas + geral)
2. Ranking por experimento
3. Pontos fortes/fracos de cada vencedor (sem atribuir a ferramenta)
4. Resumo executivo 8 linhas