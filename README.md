# TimeCapsule

A digital place with a different relationship with technology: room for reflection, dialogue and sustained participation. People sit at small tables to talk, share ideas and challenge perspectives. Trust grows through repeated participation, knowledge emerges through dialogue, and each discussion can leave a lasting record of ideas with authorship and context, an inheritance for future generations. Technology serves human expression.

This repository holds the design prototypes of the product: self-contained HTML pages (English, Italian, Spanish), the sources and scripts they are built from, email templates, legal drafts and the manifesto.

## Pages

| Page | Folder | Live prototype |
|---|---|---|
| Agenda ("Pull up a chair") | `help/live-pages/agenda.html` | [open](https://claude.ai/artifact/1HRtzD5kj8RFhEngLuAgU5) |
| World globe | `world/` | [open](https://claude.ai/artifact/WXKBrXY78yuhpghQCpK3RU) |
| Table page and private invite | `table-detail/` | [open](https://claude.ai/artifact/AQKmmAgq8JPDsrRACWEy6i) |
| Live Table | `live-table/` | [open](https://claude.ai/artifact/2CoEp7SXhBT2oP5hu3zNkk) |
| Rate and Tip | | [open](https://claude.ai/artifact/4jA3RGXJko9RmWkEKk3kCu) |
| Create a table | `help/live-pages/create.html` | [open](https://claude.ai/artifact/MFBQwEDcUA8ctJbo2BWShj) |
| My tables | `help/live-pages/mytables.html` | [open](https://claude.ai/artifact/GPnp3CiH7iGDpkbqvA4cLB) |
| Profile | `profile/` | [open](https://claude.ai/artifact/TQ3edAr7Dje1uPbGk3yEQy) |
| People | `help/live-pages/people.html` | [open](https://claude.ai/artifact/MTbRjvLFV7pPhBjpvAzXaq) |
| Chats | `help/live-pages/chats.html` | [open](https://claude.ai/artifact/PYd4f8xrcNkPc2TyPkE4ib) |
| Notifications | `notifications/` | [open](https://claude.ai/artifact/SggBcVnWacDjzBsZeke1D1) |
| Search results | `search/` | [open](https://claude.ai/artifact/NdgohZznzHtQ8p2PmohNhE) |
| Settings | `help/live-pages/settings.html` | [open](https://claude.ai/artifact/PAUksqiFCEtbuDeWsoXjWy) |
| Sign in | `auth/` | [open](https://claude.ai/artifact/BFBabdFxq8LxqDChfvRn61) |
| Onboarding | `onboarding/` | [open](https://claude.ai/artifact/Q7o5JaMGP7bHLXzJ6aw6TH) |
| Invite friends | `invite/` | [open](https://claude.ai/artifact/3erX1TAL2xoYjAmfvqkWtp) |
| TimeCoins | `timecoins/` | [open](https://claude.ai/artifact/VRtXrcZBGsWhfQkPMZuKpK) |
| Trust meter | `trust/` | [open](https://claude.ai/artifact/9vjFardtQTDB9NgmX9g9em) |
| Guides | `help/timecapsule-guides.html` | [open](https://claude.ai/artifact/WHk7qYCmXBgugxJW1kqevd) |
| FAQ | `help/timecapsule-faq.html` | [open](https://claude.ai/artifact/LTQdD5XzBLaDbCRrhHttMK) |
| Admin panel | `admin/` | [open](https://claude.ai/artifact/GcdFnhR5eggq6hB7fm1Njw) |
| Aliases proposal | `aliases/` | |
| Legal and community guidelines (draft) | `legal/` | not published yet |
| Edge and empty states (draft) | `edge-states/` | not published yet |
| Transactional emails (draft) | `emails/` | not published yet |
| Brand book | `logo/` (snippets) | [open](https://claude.ai/artifact/E9nwURawSJTDeaZNA96Rrq) |
| Manifesto (What, How, Why) | `manifesto/` | PDF in folder |

## Layout

One folder per page. Each folder keeps its sources (`body.html`, `dict-*.txt` translation dictionaries, CSS/JS parts) next to the built, self-contained HTML (`timecapsule-*.html`). `i18n/` holds the shared language script (EN/IT/ES; the language is carried in the URL as `#lang=it`). `help/live-pages/` and `invite/pages/` are snapshots of the published pages used when adding the shared footer and links.

## Rebuilding a page

The build scripts read the sources next to them and write the built HTML:

```sh
python3 emails/build.py          # email templates into emails/templates/
python3 emails/build-preview.py  # emails preview page
python3 legal/build.py
python3 edge-states/build.py
python3 timecoins/build.py
python3 invite/build.py
python3 notifications/build.py
python3 help/build.py            # Guides and FAQ
node search/build.js
node i18n/build.js
```

Some scripts still use absolute paths from the original workspace (`/mnt/project-files/...`); run them from a copy at that path, or change the path at the top of the script.

The pages run inside a claude.ai frame: cross-page links are plain `<a target="_top">` and `window.open` is not used.
