# Arquitetura de Informação — Brisa

> Produzido pelo **information-architect** seguindo `skills/information-architect/SKILL.md` + template `sitemap-fluxos.md`.
> **Fonte:** `docs/casos/brisa/research.md` (problem statement, persona Marina, escopo v1). Deriva do research — nada inventado fora do escopo v1.

## Sitemap

```
/                       ← home · tarefa: entender a proposta (origem + assinatura) e escolher uma região
├── /regioes             ← tarefa: descobrir cafés por região do Brasil
│   ├── /regioes/cerrado        ← tarefa: conhecer produtores e cafés do Cerrado
│   ├── /regioes/mantiqueira    ← tarefa: conhecer produtores e cafés da Mantiqueira
│   └── /regioes/matas-de-minas ← tarefa: conhecer produtores e cafés de Matas de Minas
├── /planos              ← tarefa: comparar frequência/quantidade/preço e assinar
├── /como-funciona       ← tarefa: entender entrega, origem e política de pausa
└── /conta (painel)      ← tarefa: gerenciar assinatura (pausar/reiniciar, endereço, pagamento)
```

### Anotações por página

| Página | Tarefa do usuário | Conteúdo essencial (3–5 blocos) | Próximo passo desejado |
|---|---|---|---|
| / | Entender proposta em 10s | Hero (proposta + origem), mapa de regiões, prova social, CTA | → /regioes ou /planos |
| /regioes | Descobrir por região | Lista de regiões com foto, perfil de origem, filtro | → região específica |
| /regioes/cerrado (padrão p/ demais) | Conhecer a região | Produtores, perfil de sabor, selo de origem, CTA assinar | → /planos |
| /planos | Comparar e assinar | 3 planos (frequência/quantidade/preço), card de assinatura, checkout | → /conta (pós-assinatura) |
| /como-funciona | Confiar no processo | Origem verificada, entrega, pausa em 1 clique, FAQ | → /planos |
| /conta | Gerenciar | Assinatura ativa, pausar/reiniciar, próximo envio, pagamento | → painel (fidelização) |

## Fluxos de usuário

### Fluxo 1 — Assinar plano (persona Marina)

**Caminho feliz:** `[gato: anúncio/post de café regional] → [clica CTA "Assinar"] → [/planos] → [escolhe plano e região] → [cadastra email + pagamento] → ✅ [/conta com assinatura ativa]`

**Alternativos:** voltar para comparar planos; trocar região sem perder o plano escolhido; sair e retomar depois (carrinho preservado).

**Bordas:** vazio → catálogo sem cafés da região escolhida (mensagem + sugestão de região próxima); erro → pagamento recusado (mensagem + token `--color-error` + tentar outro cartão); carregando → skeleton do card de assinatura.

**Saída:** confirmação na /conta com próximo envio visível (reduz ansiedade de "será que assinou?").

### Fluxo 2 — Pausar assinatura (persona Marina, dor principal)

**Caminho feliz:** `[gatilho: viagem de 2 semanas] → [/conta → "Pausar"] → [escolhe período (2 semanas)] → ✅ [status "pausada até [data]"]`

**Alternativos:** pausa por tempo indeterminado; reiniciar antes do prazo; cancelar de vez (sem retenção agressiva).

**Bordas:** vazio → sem assinatura ativa (CTA para assinar); erro → falha ao pausar (mensagem + tentar de novo); carregando → spinner/botão desabilitado.

**Saída:** confirmação clara + o que acontece com o pagamento do ciclo corrente.

## Lista de telas (resumo executável para o UI Designer)

| # | Tela | Tarefa | Conteúdo essencial | Próximo passo |
|---|---|---|---|---|
| 1 | Home | Proposta + origem em 10s | Hero, mapa de regiões, social proof | /regioes |
| 2 | /regioes | Descobrir por região | Lista + filtro + perfis | região |
| 3 | /planos | Comparar e assinar | 3 planos, card de assinatura | /conta |
| 4 | /conta | Gerenciar (pausar) | Assinatura, pausa, pagamento | painel |

> Escopo v1 respeitado: nenhuma página fora do brief (sem marketplace de produtores, sem app nativo).
