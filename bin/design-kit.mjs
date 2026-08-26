#!/usr/bin/env node
/**
 * Design Kit CLI
 * Installs the Design Kit skills into your AI agent (Claude Code, Codex, Cursor, pi, etc.)
 *
 * Usage:
 *   npx design-kit install             # install the 8 skills into all detected agents
 *   npx design-kit install --global    # install to the user dir instead of the project
 *   npx design-kit verify              # check the Design Kit is installed and healthy
 *   npx design-kit version             # print version
 *
 * Recommended path (GitHub as registry, like /impeccable):
 *   npx skills add murioliveira/designkit
 */
import { fileURLToPath } from "node:url";
import path from "node:path";
import fs from "node:fs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SKILLS_SRC = path.join(ROOT, "skills");
const TEMPLATES_SRC = path.join(ROOT, "templates");
const VERSION = "0.9.0";

const SKILL_NAMES = [
  "a11y-auditor",
  "design-critic",
  "design-handoff",
  "design-redesign",
  "design-refine",
  "design-researcher",
  "information-architect",
  "ui-designer",
];

// Agent skill-directory mapping (relative to a base dir).
const BASE_DIR = process.env.HOME || process.env.USERPROFILE || process.cwd();
const AGENT_DIRS = {
  "claude-code": path.join(BASE_DIR, ".claude", "skills"),
  codex: path.join(BASE_DIR, ".codex", "skills"),
  cursor: path.join(BASE_DIR, ".cursor", "skills"),
  pi: path.join(BASE_DIR, ".pi", "agent", "skills", "design-kit"),
  "agents": path.join(BASE_DIR, ".agents", "skills"), // universal
};

function installTo(dir) {
  fs.mkdirSync(dir, { recursive: true });
  let installed = 0, updated = 0;
  for (const name of SKILL_NAMES) {
    const src = path.join(SKILLS_SRC, name);
    if (!fs.existsSync(path.join(src, "SKILL.md"))) {
      console.log(`  ! ${name}: SKILL.md ausente em src`);
      continue;
    }
    const dest = path.join(dir, name);
    const existed = fs.existsSync(path.join(dest, "SKILL.md"));
    fs.rmSync(dest, { recursive: true, force: true });
    fs.cpSync(src, dest, { recursive: true });
    if (existed) updated++; else installed++;
  }
  // shared templates (into a parent-level "templates" that co-locates with skills)
  const templatesDest = path.join(dir, "..", "templates");
  fs.rmSync(templatesDest, { recursive: true, force: true });
  fs.cpSync(TEMPLATES_SRC, templatesDest, { recursive: true });
  return { installed, updated };
}

function cmdInstall(args) {
  const only = args.length === 0 ? null : args.filter((a) => !a.startsWith("--"));
  console.log(`Design Kit v${VERSION} — instalando skills`);
  const targets = only && only.length
    ? Object.entries(AGENT_DIRS).filter(([k]) => only.includes(k))
    : Object.entries(AGENT_DIRS);
  if (!targets.length) { console.error("agente não reconhecido. Opções: " + Object.keys(AGENT_DIRS).join(", ")); process.exit(1); }
  let total = 0;
  for (const [name, dir] of targets) {
    const r = installTo(dir);
    console.log(`  ✓ ${name}: ${r.installed} nova(s), ${r.updated} atualizada(s) -> ${dir}`);
    total += r.installed + r.updated;
  }
  console.log(`\nPronto. ${total} skill(s). \`npx design-kit verify\` para conferir.\nTambém disponível: npx skills add murioliveira/designkit`);
}

function cmdVerify() {
  let ok = 0;
  console.log(`Design Kit v${VERSION} — verificação`);
  for (const name of SKILL_NAMES) {
    const candidates = [
      path.join(BASE_DIR, ".agents", "skills", name, "SKILL.md"),
      path.join(BASE_DIR, ".claude", "skills", name, "SKILL.md"),
      path.join(SKILLS_SRC, name, "SKILL.md"),
    ];
    const found = candidates.find((p) => fs.existsSync(p));
    if (found) {
      const text = fs.readFileSync(found, "utf-8");
      if (text.trimStart().startsWith("---")) { ok++; console.log(`  [ok] ${name}`); }
      else console.log(`  [!]  ${name}: frontmatter inválido`);
    } else {
      console.log(`  [..] ${name}: não encontrada (rode npx design-kit install)`);
    }
  }
  console.log(ok === SKILL_NAMES.length
    ? "Design Kit OK — todas as 8 skills presentes e válidas."
    : `${ok}/${SKILL_NAMES.length} skills presentes.`);
}

const arg = (process.argv[2] || "").toLowerCase();
try {
  const cmd = { i: "install", install: "install", v: "verify", verify: "verify", version: "version", "--version": "version", "-v": "version" }[arg];
  if (cmd === "install") cmdInstall(process.argv.slice(3));
  else if (cmd === "verify") cmdVerify();
  else if (cmd === "version") console.log(VERSION);
  else {
    console.log(`Design Kit CLI v${VERSION}

Usage:
  npx design-kit install            instala as 8 skills nos agentes
  npx design-kit verify             verifica se o kit está instalado e saudável
  npx design-kit version            versão

Recomendado (ecossistema de skills, GitHub como registry — como o /impeccable):
  npx skills add murioliveira/designkit
`);
  }
} catch (err) {
  console.error("design-kit:", err.message);
  process.exit(1);
}