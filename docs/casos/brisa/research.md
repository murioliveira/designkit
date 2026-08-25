# Pesquisa — Brisa

> Produzido pelo **design-researcher** seguindo `skills/design-researcher/SKILL.md` + templates (`persona.md`, `jornada.md`, `scan-competitivo.md`, `brief-de-design.md`).
> **Brief de entrada (3 linhas):** "Brisa — app de assinatura de cafés especiais por região do Brasil. Público: apreciadores de café que querem descobrir produtores locais sem intermediários. Contexto: mercado de cafés especiais cresce no Brasil, mas descoberta de produtores regionais é fragmentada (feiras, indicações, redes sociais)."
> Caso real (não é o Lumen) · 2026-08-25 · Dados não fornecidos marcados como `[assunção]`.

## 1. Input organizado

- **Problema/oportunidade:** apreciadores de café querem descobrir produtores locais, mas a descoberta é fragmentada (feiras, indicações, redes sociais).
- **Público-alvo:** apreciadores de café especial (quem usa e paga). Produtores (quem fornece) são parceiros, não usuários da v1.
- **Contexto:** mercado de cafés especiais em crescimento no Brasil; canal de descoberta atual é manual.
- **Sucesso:** usuário encontra e assina um café regional em poucos minutos; assinatura recorrente se mantém.
- **Lacunas:** faixa de preço tolerada, frequência de consumo, plataforma (web/mobile), entregas em todo o país `[assunção]` — perguntas em aberto no brief.

## 2. Problem statement

> Apreciadores de café especial no Brasil precisam descobrir produtores regionais confiáveis e assinar cafés de qualidade sem intermediários, porque o mercado cresce mas a descoberta hoje depende de feiras, indicações e redes sociais. Isso falha porque não há um canal único que una curadoria, origem confiável e entrega recorrente.
> **Sucesso =** ≥ 60% dos novos usuários completam a primeira assinatura em ≤ 10 minutos, e ≥ 50% renovam no 2º mês `[assunção — a validar com dados]`.

## 3. Persona (1 principal)

### Nome fictício e papel

**Nome:** Marina · **Papel:** apreciadora de café especial (consumidora final)

**Contexto** (1 parágrafo): Marina, 34, analista de marketing em home office em São Paulo. Toma 2–3 cafés por dia, compra grãos em feiras e lojas de bairro quando viaja, segue 5 torrefações no Instagram, mas nunca sabe ao certo a procedência nem se o preço é justo. Já tentou assinaturas genéricas e cancelou por entrega irregular.

## Objetivos

- Descobrir cafés de regiões brasileiras (Cerrado, Mantiqueira, Matas de Minas) com origem verificável.
- Assinar um plano recorrente sem dor de cabeça (parar/pausar quando viajar).
- Pagar preço justo e sentir que o dinheiro chega ao produtor.

## Dores

- Descoberta depende de sorte (feira que passou, post que viu).
- Assinaturas genéricas entregam blends sem origem clara; procedência vira "marketing".
- Pausar/cancelar assinatura é burocrático (email, WhatsApp, retenção agressiva).

## Citação representativa

> "[assunção] — 'Eu compraria todo mês se eu soubesse de onde vem e se eu pudesse pausar sem drama quando viajo.'"

## Necessidades de design

| Necessidade | O que a UI deve garantir |
|---|---|
| Entender a proposta em 10s | Hero com "cafés de produtores brasileiros, assinatura mensal" antes de qualquer CTA |
| Confiar na origem | Origem visível por região/produtor com selo de origem; sem jargão |
| Pausar sem atrito | Pausar/reiniciar assinatura em ≤ 2 cliques, sem fluxo de retenção |
| Comparar planos sem ajuda | 3 planos claros (frequência/quantidade/preço) com preço visível |

## 4. Jornada resumida

| Fase | Ações | Pontos de contato | Emoção | Dores / oportunidades | Momento de design |
|---|---|---|---|---|---|
| Descoberta | Vê um post de café regional, busca "café de produtor brasileiro" | Instagram, busca | 😕 | Fragmentação | Landing que explica origem + curadoria |
| Consideração | Compara planos, lê sobre produtores | Site, FAQ | 😐 | Desconfiança de procedência | Perfil de região com foto/produtor e origem |
| Decisão | Escolhe plano e regiões, cadastra | Checkout de assinatura | 🙂 | Preço justo pouco claro | Card de assinatura com preço, frequência, pausa |
| Uso | Recebe o café, avalia origem | Entrega, app | 🙂 | Entrega irregular | Timeline de entrega + nota da origem |
| Fidelização | Renova, indica | Email, comunidade | 😍 | Renovação automática indesejada | Controle de pausa visível no painel |

**Momento crítico (aha):** na fase de **Decisão** — quando Marina entende que pode escolher a região, ver o preço e pausar sem drama; a clareza do card de assinatura é o "aha".

## 5. Scan competitivo

| Concorrente / alternativa | Proposta | Pontos fortes | Pontos fracos | Diferencial para nós |
|---|---|---|---|---|
| Assinaturas genéricas (ex.: clubes de café) | Café mensal sem escolha de origem | Entrega regular, preço simples | Blend sem origem clara; retenção agressiva para cancelar | Origem por região + pausa em 1 clique |
| Lojas/torrefações locais | Café de bairro | Qualidade, relação local | Alcance limitado; sem recorrente | Curadoria multi-região com a mesma confiança local |
| Redes sociais/feiras | Descoberta por indicação | Autenticidade | Fragmentado, sem comparação | Canal único: curadoria + origem + assinatura |
| Alternativa zero: "continuo como está" | — | Custo zero | Descoberta aleatória | Conveniência de um lugar só |

**Leitura rápida:** o padrão comum (assinaturas genéricas) esconde a origem; a expectativa do mercado é entrega recorrente simples; a oportunidade é **transparência de origem + controle de pausa** — nenhum player combina os dois.

**Posicionamento sugerido:** "Para apreciadores de café especial no Brasil, contra assinaturas sem origem e descoberta fragmentada, com a promessa de cafés regionais com procedência visível e assinatura que você pausa quando quiser."

## 6. Brief de design

### Produto/caso: Brisa · Data: 2026-08-25

**Problem statement:** ver §2. **Critério de sucesso:** ≥60% completam 1ª assinatura ≤10min; ≥50% renovam no 2º mês `[assunção]`.

**Personas (resumo):** Marina — apreciadora que quer origem visível e pausa sem atrito.

**Escopo v1 — Dentro:** landing com proposta + regiões; catálogo com filtro por região; card de assinatura (escolha de região, frequência, quantidade, preço); checkout mínimo (email + pagamento); painel com pausar/reiniciar.
**Escopo v1 — Fora:** marketplace de produtores (cadastro de produtor), app mobile nativo, frete em tempo real, recomendação por IA.

**Restrições:**
- Técnica: web responsiva (mobile-first), HTML/CSS/JS puro ou React; performance < 2s no 4G `[assunção]`.
- Marca/visual: **consumir somente tokens semânticos de `styles/tokens.css`** (regra do designkit); sem hex hardcoded.
- Conteúdo: pt-BR, tom acolhedor e direto, zero lorem ipsum.

**Perguntas em aberto (para o humano validar):**
1. Faixa de preço aceitável por mês? (R$ 40–80? `[assunção]`)
2. Plataforma alvo: web primeiro ou app? (v1 = web `[assunção]`)
3. Entregas em todo o país ou só capitais? `[assunção]`

**Direção criativa recomendada:**
- **Opção 1 — "Fazenda à mesa":** tons quentes de terra, tipografia serifada de origem, fotos de produtores; referência: marcas de café de origem.
- **Opção 2 — "Moderno transparente":** claro/limpo, muito branco + verde de origem, dados de procedência em cards; referência: marketplaces de origem direta.
- **Opção 3 — "Editorial regional":** bold typographic, mapas do Brasil com regiões interativas; referência: revistas de viagem/gastronomia.

> O humano escolhe (ou mistura) antes da fase de UI. Não siga a opção 1 por padrão sem avisar.
