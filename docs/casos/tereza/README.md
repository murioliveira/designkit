# Caso Tereza Vilela: portfólio de ilustradora editorial (modo Experience)

> Portfólio que fecha a matriz de modos do kit: o 4º modo (Experience) ganha
> prova real. O artefato lidera desde o primeiro viewport; a interface recua.
> Arquivos: `index.html` + `tereza.css` (só tokens do kit, zero hex).

## Design Read (1 linha)

> Lendo como: portfólio de ilustradora editorial para editores de arte e
> diretores de arte de revistas, com uma linguagem de tinta quente sobre papel
> frio (terracotta + slate), tendendo a galeria Experience assimétrica com a
> obra no primeiro viewport.

## Dials (justificados pelo brief)

| Dial | Valor | Razão |
|---|---|---|
| DESIGN_VARIANCE | **8** | Galeria assimétrica (capas verticais, ensaios horizontais, mural em largura total), composição de capa como linguagem. Abaixo do 9-10 porque o público (editores de arte) valoriza leitura limpa, não caos. |
| MOTION_INTENSITY | **4** | Revelação suave entre peças (IntersectionObserver, só transform/opacity) + zoom sutil no hover. Sem cinemática: a obra não compete com movimento. |
| VISUAL_DENSITY | **2** | Ar de galeria: cada peça respira, seções espaçadas, respiro generoso. |

## Família estética

**Terracotta + Slate** (alternativa nº 5 do DESIGN.md §4.1: "warm rust against
cool grey"). O accent da página é `--color-warning` (âmbar escuro do kit no claro = 5.0:1 AA; âmbar claro no escuro = 10.7:1), usado como a "tinta" da
ilustradora; os neutros slate do kit são o "papel". Razão: ilustradora
editorial = tinta sobre papel; o vermelho-tijolo é a assinatura visual das
peças (sol, toldos, capas), e o frio do slate impede a leitura "bege+latão"
do tell nº 2. Escolha deliberada de NÃO usar o índigo do kit: o índigo já é a
voz do Aurora, e o terracotta diferencia o portfólio como a marca da artista.

## Blocos usados

1. **`hero-manifesto-editorial`** (adaptado): o hero NÃO é de marketing. O
   primeiro viewport é a obra: uma ilustração grande de capa (SVG real, com
   leitora sob a árvore) domina o grid 3fr/2fr; nome + lead de uma linha +
   CTA discreto na coluna ao lado. Sem scroll cue, sem strip decorativo.
2. **`galeria-experience`**: grid assimétrico com 6 peças (2 capas, 2 ensaios,
   1 mural, 1 retrato), cada uma um SVG real com `role="img"` + `aria-label`,
   legenda sempre visível (gradiente de fundo garante contraste em touch),
   hover/foco com zoom sutil (só transform). Nenhum card: moldura mínima.
3. **Transição entre peças** (em vez de sticky-stack ou marquee): a seção
   Ensaios usa DOIS layouts distintos (destaque = peça grande + corpo embaixo;
   companhia = 2 colunas com peça à direita), sem zigzag repetido, e a
   revelação das peças é animada por IntersectionObserver.

## Como o modo Experience foi materializado

- **Chrome mínimo**: header ≤ 64px com marca + 4 links + toggle de tema (sem
  sidebar, sem banners, sem CTA no header); footer mínimo (marca + nav +
  crédito do kit).
- **A obra lidera**: primeiro viewport é a ilustração de capa; a galeria tem
  6 peças que sustentam o olhar sozinhas; a interface (legenda, meta) fica na
  borda inferior em gradiente, nunca sobre o centro da obra.
- **Curadoria**: cada peça tem título real + contexto (editora/revista + ano);
  nomes contextuais (Editora Caboré, Revista Foz, Caderno do Litoral,
  Biblioteca do Bairro), sem contadores nem labels sobre imagens.
- **Acessibilidade**: landmarks, skip-link, `aria-labelledby` nas seções,
  `role="img"` + `aria-label` descritivo em cada ilustração, navegação por
  teclado completa, foco visível do kit, `prefers-reduced-motion` colapsa
  revelação/zoom para o estado final.

## Auto-avaliação do pre-flight (DESIGN.md §6)

- [x] Design Read declarado + dials explícitos com razão do brief
- [x] Zero `—` e zero `–` em todo texto visível (verificado por grep)
- [x] Theme lock: um tema por página (claro/escuro via `[data-theme]` + prefers)
- [x] Color lock: um accent (terracotta/âmbar) em toda a página; Shape lock:
      raios do kit (xl nas peças, full nos pills, md no painel)
- [x] Contraste AA: accent 5.0:1 (claro) / 10.7:1 (escuro); body e meta com
      tokens semânticos AA; hero usa texto forte
- [x] CTA: "Solicitar portfólio" (1 linha), uma intenção por CTA (contato);
      o "Ver trabalhos" do hero é intenção de browse, distinta
- [x] Hero: obra no viewport, headline (nome) ≤ 2 linhas, lead ≤ 20 palavras,
      3 elementos de texto (eyebrow + título + lead) + 1 CTA, padding ≤ 6rem
- [x] Eyebrows: 1 no total (hero) para 5 seções (limite ceil(5/3) = 2)
- [x] Sem fake screenshots: ilustrações são SVGs reais; sem divs retangulares
- [x] Sem scroll cues, version footer, strips decorativos, dots, eyebrows numerados
- [x] Motion motivado (revelação = storytelling; zoom = feedback), só
      transform/opacity, reduced-motion coberto, sem `window scroll` listener
- [x] Nav em 1 linha ≤ 80px; zigzag 0 (ensaios em layouts distintos)
- [x] Mobile collapse explícito: grade 1 coluna < md, hero empilhado
      (obra primeiro), menu hambúrguer no mobile; `min-h-100dvh` no hero
- [x] Estados loading/empty/error: **N/A** (galeria estática sem dados
      assíncronos nem formulário; documentado, não aplicável)
- [x] Copy auditada: sem frases quebradas, sem "elevate/seamless/unleash",
      números honestos (anos e séries reais do caso)
- [x] Dark mode: definido e testado nos dois temas (SVGs usam tokens
      semânticos, trocam de tom automaticamente)
- [x] CWV plausíveis: sem imagens remotas (SVG inline), CLS ~0; LCP = hero SVG
- [x] Micro-gaps: selection herdado do kit, uma família de ícones (SVG inline
      do kit), i18n coeso (pt-BR), sem emoji como ícone
- [x] Detector: smoke-test + anti-slop PASS (ver seção Validação)

## Validação

```bash
grep -c "—\|–" index.html          # 0 (zero em-dash/en-dash)
python scripts/anti-slop-check.py  # PASS
python scripts/smoke-test.py       # PASS
```

Valores de traço nos SVGs (stroke-width, r dos olhos, delta do menu) são
constantes de desenho da ilustração, não tokens de design system; o padrão é
o mesmo dos casos Lumen/Aurora (valores de traço documentados como off-scale
tolerável). Os hexes `#f8fafc`/`#020617` estão apenas nas metas `theme-color`
do `<head>` e no favicon data-URI (`%23b45309`, asset de navegador, não cor de
UI) — padrão dos casos, exceções documentadas do detector.

## Critique esperado (rodada 1)

- **Pontos fortes**: primeiro viewport = obra (não marketing); chrome mínimo;
  curadoria com 6 peças de identidade própria; color lock terracotta; tokens
  100%; SVGs reais e acessíveis; layouts de ensaio distintos sem zigzag.
- **Riscos**: legenda sobre o gradiente pode competir com a obra em peças
  muito claras (verificar no browser); `--color-warning` como accent semântico
  (documentado: página sem estados de erro, sem conflito).
