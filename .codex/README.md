# Portabilidade para o Codex (OpenAI)

O Codex lê o `AGENTS.md` na raiz do projeto como onboarding — não há arquivo
de instruções adicional a criar. Este diretório documenta como o Codex acessa
as skills do designkit.

## Como o Codex carrega o designkit

1. **Onboarding**: o `AGENTS.md` na raiz (formato nativo do Codex) instrui o
   agente a agir como o setor de design e a percorrer o fluxo
   brief → research → IA → UI → critique → refine → a11y → handoff.
2. **Skills**: o Codex não descobre `skills/` automaticamente no formato
   `SKILL.md` do pi/Claude Code. Dois caminhos equivalentes:

   - **Caminho A (recomendado)**: o `AGENTS.md` já aponta o agente para ler as
     skills em `skills/<nome>/SKILL.md` na etapa correspondente do fluxo. O
     Codex lê o arquivo como qualquer outro markdown do repositório e segue as
     instruções — as skills foram escritas para serem auto-contidas e legíveis.
   - **Caminho B (opcional)**: se o usuário quiser skills nativas do Codex,
     copie cada `skills/<nome>/SKILL.md` para `.codex/skills/<nome>.md` (skills
     do projeto, caso a sua versão do Codex descubra esse diretório) ou para
     `~/.codex/skills/<nome>.md` (uso global). **Verifique a versão do Codex em
     uso** (ex.: `codex --version`): as versões mais recentes suportam
     descoberta nativa de skills em `.codex/skills/`; em versões anteriores o
     caminho pode não ser lido automaticamente e o Caminho A é o caminho
     confiável. O conteúdo copiado é o mesmo, sem adaptação.

3. **Fallback embutido**: as skills `ui-designer`, `design-critic` e
   `a11y-auditor` têm instruções de fallback embutidas no próprio SKILL.md —
   funcionam mesmo sem `web-design-engineer`/`impeccable` no ambiente. As
   skills originais (`design-researcher`, `information-architect`,
   `design-handoff`) são auto-contidas por construção.

## Verificação (o que deve funcionar no Codex)

- `AGENTS.md` lido na raiz → o Codex se comporta como o setor de design.
- Ao pedir "pesquisa de design", o Codex lê `skills/design-researcher/SKILL.md`
  e produz problem statement, personas, jornada e scan competitivo.
- Ao pedir "critique dessa tela", o Codex lê `skills/design-critic/SKILL.md`
  e devolve scoring por heurísticas + lista priorizada.

## Limitação conhecida

O Codex não tem um mecanismo de "skill discovery" equivalente ao
`.claude/skills/` do Claude Code — a descoberta depende do `AGENTS.md` instruir
o agente a ler as skills (Caminho A). Se a versão do Codex usada pelo usuário
suportar skills nativas, aplicar o Caminho B melhora a descoberta sem mudar o
conteúdo.
