"""Turn the regular 'Two voices, one link' logo SVG (white link) into the cut-out version (transparent link)."""
import re
LINK = re.compile(r'<g fill="#fff"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g>')
def cut(svg, mid):
    if 'mask=' in svg or not LINK.search(svg): return svg
    body = LINK.sub('', svg)
    mask = ('<mask id="%s" maskUnits="userSpaceOnUse" x="0" y="-6" width="110" height="82"><rect x="0" y="-6" width="110" height="82" fill="#fff"/>'
            '<g fill="#000"><circle cx="36" cy="35" r="4.6"/><circle cx="74" cy="35" r="4.6"/><rect x="36" y="33.4" width="38" height="3.2"/></g></mask>') % mid
    body = body.replace('</defs>', mask + '</defs><g mask="url(#%s)">' % mid, 1)
    return body.replace('</svg>', '</g></svg>')
SVGRE = re.compile(r'<svg viewBox="0 -6 110 82"[^>]*>.*?</svg>', re.S)
def cut_all(html):
    n = [0]
    def f(m):
        n[0] += 1; return cut(m.group(0), 'tcmask%d' % n[0])
    return SVGRE.sub(f, html), n[0]
