# Critique E3-c · Método C (design-taste) sobre before.html

**Input:** `docs/casos/redesign-demo/before.html` (landing "Cloudly"; IA slop clássico)
**Método C:** skill design-taste (design-taste-frontend). Usa Design Read (§0), Dials (§1), AI Tells (§9, com em-dash §9.G ZERO) e Pre-Flight (§14).
**Idioma:** pt-BR. O `before.html` NÃO foi editado, apenas auditado.

---

## Método aplicado (design-taste)

### Design Read (§0)
Lendo como: landing de SaaS para PMEs, com linguagem de "produtividade corporativa genérica", tendendo ao **default anti-slop que a skill proíbe** (3 cards iguais, Inter, gradiente roxo, fake screenshot, eyebrow em toda seção). É exatamente o protótipo que a skill foi criada para eliminar.

### Dials inferidos (§1)
- `DESIGN_VARIANCE: 2` (simetria perfeita, 3 colunas idênticas; o baseline é 8)
- `MOTION_INTENSITY: 1` (estático)
- `VISUAL_DENSITY: 4` (cards genéricos, densidade média)

Coerência: nenhuma diversidade de layout. Tudo centralizado (proibido quando VARIANCE > 4, anti-center).

---

## Heurísticas (1-5)

| Heurística | Nota | Comentário (lente do design-taste) |
|---|---|---|
| Clareza | 2 | Hero não nomeia público nem resultado concreto. A sub tem duas frases e não declara problema nem proposta única. |
| Hierarquia | 2 | 3 feature cards idênticos e 3 pricing cards idênticos (banido). Eyebrow em TODAS as seções (4 por página; limite 1 por 3 seções). Hero e CTA final com marca de mesmo peso. |
| Consistência | 1 | Hex hardcoded no CSS. Gradiente roxo (família `--ai-purple`) é o "AI purple" banido. Inter é o sans default banido. |
| Affordance | 3 | Botões e nav parecem clicáveis. Mas o scroll cue "Scroll down" é falso affordance. O painel falso não é interativo. |
| Acessibilidade | 2 | Fake screenshot feito de div sem `alt` real. Nav sem `aria-label`. Botões sem `type`. Sem `skip-link`. Checkboxes falsos são `span`, invisíveis a leitores. Contraste da CTA-final (texto branco sobre gradiente violeta) incerto. |
| Responsividade | 2 | Sem mobile-first. 3 colunas fixas em features e pricing sem colapso. Sem menu hambúrguer. |
| Copy (anti-slop) | 1 | Verbos de efeito ("Transforme sua", "nova era"). Nome genérico "John D.". Números falsos "99.9%" e "10.000 times". Em-dash 4 vezes (§ exige zero). |

**Média: 2.1/5** | **Blocker**

---

## Tells de IA encontrados (verificação §9)

### §9.A Visual e CSS
- Gradiente violeta em hero e CTA-final. VIOLAÇÃO (AI purple).
- Não há glow/borda neon, nem preto puro, nem cursor custom. OK.

### §9.B Tipografia
- **Inter** como fonte global, o default que a skill proíbe. VIOLAÇÃO.
- H1 de 48px, não grita. OK.

### §9.C Layout e espaçamento
- **3 cards iguais** em features (`repeat(3,1fr)`) e em pricing. VIOLAÇÃO.

### §9.D Conteúdo e dados
- Nome genérico "John D., Product Manager". VIOLAÇÃO.
- Números falsos "99.9%" e "mais de 10.000 times". Violação de precisão falsa.
- Verbos de efeito "Transforme sua", "nova era". Violação.

### §9.E Recursos externos e componentes
- **Fake screenshot de div** (`.fake-dashboard` com spans vazios). Violação (é o tell nº 1).
- Sem Unsplash quebrado, sem SVG pitada manual. OK.

### §9.F Produtos em produção
- **Version footer** "Cloudly v2.4.1 · build 0048" em página de marketing. Violação.
- Scroll cue "Scroll down". Violação.
- Eyebrow em todas as seções ("nova era", "Recursos poderosos", "Planos flexíveis", "O que dizem"). Excesso: 4 eyebrows, limite 1 por 3 seções. Violação.
- "uma plataforma completa", "Preços simples" são clichês genéricos.

### §9.G Zero em-dash
**Em-dashes: 4** (U+2014):
1. `<title>Cloudly  U+2014  Gestão de Tarefas Moderna</title>`
2. `<meta name="description"... Cloudly  U+2014  a plataforma...>`
3. `<h1>... produtividade  U+2014  com Cloudly</h1>`
4. `<p class="testimonial">... como trabalhamos  U+2014  nossa produtividade...`

A habilidade exige zero em-dash no texto visível. Com 4, a página não passa no Pre-Flight.

---

## Veredito

**REPROVADO (blocker).** Média 2.1/5, blocker por consolidação de tells. O design-taste, por inspeção visual e checklist, encontra os mesmos 11 tells do método A: em-dash (4), Inter, gradiente roxo, 3 cards iguais, fake screenshot, nome genérico, números falsos, scroll cue, eyebrow em excesso, version footer, verbos de efeito.

Ponto de contraste: o design-taste é prescritivo (dials, §4, §9) mas não tem verificação determinística por script (ao contrário do Design Kit, que roda `scripts/anti-slop-check.py`). É um crítico pela regra estética, não pela execução de detector. Para este input, os achados são os mesmos do método A; o que difere é a prova: o A é verificável por script, o C depende da inspeção do agente.

**Recomendação de redesign (segundo a taste):**
- `VARIANCE` de 2 para 8: hero split, bento, grade assimétrica.
- Trocar Inter por um sans-serif não padrão (Geist, Satoshi ou system-ui).
- Uma única cor de acento sobre neutro (slate/zinc); sem roxo/glow.
- Zero em-dash, zero scroll cue, zero version footer.
- Máximo 1 eyebrow por 3 seções.
- Substituir 3 cards iguais por linhas em zigue-zague, bento ou destaque full-width.
- Fake dashboard por imagem real de UI (não screenshot fake) ou componente renderizado real.
- Rever contraste da CTA-final (texto branco sobre gradiente violeta).

---
*Método C: design-taste · crítico de estética e anti-slop por inspeção. Não editou before.html.*