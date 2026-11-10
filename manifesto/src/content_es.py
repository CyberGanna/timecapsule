import copy
import content_en as E

D = {}
for l in open('/mnt/project-files/landing/dict-landing.txt'):
    p = l.rstrip('\n').split('|')
    if len(p) >= 3:
        D[p[0]] = p[2]

ANTIDOTE_ES = [
 ("h2", "Contra el aislamiento y la alienación"),
 ("p", "Estamos más conectados que nunca y, sin embargo, más solos. La conectividad da contacto, no presencia. Intercambiamos más contenido sin comprender más, y nos comunicamos más a menudo sin construir relaciones más profundas."),
 ("p", "TimeCapsule es un lugar donde las personas se encuentran a través de la tecnología, no donde la tecnología simula su presencia. Los miembros son personas reales, no bots. Con la participación repetida crece la confianza, toman forma las relaciones y crece la pertenencia. La alienación no termina con más contenido. Termina cuando alguien te escucha, te responde y te recuerda. Donde la confianza importa más, los espacios protegidos mantienen esa continuidad privada y segura."),
 ("h2", "Contra la muerte de internet"),
 ("p", "Cada día, bots y agentes producen la mayor parte de lo que contiene internet. Las palabras se multiplican, pero cada vez menos tienen a alguien detrás. Ya no sabemos quién habla, ni si alguien escucha. Lo que está muriendo no es la red, sino la presencia que antes le daba sentido."),
 ("p", "TimeCapsule no compite con esta avalancha. Restituye lo que la avalancha borró: una voz humana en la que se puede confiar que es humana. La IA ayuda pero nunca suplanta, de modo que lo que las personas leen lo escriben personas, y lo que dicen lo escuchan personas. Aquí internet puede volver a ser un espacio humano compartido."),
 ("h2", "Por la preservación de la huella humana"),
 ("p", "La mayor parte de lo que decimos en internet se pierde en pocos días, separado de su autor, de su contexto y de la conversación que lo produjo. Las ideas desaparecen en el flujo constante de contenido."),
 ("p", "TimeCapsule conserva la experiencia humana como un registro duradero, en el que cada aportación lleva consigo su historia, su autoría y su contexto. Una conversación no termina cuando acaba: se puede volver a ella, cuestionarla y desarrollarla. Juntas, estas aportaciones forman una huella humana en evolución, una herencia que las generaciones futuras podrán encontrar, cuestionar y sobre la que podrán construir. En una época en la que las máquinas pueden generar respuestas sin límite, lo que merece conservarse es la experiencia humana de la que nacen las preguntas."),
]

FAQ_ES = [
 ("q", "1. ¿Es TimeCapsule un LLM?"),
 ("p", "No. TimeCapsule no es un modelo de IA y no intenta responder a tus preguntas por ti. Es un lugar donde las personas se encuentran, y la IA cumple en él un papel de apoyo."),
 ("p", "<i>¿Por qué usarlo si las plataformas de IA ya pueden hacer tantas tareas?</i> Las plataformas de IA están hechas para producir respuestas. TimeCapsule está hecho para lo que las respuestas no pueden dar: la experiencia, el desacuerdo y la comprensión que surge cuando personas reales piensan juntas. Producir una respuesta no es lo mismo que entender por qué importa una pregunta. Aquí, la IA te ayuda a seguir las conversaciones, encontrar aportaciones relevantes y superar las barreras del idioma, mientras el pensamiento, el juicio y la autoría siguen en manos de las personas. Cada miembro es una persona real, y la participación humana nunca se sustituye por actividad artificial."),
 ("q", "2. ¿Es TimeCapsule otra red social?"),
 ("p", "No. Comparte la idea de conectar a las personas, pero no la lógica de la mayoría de las redes sociales. TimeCapsule no prioriza la velocidad, el contenido infinito ni la actividad constante. Se organiza en torno a conversaciones sostenidas, intereses compartidos y comunidades que crecen con la participación continuada."),
 ("p", "<i>¿Por qué usarlo en lugar de las redes sociales convencionales?</i> Las plataformas convencionales nos ayudan a intercambiar más contenido sin comprender más ni construir relaciones más profundas. TimeCapsule está pensado para lo contrario: una confianza que crece con la participación repetida, conversaciones que evolucionan con el tiempo y un espacio seguro, respetuoso y lo bastante privado para que las personas se expresen con libertad. Las ideas tampoco se pierden en un feed. Cada aportación conserva su autoría, su historia y su contexto, para que se pueda volver a ella, cuestionarla y desarrollarla."),
 ("q", "3. ¿Es TimeCapsule otro Zoom?"),
 ("p", "No. Las herramientas de videoconferencia conectan a las personas para una reunión, y cuando termina la llamada queda poco. TimeCapsule sí ofrece conversaciones en directo, charlas, clases y talleres, pero son parte de un espacio continuo y no eventos aislados."),
 ("p", "<i>¿Por qué usarlo en lugar de Zoom?</i> Porque lo que ocurre en una sesión en directo no termina con ella. Las conversaciones se conservan con su contexto y su autoría, y los participantes pueden volver a ellas, continuarlas y construir a partir de ellas. Las comunidades se forman en torno a intereses compartidos y continúan entre una sesión y otra. Las herramientas de IA ayudan con la preparación, las barreras del idioma y la organización del conocimiento compartido, lo que facilita organizar y participar sin sustituir a las personas."),
 ("q", "4. ¿Es TimeCapsule otro TED o TEDx?"),
 ("p", "No. Una charla TED es un formato en una sola dirección: alguien presenta y un público escucha. TimeCapsule se basa en la participación activa, donde las personas siguen siendo protagonistas y no consumidoras pasivas."),
 ("p", "<i>¿Por qué usar TimeCapsule?</i> Cualquiera puede organizar una charla, una clase o un taller, pero la charla es donde empieza el intercambio, no donde termina. El público puede hacer preguntas, cuestionar perspectivas y responder, y la conversación continúa con el tiempo. Las ideas también pueden convertirse en proyectos compartidos, a medida que las personas encuentran puntos en común y llevan a la práctica ideas colectivas. Todo se conserva como un registro duradero, para que las generaciones futuras puedan encontrarlo, cuestionarlo y construir sobre él."),
 ("q", "5. ¿Es TimeCapsule otro espacio para que los académicos presenten sus investigaciones?"),
 ("p", "TimeCapsule ofrece a los investigadores un lugar para presentar su trabajo y debatirlo a fondo con una comunidad implicada, no solo con quienes pertenecen a su propio campo o institución."),
 ("p", "<i>¿Por qué usar TimeCapsule?</i> Ofrece diálogo en lugar de difusión: los investigadores pueden presentar sus resultados en charlas, clases o talleres en directo, y luego continuar la conversación con preguntas, desacuerdos y perspectivas distintas. Las herramientas de IA ayudan a superar las barreras del idioma, para que la investigación se comparta y se debata más allá de una sola comunidad lingüística. Cada aportación conserva su historia, su autoría y su contexto original, de modo que la investigación, y el debate que la rodea, se pueden retomar y desarrollar. Los investigadores pueden encontrar puntos en común con otros y convertir ideas en proyectos compartidos. Los académicos también pueden exportar la transcripción de su ponencia en vídeo y usarla para crear contenidos, como artículos, resúmenes o material docente. El conocimiento y los debates se conservan como un registro duradero sobre el que las generaciones futuras puedan construir, en un entorno de confianza donde los miembros son personas reales, en un espacio seguro y respetuoso donde importan la privacidad y el respeto mutuo."),
 ("q", "6. ¿Es TimeCapsule otro LinkedIn?"),
 ("p", "No. LinkedIn se basa en perfiles profesionales: quién eres, dónde has trabajado y qué has logrado. TimeCapsule se basa en cómo piensan y participan las personas. El k▪universe de cada miembro, un mapa vivo de los libros y temas que dan forma a su pensamiento, lo hace visible de un vistazo."),
 ("p", "<i>¿Por qué usar TimeCapsule en lugar de LinkedIn?</i> En TimeCapsule, los intereses, la participación y la forma de pensar de un miembro se hacen visibles a través de lo que realmente aporta: las preguntas que plantea, las perspectivas que ofrece y la manera en que se relaciona con los demás. Su capacidad de captar las cosas, de comprender, interpretar y responder, se ve en las conversaciones en las que participa, en lugar de afirmarse en un perfil. Como cada aportación conserva su autoría, su historia y su contexto, este registro se construye con el tiempo mediante la participación sostenida. Permite que las personas se encuentren por intereses compartidos y por la calidad de su pensamiento, y que construyan relaciones y comunidades que nacen de un intercambio real."),
 ("q", "7. ¿Puede TimeCapsule acoger comunidades existentes y relaciones privadas?"),
 ("p", "Sí. TimeCapsule no es solo para charlas públicas y conversaciones abiertas. También puede conservar comunidades y relaciones personales que ya existen, y darles un lugar donde continuar con el tiempo."),
 ("p", "<i>¿Por qué usar TimeCapsule?</i> Una comunidad de apoyo como Alcohólicos Anónimos puede seguir reuniéndose en un mismo lugar, con su historia y su continuidad intactas. Una sesión de psicoanálisis puede tener lugar en privado, y la relación entre analista y paciente tiene un espacio al que volver en cualquier momento. O algo más sencillo: un club de lectura que se reúne una vez al mes, o viejos amigos de la universidad que hoy viven en países distintos, pueden conservar su mesa y retomar la conversación donde la dejaron. Estos espacios son privados y están protegidos con medidas de seguridad extremas, para que la confianza, de la que dependen estas relaciones, nunca se ponga en riesgo. El mismo entorno puede acoger una charla abierta y una conversación protegida: pública donde las personas quieren compartir, privada donde necesitan sentirse seguras."),
]

HEAD = {
 "what": ("QUÉ es <b>TIMECAPSULE</b>", "Qué es TimeCapsule"),
 "how": ("CÓMO usar <b>TIMECAPSULE</b>", "Cómo usar TimeCapsule"),
 "why": ("POR QUÉ usar <b>TIMECAPSULE</b>", "Por qué usar TimeCapsule"),
 "exists": ("POR QUÉ existe <b>TIMECAPSULE</b>", "Por qué existe TimeCapsule"),
 "manifesto": ("<b>MANIFIESTO</b> DE TIMECAPSULE<span class=\"sub\">Creemos</span>", "Manifiesto de TimeCapsule"),
 "antidote": ("<b>TIMECAPSULE</b>: un antídoto", "TimeCapsule: un antídoto"),
 "faq": ("<b>TIMECAPSULE</b>: preguntas frecuentes", "TimeCapsule: preguntas frecuentes"),
}
LABELS = {"Host and participate:": "Acoger y participar:",
          "Turn ideas into shared projects:": "Convertir ideas en proyectos compartidos:",
          "Preserve and pass on knowledge:": "Conservar y transmitir el conocimiento:"}


FIXES = [
 ("construido sobre una relación distinta con la tecnología: una que aprovecha sus posibilidades sin dejar que", "construido sobre una relación distinta con la tecnología, que aprovecha sus posibilidades sin permitir que"),
 ("deja espacio a la reflexión, al diálogo y a una participación humana sostenida", "da cabida a la reflexión, al diálogo y a una participación humana sostenida"),
 ("En su centro está la convicción de que", "En su esencia está la convicción de que"),
 ("se comunican y desarrollan juntas la comprensión,", "se comunican y construyen juntas su comprensión,"),
 ("Así la participación es más accesible y la colaboración más fácil, mientras el juicio", "Esto hace que la participación sea más accesible y la colaboración más sencilla, mientras que el juicio"),
 ("participa cada vez más en actividades que antes guiaban el juicio, la creatividad y la experiencia humanas", "interviene cada vez más en actividades que antes dependían del juicio, la creatividad y la experiencia humanos"),
 ("y qué arriesgamos perder cuando sus capacidades empiezan", "y qué corremos el riesgo de perder cuando sus capacidades empiezan"),
 ("no significa automáticamente una participación con más sentido", "no significa automáticamente una participación más significativa"),
 ("El juicio, la responsabilidad y la experiencia humanas siguen en el centro.", "El juicio, la responsabilidad y la experiencia humanos siguen siendo lo esencial."),
 ("porque una comunicación con sentido no puede desarrollarse sin una sensación de seguridad", "porque no puede haber una comunicación significativa si las personas no se sienten seguras"),
 ("y la libertad de preguntar.", "y la libertad de cuestionar."),
 ("Creemos que la participación debe ser activa y con sentido. Las personas deben seguir aportando al conocimiento", "Creemos que la participación debe ser activa y significativa. Las personas deben seguir contribuyendo al conocimiento"),
 ("ni la responsabilidad humanas.", "ni la responsabilidad humanos."),
 ("donde las personas participan en lugar de limitarse a consumir, comprenden en lugar de simplemente procesar, crean juntas en lugar de producir en aislamiento y construyen relaciones", "donde las personas participen en lugar de limitarse a consumir, comprendan en lugar de simplemente procesar, creen juntas en lugar de producir en aislamiento y construyan relaciones"),
 ("toman forma las relaciones y crece la pertenencia.", "toman forma las relaciones y se fortalece el sentido de pertenencia."),
 ("Restituye lo que la avalancha borró: una voz humana en la que se puede confiar que es humana. La IA ayuda pero nunca suplanta,", "Recupera lo que la avalancha borró: una voz humana de la que se puede tener la certeza de que es humana. La IA ayuda, pero nunca suplanta a nadie,"),
 ("Una conversación no termina cuando acaba:", "Una conversación no se agota cuando termina:"),
 ("Las ideas tampoco se pierden en un feed.", "Las ideas tampoco se pierden en un flujo interminable de publicaciones."),
 ("Organizar y participar en conversaciones en directo, charlas, clases y talleres para", "Organizar conversaciones en directo, charlas, clases y talleres, y participar en ellos, para"),
]
_USED = set()
def fix(s):
    for i, (a, b) in enumerate(FIXES):
        if a in s: s = s.replace(a, b); _USED.add(i)
    return s

def tr(s):
    if s['id'] == 'antidote': blocks = ANTIDOTE_ES
    elif s['id'] == 'faq': blocks = FAQ_ES
    else:
        blocks = []
        for t, v in s['blocks']:
            if t == 'ul': v = [[LABELS[a], D[b]] for a, b in v]
            elif t == 'bel': v = [D[x] for x in v]
            else: v = D[v]
            blocks.append((t, v))
    blocks = [(t, [[fix(a), fix(b)] for a, b in v] if t == 'ul' else [fix(x) for x in v] if t == 'bel' else fix(v)) for t, v in blocks]
    n = dict(s); n['h1'], n['foot'] = HEAD[s['id']]; n['blocks'] = blocks
    return n

_m = {s['id']: tr(s) for s in E.FULL}
FULL = [_m[s['id']] for s in E.FULL]
SHORT = [_m[s['id']] for s in E.SHORT]
assert len(_USED) == len(FIXES), [FIXES[i][0] for i in range(len(FIXES)) if i not in _USED]
COVER = {"title": "Introducción a", "short": "Edición breve"}
UI = {"lang": "es", "contents": "Índice", "file": "Introduccion-a-TimeCapsule"}
