#!/usr/bin/env python3
"""Chat, not Message (Gabriele, 2026-11-22: "in conference still say message instead of chat").
The feature is called Chat everywhere (header Chats, Profile "Chat with Gregory"); labels that
still named it "Message(s)" now say Chat. Sentences that use "message" as an ordinary word
("Write a message…", "Amara sent you a message", "private messages") are kept on purpose.
Idempotent. Re-run after rebuilding any page listed below.
Usage: python3 chat-wording/patch.py"""
import os, re, json, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# English swaps, applied to every file below that contains them
SWAPS = [
    # Live Table side panel tab and per-person action
    ('data-tab="msg" aria-selected="false">Messages <b', 'data-tab="msg" aria-selected="false">Chat <b'),
    ('title="Message ${p.n}" aria-label="Message ${p.n}"', 'title="Chat with ${p.n}" aria-label="Chat with ${p.n}"'),
    ('aria-label="Message ${p.n}"', 'aria-label="Chat with ${p.n}"'),
    # Live Table mock-ups on the landing and in Guides
    ('<span class="on">Transcript</span><span>Messages</span>', '<span class="on">Transcript</span><span>Chat</span>'),
    # Host tools on the Table page and My tables
    ('<span>Message guests</span>', '<span>Chat with guests</span>'),
    ('}Message guests</button>', '}Chat with guests</button>'),
    ('"msg","Message guests")', '"msg","Chat with guests")'),
    ('head("Message guests",', 'head("Chat with guests",'),
    ("'Message guests': ['Scrivi agli ospiti', 'Escribir a los invitados', 'Μήνυμα στους καλεσμένους']",
     "'Chat with guests': ['Chatta con gli ospiti', 'Chatear con los invitados', 'Συζήτηση με τους καλεσμένους']"),
    # My tables: guest's menu
    ('`Message ${t.host}`', '`Chat with ${t.host}`'),
    # FAQ
    ('Can I message someone privately during a table?', 'Can I chat with someone privately during a table?'),
    ('Yes. Open Messages and pick a person.', 'Yes. Open Chat and pick a person.'),
    # Aliases page
    ('The transcript, Messages and guest list show your name.', 'The transcript, Chat and guest list show your name.'),
    # Admin: a table's conversation view (the chat said at the table)
    ('data-tab="messages">Messages (${ch.length})', 'data-tab="messages">Chat (${ch.length})'),
]
FAQ_A_OLD = "Yes. Open Messages and pick a person. Only the two of you see it. The host can't see or control private messages."
FAQ_A = "Yes. Open Chat and pick a person. Only the two of you see it. The host can't see or control private messages."
FAQ_Q = 'Can I chat with someone privately during a table?'
NEW = {  # English: [it, es, el]
    'Chat with guests': ['Chatta con gli ospiti', 'Chatear con los invitados', 'Συζήτηση με τους καλεσμένους'],
    FAQ_Q: ['Posso chattare in privato con qualcuno durante un tavolo?', '¿Puedo chatear en privado con alguien durante una mesa?',
            'Μπορώ να κάνω ιδιωτική συζήτηση με κάποιον κατά τη διάρκεια ενός τραπεζιού;'],
    FAQ_A: ["Sì. Apri Chat e scegli una persona. Lo vedete solo voi due. L'host non può vedere né controllare i messaggi privati.",
            'Sí. Abre Chat y elige a una persona. Solo lo veis vosotros dos. El anfitrión no puede ver ni controlar los mensajes privados.',
            'Ναι. Άνοιξε τη Συζήτηση και διάλεξε ένα άτομο. Το βλέπετε μόνο εσείς οι δύο. Ο οικοδεσπότης δεν βλέπει ούτε ελέγχει τα ιδιωτικά μηνύματα.'],
}
PAGES = '''live-table/timecapsule-live-table.html
landing/timecapsule-landing.html landing/timecapsule-landing-artifact.html landing/body.html
help/timecapsule-guides.html help/guides-body.html legal/guides-live.html
help/timecapsule-faq.html help/faq-body.html
table-detail/timecapsule-table.html table-detail/patch_mytables_link.py
help/live-pages/mytables.html invite/pages/mytables.html edge-states/pages/mytables.html
aliases/timecapsule-aliases.html admin/timecapsule-admin.html'''.split()

def add_dict(s):
    """Add NEW entries to every embedded tc-i18n dictionary that lacks them."""
    def ins(m):
        body = m.group(0)
        add = ''.join('%s:%s,' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
                      for k, v in NEW.items() if json.dumps(k, ensure_ascii=False) + ':' not in s)
        return body + add
    # a swapped English key may still carry its old translation: overwrite it
    for k, v in NEW.items():
        jk = json.dumps(k, ensure_ascii=False)
        s = re.sub(re.escape(jk) + r':\[[^\]]*\]', lambda m: jk + ':' + json.dumps(v, ensure_ascii=False), s)
    return re.sub(r'window\.TCI18N_DICT=\{', ins, s)

changed = []
for f in PAGES:
    p = os.path.join(ROOT, f)
    if not os.path.exists(p): print('skip', f); continue
    s = open(p, encoding='utf-8').read(); o = s
    for a, b in SWAPS: s = s.replace(a, b)
    if f.endswith('.html') and 'TCI18N_DICT=' in s: s = add_dict(s)
    if s != o:
        open(p, 'w', encoding='utf-8').write(s); changed.append(f)
    print(f, 'changed' if s != o else 'ok')

# source dictionaries
def edit_lines(path, fn):
    p = os.path.join(ROOT, path); s = open(p, encoding='utf-8').read(); n = fn(s)
    if n != s: open(p, 'w', encoding='utf-8').write(n)
def help_dict(s):
    s = re.sub(r'^Can I message someone privately during a table\?\|.*$', FAQ_Q + '|' + '|'.join(NEW[FAQ_Q][:2]), s, flags=re.M)
    s = re.sub(r'^' + re.escape(FAQ_A_OLD) + r'\|.*$', (FAQ_A + '|' + '|'.join(NEW[FAQ_A][:2])).replace('\\', '\\\\'), s, flags=re.M)
    return s
edit_lines('help/dict-help.txt', help_dict)
def el_dict(s):
    for k, v in NEW.items():
        if '\n' + k + '|' not in '\n' + s: s = s.rstrip('\n') + '\n' + k + '|' + v[2] + '\n'
    return s
edit_lines('i18n/dict-el.txt', el_dict)
def dict3(s):
    k = 'Chat with guests'
    return s if '\n' + k + '|' in '\n' + s else s.rstrip('\n') + '\n' + k + '|' + '|'.join(NEW[k][:2]) + '\n'
edit_lines('i18n/dict3.txt', dict3)
def dland(s):
    return s if '\nChat|' in '\n' + s else s.rstrip('\n') + '\nChat|Chat|Chat\n'
edit_lines('landing/dict-landing.txt', dland)

# Greek post-build step on built tc-i18n pages
for f in changed:
    p = os.path.join(ROOT, f)
    if f.endswith('.html') and 'id="tc-i18n"' in open(p, encoding='utf-8').read():
        subprocess.run(['python3', os.path.join(ROOT, 'i18n/add-greek.py'), p], check=False, capture_output=True)
print('done')
