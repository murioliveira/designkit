# Research - Farol

> Skill: `design-researcher` · Entrada: `brief.md` · Saída: problem statement, persona, jornada, scan competitivo, brief de design.

## Problem statement

Livreiros de bairro (donos de livraria independente, em geral não-técnicos) precisam escolher títulos de vários distribuidores e controlar estoque e relatório sem afogar o pouco tempo livre em planilha, porque hoje isso é feito por email, caderno e conferência manual no fim do mês. Sucesso = relatório mensal em menos de 15 minutos, sem abrir planilha.

## Persona (1)

**Otávio, 52, dono da Livraria Quilombo** (bairro, 15 anos de portas abertas).

- **Contexto:** trabalha sozinho no balcão de manhã, com a filha à tarde. Compra de 4 distribuidores. Não é técnico: usa celular e computador do balcão para o básico.
- **Objetivos:** manter a vitrine cheia de títulos que vendem, saber o que gastou no mês, fechar o relatório pro contador sem dor.
- **Dores:** catálogo chega por email em PDF e planilha em formatos diferentes; anota escolhidos num caderno; no fim do mês soma tudo na calculadora e leva horas.
- **Citação:** "O que mais me cansa não é vender, é a papelada depois que a loja fecha." [assunção: derivada do problema descrito no brief]
- **Necessidades de design:** 1) escolher títulos com poucos toques, sem caçamba de planilha; 2) ver em uma tela o que pediu e o que chegou; 3) relatório pronto em 1 clique, legível e exportável.

## Jornada (resumida)

| Fase | Ação | Emoção | Momento de design |
|---|---|---|---|
| Descoberta | Recebe convite da distribuidora parceira | 🙂 | Explicar em 1 tela de onboarding |
| Decisão | Importa primeiro catálogo | 😕 (medo de ser difícil) | Upload guiado com resultado visível na hora |
| Uso | Escolhe títulos para a vitrine | 😐→🙂 | Seleção por toque; busca por autor/editora |
| Uso | Confere o que chegou | 🙂 | Lista pedidos x entregas lado a lado |
| Fidelização | Gera relatório mensal | 😍 (vira herói) | Botão único, PDF pronto, sem planilha |

## Scan competitivo (rápido)

- **Planilha + email (alternativa zero):** o que o livreiro usa hoje. Forte: é conhecida. Fraco: manual, propensa a erro, nenhum relatório pronto. O Farol ganha ao automatizar a coleta e gerar relatório.
- **Sistemas de PDV de grande porte:** feitos para lojas com equipe e estoque complexo. Forte: robustos. Fraco: caros, complexos para o livreiro solo. O Farol ganha em simplicidade e foco no balcão. [assunção: baseada em conhecimento geral do mercado]

## Brief de design

- **Dentro do escopo v1:** catálogo, seleção de títulos, vitrine, estoque, relatório. **Fora:** PDV, marketplace, app do cliente.
- **Restrições:** tokens do designkit, zero hex, mobile-first no tablet, desktop no balcão.
- **Direções criativas (2 opções):** A) "bancada de trabalho" - tons neutros quentes, tipografia editorial, acolhedora; B) "vitrine iluminada" - neutros frios com accent marcante tipo lâmpada de vitrine, mais presença.
- **Pergunta em aberto:** o livreiro prefere importar catálogo automaticamente (integração com distribuidor) ou por arquivo manual na v1? [as duas são cobertas na UI proposta com fallback manual]

**Recomendação de direção:** B (vitrine iluminada), porque o accent lâmpada comunica o benefício central (dar visibilidade aos títulos) e se diferencia da planilha cinza que ele quer deixar.