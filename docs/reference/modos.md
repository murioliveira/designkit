# Modos de superfície - Referência do Design Kit

> Aprofundamento do DESIGN.md §1. O modo vem da **superfície**, não do produto: uma landing de dashboard continua Persuade; a documentação de um SaaS continua Read; o app do mesmo SaaS é Operate. Antes de desenhar, declare o modo no Design Read e ajuste os dials por ele.
> Âncoras: [Persuade](#1-persuade-landing-o-design-é-o-produto) · [Operate](#2-operate-apps-dashboards-admin) · [Read](#3-read-docs-artigos-help) · [Experience](#4-experience-portfólios-galerias-vitrines) · [Como escolher](#5-como-escolher-o-modo) · [Cross-mode](#6-cross-mode-o-que-muda-e-o-que-não-muda)

---

## 1. Persuade (landing, o design é o produto)

**Quando:** landing pages, marketing, pricing, campanhas, qualquer superfície cujo trabalho é fazer o visitante decidir e agir. O design É o produto: a estética é o argumento.

**Referências no repo:** `docs/casos/aurora/` (landing premium de ateliê, 14/14 pre-flight, zero tells) e `docs/casos/lumen/` (landing de produto com IA, critique 4.7/5).

### Hierarquia de prioridade: atenção → ação

1. **Atenção (primeiro viewport):** o hero precisa ganhar o olhar em segundos. O DESIGN.md §4.2 já fixa a disciplina (headline ≤ 2 linhas, subtext ≤ 20 palavras, CTA visível, ≤ 4 elementos, padding ≤ 6rem). O que o Aurora prova: hero split assimétrico (conteúdo | peça em SVG), headline como manifesto ("Cerâmica que nasce da mão, não da máquina."), zero scroll cue, zero logo wall dentro do hero.
2. **Crença (meio da página):** prova social, processo, materialidade. No Aurora, o manifesto editorial vem logo após o hero (coluna estreita, tipografia como voz), depois a coleção (grid assimétrico), depois o processo ("Moldar, Queimar, Esmalta" em verbo-nome, sem "Etapa 1/2/3"), depois depoimentos com hairlines (quotes ≤ 3 linhas, atribuição nome + papel, sem estrelas decorativas).
3. **Ação (fechamento):** CTA final com intenção distinta das anteriores (o Aurora termina em "Falar com o ateliê", que é intenção de contato, diferente do browse "Ver a coleção"). UMA intenção por CTA em toda a página, labels que não quebram.

### Padrões de conversão (Persuade específico)

- **Estrutura narrativa:** promessa → prova → processo → fechamento. Cada seção tem UM trabalho. Nunca duas seções com o mesmo layout (diversidade de famílias: hero split, manifesto, grid assimétrico, depoimentos com hairlines).
- **Prova social honesta:** depoimentos com nomes reais e papéis (o Aurora usa Duarte/Andrade/Prado, arquiteta/colecionador/chef), nunca "Jane Doe" nem estrelas falsas. Logo wall DEBAIXO do hero, com logos SVG reais, sem labels de categoria.
- **Imagens são o produto:** fotografia real ou slot marcado (`<!-- TODO: foto ... -->`), nunca fake screenshot de div. O Aurora declara 3 slots de foto onde a fotografia faria o trabalho (bule, cumbuca, esmaltação).
- **Números honestos:** dados reais ou marcados `<!-- mock -->`. O Aurora usa "mil e duzentos graus" (processo real de queima), não "99.9%".

### Armadilhas específicas de Persuade

- **Paleta bege+latão+oxblood** em briefs premium (tell nº 2): o Aurora escolheu monocromático de pedra + pop índigo, e documenta o porquê.
- **Eyebrow em toda seção:** o Aurora usa 2 eyebrows para 6 seções (≤ ceil(6/3)); hero conta como 1.
- **Serifa como atalho de "criativo":** o Aurora não usa serifa; a voz vem da escala (display 56px) e do tracking apertado.
- **Scroll cues, strips decorativos, version footers:** banidos (DESIGN.md §4.1).
- **Motion não motivado:** landing premium tende ao calmo; MOTION_INTENSITY 3 com hover/active apenas é decisão, não preguiça (o Aurora documenta isso).

---

## 2. Operate (apps, dashboards, admin)

**Quando:** dashboards, apps de produto, admin, settings, ferramentas. O visitante **completa uma tarefa**; scanability, consistência e expectativas nativas superam expressão. A marca vive em detalhes precisos, não em espetáculo.

**Referência no repo:** `docs/casos/norte/` (dashboard de gestão financeira, critique 4.6/5, reuso real de 12 grupos do kit), a prova real de Operate.

### Densidade de dados e scanability

- **Métrica primeiro, detalhe depois:** o Norte ordena a tela como o olhar de um gestor: situação imediata (4 cards de métrica) → tendência (gráfico com granularidade Semana/Mês/Trimestre) → lançamentos (tabela). O usuário encontra o número que procura sem caçar.
- **Dígitos tabulares:** `.table__num` do kit alinha valores em coluna (R$ 48.230,00 alinhado sob R$ 312,00), decisivo em colunas monetárias.
- **Densidade via tokens:** `VISUAL_DENSITY` alto significa menos ar, nunca valores fora da escala. O Norte usa `--space-1..16` do kit, com padding de página controlado.

### Tabelas (o coração de Operate)

O Norte demonstra os quatro estados e o que o kit cobre sem override:

- **Denso:** `.table--zebra` para leitura por linha; `overflow-x` (`.table-wrap`) para mobile, sem quebrar colunas.
- **Numérico:** `.table__num` (dígitos tabulares) + valores em BRL realistas.
- **Vazio:** `<tbody hidden>` alternado com `.table__empty` (colspan 6) via filtro JS, com ação de recuperação ("Limpar filtro").
- **Acessível:** `aria-describedby` no `<table>` apontando para o `<caption>`; `aria-current="page"` na paginação; `aria-disabled` na seta inativa.
- **Ação em contexto:** dropdown de ações do relatório (exportar/imprimir/arquivar) e modal de detalhe com `role="dialog" aria-modal="true"`, trap de foco, Esc e devolução de foco ao gatilho.

### Navegação e hierarquia em telas densas

- **Breadcrumb** para posição ("Início / Financeiro / Relatórios") com `aria-current="page"` no item atual; separador vindo do CSS, não do texto.
- **Tabs** para granularidade de dados (Semana/Mês/Trimestre) com roving tabindex + setas + Home/End.
- **Stepper** para progresso de onboarding (`.stepper--vertical`, `aria-current="step"`) com nota de valor real (R$ 588,00 anual), não "Etapa 1/2/3".
- **Alertas contextuais:** erro (fatura #4817) e info (importação concluída) com `role=alert`/`role=status`, posicionados onde a tarefa acontece.

### Formas longas (settings, onboarding, cadastro)

- Progresso visível (stepper) e validação **inline** (erro abaixo do input, `aria-invalid` + `role=alert`, foco no primeiro inválido, conforme `docs/componentes/formularios.md`).
- Label acima do input; helper opcional no markup; nunca placeholder-como-label.
- Estados de loading (skeleton no formato final) e empty (composto, indica como popular) em toda seção de dados.

### Diferenças vs Persuade (o que cede)

| Dimensão | Persuade | Operate |
|---|---|---|
| Expressão | alta, a estética é o argumento | contida, a eficiência é o argumento |
| Motion | pode ser cinemático (dial alto) | só feedback (hover/active/transição de estado) |
| Densidade | baixa a média | média a alta (cockpit) |
| Layout | diversidade de famílias por seção | grelhas estáveis e repetíveis entre telas |
| Hierarquia | narrativa (atenção → ação) | scanability (métrica → detalhe) |

O Norte não usa nenhum dos padrões de Persuade: sem hero, sem manifesto, sem narrativa. A expressão do dashboard está no alinhamento dos números, na consistência dos badges de status e no teclado completo.

---

## 3. Read (docs, artigos, help)

**Quando:** documentação, guias, artigos, help, changelog. O visitante **entende algo**; a estrutura para compreensão é o design.

**Referências no repo:** `docs/guia-de-uso.md`, `docs/arquitetura-agente-design.md`, `docs/componentes/`; o próprio repositório é a prova viva do modo Read (o kit come sua própria comida).

### Estrutura para compreensão

- **TOC e âncoras no topo** (como este arquivo): o leitor localiza a seção antes de rolar.
- **Headings com hierarquia real** (h2/h3 sem pular níveis) e `aria-labelledby` nas seções quando interativas.
- **Exemplo > explicação:** mostrar o componente com classes e tokens primeiro, explicar depois (padrão dos docs de handoff em `docs/componentes/`).
- **Uma ideia por seção**; parágrafos curtos; listas para enumerar; tabelas para comparar (ver §6 de `docs/arquitetura-agente-design.md`, que compara funções do setor × capacidades do agente).

### Tipografia de leitura

- Coluna de texto com `max-width: 65ch` e `leading-relaxed` (tokens `--font-line-height-body`); nunca largura cheia para prosa.
- Escala do kit: h2/h3 para títulos, body para leitura, caption para notas; `--font-family-mono` para código e tokens.
- Zero em-dash no texto visível; hífen para intervalos ("2018-2026").

### Code blocks e tabelas de referência

- Code blocks com `--font-family-mono` e cores semânticas do kit (nunca syntax highlighting exótico que fura o color lock).
- Tabelas de referência (tokens, classes, severidades) com zebra e `caption` acessível; colunas curtas e alinhadas.

### Experiência de leitura que vale ficar

- Margens generosas e ritmo vertical consistente (galeria de leitura: densidade baixa, `VISUAL_DENSITY` 2-3).
- Hairlines para separar blocos em vez de cards (card só quando elevação comunica hierarquia).
- Dark mode funcional nos dois temas; micro-gaps (selection coerente, underline de links com offset); o leitor passa horas na página.

---

## 4. Experience (portfólios, galerias, vitrines)

**Quando:** portfólios, galerias, showcases, vitrines. O **artefato lidera** desde o primeiro viewport; a interface recua. O kit trata Experience como disciplina de curadoria sobre Persuade: menos chrome, mais obra.

**Referência no repo:** o próprio `index.html` do showcase (14 seções) e o caso Aurora (landing que funciona como vitrine das peças do ateliê) são os exemplos mais próximos; um portfólio puro ainda não existe como caso, então esta seção é diretriz.

### O artefato lidera

- **Chrome mínimo:** nav discreta (altura ≤ 64px, ou oculta com acesso por teclado), zero footer gigante, zero sidebar explicativa.
- **A peça no viewport inteiro:** imagens grandes (SVG inline ou slots de foto), uma peça por tela em densidade baixa (`VISUAL_DENSITY` 1-3), com respiro.
- **Interface recede:** o tema do kit (claro/escuro) se mantém, mas o accent fica nos micro-detalhes (links, paginação), nunca competindo com a obra.

### Curadoria (menos é mais)

- **Cada peça justifica presença:** se uma obra não sustenta o viewport sozinha, não está na vitrine. O Aurora faz isso com 3 SVGs de peças + 3 slots de foto: seis itens, cada um com identidade própria.
- **Nomes reais e contextuais:** títulos de peça com material e processo ("Bule de porcelana, queima a 1.200°C"), não "Obra 01 / 02".
- **Sem contadores, sem index numerado, sem labels sobre imagens:** a peça fala sozinha; legenda funcional abaixo, se necessário.

### Transições entre peças

- Transição de estado (próxima peça) com `transform`/`opacity` apenas, física suave (spring ~100/~20), `prefers-reduced-motion` colapsa para instantâneo.
- Navegação por teclado (setas) com estado de foco visível; carousel só se a peça for navegável por natureza (galeria), nunca marquee decorativo.

---

## 5. Como escolher o modo

| Superfície (o que é) | Modo | Referência no repo | O que priorizar |
|---|---|---|---|
| Landing, marketing, pricing, campanha | **Persuade** | `docs/casos/aurora/`, `docs/casos/lumen/` | atenção → ação; hero §4.2; prova social honesta; imagens reais |
| Dashboard, app, admin, settings, ferramenta | **Operate** | `docs/casos/norte/` | scanability; tabelas com 4 estados; teclado completo; consistência |
| Docs, artigos, help, changelog | **Read** | `docs/guia-de-uso.md`, `docs/componentes/` | estrutura (TOC/headings); 65ch; exemplo > explicação |
| Portfólio, galeria, vitrine, showcase | **Experience** | `index.html` (showcase), Aurora (vitrine de peças) | artefato lidera; chrome mínimo; curadoria |

Se a superfície for ambígua, use o DESIGN.md §2 (sinais + Design Read + UMA pergunta). O modo vem da superfície, nunca do produto: a landing de um dashboard é Persuade; o dashboard é Operate; a doc do dashboard é Read.

---

## 6. Cross-mode (o que muda e o que não muda)

### Não muda (vale nos 4 modos)

- **Tokens como única fonte de verdade** (regra auditável: zero hex fora de `tokens.css`).
- **A11y e teclado:** landmarks, skip-link, `aria-labelledby`, foco visível, contraste AA (AAA no hero), `prefers-reduced-motion`.
- **Tells da IA banidos** (DESIGN.md §4): zero em-dash, zero 3-cards-iguais, zero fake screenshots, zero nomes genéricos, zero scroll cues, eyebrows ≤ ceil(seções/3).
- **Locks:** 1 accent, 1 raio, 1 tema por página.
- **Pre-flight do DESIGN.md §6** completo antes de shipar, em qualquer modo.
- **Motion motivado** (hierarquia/storytelling/feedback/transição), só `transform`/`opacity`.

### Muda (o dial é do modo)

| Dimensão | Persuade | Operate | Read | Experience |
|---|---|---|---|---|
| VISUAL_DENSITY | 3-5 | 6-9 | 2-3 | 1-3 |
| MOTION_INTENSITY | 5-8 | 2-3 | 1-2 | 3-5 |
| DESIGN_VARIANCE | 6-10 | 2-4 | 2-3 | 5-8 |
| Expressão | alta | contida | neutra | alta, mas na obra |
| Layout | narrativa, famílias variadas | grelhas estáveis | coluna 65ch + tabelas | peça por viewport |
| Formas longas | raras (CTAs) | comuns (settings/onboarding) | formulários de busca | raras |

**Regra prática:** o modo define densidade, motion e expressão; os tokens, a a11y, os tells e o pre-flight são constantes. Se um modo pede algo fora dos tokens (ex.: uma família de ícones específica), proponha via `impeccable extract`, nunca invente.

---

## Resumo (10 linhas)

1. Persuade: o design é o produto; atenção → ação; hero disciplinado; prova social honesta; o Aurora é a referência (14/14 pre-flight).
2. Operate: a tarefa é o produto; scanability e consistência; o Norte prova com 12 grupos do kit, tabela com 4 estados e teclado completo.
3. Read: a compreensão é o produto; TOC + headings + 65ch + exemplo > explicação; os próprios docs do kit são a referência.
4. Experience: o artefato lidera; chrome mínimo; curadoria; cada peça justifica presença.
5. O modo vem da superfície, não do produto (tabela do §5).
6. Tokens, a11y, tells e pre-flight não mudam entre modos; densidade, motion e expressão mudam.
7. Declare o modo no Design Read e fixe os dials por ele, com razão do brief.
8. Em dúvida: uma pergunta ao humano, nunca palpite em silêncio.
9. O kit cobre os 4 modos com os mesmos tokens e componentes; o caso Norte comprova que Operate reusa tudo sem override.
10. Próximo caso sugerido: um portfólio (Experience puro) para fechar a matriz de modos com prova real.
