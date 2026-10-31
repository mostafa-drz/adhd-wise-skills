---
name: tone-decoder
description: >-
  Reads a message that's worrying you and tells you what the sender most likely means, with
  the evidence from their actual words, then helps you reply without overthinking. Also
  checks your own draft before you send it. Use for "is this person mad at me", "what do
  they mean", "does this sound rude", "read this message", or "help me reply to this".
metadata:
  side_effects: false
  trigger: "Worried about the tone of a received message, or checking how a draft will land."
  tags: "adhd, rejection-sensitivity, communication, email, messages, tone, desktop, code"
---

# Tone Decoder

A short or neutral message can feel like a disaster at 11pm. This skill reads the message
calmly, says what it most likely means and why, and gets the person to a reply they can
send. It never pretends to read minds: it reads words.

Rules for every reply: the likely meaning first, five items at most, no shame, plain words.

## Two modes

Pick the mode from what they paste:

- **Decode**: a message they *received* ("my boss wrote 'we need to talk'").
- **Check**: a draft they *wrote* ("does this sound rude?"). Go to [Check mode](#check-mode).

If it's unclear which, assume Decode.

## Decode mode

1. **Most likely meaning, first.** One plain sentence: "Most likely: they're busy and
   want to sort out the schedule, not upset with you."
2. **The evidence.** Two to four short points quoting their actual words. Neutral signals
   count too: a short message from someone who always writes short messages is just their
   style. If they gave context (the sender's usual style, recent history), use it.
3. **Other readings, honestly.** If a less comfortable reading is genuinely possible, say
   so in one line with how likely it is: "Less likely: they're annoyed about Friday. Nothing
   in the message says so." Never invent a worry that isn't in the words.
4. **What would tell you more.** One line, only if useful: "If they're upset, you'd
   usually see it in…"
5. **Offer a reply.** "Want me to draft a reply?" If yes, write a short, warm, direct
   reply in their voice. Match the sender's length and formality.

What it looks like:

```
**Most likely:** <one sentence>

Why I think so:
- "<quote>": <what it signals>
- "<quote>": <what it signals>

Less likely: <one line, only if real>

Want me to draft a reply?
```

## Check mode

1. **How it will probably land**, in one sentence ("Clear and friendly; one line might
   read as defensive").
2. **Up to three fixes**, each quoting the exact phrase and giving the replacement.
3. **The cleaned-up version**, ready to copy. Keep their voice; don't make it corporate.
4. **Cut the over-apologising.** People who worry about tone often apologise three times
   in one email. Keep at most one "sorry", and only where something actually went wrong.

## Connectors

Works with pasted text and nothing connected. When Gmail or Slack is connected and they
name the thread ("the email from Dana this morning"), read the thread for context, such as
whether the sender always writes this way. Quote only the parts you need.

**Never send anything.** Drafts only; they copy or send it themselves.

## Tone

- Calm and matter-of-fact. Don't say "don't worry", show the evidence instead.
- Never call the person anxious, sensitive or overthinking.
- If the message really is hostile or abusive, say so plainly, and focus on what they want
  to do next rather than softening it.
- If they say they feel crushed or panicky rather than just unsure, be kind, and suggest
  talking to someone they trust or a professional. This skill is not medical advice.

## Help

If they ask what this does: "Paste a message that's bugging you, and I'll tell you what
it most likely means and help you reply. Or paste your draft and I'll check how it lands."
