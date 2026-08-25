# Arquitetura da Informação - Farol

> Skill: `information-architect` · Entrada: `research.md` · Saída: sitemap + fluxos com estados de borda.

## Sitemap

```
/                              ← visão geral (painel do balcão: vitrine, pedidos, relatório em 1 olhar)
├── /catalogo                  ← tarefa: escolher títulos dos distribuidores
│   ├── /catalogo/importar     ← importar catálogo (upload ou link)
│   └── /catalogo/selecionados ← títulos escolhidos para a vitrine
├── /vitrine                   ← tarefa: ver e organizar o que está à venda
├── /pedidos                   ← tarefa: acompanhar o que pediu e o que chegou
├── /relatorios                ← tarefa: gerar relatório mensal pro contador
└── /configuracoes             ← tarefa: livraria, distribuidores, conta
```

Navegação primária: 5 itens (dentro do limite 3-7, 1 nível). Rotulagem na linguagem do livreiro ("vitrine", "pedidos"), não em termos técnicos ("inventário", "supply chain").

## Fluxos

### Fluxo 1: cadastrar livro (caminho feliz)

```
[/catalogo] → busca/importa → [tela catálogo] → marca título → /catalogo/selecionados → define preço → [/vitrine] título ativo
```

- **Alternativo:** título já existe no estoque → aviso "já na vitrine" + botão "editar posição".
- **Borda vazio:** catálogo sem títulos → empty state "Importe seu primeiro catálogo" com CTA.
- **Borda erro:** upload de arquivo inválido → alert de erro + mantém o que já foi importado.
- **Borda carregando:** importação longa → skeleton da lista + progresso.

### Fluxo 2: gerar relatório mensal

```
[/relatorios] → escolhe mês → [botão "Gerar PDF"] → download → sucesso
```

- **Alternativo:** mês sem vendas → relatório com zeros honestos + nota "sem movimento".
- **Borda erro:** falha na geração → alert erro + botão "tentar de novo" (não perde o mês selecionado).
- **Borda carregando:** geração em andamento → progress bar + estado do botão (disabled).

## Telas (tarefa + próximo passo)

| Tela | Tarefa do usuário | Próximo passo desejado |
|---|---|---|
| Visão geral | Entender o estado da livraria em 1 olhar | Ir para a tarefa pendente (ex.: importar catálogo) |
| Catálogo | Escolher títulos que vendem | Definir preço → vitrine |
| Selecionados | Revisar a seleção antes de publicar | Publicar na vitrine |
| Vitrine | Ver o que está à venda | Ajustar posição/preço |
| Pedidos | Conferir o que chegou | Atualizar estoque |
| Relatórios | Fechar o mês pro contador | Baixar PDF |
| Configurações | Cadastrar livraria e distribuidores | Voltar ao balcão |