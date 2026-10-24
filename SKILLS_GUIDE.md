# ADHD Wise skills guide

House rules for every skill in ADHD Wise repos. The official format lives at
[agentskills.io/specification](https://agentskills.io/specification) and
[code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills); this guide only
covers what is ours. `make check` enforces the rules marked **(checked)**.

## Who we write for

An adult with ADHD who uses Claude Desktop or claude.ai, is not a developer, and opened
this skill because they are stuck, overwhelmed or avoiding something. Every extra step is
a chance to drop off.

## The ADHD rules

1. **One next action first.** The first thing the reader sees is the single next step,
   with a time estimate. Context comes after, if at all.
2. **Five items maximum** in any list the reader acts on. More goes behind "Can wait".
3. **Small steps.** Every step names a time; the first takes 5 minutes or less.
4. **Do, don't just advise.** Offer to do the first step now: draft the text, open the
   outline, find the file, propose the calendar block. Ask before anything that sends,
   books, deletes or shares.
5. **No setup interview.** Work on the first message with sensible defaults. Ask at most
   one question, and only when the answer changes everything.
6. **No shame.** No streaks, no "you failed", no "you should have". Coming back after a gap
   is normal; say so plainly when it comes up.
7. **Plain words.** Short sentences, no jargon, no productivity-guru tone.
8. **Works with nothing connected.** Every skill has a paste-in mode. Connectors (Gmail,
   Calendar, Drive) make it better, never required.

## Safety and claims

- These are productivity and organisation tools. Skills never diagnose, assess symptoms,
  or advise on medication, dose or treatment. If asked, say it is outside what the skill
  does and suggest a clinician.
- Any skill that touches feelings ends with a short line pointing to professional support,
  and gives crisis resources if the person mentions self-harm.
- Descriptions and READMEs never use treatment language: no "treats", "cures", "reduces
  symptoms", "clinically proven", "therapy". **(checked)**
- Never quote email bodies, health details, passwords or codes back into memory.

## Format

- One folder per skill under `plugins/<plugin>/skills/<name>/`, holding `SKILL.md`, and
  optionally `references/`, `assets/`, `scripts/` and `evals/evals.json`.
- `name` matches the folder, lowercase and hyphens, 64 characters max. **(checked)**
- `description` says what it does and when to use it, in the user's words, 1024 characters
  max. **(checked)**
- `metadata.side_effects`: `true` if the skill can send, book, write or share anything. **(checked)**
- No top-level `bin/` folder in a plugin: claude.ai and Cowork refuse those plugins. **(checked)**
- No "claude" in plugin or skill names. **(checked)**
- Every skill ships `evals/evals.json` with at least two cases: one with nothing
  connected, one with connectors. **(checked)**

## Releasing

Bump `version` in the plugin's `plugin.json` for every release. Claude Code only updates
installed copies when the version changes. `make dist` builds the files buyers install.
