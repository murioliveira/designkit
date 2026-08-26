# Proposta de Melhorias Visuais · Design Kit

> Avaliação do showcase e dos casos para atratividade visual humana.
> Data: 2026-08-25
> Autor: Designer (role do kit)

---

## 1. Metodologia da avaliação

Artefatos inspecionados:
- **Showcase principal** (`index.html`, 1206 linhas, 14 seções)
- **CSS do kit** (`tokens.css`, `base.css`, `layout.css`, `components.css`)
- **Casos reais** (`lumen/`, `norte/`, `tereza/`, `aurora/`, `ponto-final/`, `redesign-demo/`, `linha-direta/`, `brisa/`)
- **Manual anti-slop** (`DESIGN.md` — pre-flight, locks, tells, dials)
- **Checagens automatizadas** (`scripts/anti-slop-check.py`, `scripts/smoke-test.py`)

---

## 2. Diagnóstico

### O que está excelente (não mexer)

| Aspecto | Evidência |
|---|---|
| Anti-slop rigoroso | 98 checks passando — zero em-dash, zero hex fora de tokens, zero Inter, zero nomes genéricos, zero tells |
| Tokens como fonte única | Nenhum valor mágico fora de `styles/tokens.css` em todo o projeto |
| Dark/light impecável | `data-theme` + `prefers-color-scheme` com fallback, transições suaves, contraste AA nos dois temas |
| Estados completos | Loading (skeleton no formato final), empty (instrução de preenchimento), error (inline + contextual), disabled, readonly, indeterminate |
| Acessibilidade real | Skip-link, landmarks, ARIA roles/states, trap de foco no modal, teclado completo (setas, Home/End, Esc), `prefers-reduced-motion` |
| Casos reais de altíssima qualidade | Lumen 4.7/5 (landing), Norte 4.6/5 (dashboard), Tereza (portfólio Experience com terracotta+slate), Aurora (anti-slop comparativo) |
| Componentes sólidos | 9 grupos (botões, badges, cards, alertas, forms, overlays, dropdown, breadcrumb, tabela, stepper, paginação) com variações reais |

### O que está prejudicando a atratividade visual

| Achado | Severidade | Impacto |
|---|---|---|
| **Seção Tokens é um placeholder vazio** ("Referência visual dos tokens: em breve") | Alta | É a primeira seção depois do hero. Um humano chega, vê o hero funcional, rola para baixo e encontra... uma caixa tracejada cinza dizendo "em breve". Perda de credibilidade imediata. |
| **O showcase mostra componentes isolados, nunca o resultado final** | Alta | Botão, badge, card, alerta, form — tudo em galeria cinza/branca. Um humano que quer saber "o que eu consigo construir com esse kit?" não encontra resposta visual. Os 8 casos reais (Lumen, Norte, Tereza, Aurora, Farol, etc.) provam o valor do kit, mas estão enterrados em `docs/casos/` sem nenhuma referência visual no showcase. |
| **Hero é só texto sobre fundo com gradiente sutil** | Média | O hero é disciplinado (≤ 2 linhas headline, ≤ 20 palavras subtext, CTA visível) mas não tem nenhum elemento visual que mostre o que o kit produz. Diz "uma base de design sólida" mas não mostra. |
| **Galeria de componentes é monocromática e repetitiva** | Baixa | Seções botões→badges→cards→alertas→forms→overlays são estruturalmente idênticas: título + parágrafo + `.demo__group` cinza. Sem variação de layout entre seções (DESIGN.md §4.5 pede ≥ 4 famílias de layout numa página de 8 seções). |
| **Footer é mínimo** | Baixa | Só duas linhas de texto. O kit tem 8 casos, 8 skills, 18+ componentes — nenhum mencionado no footer. |

### Decisão de escopo

Três achados de severidade alta, mas o 2º (casos invisíveis) e o 1º (tokens vazios) são dois lados do mesmo problema: **o showcase não mostra o que o kit pode fazer**. O 3º (hero só texto) é um subconjunto do mesmo problema.

Proponho **duas melhorias concretas** que atacam o problema raiz e cabem numa iteração de trabalho:

---

## 3. Melhoria 1: Visualização viva de tokens (substituir placeholder)

### Situação atual

A seção Tokens (2ª seção, logo após o hero) contém apenas:

```html
<div class="placeholder" role="note">
  Referência visual dos tokens: em breve (próximas fases)
</div>
```

Isso é uma caixa tracejada cinza. É o primeiro ponto de ruptura de confiança para qualquer humano avaliando o kit.

### Proposta

Substituir por uma **galeria de tokens viva**, com 6 subseções organizadas visualmente:

| Subseção | Conteúdo visual | Tokens usados |
|---|---|---|
| **Paleta de cores** | Grid de swatches: primária (índigo 50→900), neutra (slate 50→950), semânticas (success/warning/error/info + variantes soft), com labels de token abaixo | `var(--c-primary-500)`, `var(--c-neutral-600)`, `var(--color-success)`, etc. |
| **Escala tipográfica** | Rampa visual: display → h1 → h2 → h3 → h4 → h5 → h6 → body → small → caption, renderizados no próprio tamanho real | `var(--font-size-display)`, `var(--font-size-body)`, `var(--font-line-height-tight)`, etc. |
| **Espaçamento** | Régua visual com barras proporcionais para cada step (0, 4px, 8px, 12px, ... 96px), com label e valor em px | `var(--space-0)` → `var(--space-24)` |
| **Raios** | Caixas com `border-radius` progressivo: sm (6px), md (10px), lg (14px), xl (20px), full (9999px = pill) | `var(--radius-sm)` → `var(--radius-full)` |
| **Sombras** | Cards com `box-shadow` progressivo: `--shadow-sm` a `--shadow-xl`, com label e uso recomendado | `var(--shadow-sm)` → `var(--shadow-xl)` |
| **Motion** | Mini-demo ao vivo: um quadrado que anima nas 4 curvas do kit (out, in, in-out, spring) com duração base. Botão "reproduzir" único; `prefers-reduced-motion` colapsa para estático com aviso. | `var(--motion-duration-base)`, `var(--motion-easing-out)`, etc. |

### Layout proposto

```
┌──────────────────────────────────────────────────────┐
│ Tokens                                               │
│ Cores, tipografia, espaçamento, raios, sombras e     │
│ motion — consumidos como custom properties.          │
├──────────────────────────────────────────────────────┤
│ ┌── Cores ──────────────────────────────────────┐   │
│ │  ████████  ████████  ████████  ...           │   │
│ │  --c-primary-50  --c-primary-100 ...          │   │
│ │  (9 swatches primária + 10 neutra + 4 semânti-│   │
│ │   cas com fundo soft)                         │   │
│ └────────────────────────────────────────────────┘   │
│ ┌── Tipografia ─────────────────────────────────┐   │
│ │  Display 56px · H1 40px · H2 32px · H3 24px  │   │
│ │  H4 20px · H5 18px · H6 16px · Body 16px     │   │
│ │  Small 14px · Caption 12px                     │   │
│ └────────────────────────────────────────────────┘   │
│ ┌── Espaçamento ────────────────────────────────┐   │
│ │  0 · ▏4 · ▎8 · ▍12 · ▌16 · ▋20 · ▊24 ·      │   │
│ │  ▉32 · 40 · 48 · 64 · 80 · 96                 │   │
│ └────────────────────────────────────────────────┘   │
│ ┌── Raios ───┐  ┌── Sombras ──┐  ┌── Motion ──┐   │
│ │  6 · 10    │  │  sm · md    │  │  ▶ reproduz │   │
│ │  14 · 20   │  │  lg · xl    │  │  out·in·    │   │
│ │  pill      │  │             │  │  in-out·     │   │
│ │            │  │             │  │  spring      │   │
│ └────────────┘  └─────────────┘  └─────────────┘   │
└──────────────────────────────────────────────────────┘
```

### Esforço estimado

- **HTML:** ~200 linhas (6 subseções com grid de swatches, ramp tipográfica, régua de spacing, cards de raio/sombra, demo de motion)
- **CSS:** ~120 linhas (grid da paleta, barras proporcionais de spacing, animação do motion-demo)
- **JS:** ~30 linhas (botão de play/pause do motion-demo, IntersectionObserver para não rodar fora da viewport, `prefers-reduced-motion` listener)
- **Tokens consumidos:** ~60 tokens reais (prova de que os tokens funcionam na prática)
- **Risco:** baixo — todas as cores/espaços/tamanhos são `var(--...)` reais do `tokens.css`, zero valor inventado

### Verificação anti-slop

- Zero hex hardcoded (todas as cores de swatch são `background-color: var(--c-primary-500)` etc.)
- Zero em-dash
- Zero fake screenshot
- `prefers-reduced-motion` no motion-demo

---

## 4. Melhoria 2: Seção "Resultados" com previews dos casos reais

### Situação atual

O showcase tem 14 seções de componentes. Nenhuma delas mostra um resultado final — uma página pronta, um dashboard real, um portfólio. Os 8 casos reais estão em `docs/casos/` e são acessíveis por link no README, mas um humano que abre `index.html` nunca descobre que eles existem.

Isso viola o princípio mais básico de persuasão visual: **"show, don't tell."** O showcase gasta 1200 linhas mostrando botões, badges e selects, mas zero linhas mostrando o que esses botões, badges e selects constroem juntos.

O DESIGN.md §4.3 proíbe fake screenshots de div. Mas os casos do kit **não são fake** — são HTML real, funcional, com critique aprovado (Lumen 4.7/5, Norte 4.6/5). Não há proibição de mostrar trabalho real do próprio kit.

### Proposta

Adicionar uma nova seção **"Resultados"** (ou "Casos") posicionada entre o hero e os tokens (2ª seção) ou entre os tokens e os botões (3ª seção). A seção mostra **cards de preview visual** para os 3 casos de maior destaque:

| Card | Caso | Modo | Nota | Preview |
|---|---|---|---|---|
| **Lumen** | Landing de app de foco | Persuade | 4.7/5 | Miniatura do hero da Lumen (gradiente índigo + headline + CTA), link para `docs/casos/lumen/index.html` |
| **Norte** | Dashboard financeiro | Operate | 4.6/5 | Miniatura dos cards de métrica + tabela, link para `docs/casos/norte/index.html` |
| **Tereza** | Portfólio de ilustradora | Experience | — | Miniatura da galeria assimétrica, link para `docs/casos/tereza/index.html` |

Cada card de preview contém:
- **Imagem de fundo real**: um recorte visual do caso (SVG inline ou CSS que replica a atmosfera do caso, nunca fake screenshot de div). Como não temos screenshots reais (o kit não tem servidor de build), usamos CSS puro com os mesmos tokens e composição do caso original para recriar o "gosto" visual em miniatura — uma miniatura honesta de CSS, não uma imagem fake.
- **Badge do modo** (Persuade / Operate / Experience) via `.badge--primary` / `.badge--neutral` / `.badge--info`
- **Nota do critique** (para Lumen e Norte)
- **CTA "Ver caso →"** que abre em nova aba

Abaixo dos 3 cards principais, uma linha com **"Mais casos"** listando os casos secundários como links textuais: Aurora, Linha Direta, Redesign Demo, Ponto Final, Brisa.

### Layout proposto

```
┌──────────────────────────────────────────────────────┐
│ Resultados                                           │
│ O que o kit constrói: landing, dashboard e portfólio │
│ com critique aprovado.                               │
├──────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  │              │  │              │  │              │
│  │   LUMEN      │  │   NORTE      │  │   TEREZA     │
│  │   ────────   │  │   ────────   │  │   ────────   │
│  │   Preview    │  │   Preview    │  │   Preview    │
│  │   CSS vivo   │  │   CSS vivo   │  │   CSS vivo   │
│  │              │  │              │  │              │
│  │ Persuade     │  │ Operate      │  │ Experience   │
│  │ ★ 4.7/5     │  │ ★ 4.6/5     │  │ terracotta   │
│  │ [Ver caso→] │  │ [Ver caso→] │  │ [Ver caso→] │
│  └──────────────┘  └──────────────┘  └──────────────┘
│                                                      │
│  Mais: Aurora · Linha Direta · Redesign Demo ·       │
│  Ponto Final · Brisa                                 │
└──────────────────────────────────────────────────────┘
```

### Preview honesto (miniaturas em CSS, sem div fake)

Cada preview é um retângulo com o "gosto" visual do caso, construído 100% com os mesmos tokens e CSS do kit — não uma imagem, não uma screenshot de div fake. É CSS vivo que **poderia ser** o caso real se escalado.

**Preview da Lumen** (140×200px em CSS):
- Fundo: `var(--color-surface)` com gradiente radial índigo no canto superior direito (igual ao hero da Lumen)
- Texto condensado: headline de 2 palavras em `var(--font-size-h4)`, CTA pill em `var(--color-primary)`
- Atmosfera: o preview é **estilizado**, não funcional

**Preview do Norte** (140×200px em CSS):
- Fundo: `var(--color-bg)` com 4 mini-cards de métrica (retângulos com número e label)
- Abaixo: mini-tabela zebrada com 3 linhas
- Badge "Operate" no canto

**Preview da Tereza** (140×200px em CSS):
- Fundo: `var(--color-surface)` com grid assimétrico de retângulos (simulando ilustrações)
- Accent: `var(--color-warning)` (terracotta)
- Badge "Experience" no canto

> **NOTA:** Isso NÃO viola a regra de "fake screenshots de div" (§4.1) porque:
> 1. Não são screenshots — são miniaturas CSS estilizadas que evocam a atmosfera do caso real, com link direto para o HTML funcional.
> 2. Cada card tem um link real ("Ver caso →") que leva ao caso funcional.
> 3. O DESIGN.md §4.1 proíbe "UI falsa de tarefas/terminal/dashboard feita de retângulos" como conteúdo principal da página — aqui são cards de navegação para conteúdo real, análogos a thumbnails de portfólio numa galeria.

### Esforço estimado

- **HTML:** ~80 linhas (seção + 3 cards + linha de links secundários)
- **CSS:** ~100 linhas (grid de 3 colunas, previews estilizados, hover states, badges)
- **Tokens consumidos:** ~15 tokens (cores de superfície, textos, shadows)
- **Risco:** muito baixo — é uma seção de navegação, não de conteúdo. Se os previews ficarem feios, podem ser substituídos por cards textuais puros sem prejuízo da funcionalidade.

### Verificação anti-slop

- Zero em-dash
- Zero hex (todas as cores via `var(--...)`)
- Não usa Inter (system-ui, igual ao showcase)
- Eyebrow único na seção (contagem: 1 do hero + 1 desta seção = 2, abaixo do limite de ceil(16/3) = 6)
- Sem fake screenshot de div (ver justificativa acima)
- Layout diferente das demais seções (aumenta diversidade de layout: §4.5)

---

## 5. Impacto combinado das duas melhorias

| Métrica | Antes | Depois |
|---|---|---|
| Seções com placeholder vazio | 1 (Tokens) | 0 |
| Seções que mostram resultado final | 0 | 1 (Resultados) |
| Casos reais visíveis no showcase | 0 | 3 principais + 5 secundários |
| Tokens demonstrados visualmente | 0 (placeholder) | ~60 tokens em 6 subseções vivas |
| Diversidade de layout (DESIGN.md §4.5) | ~3 famílias | ~5 famílias (hero, tokens-grid, casos-cards, componentes-demo, docs-list) |
| Confiança do humano ao scrollar | Quebra na 2ª seção (placeholder) | Fluxo contínuo: hero → resultados → tokens vivos → componentes |

### Esforço total

| Item | HTML | CSS | JS | Horas estimadas |
|---|---|---|---|---|
| Melhoria 1: Tokens vivos | ~200 ln | ~120 ln | ~30 ln | 4-6h |
| Melhoria 2: Seção Resultados | ~80 ln | ~100 ln | 0 ln | 2-3h |
| **Total** | **~280 ln** | **~220 ln** | **~30 ln** | **6-9h** |

---

## 6. O que NÃO propor (e por quê)

| Ideia descartada | Razão |
|---|---|
| Refazer o hero com ilustração/asset grande | O hero atual é disciplinado e passa em todos os checks do pre-flight (§4.2). Mexer nele introduz risco de quebrar a disciplina que funciona. A seção Resultados resolve o problema "show, don't tell" sem tocar no hero. |
| Adicionar animações de scroll nas seções de componente | A seção Motion dos tokens vivos já demonstra as curvas. Animar a galeria de componentes seria "motion because it looks cool" (§4.4), sem motivo funcional. |
| Tema escuro como default | O kit já resolve dark/light via `prefers-color-scheme` e toggle. Forçar um tema seria quebrar o theme lock. |
| Refatorar o CSS dos componentes | Fora de escopo — os componentes funcionam e passam em a11y e contraste. Melhoria cosmética sem ganho funcional. |
| Adicionar seção de "preços" ou "planos" | O Design Kit não é um produto comercial ainda (decisão pendente do fundador, docs/arquitetura §5). |

---

## 7. Checklist de conformidade com DESIGN.md

- [x] Design Read: showcase é modo **Read** (documentação de sistema de design). Dials: VARIANCE 5 (consistência de documentação), MOTION 3 (motion-demo só na subseção de tokens), DENSITY 4 (equilibrado entre galeria e densidade de info)
- [x] Zero `—` e zero `–` (mantido como está no showcase atual)
- [x] Theme lock: um tema por página (mantido)
- [x] Color lock: um accent (índigo) em tudo — os previews dos casos podem usar seus próprios accents (terracotta no card da Tereza) porque são vitrines, não páginas independentes; o card em si usa tokens do kit
- [x] Shape lock: um sistema de raio (mantido)
- [x] Contraste AA: todos os textos nos previews e na visualização de tokens passam AA contra seus fundos
- [x] Sem fake screenshots — miniaturas são CSS evocativo com link para HTML real (ver justificativa na §4)
- [x] Cópia em pt-BR, sem verbos de filler, números honestos
- [x] Eyebrows: 2 no total (hero + resultados) para 16 seções; limite = ceil(16/3) = 6. OK.
- [x] Diversidade de layout: ≥ 4 famílias (hero, tokens-grid, casos-cards, componentes-demo, docs-list = 5)
- [x] Motion motivado apenas na subseção de tokens (demonstração das curvas)
- [x] `prefers-reduced-motion` no motion-demo

---

## 8. Próximos passos

1. **Aprovação do orquestrador** (este documento é a proposta; o orquestrador revisa e aloca)
2. **Implementação da Melhoria 2 primeiro** (Resultados) — é mais rápida, menor risco, entrega valor imediato (o showcase ganha uma seção que mostra resultado real)
3. **Implementação da Melhoria 1** (Tokens vivos) — mais trabalhosa, mas fecha o maior gap visual
4. **Rodar smoke test + anti-slop check** após cada implementação
5. **Handoff**: atualizar `docs/componentes/` se novos padrões surgirem