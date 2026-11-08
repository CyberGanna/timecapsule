# Builds TimeCapsule transactional emails (EN/IT/ES) as email-safe HTML.
# Usage: python3 build.py  -> templates/*.html (with {{placeholders}}) and preview data (sample values).
import json, os, base64, html
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "'Sora','Helvetica Neue',Helvetica,Arial,sans-serif"
NAVY, INK, MUTE, LINE, PAPER, VIOLET = "#1B2144", "#1B2144", "#555D86", "#E3E6F4", "#F4F5FC", "#7C5CFF"

T = json.load(open(os.path.join(HERE, "copy.json"), encoding="utf-8"))

SAMPLE = {
 "en": dict(first="Gregory", host="Mia Laurent", inviter="Mia", topic="Cities", title="Should cities ban cars from their centres?",
            when="Thursday 12 November · 19:00 (CET)", taken="6", chairs="8", others="Tomás, Aiko and 3 others", length="45 minutes",
            rtopic="Philosophy", rtitle="What do we owe future generations?", names="Mia, Tomás and 4 others", coins="8", expiry="Tuesday 10 November",
            note="I think you'd love this one. Come and argue with me about bikes!"),
 "it": dict(first="Gregory", host="Mia Laurent", inviter="Mia", topic="Cities", title="Should cities ban cars from their centres?",
            when="giovedì 12 novembre · 19:00 (CET)", taken="6", chairs="8", others="Tomás, Aiko e altri 3", length="45 minuti",
            rtopic="Philosophy", rtitle="What do we owe future generations?", names="Mia, Tomás e altre 4 persone", coins="8", expiry="martedì 10 novembre",
            note="I think you'd love this one. Come and argue with me about bikes!"),
 "es": dict(first="Gregory", host="Mia Laurent", inviter="Mia", topic="Cities", title="Should cities ban cars from their centres?",
            when="jueves 12 de noviembre · 19:00 (CET)", taken="6", chairs="8", others="Tomás, Aiko y 3 más", length="45 minutos",
            rtopic="Philosophy", rtitle="What do we owe future generations?", names="Mia, Tomás y 4 personas más", coins="8", expiry="martes 10 de noviembre",
            note="I think you'd love this one. Come and argue with me about bikes!"),
 "el": dict(first="Gregory", host="Mia Laurent", inviter="Mia", topic="Cities", title="Should cities ban cars from their centres?",
            when="Πέμπτη 12 Νοεμβρίου · 19:00 (CET)", taken="6", chairs="8", others="Tomás, Aiko και 3 ακόμα", length="45 λεπτά",
            rtopic="Philosophy", rtitle="What do we owe future generations?", names="Mia, Tomás και 4 ακόμα", coins="8", expiry="Τρίτη 10 Νοεμβρίου",
            note="I think you'd love this one. Come and argue with me about bikes!"),
}
VARS = dict(first="first_name", host="host_name", inviter="inviter_first_name", topic="topic_name", title="table_title", when="table_when",
            taken="chairs_taken", chairs="chairs_total", others="other_guests", length="table_length", rtopic="topic_name", rtitle="table_title",
            names="table_people", coins="coins_left", expiry="coins_expiry_date", note="personal_message")
TOPIC_DOT = {"Cities": "#17C3C8", "Philosophy": "#7C5CFF"}

def fill(s, vals):
    for k, v in vals.items():
        s = s.replace("{" + k + "}", v)
    return s

def button(label, href):
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:28px 0 8px"><tr><td align="center" bgcolor="{VIOLET}" style="border-radius:10px;background:{VIOLET}">
<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{href}" style="height:48px;v-text-anchor:middle;width:240px" arcsize="20%" stroke="f" fillcolor="{VIOLET}"><center style="color:#ffffff;font-family:Arial,sans-serif;font-size:16px">{label}</center></v:roundrect><![endif]-->
<!--[if !mso]><!--><a href="{href}" class="btn" style="display:inline-block;padding:14px 28px;font-family:{FONT};font-size:16px;font-weight:500;line-height:20px;color:#ffffff;text-decoration:none;border-radius:10px;mso-hide:all">{label}</a><!--<![endif]-->
</td></tr></table>'''

def p(text, size=16, color=MUTE, extra=""):
    return f'<p style="margin:0 0 16px;font-family:{FONT};font-size:{size}px;line-height:1.6;font-weight:300;color:{color};{extra}">{text}</p>'

def table_card(L, v, topic_key, title_key, rows):
    dot = TOPIC_DOT.get(SAMPLE["en"][topic_key], "#17C3C8")
    meta = "".join(f'<tr><td style="padding:2px 0;font-family:{FONT};font-size:14px;line-height:1.5;font-weight:300;color:{MUTE}">{r}</td></tr>' for r in rows)
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;margin:8px 0 8px;border:1px solid {LINE};border-radius:12px;background:#FAFAFE">
<tr><td style="padding:18px 20px">
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td valign="middle" style="padding-right:7px"><div style="width:8px;height:8px;border-radius:4px;background:{dot};font-size:0;line-height:0">&nbsp;</div></td><td valign="middle" style="font-family:{FONT};font-size:13px;line-height:1;font-weight:400;color:{MUTE}">{v[topic_key]}</td></tr></table>
<p style="margin:10px 0 8px;font-family:{FONT};font-size:19px;line-height:1.35;font-weight:400;letter-spacing:-.01em;color:{INK}">{v[title_key]}</p>
<table role="presentation" cellpadding="0" cellspacing="0" border="0">{meta}</table>
</td></tr></table>'''

def steps(L):
    out = []
    for i, (h, d) in enumerate(L["steps"], 1):
        out.append(f'''<tr><td valign="top" width="36" style="padding:0 0 16px"><div style="width:26px;height:26px;border-radius:13px;background:#EFEBFF;color:{VIOLET};font-family:{FONT};font-size:13px;font-weight:500;line-height:26px;text-align:center">{i}</div></td>
<td valign="top" style="padding:2px 0 16px;font-family:{FONT};font-size:15px;line-height:1.55;font-weight:300;color:{MUTE}"><span style="font-weight:500;color:{INK}">{h}</span><br>{d}</td></tr>''')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 4px">{"".join(out)}</table>'

def coin_box(L, v, coin_src, lines):
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;margin:8px 0 4px;background:#FFF7E3;border:1px solid #F1D48C;border-radius:12px">
<tr><td width="46" valign="top" style="width:46px;padding:16px 0 16px 18px"><img src="{coin_src}" width="28" height="28" alt="" style="display:block;border:0"></td>
<td valign="middle" style="padding:16px 18px 16px 4px;font-family:{FONT};font-size:15px;line-height:1.5;font-weight:300;color:#5B4310">{lines}</td></tr></table>'''

def quote(text, who):
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 16px"><tr><td style="border-left:3px solid {VIOLET};padding:4px 0 4px 16px;font-family:{FONT};font-size:17px;line-height:1.55;font-weight:300;color:{INK}">“{text}”<br><span style="font-size:13px;color:{MUTE}">{who}</span></td></tr></table>'''

def small_link(pre, label, href):
    return p(f'{pre} <a href="{href}" style="color:{VIOLET};text-decoration:underline">{label}</a>', 14)

def body_for(key, L, C, v, coin_src, url):
    E = L[key]
    h = lambda t: f'<h1 style="margin:0 0 16px;font-family:{FONT};font-size:26px;line-height:1.3;font-weight:400;letter-spacing:-.02em;color:{INK}">{t}</h1>'
    eyebrow = lambda t: f'<p style="margin:0 0 10px;font-family:{FONT};font-size:12px;line-height:1;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:#0E9DA2">{t}</p>'
    f = lambda s: fill(s, v)
    if key == "welcome":
        return h(f(E["h"])) + p(f(E["p1"])) + steps(E) + button(E["btn"], url("agenda")) + p(E["after"], 14) + p(E["sig"], 15, INK, "margin-top:24px")
    if key == "reminder":
        card = table_card(L, v, "topic", "title", [f(C["hosted_by"]), v["when"], f(C["chairs"]) + " · " + v["length"], f(E["with"])])
        return eyebrow(E["eyebrow"]) + h(E["h"]) + p(E["p1"]) + card + button(E["btn"], url("table")) + \
            p(f'<a href="{url("calendar")}" style="color:{VIOLET};text-decoration:underline">{E["cal"]}</a>', 14) + \
            small_link(E["cant"], E["free"], url("free-chair"))
    if key == "rate":
        box = coin_box(L, v, coin_src, f'<span style="font-weight:500">{f(E["coins1"])}</span><br>{f(E["coins2"])}')
        return eyebrow(E["eyebrow"]) + h(E["h"]) + p(f(E["p1"])) + box + button(E["btn"], url("rate")) + p(E["after"], 14)
    if key == "invite_join":
        box = coin_box(L, v, coin_src, E["coins"])
        return h(f(E["h"])) + p(E["p1"]) + p(E["p2"]) + box + button(E["btn"], url("join"))
    if key == "invite_table":
        card = table_card(L, v, "topic", "title", [f(C["hosted_by"]), v["when"], f(C["chairs"]) + " · " + v["length"]])
        box = coin_box(L, v, coin_src, E["coins"])
        return h(f(E["h"])) + quote(v["note"], v["inviter"]) + card + box + button(E["btn"], url("accept")) + small_link(E["notnow_pre"], E["notnow"], url("decline"))

def page(key, lang, mode, logo_src, coin_src):
    L, C = T[lang], T[lang]["common"]
    if mode == "template":
        v = {k: "{{" + n + "}}" for k, n in VARS.items()}
        url = lambda n: "{{url_" + n.replace("-", "_") + "}}"
    else:
        v = dict(SAMPLE[lang]); url = lambda n: "#"
    E = L[key]
    subject, pre = fill(E["subject"], v), fill(E["pre"], v)
    inner = body_for(key, L, C, v, coin_src, url)
    why = fill(E.get("why", C["why"]), v)
    foot_links = f'<a href="{url("email-settings")}" style="color:#8A91B8;text-decoration:underline">{C["settings"]}</a> &nbsp;·&nbsp; <a href="{url("help")}" style="color:#8A91B8;text-decoration:underline">{C["help"]}</a>' if not key.startswith("invite") else \
                 f'<a href="{url("help")}" style="color:#8A91B8;text-decoration:underline">{C["about"]}</a>'
    return f'''<!doctype html>
<html lang="{lang}" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light only"><meta name="supported-color-schemes" content="light only">
<title>{html.escape(subject)}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
body{{margin:0;padding:0;width:100%!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}}
table{{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}} img{{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic}}
a.btn:hover{{background:#6A4BEB!important}}
@media only screen and (max-width:620px){{
 .wrap{{width:100%!important}} .pad{{padding-left:22px!important;padding-right:22px!important}} .hpad{{padding:20px 22px!important}}
 .card{{border-radius:0!important}} h1{{font-size:23px!important}}
}}
</style></head>
<body style="margin:0;padding:0;background:{PAPER}">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{PAPER}">{pre}&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPER}" style="background:{PAPER}"><tr><td align="center" style="padding:24px 0">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px">
<tr><td class="hpad card" bgcolor="{NAVY}" style="background:{NAVY};padding:22px 40px;border-radius:16px 16px 0 0"><a href="{url("home")}" style="text-decoration:none"><img src="{logo_src}" width="152" height="24" alt="timecapsule" style="display:block;border:0;color:#EEF1FF;font-family:{FONT};font-size:20px"></a></td></tr>
<tr><td class="pad card" bgcolor="#FFFFFF" style="background:#FFFFFF;padding:36px 40px 28px;border-radius:0 0 16px 16px">
{inner}
</td></tr>
<tr><td class="pad" style="padding:22px 40px 8px;font-family:{FONT};font-size:12px;line-height:1.6;font-weight:300;color:#8A91B8;text-align:center">
{why}<br>{foot_links}<br><span style="color:#A3A9C8">TimeCapsule · {C["tag"]}</span></td></tr>
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr></table>
</body></html>''', subject, pre

KEYS = ["welcome", "reminder", "rate", "invite_join", "invite_table"]
if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "templates"), exist_ok=True)
    b64 = lambda f: "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, f), "rb").read()).decode()
    logo64, coin64 = b64("timecapsule-logo-email.png"), b64("timecoin.png")
    preview = {}
    for lang in ["en", "it", "es", "el"]:
        for k in KEYS:
            t, subj, pre = page(k, lang, "template", "{{asset_url}}/timecapsule-logo-email.png", "{{asset_url}}/timecoin.png")
            open(os.path.join(HERE, "templates", f"{k.replace('_','-')}.{lang}.html"), "w", encoding="utf-8").write(t)
            s, subj, pre = page(k, lang, "sample", "__LOGO__", "__COIN__")
            preview[f"{k}.{lang}"] = dict(html=s, subject=subj, pre=pre)
    json.dump(preview, open(os.path.join(HERE, "preview-data.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("built", len(preview))
