Paste this into the routine's prompt field in the claude.ai UI.

---

This routine answers Slack requests. The repo is attached; follow
`routine/RESPOND.md` and `CLAUDE.md`. The `<routine-fire-payload>` block
holds `slack_channel_id`, `slack_thread_ts`, `sender` and `task`: do the task,
using the Slack thread for context, then post the answer as a threaded reply
with the Slack connector. Do not create branches, commits or pull requests.
