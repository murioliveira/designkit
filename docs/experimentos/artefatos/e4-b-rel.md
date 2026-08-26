# E4 · Redesign (preservar marca) - Método B: impeccable

**Experimento:** E4 · **Método:** B (impeccable v4.1.1) · **Input:** `docs/casos/redesign-demo/before.html` (landing "Cloudly" com tells de IA)
**Artefato:** `docs/experimentos/artefatos/e4-b.html` · **Data:** 2026-08-26

---

## 1. Direção (contrato, no comentário do artefato)

- **THESIS:** Cloudly é uma ferramenta de trabalho, não um slogan. A primeira dobra mostra a trilha de hoje sobre papel morno, com o trabalho em andamento visível antes de qualquer promessa. Recusa o hero-central-roxo com métrica decorativa e a prévia falsa de barras.
- **OWN-WORLD:** papel morno (casca de ovo) como chão; tinta quase-preta azulada para texto; cobalto elétrico como único acento, reservado a ação e a um fio fino de destaque. Display grotesco pesado e apertado; mono apenas para dados e rótulos de sistema. Nenhuma sombra falsa; divisão por tinta e espaço.
- **STORY:** o visitante entende em 5 segundos que Cloudly organiza hoje: o que está pendente, quem atrasou, o que fecha. Ele acredita porque vê trabalho real na primeira dobra e prova de funcionamento, não slide.
- **FIRST VIEWPORT:** barra de navegação fina; h1 grande em uma linha curta; subtexto em 20 palavras; dois CTAs; abaixo, a trilha "hoje" real (3 itens de tarefa com status concreto e prazos em pt-BR).
- **FORM:** painel-operacional sobre papel, posto 1, comprometido com a própria gramática de grade e tinta.

## 2. O que foi PRESERVADO (IA e conteúdo)

- Nome da marca: **Cloudly** (preservado).
- Navegação: Recursos, Preços, Depoimentos (mesmos labels e âncoras `#recursos`, `#precos`, `#depoimentos`).
- CTAs: "Começar grátis" (nav, hero, CTA final), "Ver demonstração", "Começar", "Falar com vendas" (mesmos labels).
- Estrutura de seções: hero → recursos → como funciona → depoimentos → preços → CTA final → footer (mesma IA).
- Preços: Básico R$ 0, Profissional R$ 29, Empresa R$ 99 (mesmos valores e hierarquia com plano destacado).
- Idioma pt-BR.

## 3. O que foi SUBSTITUÍDO (nova linguagem visual - o antigo é anti-referência)

| Tell do before | Substituição no after |
|---|---|
| Gradiente roxo de IA (`#7c3aed` → `#6d28d9`) | Paleta comprometida: papel morno + tinta azulada + cobalto único (5.79:1 AA) |
| Fonte Inter (Google Fonts) | System-ui grotesco + mono para dados; zero download de fonte |
| Eyebrow/kicker acima de TODA seção | **Removidos por completo** (craft-floor: ban) - o heading fala sozinho |
| Fake screenshot de div (barras cinzas) | Trilha "hoje" com conteúdo real: 3 tarefas com horário, nome, valor, status (no prazo / em andamento / atrasado) |
| 3 cards idênticos de features | 3 blocos distintos: 1º papel-deep, 2º transparente, 3º tinta (invertido) - variação real de material |
| Scroll cue ("Scroll down") | Removido |
| Version footer ("v2.4.1 · build 0048") | Removido (footer limpo) |
| Nome genérico "John D., Product Manager" | Mariana Alves · designer autônoma, São Paulo (nome real pt-BR) |
| Número falso "99.9%" | Removido; depoimento com linguagem concreta |
| "10.000 times" (fake social proof) | Removido |
| Hero centralizado com métrica | Hero split: título à esquerda, trilha de hoje à direita (prova no primeiro viewport) |
| Sombra dura `0 20px 60px` | Sem sombras falsas; divisão por tinta e bordas finas |

## 4. Validação mecânica (anti-slop)

| Check | Resultado |
|---|---|
| Em-dash / en-dash visível | 0 / 0 ✓ |
| Fonte Inter | ausente ✓ |
| Hex de gradiente roxo de IA | ausente ✓ |
| Fake screenshot de div | ausente ✓ |
| Scroll cue | ausente ✓ |
| Version footer | ausente ✓ |
| Nomes genéricos (John/Jane/Acme) | ausente ✓ |
| Gradient text | ausente ✓ |
| Eyebrow acima de heading | 0 (removidos) ✓ |
| Contraste AA (9 pares chave) | todos ≥ 4.5:1 (mín. 5.23:1, máx 13.61:1) ✓ |
| Mobile-first | grid colapsa para 1 coluna < 820px; nav-links ocultos ✓ |
| prefers-reduced-motion | transições desativadas ✓ |
| Browser surfaces | `::selection` cobalto, scrollbar temática, focus-visible ✓ |

## 5. Notas de método (impeccable)

- Segui o fluxo de **redesign** do new-work: preservar product truth/conteúdo/IA, substituir o mundo visual (o antigo é evidência, não autoridade).
- **Craft floor** aplicado: contraste AA, sem eyebrow (ban), sem gradient text, sem glass decorativo, sem sombra dura, mono só para dados, browser surfaces tematizadas, motion único e motivado.
- **Estratégia de cor:** Committed (cobalto carrega ação; papel morno é o chão) - coerente com Persuade.
- **Prova, não promessa:** a trilha "hoje" demonstra o mecanismo (organizar o dia) em vez de reafirmar claims.
- Limitação do experimento: sem geração de imagem disponível, a "imagem real" foi substituída por conteúdo real autorado (trilha de tarefas) - dentro do que o craft-floor permite (conteúdo real > chrome).

## 6. Riscos residuais

- Sem screenshot em navegador (ambiente sem browser) - a validação foi estática (contraste calculado, checks mecânicos).
- A trilha "hoje" usa dados fictícios coerentes (nomes de clientes inventados) - rotulável como synthetic se fosse produção.
- Fonte system-ui (sem self-host de face distinta) - limitação de artefato auto-contido sem build; o craft-floor pediria face própria em produção.
