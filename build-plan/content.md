## In short

My recommendation is to build TimeCapsule as a web app on ready-made services, with a small team of two freelance developers, and reach a public launch in about six months for roughly €80,000 to €120,000.

- **Stack:** a web app (works on phones too), Supabase for accounts and data, LiveKit Cloud for live video, a speech-to-text service for transcripts, Resend for emails. Nothing is built from scratch that can be rented.
- **Order:** first the basics (accounts, tables, invites), then the Live Table with transcripts and Rate and Tip, then a closed beta with founding hosts, then the public launch with the globe and Listen in. Private groups follow right after.
- **Running costs:** about €200 a month during the beta, around €1,500 a month with a few thousand active people. Transcripts are the biggest cost line, more than video.
- **What I need from you first:** the company country, the team option, and ideally the name. Everything else can be decided along the way.

All prices are approximate, from my own knowledge of these services, and should be checked before signing anything.

## Where we are

Every screen is designed and clickable in four languages, but nothing works behind it yet: no accounts, no saved data, no video, no transcripts.

The prototype is still very valuable. It is the full specification: a developer can see exactly what each screen does, in which states, with which words in EN, IT, ES and EL. The translation dictionaries and the email templates can be reused almost as they are. The screens themselves will be rebuilt as real app pages, using the prototype as the model.

Features that are not yet designed and must be added to the build:

- The blocked list in Settings is now designed, with unblock in place, so it only needs building.
- From Fedor's private-group journey: a group entity for members-only groups, a standing recurring link, a waiting room, co-hosts, more than 10 chairs, a per-table switch for transcript and AI, a per-table switch for Rate and TimeCoins, and private tables never shown on the globe or in Listen in.

## Recommended stack

The rule is simple: rent the hard parts (video, speech-to-text, email, sign-in) and build only what makes TimeCapsule different (tables, the record, TimeCoins, trust).

| Part | Recommendation | What it does for TimeCapsule | Alternative |
| --- | --- | --- | --- |
| App | Web app built with Next.js, one codebase for desktop and phone | All screens, in four languages, reusing the existing translation files | Native phone apps later, once people ask for them |
| Accounts and data | Supabase (database, sign-in, file storage, live updates), hosted in the EU | Profiles, tables, chats, notifications, TimeCoins, Admin | Firebase |
| Live video | LiveKit Cloud | The Live Table, Listen in (listen-only seats), more than 10 chairs, waiting room | Jitsi, if costs or control require self-hosting |
| Transcripts | A speech-to-text service through LiveKit (for example Deepgram), with a no-training contract | The lasting record, in all four languages | AssemblyAI or Speechmatics |
| AI summaries and notes | Claude through the API, with zero data retention | Table notes and summaries, only where the host allows it | None needed at first |
| Emails | Resend, with the five existing templates | Welcome, reminders, rate reminder, invites | Postmark |
| Reminders by SMS or WhatsApp | Twilio, later | Fedor's reminders | Email only at first |
| Hosting | Cloudflare (already in use) or Vercel | Serves the app; the prototype stays where it is | |
| Payments | Stripe, only when buying TimeCoins is decided | Buying spendable coins | Not needed for launch |
| Monitoring | Sentry and simple uptime checks | Tells us when something breaks | |

Two points matter for later decisions. TimeCoins are just numbers in our own database, not crypto, so tipping and reputation need no payment provider; only *buying* coins brings payments and legal rules into play. And Knowledge orbits connect to k▪universe through a simple link between accounts, so k▪universe needs to offer a way for TimeCapsule to read a person's favourites, with their consent.

## Phases

Phases 0 to 4 take about six months to a public launch, with private groups ready one to two months later. Each phase ends with something real that people can use.

[[ROADMAP]]

1. **Phase 0, Setup (2 weeks).** Choose the team, make the repo private, open accounts with the services, set up the company basics and data-protection contracts. I turn the prototype into a written build list, screen by screen.
2. **Phase 1, Foundation (5 to 6 weeks).** Sign in, onboarding, Profile, Settings with the blocked list, Create a table, the Tables page, the table page and private invites, My tables, Host again, the five emails, all four languages. At the end you can create a table and invite people, but not yet sit at it.
3. **Phase 2, Live Table (5 to 6 weeks).** Video at the table with host controls, private messages between guests, notes, transcripts with an off switch per table, Rate and Tip, the TimeCoins ledger (Received and To use), reminders. Private tables never appear on the globe from day one. At the end a full table works from invite to tip.
4. **Phase 3, Closed beta (4 to 6 weeks).** Founding hosts and about 100 to 200 invited people. Chats, notifications, People, Search, Admin with reporting and the Trusted host badge given by hand. 24/7 on-call: uptime and error monitoring that emails Gabriele within a minute, plus an AI agent that investigates each alert and emails a summary and a proposed fix for approval. We fix what real conversations show us and collect data to set the Trusted rule.
5. **Phase 4, Public launch (4 to 6 weeks).** The globe with Listen in, the automatic Trusted rule, Knowledge orbits with k▪universe, the landing page, security and privacy review, load test.
6. **Phase 5, Private groups (6 to 8 weeks, can start during Phase 4).** The group entity with a members-only page, standing recurring link, waiting room, co-hosts, more than 10 chairs, the per-table switch for Rate and TimeCoins, SMS or WhatsApp reminders.

If a recovery group like Fedor's is one of the first communities you want, Phase 5 can move ahead of the globe and Listen in. That is a choice about who you launch with first.

## Team and build cost

I recommend option B: two experienced freelance developers, with you as product owner and me keeping the design, copy and translations in step.

| Option | Who | Time to public launch | Rough cost to launch | Fits if |
| --- | --- | --- | --- | --- |
| A. Agency | A small studio with project manager, developers and QA | 5 to 6 months | €150,000 to €250,000 | You want one contract and little day-to-day involvement |
| **B. Two freelancers** {hi:Claude's choice} | One senior full-stack developer full time, one front-end developer part time | about 6 months | €80,000 to €120,000 | You can spend a few hours a week deciding and testing |
| C. One developer with AI help | One senior developer working closely with Claude | 8 to 10 months | €60,000 to €90,000 | Budget matters more than speed |
| **D. Gabriele and Claude** {pick:Gabriele's choice} | Claude writes the code, Gabriele decides and tests, a senior developer reviews a few days a month | 6 to 9 months | €10,000 to €25,000 | You can test several hours a week and want to keep control |

On top of the build, plan for about €10,000 to €20,000 of one-off costs: a lawyer for terms, privacy and the trademark clearance (€5,000 to €12,000), a security review before launch (€3,000 to €6,000), and a small budget for beta testers and founding hosts.

Rates assume European freelancers at roughly €500 to €700 a day. Private groups (Phase 5) add about €20,000 to €35,000 to option B.

### Option D in detail

In option D, I write the code and you act as product owner and tester. The pace depends mostly on how much time you have to test.

- **What you do:** open and pay for the service accounts (LiveKit, Supabase, email and the rest), add their keys to the project settings with my step-by-step help, try each piece and approve what goes live.
- **The part-time developer:** about €1,500 to €3,000 a month for a few days of code review, help with the hard parts and standby at launch. On top of that, an independent security and privacy review before real people use it (€3,000 to €6,000).
- **Why a human is still needed:** my sessions start fresh each time and run only while we work, and TimeCapsule will hold personal conversations, so someone independent should check the code.

### 24/7 on-call

From the beta onward, an alert setup watches the product day and night and emails you.

- **Monitoring (no AI):** an uptime service such as Better Stack checks the site every minute, and Sentry catches app errors. Either one emails or texts you within a minute. About €0 to €30 a month.
- **AI agent:** each alert, plus a check every few hours, starts a Claude session. It reads the errors and logs, finds the cause, prepares a fix and emails you a plain summary: what broke, how many people were affected, what it proposes. A fix goes live only after you approve it.
- **Limits:** it can't fix an outage at LiveKit or Supabase, an expired card or a full account; for those, the email tells you what to do. For the first weeks after launch, keep a human developer you can call in an emergency.

## Monthly running costs

Running costs stay small until TimeCapsule has thousands of active people, and transcripts are the largest line at every size.

| Size | Beta | Launch | Growth |
| --- | --- | --- | --- |
| Active people | 200 | 5,000 | 50,000 |
| Tables a month (6 people, 1 hour) | 100 | 2,000 | 20,000 |
| Live video (LiveKit) | €50 | €350 to €500 | €3,500 to €5,000 |
| Transcripts (speech-to-text) | €30 | €500 to €700 | €5,000 to €7,000 |
| AI notes and summaries | €10 | €100 | €1,000 |
| Database, sign-in, storage (Supabase) | €25 | €50 to €100 | €400 to €800 |
| Emails, hosting, monitoring | €30 | €100 | €300 |
| **Total a month** | **about €150 to €250** | **about €1,100 to €1,500** | **about €10,000 to €14,000** |

A one-hour table with six people costs roughly €0.50 to €0.70 to run. Tables with the transcript switched off cost about half. Listen-in listeners add little, because they only receive sound. These figures are approximate, from my knowledge of each service's public pricing, and need checking with current price lists. Ongoing maintenance by a developer (about €2,000 to €5,000 a month after launch) is not included.

## Your decisions, and when each one blocks the build

Only two decisions block the start: the team option and the company country. The rest can wait for the phase that needs them. Already decided: minimum age 16 and no AI training on conversations, both written into the Terms and Privacy page.

| Decision | What it affects | Needed by |
| --- | --- | --- |
| Team option (A, B, C or D) | Who builds, the budget, the timeline | Start of Phase 0 |
| Company country and first launch market | Contracts with every service, where data is stored (EU recommended), legal pages, trademark, tax on TimeCoins later | Start of Phase 0 |
| Minimum age 16 and no AI training on conversations (decided) | The sign-up check; only speech-to-text and AI providers that sign no-training terms qualify | Decided |
| The name | Domain, sign-in emails, the app's name in four languages. Cheap to change until the beta, costly after the public launch | Before Phase 3 (beta) |
| Transcript default (on or off for new tables) and who can see it | The Live Table and the lasting record | Phase 2 |
| Listen-in rules (who, how long, free minutes) | The globe and listen-only seats | Phase 4 |
| The Trusted rule | The automatic badge. The beta gives real numbers to set it | Phase 4 |
| TimeCoin prices and whether coins can be bought | Earning and tipping need no decision. Buying coins needs payments and a legal check in your country | After launch |
| What k▪universe shares with TimeCapsule | Knowledge orbits | Phase 4 |

## Risks and next steps

The biggest risk is not technical: it is empty tables at launch, which is why the beta starts with founding hosts.

- **Empty tables.** Recruit 10 to 20 founding hosts before the beta, each committed to a regular table.
- **Privacy of conversations.** Transcripts of personal talks (Fedor's group, for example) are sensitive. Off by default for private tables, EU storage, no-training contracts, and a privacy review before launch.
- **Transcript quality in Greek and Italian.** Test two speech-to-text services on real recordings in Phase 2 before choosing.
- **Safety on open tables and Listen in.** Reporting, blocking and host removal must work before the public launch, with someone named to handle reports.
- **Scope creep.** Each phase ships only its list; new ideas go to the next phase.

### Next steps

- [ ] Gabriele: choose the team option and tell me the company country
- [ ] Gabriele: make the GitHub repo private
- [ ] Claude: write the screen-by-screen build list from the prototype, ready for developers
- [ ] Claude: draft a short job brief to find the two developers
