---
title: "Why I Built AgentsMail — The 19-Step Gmail Nightmare"
description: "I tried to connect my AI agent to Gmail. It took 19 steps, 3 security warnings, and still failed. So I built something better."
pubDate: 2026-03-26
tags: ["agentsmail", "ai-agents", "email", "open-source"]
lang: en
---

# Why I Built AgentsMail

It started with a simple idea: let my AI agent send an email.

## The Gmail Nightmare

I asked my agent to connect to Gmail. What followed was a 19-step obstacle course:

1. Create a Google Cloud account
2. Create a new project
3. Enable the Gmail API
4. Configure OAuth consent screen
5. Create OAuth credentials
6. Set up redirect URIs
7. Handle OAuth flow in code
8. Exchange authorization code for tokens
9. Store refresh tokens securely
10. Handle token refresh logic
11. Deal with 2FA requirements
12. Navigate "Less secure app access" deprecation
13. Generate App-specific passwords
14. Configure SMTP settings
15. Handle rate limits and quotas
16. Parse Gmail's API response format
17. Deal with label/thread complexity
18. Test... get a security warning from Google
19. Give up.

My agent couldn't do any of this. It doesn't have a browser. It can't click through OAuth consent screens. It can't receive 2FA codes.

## The Security Problem

Even if I could connect Gmail, there was a deeper issue: **I didn't want my agent reading my personal email.**

My inbox has bank statements, medical records, private conversations. Giving an AI agent full access to that? No thanks.

The alternative — creating a new Gmail account just for the agent — meant going through the entire registration process again. More phone verification, more CAPTCHA, more friction.

## The Realization

Email is the internet's oldest and most universal communication protocol. Federated, asynchronous, identity built into DNS, security built into DKIM/SPF/DMARC. Every system in the world can send and receive email.

But there was no email service designed for AI agents. Every existing solution assumed a human sitting at a keyboard.

## One API Call

So I built AgentsMail. The entire registration is one POST request:

```bash
curl -X POST https://agentsmail.org/api/getemailaddress \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "my-agent"}'
```

That's it. No OAuth. No Google Cloud console. No 2FA. Your agent gets its own email address, 10 free sends, and can start communicating immediately.

## What Makes It Different

- **Zero friction** — One API call, no sign-up needed
- **Agent-native** — Designed for programs, not people
- **Free** — 10 sends included, upgrade for unlimited
- **Encrypted** — AES-256-GCM at rest
- **Open source** — [github.com/huberthe-pro/agents-mail](https://github.com/huberthe-pro/agents-mail)

## Try It

Install the [AgentsMail skill on ClawHub](https://clawhub.ai/huberthe-pro/agentsmail), or tell your agent:

```
Install agentsmail.org/skill.md and register a mailbox for yourself.
```

Your agent will have its own email in 30 seconds.

---

*AgentsMail is open source and free. Built with Cloudflare Workers, D1, and TypeScript. [Check it out on GitHub](https://github.com/huberthe-pro/agents-mail).*
