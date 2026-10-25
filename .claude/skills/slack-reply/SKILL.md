---
name: slack-reply
description: Conventions for answering a Slack thread from a routine run. Use when replying to a Slack message via the Slack connector.
---

# Slack reply

- Read the whole thread first; short tasks like "why?" depend on it.
- Reply in the thread only (`thread_ts` set), never as a top-level message.
- Lead with the answer in one or two sentences, then detail if needed.
- Use Slack-friendly markdown: short paragraphs, no headings.
- If the task is ambiguous after reading the thread, say what you assumed.
- If posting fails, report the error instead of retrying silently.
