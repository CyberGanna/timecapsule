"""Community guidelines, second pass (Gabriele 2026-11-22): gaps found by comparing with Clubhouse's
Trust & Safety articles and Terms, written in our own words (nothing copied):
child safety and grooming, intimate images incl. AI-made, terrorism / violent extremism and graphic violence,
a fuller hate list, doxxing details and threats to share, honest age (16+), a supportive line on self-harm,
and telling the police about threats. EN/IT/ES/EL. Idempotent, marker "gl-v2"."""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'legal/timecapsule-legal.html')

def h(x):  # body text as the page writes it
    return html.escape(x, quote=False).replace("'", "&#x27;")

NEW = {
 "Hate or contempt aimed at people for who they are: origin, race, nationality, religion, gender, sexuality, disability or age.": [
  "Odio o disprezzo verso le persone per ciò che sono: origine, etnia, nazionalità, religione, genere, sessualità, disabilità o età.",
  "Odio o desprecio hacia las personas por lo que son: origen, raza, nacionalidad, religión, género, sexualidad, discapacidad o edad.",
  "Μίσος ή περιφρόνηση προς ανθρώπους για αυτό που είναι: καταγωγή, φυλή, εθνικότητα, θρησκεία, φύλο, σεξουαλικότητα, αναπηρία ή ηλικία."],
 "Sexual content or nudity.": ["Contenuti sessuali o nudità.", "Contenido sexual o desnudos.", "Σεξουαλικό περιεχόμενο ή γυμνό."],
 "Sharing someone's intimate images, real or made with AI, threatening to share them, or pressuring anyone to send them.": [
  "Condividere immagini intime di qualcuno, vere o create con l'IA, minacciare di condividerle o fare pressione perché qualcuno le invii.",
  "Compartir imágenes íntimas de alguien, reales o creadas con IA, amenazar con compartirlas o presionar a alguien para que las envíe.",
  "Να μοιράζεσαι προσωπικές εικόνες κάποιου, αληθινές ή φτιαγμένες με τεχνητή νοημοσύνη, να απειλείς ότι θα τις μοιραστείς ή να πιέζεις κάποιον να τις στείλει."],
 "Anything that sexualises, grooms or endangers a child. We report it to the authorities.": [
  "Qualsiasi cosa che sessualizzi, adeschi o metta in pericolo un minore. Lo segnaliamo alle autorità.",
  "Cualquier cosa que sexualice, capte o ponga en peligro a un menor. Lo denunciamos a las autoridades.",
  "Οτιδήποτε σεξουαλικοποιεί, αποπλανά ή θέτει σε κίνδυνο ένα παιδί. Το αναφέρουμε στις αρχές."],
 "Praising or supporting terrorist or violent extremist groups, or showing graphic violence.": [
  "Elogiare o sostenere gruppi terroristici o estremisti violenti, o mostrare violenza esplicita.",
  "Elogiar o apoyar a grupos terroristas o extremistas violentos, o mostrar violencia explícita.",
  "Να επαινείς ή να υποστηρίζεις τρομοκρατικές ή βίαιες εξτρεμιστικές ομάδες, ή να δείχνεις ωμή βία."],
 "Talking about your own hard times is welcome. If someone at a table seems at risk of harming themselves, report it and we will reach out with support.": [
  "Parlare dei propri momenti difficili è benvenuto. Se qualcuno a un tavolo sembra a rischio di farsi del male, segnalalo e lo contatteremo per offrire sostegno.",
  "Hablar de tus propios momentos difíciles es bienvenido. Si alguien en una mesa parece estar en riesgo de hacerse daño, denúncialo y nos pondremos en contacto para ofrecerle apoyo.",
  "Είναι ευπρόσδεκτο να μιλάς για τις δικές σου δύσκολες στιγμές. Αν κάποιος σε ένα τραπέζι φαίνεται να κινδυνεύει να κάνει κακό στον εαυτό του, ανάφερέ το και θα επικοινωνήσουμε μαζί του για να του προσφέρουμε στήριξη."],
 "Never share someone's surname, address, phone number, email, workplace or photos without their permission, and never threaten to.": [
  "Non condividere mai cognome, indirizzo, numero di telefono, email, luogo di lavoro o foto di qualcuno senza il suo permesso, e non minacciare mai di farlo.",
  "Nunca compartas el apellido, la dirección, el teléfono, el correo, el lugar de trabajo ni las fotos de alguien sin su permiso, y nunca amenaces con hacerlo.",
  "Μη μοιράζεσαι ποτέ το επώνυμο, τη διεύθυνση, το τηλέφωνο, το email, τον χώρο εργασίας ή φωτογραφίες κάποιου χωρίς την άδειά του, και μην απειλείς ποτέ ότι θα το κάνεις."],
 "Be honest about your age. TimeCapsule is for people aged 16 and over.": [
  "Sii onesto sulla tua età. TimeCapsule è per persone dai 16 anni in su.",
  "Sé honesto con tu edad. TimeCapsule es para personas de 16 años o más.",
  "Να λες την αλήθεια για την ηλικία σου. Το TimeCapsule είναι για άτομα 16 ετών και άνω."],
 "If someone threatens you or a table, report it here and tell the local police as well.": [
  "Se qualcuno minaccia te o un tavolo, segnalalo qui e avvisa anche la polizia locale.",
  "Si alguien te amenaza a ti o a una mesa, denúncialo aquí y avisa también a la policía local.",
  "Αν κάποιος απειλήσει εσένα ή ένα τραπέζι, ανάφερέ το εδώ και ενημέρωσε και την τοπική αστυνομία."],
}
K = list(NEW)
REPS = [
 ("<li>Hate or contempt aimed at people for who they are: origin, religion, gender, sexuality, disability or age.</li>", f"<li>{h(K[0])}</li>"),
 ("<li>Sexual content, nudity, or anything that sexualises minors.</li>\n<li>Encouraging violence, self-harm or illegal acts.</li>\n</ul>",
  f"<li>{h(K[1])}</li>\n<li>{h(K[2])}</li>\n<li>{h(K[3])}</li>\n<li>Encouraging violence, self-harm or illegal acts.</li>\n<li>{h(K[4])}</li>\n</ul>\n<p style=\"margin-top:14px\">{h(K[5])}</p><!--gl-v2-->"),
 (f"<li>{h(chr(78)+'ever share someone' + chr(39) + 's surname, address, workplace or photos without their permission.')}</li>", f"<li>{h(K[6])}</li>"),
 ("<li>No bots, no fake accounts, and no AI speaking or writing for you at a table.</li>", f"<li>No bots, no fake accounts, and no AI speaking or writing for you at a table.</li>\n<li>{h(K[7])}</li>"),
 ("<li>If someone is in danger right now, contact local emergency services first.</li>", f"<li>If someone is in danger right now, contact local emergency services first.</li>\n<li>{h(K[8])}</li>"),
]
s = open(P, encoding='utf8').read()
if 'gl-v2' not in s:
    for a, b in REPS:
        assert s.count(a) == 1, (a[:60], s.count(a))
        s = s.replace(a, b)
    m = re.search(r'window\.TCI18N_DICT=(\{.*?\});\n', s, flags=re.S)
    d = json.loads(m.group(1)); d.update(NEW)
    s = s[:m.start(1)] + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + s[m.end(1):]
    open(P, 'w', encoding='utf8').write(s); print('guidelines v2')
# keep the Greek source dictionary in step
de = os.path.join(ROOT, 'i18n/dict-el.txt'); e = open(de, encoding='utf8').read()
for k, v in NEW.items():
    if '\n' + k + '|' not in '\n' + e:
        e = e.rstrip('\n') + '\n' + f'{k}|{v[2]}\n'
open(de, 'w', encoding='utf8').write(e)
