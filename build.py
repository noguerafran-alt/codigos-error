import os,json,html
B="https://codigos-error.onrender.com"
SITE="Códigos de error · guía independiente"
FOOT='''<footer><p><strong>Guía independiente.</strong> Este sitio no está afiliado, patrocinado ni avalado por Drean, Longvie, Whirlpool, BGH ni ninguna otra marca. Los nombres y marcas pertenecen a sus dueños. La información se transcribe de manuales y páginas oficiales enlazados en cada página; ante cualquier duda, manda el manual de tu modelo y el service oficial.</p><p>Si el equipo tiene riesgo eléctrico o de gas, no lo abras: llamá a un técnico matriculado o al service oficial.</p></footer>'''
def fmt(d): y,m,dd=d.split('-'); return f'{dd}/{m}/{y}'
def page(path,title,desc,body,crumb=None,faq=None,pub=None,mod=None):
    url=f'{B}/{path}'
    hdr='<a href="/">'+SITE+'</a>'
    ld=[]; extra=''
    if crumb:
        hdr=f'<nav class="crumb" aria-label="Ruta"><a href="/">Inicio</a> › <span>{crumb}</span></nav>'
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Inicio","item":B+"/"},
            {"@type":"ListItem","position":2,"name":crumb,"item":url}]})
        ld.append({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
            "inLanguage":"es-AR","mainEntityOfPage":url,"datePublished":pub,"dateModified":mod,
            "author":{"@type":"Organization","name":SITE,"url":B+"/"}})
        extra+=f'<p class="rev">Revisado el {fmt(mod)} contra las fuentes oficiales enlazadas abajo.</p>'
    if faq:
        body+='\n<h2>Preguntas frecuentes</h2>\n'+'\n'.join(f'<h3>{q}</h3>\n<p>{a}</p>' for q,a in faq)
        strip=lambda s: html.unescape(__import__('re').sub(r'<[^>]+>','',s))
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in faq]})
    body=body.replace('<table>','<div class="tw"><table>').replace('</table>','</table></div>')
    scripts=''.join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>\n' for x in ld)
    h=f'''<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><link rel="stylesheet" href="/style.css">
{scripts}</head><body>
<header>{hdr}</header>
<main>
{extra}{body}
</main>
{FOOT}
</body></html>
'''
    d=path.rstrip('/') or '.'
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w').write(h)
    assert len(title)<=60 or path=='' , (path,len(title))
    print(path or '/',len(title),len(desc))

ECO='https://drean.com.ar/medias/Manual-Drean-Next-ECO-LFDRI0710SB0.pdf?context=bWFzdGVyfGltYWdlc3wxODg4NDUyfGFwcGxpY2F0aW9uL3BkZnxhRFU0TDJnM01pOHhNakU0TnpnNE1EUXlNelExTkM5TllXNTFZV3d0UkhKbFlXNHRUbVY0ZEMxRlEwOHRURVpFVWtrd056RXdVMEl3TG5Ca1pnfDY5Zjk2NTllMmIyZWZjNTU1YmY5NDE4Y2VjYjE5ZDc0ODdiMzFlMWMzNmFkODU4MDk2ZjM0ZDM4Zjg3OTMyNjY'
TOUCH='https://drean.com.ar/medias/Manual-Drean-Next-Touch-ECO.pdf?context=bWFzdGVyfGltYWdlc3wyNDU4MDY5fGFwcGxpY2F0aW9uL3BkZnxhREJtTDJnNE15OHhNVFE0TWprd05qVTFPRFE1TkM5TllXNTFZV3d0UkhKbFlXNHRUbVY0ZEMxVWIzVmphQzFGUTA4dWNHUm18NDMxY2EyN2Y0ZDQ4OWQxN2UwZmVmZmM4ZjU4YjMzMzA0ZDBjMjhiZjcxYmJiNDY5Y2YyNTA0YjMxNDkxYjg4YQ'
LV='https://longvie-gestion.appsinnovategroup.com/api/uploads/7494468/13280-V6.pdf'
WCCR='https://portal.bgh.com.ar/wp-content/uploads/2023/07/UM-BGH-Minisplit-OnOff-BS_WCCR-ES-MAR23.pdf'
WCEW='https://portal.bgh.com.ar/wp-content/uploads/2025/10/UM-BGH-Minisplit-OnOff-WCEW-ES-SEP25.pdf'
BSI='https://portal.bgh.com.ar/wp-content/uploads/2026/06/Manual-BSI106WCAW-1.pdf'
AYUDA='https://www.bgh.com.ar/institucional/ayuda'


DST='https://drean.com.ar/servicio_tecnico'
DFAQ='https://drean.com.ar/es_AR/preguntasfrecuentes'
DEXP='https://drean.com.ar/es_AR/servicio-express'
P0='2026-10-23'; M='2026-10-27'

page('','Códigos de error de lavarropas y aires acondicionados (Drean, Longvie, BGH)',
'Guía independiente de códigos de error de lavarropas Drean y Longvie y aires acondicionados BGH, transcriptos de los manuales oficiales con la fuente enlazada.',
'''<h1>Códigos de error de electrodomésticos en Argentina</h1>
<p>Qué significa cada código según el <strong>manual oficial</strong> del fabricante, qué podés revisar vos sin riesgo y cuándo llamar al service. Cada página enlaza el manual del que sale la información. Si un código no está en el manual, lo decimos.</p>
<h2>Lavarropas</h2>
<ul class="cards">
<li><a href="/drean-next-error-6/">Drean Next error 6 (Er 6, E6) y códigos de error del manual</a></li>
<li><a href="/longvie-lavarropas-error-e03/">Longvie lavarropas error 3 (E03): no desagota, y tabla de errores</a></li>
<li><a href="/longvie-lavarropas-error-e20/">Longvie lavarropas error E20: qué dice el manual oficial</a></li>
</ul>
<h2>Aire acondicionado</h2>
<ul class="cards">
<li><a href="/bgh-aire-acondicionado-codigos-de-error/">Aire acondicionado BGH: qué significa "CF" y tabla de códigos de error</a></li>
</ul>
<h2>Service oficial por marca</h2>
<ul class="cards">
<li><a href="/servicio-tecnico-drean/">Servicio técnico oficial Drean: teléfonos, WhatsApp y horarios</a></li>
</ul>''')

page('drean-next-error-6/','Drean Next error 6 (Er 6, E6): qué significa y qué hacer',
'Según el manual oficial de Drean, el Er 6 del Next es un problema en el motor de lavado y hay que llamar al service. Tabla de códigos y canales del service.',
f'''<h1>Drean Next error 6 (Er 6, E6): qué significa y qué hacer</h1>
<div class="box"><strong>Respuesta corta:</strong> en el Drean Next, el <span class="code">Er 6</span> (o <span class="code">E6</span>, y en algunos modelos <span class="code">Er 6A</span>, <span class="code">Er 6b</span>, <span class="code">Er 6C</span>) significa <strong>"problema en el motor de lavado"</strong>. Para este código el manual oficial indica <strong>comunicarse con el Servicio de Asistencia Técnica</strong>; no trae una solución casera.</div>
<div class="box warn">El motor y la placa funcionan con 220 V. No desarmes el lavarropas: desenchufalo y llamá al service oficial o a un técnico matriculado.</div>
<h2>Cómo se muestra el error 6 según tu modelo</h2>
<ul>
<li><strong>Next con display (perilla):</strong> 10·12, 8·14, 8·12, LFDRI0710SB y 7·10 muestran <span class="code">Er</span> + número. En 10·12P y 8·14 el error 6 aparece como <span class="code">Er 6A</span>, <span class="code">Er 6b</span> o <span class="code">Er 6C</span>.</li>
<li><strong>Next sin display (con LEDs):</strong> 8·10, 7·09, 6·09, 6·08 y 6·06 indican el error con la cantidad de destellos de las 3 luces de los botones de función: <strong>6 destellos = error 6</strong>. Un <em>destello escalonado</em> indica tensión fuera de rango.</li>
<li><strong>Next Touch ECO (WiFi):</strong> 10·12 WCR/WCRG ECO y 8·14 WCR/WCRG ECO muestran <span class="code">E1</span> a <span class="code">E11</span> (E6A/E6B/E6C para el motor).</li>
</ul>
<h2>Resumen de códigos Drean Next (según manual oficial)</h2>
<p>El foco de esta página es el error 6. Para ubicarlo, este es el resumen de la lista de errores del manual:</p>
<table>
<tr><th>Código</th><th>Significado (manual Drean)</th><th>Qué indica el manual</th></tr>
<tr><td class="code">Er 1 / E1</td><td>Circuito de desagüe obstruido</td><td>Revisar filtro y manguera de desagote. Si sigue, service.</td></tr>
<tr><td class="code">Er 2 / E2</td><td>Tiempo de carga de agua excedido</td><td>Revisar presión, grifo, filtro de entrada y manguera de desagote. Si sigue, service.</td></tr>
<tr><td class="code">Er 3 / E3</td><td>Resistencia de calentamiento averiada</td><td>Service.</td></tr>
<tr><td class="code">Er 4 / E4</td><td>Problema en el sensor de temperatura</td><td>Service.</td></tr>
<tr><td class="code">Er 5 / E5</td><td>Error de puerta</td><td>Service.</td></tr>
<tr><td class="code">Er 6 / E6 (6A, 6b, 6C)</td><td><strong>Problema en el motor de lavado</strong></td><td><strong>Service.</strong></td></tr>
<tr><td class="code">Er 7 / E7</td><td>Sobrenivel de agua</td><td>Service.</td></tr>
<tr><td class="code">Er 8 / E8</td><td>Falla en el control del motor</td><td>Reiniciar el ciclo. Si sigue, service.</td></tr>
<tr><td class="code">Er 9 / E9</td><td>Sobrecalentamiento del agua</td><td>Verificar que no esté conectado a agua caliente. Si sigue, service.</td></tr>
<tr><td class="code">E10</td><td>Tensión fuera de rango (manual Next Touch ECO)</td><td>—</td></tr>
<tr><td class="code">Er 11 / E11</td><td>Error en el circuito de medición de nivel</td><td>Service.</td></tr>
</table>
<h2>Qué podés revisar vos sin riesgo</h2>
<p>Para el error 6, nada: el manual deriva al service. Solo en los errores 1, 2, 8 y 9 el manual sugiere una revisión: con el equipo <strong>desenchufado</strong>, revisá que el grifo esté abierto, que las mangueras no estén dobladas y que los filtros de entrada y de desagote estén limpios.</p>
<h2>Service oficial Drean</h2>
<p>Según <a href="{DST}" rel="nofollow">drean.com.ar/servicio_tecnico</a>: <strong>CABA y GBA (011) 5246-8663</strong>, <strong>interior 0800-345-6580</strong>, WhatsApp <strong>11 5023-7973</strong>, de lunes a viernes de 9 a 19:30 y sábados de 9 a 14. Todos los canales, la garantía y qué tener a mano están en <a href="/servicio-tecnico-drean/">servicio técnico oficial Drean</a>.</p>
<p class="src"><strong>Fuentes (oficiales, drean.com.ar):</strong><br>
<a href="{ECO}" rel="nofollow">Manual Drean Next ECO (perilla): 10.12, 8.14, 8.12, 8.10, LFDRI0710SB, 7.10, 7.09, 6.09, 6.08, 6.06</a>, listado de errores (pág. 25).<br>
<a href="{TOUCH}" rel="nofollow">Manual Drean Next Touch ECO (WiFi): 10·12 y 8·14 WCR/WCRG ECO</a>, lista de errores (pág. 27 del manual).<br>
<a href="{DST}" rel="nofollow">Servicio técnico Drean</a> y <a href="{DFAQ}" rel="nofollow">Preguntas frecuentes Drean</a> (garantía).</p>''',
crumb='Drean Next error 6',pub=P0,mod=M,faq=[
('¿Qué significa Er 6 en el Drean Next?','Según el manual oficial de Drean, el Er 6 (o E6) indica un problema en el motor de lavado. El manual indica comunicarse con el Servicio de Asistencia Técnica.'),
('¿Qué diferencia hay entre Er 6A, Er 6b y Er 6C?','El manual las muestra en los modelos 10·12P y 8·14 dentro del mismo error del motor de lavado, pero no detalla la diferencia entre cada una. En todos los casos indica llamar al service.'),
('¿Qué significan 6 destellos en las luces del Drean Next?','En los Next sin display (8·10, 7·09, 6·09, 6·08 y 6·06), 6 destellos en las 3 luces de los botones de función equivalen al error 6: problema en el motor de lavado.'),
('¿Lo cubre la garantía?','Según la página de preguntas frecuentes de Drean, los productos de línea blanca tienen 12 meses de garantía oficial conforme a los términos del manual. Para usarla tenés que conservar la factura o ticket de compra.'),
('¿A qué teléfono llamo?','Según drean.com.ar: CABA y GBA (011) 5246-8663, interior 0800-345-6580 y WhatsApp 11 5023-7973.')])

page('servicio-tecnico-drean/','Servicio técnico Drean: teléfono, WhatsApp y horarios',
'Teléfonos, WhatsApp, mail y horarios del servicio técnico oficial Drean según drean.com.ar, cómo usar la garantía y qué tener a mano antes de llamar.',
f'''<h1>Servicio técnico oficial Drean: teléfonos, WhatsApp y horarios</h1>
<div class="box warn"><strong>Guía independiente:</strong> este sitio no es Drean ni toma pedidos de service. Los datos de abajo se copian de drean.com.ar; verificalos ahí antes de llamar, porque pueden cambiar.</div>
<div class="box"><strong>Respuesta corta:</strong> el servicio técnico oficial Drean atiende en CABA y GBA al <strong>(011) 5246-8663</strong> y en el interior al <strong>0800-345-6580</strong>. También por WhatsApp al <strong>11 5023-7973</strong> y por mail a <strong>serviciodrean@drean.com.ar</strong>. Horario: lunes a viernes de 9 a 19:30 y sábados de 9 a 14.</div>
<h2>Canales oficiales del service Drean</h2>
<table>
<tr><th>Canal</th><th>Dato (según drean.com.ar)</th></tr>
<tr><td>Teléfono CABA y GBA</td><td>(011) 5246-8663</td></tr>
<tr><td>Teléfono interior del país</td><td>0800-345-6580</td></tr>
<tr><td>WhatsApp</td><td>11 5023-7973</td></tr>
<tr><td>Mail del service</td><td>serviciodrean@drean.com.ar</td></tr>
<tr><td>Horario del service</td><td>Lunes a viernes de 9 a 19:30 y sábados de 9 a 14</td></tr>
</table>
<p>La atención comercial (ventas, compras) es otra: lunes a viernes de 9 a 18, mail contacto@drean.com.ar. A ese mismo mail, según la página de preguntas frecuentes, se pide el manual de usuario indicando el modelo.</p>
<h2>Antes de llamar, te conviene tener a mano</h2>
<ul>
<li>El <strong>modelo</strong> del equipo, tal como figura en su etiqueta.</li>
<li>La <strong>factura o ticket de compra original</strong>: Drean pide conservarlo para usar la garantía de fábrica.</li>
<li>El <strong>código de error</strong> que muestra el equipo. Si es un Drean Next, buscalo en la <a href="/drean-next-error-6/">tabla de códigos del Drean Next</a>.</li>
</ul>
<h2>¿Hace falta llamar?</h2>
<p>Si el código tiene una revisión casera en el manual (por ejemplo, filtros o mangueras en los errores 1 y 2 del Next), probala primero con el equipo desenchufado. Si el equipo está en garantía, no lo abras: llamá directamente.</p>
<h2>Garantía: cuándo te cubre</h2>
<ul>
<li>Según las <a href="{DFAQ}" rel="nofollow">preguntas frecuentes de Drean</a>, todos los productos de línea blanca tienen <strong>12 meses de garantía oficial</strong>, conforme a los términos de la garantía de fábrica que viene en el manual.</li>
<li>Para usarla, Drean pide leer antes las instrucciones de uso e instalación y conservar la factura o ticket de compra original.</li>
<li>Las <strong>reparaciones</strong> del servicio técnico tienen <strong>90 días de garantía</strong>, según <a href="{DST}" rel="nofollow">drean.com.ar/servicio_tecnico</a>.</li>
</ul>
<h2>Servicio express (solo Capital Federal)</h2>
<p>Según <a href="{DEXP}" rel="nofollow">la página de servicio express de Drean</a>, podés coordinar día y horario de la visita, sujeto a disponibilidad de técnicos. Está disponible <strong>únicamente en Capital Federal</strong>; en otras zonas te contactan con la red de Servicio Técnico Autorizado. Se pide por las mismas líneas de atención.</p>
<h2>Service oficial de otras marcas</h2>
<table>
<tr><th>Marca</th><th>Dato y fuente</th></tr>
<tr><td>Longvie (lavarropas)</td><td>(011) 4709-8501, Laprida 4851, Villa Martelli, según el manual oficial. Ver <a href="/longvie-lavarropas-error-e03/">errores de lavarropas Longvie</a>.</td></tr>
<tr><td>BGH (climatización)</td><td>0810-222-1244, según bgh.com.ar. Ver <a href="/bgh-aire-acondicionado-codigos-de-error/">códigos de error de aires BGH</a>.</td></tr>
</table>
<div class="box warn">Desconfiá de "services oficiales" que no figuran en la web de la marca. Antes de dejar entrar a alguien o pagar, verificá el canal en drean.com.ar.</div>
<p class="src"><strong>Fuentes (oficiales, drean.com.ar, revisadas el 27/10/2026):</strong><br>
<a href="{DST}" rel="nofollow">Servicio Drean: servicio técnico especializado</a> (canales, horario y 90 días de garantía en reparaciones).<br>
<a href="{DFAQ}" rel="nofollow">Preguntas frecuentes Drean</a> (garantía de 12 meses, factura y pedido de manuales).<br>
<a href="{DEXP}" rel="nofollow">Servicio express Drean</a> (solo Capital Federal).</p>''',
crumb='Servicio técnico Drean',pub=M,mod=M,faq=[
('¿Cuál es el teléfono del servicio técnico Drean en el interior?','Según drean.com.ar, el 0800-345-6580. Para CABA y GBA es el (011) 5246-8663.'),
('¿Drean tiene WhatsApp para el service?','Sí. drean.com.ar publica el WhatsApp 11 5023-7973 en los datos del servicio técnico.'),
('¿Qué horario tiene el service Drean?','Lunes a viernes de 9 a 19:30 y sábados de 9 a 14, según drean.com.ar.'),
('¿Cuánto dura la garantía de un lavarropas Drean?','12 meses de garantía oficial para los productos de línea blanca, según las preguntas frecuentes de Drean, conforme a los términos de la garantía del manual.'),
('¿Las reparaciones del service Drean tienen garantía?','Sí: drean.com.ar indica 90 días de garantía en todas sus reparaciones.'),
('¿Este sitio es el service oficial de Drean?','No. Es una guía independiente que junta los datos publicados por Drean con su fuente. Para pedir un service, usá los canales de drean.com.ar.')])

page('longvie-lavarropas-error-e03/','Longvie error E03 (error 3): qué significa y qué revisar',
'¿Tu Longvie marca error 3? Según el manual oficial, no descarga el agua. Qué revisar vos, tabla de errores 2, 4, 7 y 8 y cuándo llamar al service.',
f'''<h1>Lavarropas Longvie error 3 (E03): qué significa y tabla de errores</h1>
<div class="box"><strong>Respuesta corta:</strong> en los lavarropas Longvie L16508, L16510, L18010, L18012 y el lavasecarropas LS18012, el manual oficial indica que el <span class="code">error Nº 3</span> significa que <strong>el lavarropas no descarga el agua</strong>. Revisá que el tubo de desagote no esté doblado y que el filtro de la bomba no tenga cuerpos extraños. Si sigue, llamá al service oficial de Longvie.</div>
<div class="box warn">Agua y 220 V: antes de tocar nada, desenchufá el lavarropas y cerrá la llave de paso del agua. Al abrir el filtro va a salir agua. No abras paneles ni desconectes piezas internas.</div>
<h2>Qué significa el error 3 en Longvie</h2>
<p>El manual 13280-V6 lo nombra como "error Nº 3" en la pantalla y no aclara si el display lo muestra como "3" o como "E03". Su significado: <strong>el lavarropas no descarga el agua</strong>.</p>
<h3>Modelos que cubre este manual</h3>
<p>Lavarropas L16508, L16510, L18010, L18012 / L18012C / L18012P y lavasecarropas LS18012 / LS18012C / LS18012P (línea Sensitive Touch, edición 02-2026). Si tu modelo es otro, por ejemplo de la línea Cleanium, buscá su propio manual en <a href="https://www.longvie.com" rel="nofollow">longvie.com</a>: el significado del código puede cambiar.</p>
<h2>Qué podés revisar vos (según el manual)</h2>
<ol>
<li>Desenchufá el lavarropas y cerrá la llave de paso del agua.</li>
<li>Revisá que el <strong>tubo de desagote</strong> no esté doblado ni aplastado. Si lo está, enderezalo.</li>
<li>Limpiá el <strong>filtro de la bomba de desagote</strong>: poné un paño en el piso y encima un recipiente bajo, abrí la tapa de la parte inferior del frente, girá el filtro en sentido antihorario hasta que haga tope en posición vertical, sacalo y limpialo. Volvé a colocarlo girando en sentido horario hasta ajustarlo del todo.</li>
</ol>
<p>Los mismos pasos, con el resto de los errores, están en <a href="/longvie-lavarropas-error-e20/">limpieza del filtro de la bomba Longvie</a>.</p>
<h2>Desagota pero no centrifuga y marca error 3</h2>
<p>El manual no cubre ese caso. Para "no centrifuga" sin código, el manual menciona solo dos causas: que todavía no terminó de desagotar (esperá unos minutos) o que está activada la exclusión de centrifugado. Si aparece el error 3 aunque el agua salga, no sigas probando: llamá al service.</p>
<h2>Tabla de errores Longvie (manual 13280-V6)</h2>
<table>
<tr><th>Error en pantalla</th><th>Qué indica el manual</th><th>¿Vos o service?</th></tr>
<tr><td class="code">2</td><td>No se llena de agua: revisar que el grifo esté abierto, que el selector de programas esté bien posicionado y limpiar el filtro de la electroválvula.</td><td>Vos, con esas revisiones. Si sigue, service.</td></tr>
<tr><td class="code">3</td><td>No descarga el agua: enderezar el tubo de desagote y desobstruir el filtro de la bomba.</td><td>Vos, con esas revisiones. Si sigue, service.</td></tr>
<tr><td class="code">4</td><td>Hay demasiada agua: cerrar la llave del agua.</td><td>Service.</td></tr>
<tr><td class="code">0, 1, 5, 7, 8, 9</td><td>Dirigirse al Servicio de Asistencia Técnica.</td><td>Service.</td></tr>
</table>
<h2>¿Y el error E20?</h2>
<p>No figura en este manual. Lo explicamos en <a href="/longvie-lavarropas-error-e20/">Longvie error E20</a>.</p>
<h2>Service oficial Longvie</h2>
<p>Dato que figura en el manual oficial: <strong>Servicio de Asistencia al Cliente, Laprida 4851 (1603) Villa Martelli, Buenos Aires · Tel. (011) 4709-8501</strong>. El manual pide indicar el modelo, que está en la placa del producto. Otras marcas: <a href="/servicio-tecnico-drean/">service oficial Drean</a>.</p>
<p class="src"><strong>Fuente:</strong> <a href="{LV}" rel="nofollow">Manual oficial Longvie 13280-V6 (L16508, L16510, L18010, L18012, LS18012)</a>: "Limpieza de los filtros" (pág. 24 y 25), "Resolución de inconvenientes" y "Posibles causas de desperfectos" (pág. 26 y 27), certificado de garantía.</p>''',
crumb='Longvie error 3 (E03)',pub=M,mod=M,faq=[
('¿Qué significa error 3 en un lavarropas Longvie?','Según el manual oficial 13280-V6, el error Nº 3 significa que el lavarropas no descarga el agua. Hay que revisar el tubo de desagote y el filtro de la bomba.'),
('¿E03 y error 3 son lo mismo?','El manual lo llama "error Nº 3" y no aclara cómo se ve en el display. Si tu equipo muestra E03 y es uno de los modelos de este manual, revisá lo mismo; si es de otra línea, confirmalo en su manual.'),
('¿Por qué mi Longvie desagota pero marca error 3?','El manual no explica ese caso. Si el agua sale y el error 3 vuelve a aparecer, llamá al Servicio de Asistencia Técnica de Longvie.'),
('¿Qué significa el error 2 en Longvie?','Que el lavarropas no se llena de agua. El manual indica revisar que el grifo esté abierto, que el selector esté bien posicionado y que el filtro de la electroválvula no esté tapado.'),
('¿Qué hago si aparece el error 7 o el 8?','El manual indica dirigirse al Servicio de Asistencia Técnica, igual que con los errores 0, 1, 5 y 9.'),
('¿Cuál es el teléfono del service Longvie?','El manual oficial indica el (011) 4709-8501, Laprida 4851, Villa Martelli.'),
('¿Si abro el lavarropas pierdo la garantía?','El certificado de garantía del manual menciona como causa de anulación la intervención al artefacto por personal no autorizado por Longvie. La garantía es de 1 año desde la fecha de la factura.')])

page('longvie-lavarropas-error-e20/','Longvie error E20: qué significa (no figura en el manual)',
'¿Tu lavarropas Longvie marca E20? El manual oficial no lo incluye. Qué errores sí trae y qué hacer: revisá el filtro o llamá al service.',
f'''<h1>Longvie lavarropas error E20: qué dice el manual oficial</h1>
<div class="box"><strong>Respuesta honesta:</strong> el código <span class="code">E20</span> <strong>no figura en el manual oficial</strong> de Longvie que revisamos (lavarropas L16508, L16510, L18010, L18012/C/P y lavasecarropas LS18012/C/P, edición 02-2026). No vamos a inventarle un significado. Próximo paso: anotá el modelo exacto (está en la placa del producto) y llamá al service oficial al <strong>(011) 4709-8501</strong> (dato del manual).</div>
<div class="box warn">Un lavarropas combina agua y 220 V. Antes de tocar cualquier cosa, desenchufalo. No abras paneles ni la placa: eso es trabajo del service oficial o de un técnico matriculado.</div>
<h2>Códigos de error que sí trae el manual Longvie</h2>
<p>El manual los nombra como "error Nº" seguido del número y no aclara si el display muestra "2" o "E02".</p>
<table>
<tr><th>Error Nº</th><th>Qué indica el manual</th></tr>
<tr><td class="code">2</td><td>No se llena de agua. Revisar que el grifo esté abierto, que el selector esté bien posicionado y que el filtro de la electroválvula no esté tapado.</td></tr>
<tr><td class="code">3</td><td>No descarga el agua. Revisar que el tubo de desagote no esté doblado y que no haya cuerpos extraños en el filtro de la bomba. Más en <a href="/longvie-lavarropas-error-e03/">error 3: no desagota</a>.</td></tr>
<tr><td class="code">4</td><td>Demasiada agua. Cerrar la llave del agua y llamar al service.</td></tr>
<tr><td class="code">0, 1, 5, 7, 8, 9</td><td>Dirigirse al Servicio de Asistencia Técnica.</td></tr>
<tr><td class="code">E20</td><td><strong>No figura en el manual.</strong></td></tr>
</table>
<h2>¿E20 puede ser un error de desagote?</h2>
<p>El manual no lo dice. Si además de E20 el lavarropas no desagota, revisá el filtro de la bomba con los pasos de abajo; si no, llamá al service.</p>
<h2>Limpieza del filtro de la bomba (según el manual)</h2>
<ol>
<li>Desenchufá el lavarropas y cerrá la llave de paso del agua.</li>
<li>Poné un paño en el piso y un recipiente bajo: va a salir agua.</li>
<li>Abrí la tapa de la parte inferior del frente.</li>
<li>Girá el filtro en sentido antihorario hasta que haga tope en posición vertical, sacalo y limpialo.</li>
<li>Volvé a colocarlo girando en sentido horario hasta ajustarlo y cerrá la tapa.</li>
</ol>
<h2>Otros códigos Longvie</h2>
<p>El error más consultado es el 3: <a href="/longvie-lavarropas-error-e03/">error E03 Longvie (no desagota)</a>.</p>
<h2>Service oficial Longvie</h2>
<p>Dato que figura en el manual oficial: <strong>Laprida 4851 (1603) Villa Martelli, Buenos Aires · Tel. (011) 4709-8501</strong>.</p>
<p class="src"><strong>Fuente:</strong> <a href="{LV}" rel="nofollow">Manual oficial Longvie 13280-V6 (L16508, L16510, L18010, L18012, LS18012)</a>, secciones "Limpieza de los filtros" y "Posibles causas de desperfectos". Si tu modelo es otro, buscá su manual en el sitio de Longvie: la tabla puede ser distinta.</p>''',
crumb='Longvie error E20',pub=P0,mod=M,faq=[
('¿Qué significa E20 en Longvie?','No lo sabemos con fuente oficial: E20 no figura en el manual 13280-V6 de Longvie. Consultá al service con el modelo exacto.'),
('¿Por qué no está en el manual?','El manual que revisamos solo lista los errores 0 a 9. Puede tratarse de otro modelo o de un código que el manual de usuario no describe; el manual no lo aclara.'),
('¿Puedo seguir lavando?','El manual no habla del E20. Para cualquier problema de funcionamiento indica que la reparación la haga el Servicio de Asistencia al Cliente de Longvie.'),
('¿Cómo limpio el filtro de la bomba?','Con el equipo desenchufado y el agua cerrada: abrí la tapa inferior del frente, girá el filtro en sentido antihorario, sacalo, limpialo y volvé a colocarlo en sentido horario.'),
('¿Cuál es el teléfono del service Longvie?','El manual oficial indica el (011) 4709-8501, Laprida 4851, Villa Martelli.')])

page('bgh-aire-acondicionado-codigos-de-error/','Aire BGH error CF: qué significa y tabla de códigos',
'¿Tu aire BGH muestra CF? Según el manual oficial no es una falla: indica la función Hot Start en calefacción. Además, tabla de códigos de error E1, E0, EC y más.',
f'''<h1>Aire acondicionado BGH: qué significa "CF" y tabla de códigos de error</h1>
<div class="box"><strong>Respuesta corta:</strong> en los splits BGH cuyo manual lo describe, <span class="code">cF</span> en el display <strong>no es un código de falla</strong>: se muestra cuando la función <strong>Hot Start</strong> se activa en modo calefacción. El ventilador interior arranca recién cuando el radiador está lo suficientemente caliente, para no tirar aire frío al ambiente. Es normal que dure unos minutos al encender en calor.</div>
<p>Esto figura en la sección "Display" de los manuales oficiales BGH Silent Air BS26/35/52/53/65 WCCR-WFCR y BS26/35/52/65 WCEW. En esos mismos manuales, <span class="code">dF</span> indica descongelamiento (DEFROST), <span class="code">SC</span> autolimpieza (opcional) y <span class="code">FP</span> calefacción de 8 °C (opcional). Si tu modelo es otro, revisá su manual: no todos los equipos usan los mismos indicadores.</p>
<div class="box warn">El aire acondicionado trabaja con 220 V y gas refrigerante a presión (en modelos R32, inflamable). BGH aclara que los códigos de falla son para el servicio técnico especializado y que no intentes repararlo vos. Ante un código de falla, llamá al service oficial o a un técnico matriculado.</div>
<p>Si ves <span class="code">E1</span>, <span class="code">E5</span>, <span class="code">EC</span> u otro código, buscá tu modelo en las tablas de abajo.</p>
<h2>El mismo código cambia según el modelo</h2>
<p>Ojo: un mismo código no significa lo mismo en todos los BGH. Por ejemplo, <span class="code">E1</span> es "EEPROM averiada" en los Silent Air WCCR/WFCR y "fallo del sensor de temperatura de ambiente interior" en los WCEW. Fijate el modelo en la etiqueta de la unidad interior antes de buscar el código.</p>
<h2>Códigos de falla: BGH Silent Air WCCR / WFCR (modelos 2600 a 5300 frigorías)</h2>
<table>
<tr><th>Visor</th><th>Luz de operación</th><th>Falla según el manual</th></tr>
<tr><td class="code">E1</td><td>Titila 1 vez</td><td>Error placa electrónica: EEPROM averiada</td></tr>
<tr><td class="code">E2</td><td>Titila 2 veces</td><td>Error placa electrónica: el chip principal no detecta el paso de cero de la señal</td></tr>
<tr><td class="code">E3</td><td>Titila 3 veces</td><td>Error placa ventilación: el ventilador no funciona correctamente</td></tr>
<tr><td class="code">E4</td><td>Titila 4 veces</td><td>No aplica</td></tr>
<tr><td class="code">E5</td><td>Titila 5 veces</td><td>Sensor de temperatura ambiente abierto o en corto</td></tr>
<tr><td class="code">E6</td><td>Titila 6 veces</td><td>Sensor de temperatura de caño abierto o en corto</td></tr>
<tr><td class="code">EC</td><td>Titila 2 veces (luz de timer encendida)</td><td>Error de refrigerante: fuga de refrigerante</td></tr>
</table>
<p>En el modelo de 5500 frigorías, el mismo manual suma <span class="code">E7</span> (sensor de caño de la unidad exterior abierto o en corto, titila 7 veces) y <span class="code">E9</span> (no hay comunicación entre las unidades, titila 9 veces).</p>
<h2>Códigos de falla: BGH WCEW y BSI106WCAW</h2>
<table>
<tr><th>Visor</th><th>Falla según el manual</th></tr>
<tr><td class="code">E1</td><td>Fallo del sensor de temperatura de ambiente interior</td></tr>
<tr><td class="code">E2</td><td>Fallo del sensor de temperatura de tubo interior</td></tr>
<tr><td class="code">E3</td><td>Fallo del sensor de temperatura de tubo exterior</td></tr>
<tr><td class="code">E4</td><td>Fuga o fallo del sistema de refrigerante</td></tr>
<tr><td class="code">E6</td><td>Mal funcionamiento del motor del ventilador interior</td></tr>
<tr><td class="code">E7</td><td>Fallo del sensor de temperatura de ambiente exterior</td></tr>
<tr><td class="code">E0</td><td>Fallo de comunicación interior y exterior</td></tr>
<tr><td class="code">E8</td><td>Fallo del sensor de temperatura de descarga exterior</td></tr>
<tr><td class="code">E9</td><td>Fallo del módulo IPM exterior</td></tr>
<tr><td class="code">EA</td><td>Fallo de detección de corriente exterior</td></tr>
<tr><td class="code">EE</td><td>Fallo de PCB EEPROM exterior</td></tr>
<tr><td class="code">EF</td><td>Fallo del motor del ventilador exterior</td></tr>
<tr><td class="code">EH</td><td>Fallo del sensor de temperatura de succión exterior</td></tr>
</table>
<h2>Service oficial BGH</h2>
<p>Servicio técnico de Climatización (según <a href="{AYUDA}" rel="nofollow">bgh.com.ar/institucional/ayuda</a> y los manuales): <strong>0810-222-1244</strong>. Otras marcas: <a href="/servicio-tecnico-drean/">service oficial Drean</a>.</p>
<p class="src"><strong>Fuentes (manuales oficiales en portal.bgh.com.ar):</strong><br>
<a href="{WCCR}" rel="nofollow">Manual BGH Silent Air On/Off BS26/35/53 WFCR y BS26/35/52/65 WCCR (MAR23)</a>: display "cF" (pág. 6) y códigos de fallas (sección 7).<br>
<a href="{WCEW}" rel="nofollow">Manual BGH On/Off BS26/35/52/65 WCEW (SEP25)</a>: display y códigos de fallas (sección 7).<br>
<a href="{BSI}" rel="nofollow">Manual BGH BSI106WCAW</a>: códigos de fallas unidad interior (sección 7).</p>''',
crumb='Aire BGH error CF',pub=P0,mod=M,faq=[
('¿Qué significa CF en un aire BGH?','En los manuales BGH Silent Air WCCR/WFCR y WCEW, cF no es una falla: indica que la función Hot Start está activa en calefacción, y el ventilador interior arranca cuando el radiador está caliente.'),
('¿Qué significa dF en el display?','En esos mismos manuales, dF indica descongelamiento (DEFROST).'),
('¿Qué significa E1 en un aire BGH?','Depende del modelo: en los Silent Air WCCR/WFCR es "EEPROM averiada" y en los WCEW es "fallo del sensor de temperatura de ambiente interior".'),
('¿Qué significa EC en un aire BGH?','En los Silent Air WCCR/WFCR, EC es error de refrigerante: fuga de refrigerante. Es trabajo del service.'),
('¿Puedo arreglar el código de falla yo?','No. BGH aclara que los códigos de falla son para el servicio técnico especializado y que no intentes repararlo vos.'),
('¿Cuál es el teléfono del service BGH?','El servicio técnico de Climatización de BGH es el 0810-222-1244, según bgh.com.ar.')])
