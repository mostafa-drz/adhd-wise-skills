# ADHD Wise skills (free)

Free productivity skills for Claude, designed by and for ADHD brains, from
[ADHD Wise](https://www.adhdwiseai.com/toolkit?utm_source=github&utm_medium=readme&utm_campaign=free_skills). No new app to abandon: they work inside the AI you already use, and
they do the first step with you instead of just giving advice.

> **You:** I can't start my expense report. It's been three weeks.
>
> **Task Unsticker:** Next, 5 min: search your email for "receipt" from October and star each
> one. Why it's sticky: boring, and the first step was unclear. Want me to write the search
> for you now?

| Skill | What it does |
| --- | --- |
| **Task Unsticker** | Shrinks a task you keep avoiding to a 5-minute first step, then does that step with you |
| **Tone Decoder** | Tells you what a worrying message most likely means, with evidence, and helps you reply; also checks your drafts |
| **Brain Dump → Today** | Turns everything in your head into at most three things that fit today, and parks the rest |

**Want more?** The full [ADHD Wise Kit](https://www.adhdwiseai.com/toolkit?utm_source=github&utm_medium=readme&utm_campaign=free_skills) has ten skills for what piles up quietly:
the inbox you avoid, bills and renewals, getting back on track after a break, and plans that
fit the real day. $29 founding price until Nov 30 ($39 after), one payment, 30-day refund.

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

**One Thing Today** picks the one thing that matters most today and gives you a 5-minute
start. **Body Double** keeps you company while you work. Both come by email, free, when you
sign up at [adhdwiseai.com/toolkit](https://www.adhdwiseai.com/toolkit?utm_source=github&utm_medium=readme&utm_campaign=bonus#free).

## Use it

Just say what's going on: "I can't start my expense report", "is my boss mad at me?" or
"brain dump: …". Claude picks up the right skill on its own.

## Privacy

The skills run inside your own Claude. ADHD Wise never sees your messages, files or
email.

Productivity tools only. Not medical advice or a substitute for professional care.

## License

MIT
