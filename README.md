# ADHD Wise skills (free)

Free productivity skills for Claude, designed by and for ADHD brains, from
[ADHD Wise AI](https://adhdwise.ai). No new app to abandon: they work inside the AI you
already use.

| Skill | What it does |
| --- | --- |
| **Task Unsticker** | Shrinks a task you keep avoiding to a 5-minute first step, then does that step with you |
| **Tone Decoder** | Tells you what a worrying message most likely means, with evidence, and helps you reply; also checks your drafts |
| **Brain Dump → Today** | Turns everything in your head into at most three things that fit today, and parks the rest |

The full **ADHD Wise Kit** (inbox triage, admin sweep,
"where was I?" and more) is at [adhdwise.ai](https://adhdwise.ai).

## Install (about 2 minutes)

**Claude Desktop, claude.ai or Cowork** (Pro plan or higher)

1. In Claude, open **Customize → Plugins → Add → Add marketplace**.
2. Enter `mostafa-drz/adhd-wise-skills` and install **ADHD Wise (free)**.
3. Make sure **Code execution and file creation** is on in Settings.

**Claude Code**

```
/plugin marketplace add mostafa-drz/adhd-wise-skills
/plugin install adhd-wise-free@adhd-wise-free
```

**Codex, Cursor, GitHub Copilot, Gemini CLI**

```
npx skills add mostafa-drz/adhd-wise-skills
```

Or copy the folders in `plugins/adhd-wise-free/skills/` into `~/.agents/skills/`.

## Two more free skills

**One Thing Today** and **Body Double** come by email when you sign up at
[adhdwise.ai/toolkit](https://adhdwise.ai/toolkit).

## Use it

Just say what's going on: "I can't start my expense report", "is my boss mad at me?" or
"brain dump: …". Claude picks up the right skill on its own.

## Privacy

The skills run inside your own Claude. ADHD Wise AI never sees your messages, files or
email.

Productivity tools only. Not medical advice or a substitute for professional care.

## License

MIT
