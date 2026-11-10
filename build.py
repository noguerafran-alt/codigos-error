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
    h=f'''<!doctype html><html lang="es-AR"><head>
  <meta name="google-site-verification" content="DpjskLy1H_29-NI7YUvKYSNKFsn-YUInQMvW47vc6ts" /><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
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
P0='2026-10-23'; M='2026-10-27'; N='2026-11-03'
C505='https://drean.com.ar/medias/Manual-Concept-5.05.pdf?context=bWFzdGVyfGltYWdlc3w5MDc1ODh8YXBwbGljYXRpb24vcGRmfGFHTmtMMmc0T1M4eE1UUTRNamt3TmpNMk1UZzROaTlOWVc1MVlXd3RRMjl1WTJWd2RDMDFMakExTG5Ca1pnfDA2MmRkZmYyNTIwZjRjMjZlNGI0MTJlNWVhMDU0OTg3MTI0N2Q2ZGNiMWJkMzRlNjRjODMzOWNkNzFkZDA2YjM'
C505B='https://blog.drean.com.ar/manual-de-lavarropas-drean-concept-505v1/'

page('','Códigos de error de lavarropas y aires acondicionados (Drean, Longvie, BGH)',
'Guía independiente de códigos de error de lavarropas Drean, Longvie y Whirlpool y aires BGH, transcriptos de los manuales oficiales con la fuente enlazada.',
'''<h1>Códigos de error de electrodomésticos en Argentina</h1>
<p>Qué significa cada código según el <strong>manual oficial</strong> del fabricante, qué podés revisar vos sin riesgo y cuándo llamar al service. Cada página enlaza el manual del que sale la información. Si un código no está en el manual, lo decimos.</p>
<h2>Lavarropas</h2>
<ul class="cards">
<li><a href="/drean-next-error-6/">Drean Next error 6 (Er 6, E6) y códigos de error del manual</a></li>
<li><a href="/longvie-lavarropas-error-e03/">Longvie lavarropas error 3 (E03): no desagota, y tabla de errores</a></li>
<li><a href="/longvie-lavarropas-error-e20/">Longvie lavarropas error E20: qué dice el manual oficial</a></li>
<li><a href="/drean-gold-eco-codigos-de-error/">Drean Gold Eco: tabla de códigos de error (Err 1 a Err 9) y destellos</a></li>
<li><a href="/drean-lcfdr-clr-fltr-codigos-de-error/">Drean LCFDR: qué significan CLR FLTR, E2 y E4, y tabla de códigos</a></li>
<li><a href="/whirlpool-wcs60zb-codigos-de-error/">Whirlpool WCS60ZB: qué significan FA, F09, Fod y «limpie la bomba»</a></li>
</ul>
<h2>Repuestos y fallas comunes</h2>
<ul class="cards">
<li><a href="/drean-concept-5-05-v1-bomba-de-desagote/">Drean Concept 5.05 V1 no desagota: ¿es la bomba de desagote?</a></li>
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
<p>El foco de esta página es el error 6. Para ubicarlo, este es el resumen de la lista de errores del manual. Si tu lavarropas no es un Next, la tabla es otra: <a href="/drean-gold-eco-codigos-de-error/">códigos del Gold Eco, que es otra línea</a>, o <a href="/drean-lcfdr-clr-fltr-codigos-de-error/">CLR FLTR, E2 y E4 de los LCFDR SB/LB (otra línea Drean)</a>.</p>
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
crumb='Drean Next error 6',pub=P0,mod='2026-11-10',faq=[
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
<li>El <strong>código de error</strong> que muestra el equipo. Si es un Drean Next, buscalo en la <a href="/drean-next-error-6/">tabla de códigos del Drean Next</a>; si es un Gold Eco, en la <a href="/drean-gold-eco-codigos-de-error/">tabla del Drean Gold Eco</a>; si es un LCFDR de la línea SB/LB, en <a href="/drean-lcfdr-clr-fltr-codigos-de-error/">CLR FLTR, E2 y E4 del Drean LCFDR</a>; si es un Concept 5.05 V1 que no desagota, mirá <a href="/drean-concept-5-05-v1-bomba-de-desagote/">qué revisar antes de cambiar la bomba</a>.</li>
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
<tr><td>Whirlpool</td><td>0800-666-6266, según whirlpool.com.ar. Ver <a href="/whirlpool-wcs60zb-codigos-de-error/">códigos del Whirlpool WCS60ZB</a>.</td></tr>
</table>
<div class="box warn">Desconfiá de "services oficiales" que no figuran en la web de la marca. Antes de dejar entrar a alguien o pagar, verificá el canal en drean.com.ar.</div>
<p class="src"><strong>Fuentes (oficiales, drean.com.ar, revisadas el 27/10/2026):</strong><br>
<a href="{DST}" rel="nofollow">Servicio Drean: servicio técnico especializado</a> (canales, horario y 90 días de garantía en reparaciones).<br>
<a href="{DFAQ}" rel="nofollow">Preguntas frecuentes Drean</a> (garantía de 12 meses, factura y pedido de manuales).<br>
<a href="{DEXP}" rel="nofollow">Servicio express Drean</a> (solo Capital Federal).</p>''',
crumb='Servicio técnico Drean',pub=M,mod='2026-11-10',faq=[
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

page('drean-concept-5-05-v1-bomba-de-desagote/','Bomba de desagote Drean Concept 5.05 V1: falla y repuesto',
'¿Tu Drean Concept 5.05 V1 no desagota? Qué revisar antes de culpar a la bomba, cómo buscar el repuesto compatible y cuándo llamar al service.',
f'''<h1>Bomba de desagote del Drean Concept 5.05 V1: cómo saber si falla y qué repuesto buscar</h1>
<div class="box"><strong>Respuesta corta:</strong> si tu Drean Concept 5.05 V1 no desagota, antes de comprar una bomba revisá lo que indica el manual oficial: que la <strong>manguera de desagote</strong> no esté doblada ni obstruida, que esté colocada a una altura de <strong>entre 70 y 90 cm</strong> del piso y que no tenga una prolongación. Si el lavarropas sigue sin desagotar, que el service confirme si es la bomba. Recién ahí buscá el repuesto.</div>
<div class="box warn">Agua y 220 V: desenchufá el lavarropas y cerrá la canilla antes de tocar nada. La bomba es una pieza eléctrica dentro del gabinete: no lo abras. Según el manual, la manipulación interna la tiene que hacer el service oficial para conservar la garantía.</div>
<h2>Síntomas de que el problema está en el desagote</h2>
<p>El agua queda en la cuba, no centrifuga o el lavarropas se detiene con agua. El Concept 5.05 V1 no tiene display con números: avisa las fallas con combinaciones de luces (LED) del panel. Según la tabla "Detección de averías" del manual:</p>
<table>
<tr><th>Luces encendidas</th><th>Posibles causas (manual Drean)</th><th>Qué indica el manual</th></tr>
<tr><td class="code">Algodón EEE + Plancha fácil + 1/2 Carga</td><td>Manguera de desagote obstruida o mal ubicada</td><td>Al presionar Inicio, intenta la operación de nuevo. Para salir del modo error, mantené apretado Encendido/Apagado.</td></tr>
<tr><td class="code">ECO Rápido + Plancha fácil + 1/2 Carga</td><td>Pérdida de agua o mala ubicación de la manguera de desagote</td><td>No se puede reiniciar. Para salir del modo error, mantené apretado Encendido/Apagado.</td></tr>
<tr><td class="code">Algodón + Plancha fácil + 1/2 Carga</td><td>Sin agua o grifo cerrado, caudal deficiente, electroválvula tapada o que no funciona</td><td>Es un problema de carga de agua, no de desagote.</td></tr>
<tr><td class="code">Lana + Plancha fácil + 1/2 Carga</td><td>Problemas en el sensor de nivel de agua</td><td>No se puede reiniciar. Para salir, mantené apretado Encendido/Apagado.</td></tr>
<tr><td class="code">Enjuague / Centrifugado + Plancha fácil + 1/2 Carga</td><td>Tapa abierta o mal cerrada</td><td>Cerrar la tapa.</td></tr>
</table>
<p>El manual pide no desenchufarlo ni apagarlo antes de leer la tabla, anotar qué luces viste y, si después de revisar las causas el problema sigue, llamar al Servicio de Asistencia Técnica.</p>
<h3>¿Tenés activada la función Plancha fácil?</h3>
<p>No es una falla: con <strong>Plancha fácil</strong> activada, el lavarropas se detiene con el agua del último enjuague y deja titilando las luces de Plancha fácil y Centrifugado. Según el manual, si presionás Inicio/Pausa desagota sin centrifugar, y si presionás el selector Antiarrugas sigue con el desagote y el centrifugado.</p>
<h2>Qué revisar antes de comprar una bomba</h2>
<p>Con el equipo desenchufado, revisá lo que el manual indica para la manguera de descarga:</p>
<ul>
<li>Que no quede doblada en ángulo: eso provoca una obstrucción.</li>
<li>Que esté entre <strong>70 y 90 cm</strong> de altura respecto del piso.</li>
<li>Que el conducto de desagüe tenga más diámetro que la manguera (mínimo 4 cm), para evitar el efecto sifón.</li>
<li>Que no tenga una manguera de prolongación: el manual dice que no se use.</li>
<li>Si va a una pileta, que esté sujeta de manera estable.</li>
</ul>
<h3>¿Dónde está el filtro del Concept 5.05 V1?</h3>
<p>El manual describe un <strong>filtro de pelusas ubicado en el recirculador de agua</strong>, dentro de la cuba: se retira destrabándolo desde arriba, se le sacan las pelusas, se lava bajo la canilla y se vuelve a colocar. El manual recomienda revisarlo y limpiarlo de forma periódica. No describe un filtro de bomba que se abra desde afuera, así que no abras el gabinete para buscarlo.</p>
<h2>Cuándo puede ser la bomba (y quién lo confirma)</h2>
<p>Si la manguera está bien ubicada, sin dobleces, y la falla de desagote sigue, el manual indica llamar al Servicio de Asistencia Técnica. No hagas diagnóstico casero con tester: la bomba está conectada a 220 V dentro del gabinete. Que un técnico confirme que es la bomba antes de comprar un repuesto.</p>
<h2>Qué bomba de desagote es compatible con el Concept 5.05 V1</h2>
<p>El manual oficial <strong>no indica el código ni la marca de la bomba</strong>, y Drean no lo publica en su sitio. Por eso no te vamos a recomendar un modelo. Según <a href="{DST}" rel="nofollow">drean.com.ar/servicio_tecnico</a>, el service oficial trabaja con repuestos genuinos y da 90 días de garantía en sus reparaciones. Si igual vas a comprar el repuesto por tu cuenta, antes chequeá:</p>
<ul>
<li>El modelo exacto, tal como figura en la placa de características (en la parte trasera del producto, según el manual).</li>
<li>Que la tensión sea la del equipo: el manual indica 220 V - 50 Hz.</li>
<li>Que la forma de fijación y el conector sean iguales a los de la pieza original.</li>
<li>Si es original o alternativa: pedile al vendedor que confirme la compatibilidad con tu modelo exacto.</li>
</ul>
<h2>¿La cambio yo o llamo al service?</h2>
<ul>
<li><strong>Vos:</strong> revisar la manguera de desagote y limpiar el filtro de pelusas, como indica el manual.</li>
<li><strong>Service:</strong> si el equipo está en garantía (no lo abras), para cambiar la bomba, y si la bomba arranca sola al enchufar, salta la térmica o hay olor a quemado.</li>
</ul>
<h2>La bomba no para nunca (está siempre prendida)</h2>
<p>El manual no cubre ese caso. Si la bomba arranca sola al enchufar el lavarropas, no compres repuestos: llamá al service.</p>
<h2>Service oficial Drean</h2>
<p>Teléfonos que figuran en el manual: <strong>CABA y GBA (011) 5246-8663</strong> e <strong>interior 0800-345-6580</strong>. WhatsApp, horarios y garantía, en <a href="/servicio-tecnico-drean/">servicio técnico oficial Drean</a>. Otros códigos de la marca: <a href="/drean-next-error-6/">códigos de error Drean Next</a>. Si tenés un Longvie que no desagota: <a href="/longvie-lavarropas-error-e03/">Longvie error 3</a>.</p>
<p class="src"><strong>Fuentes (oficiales, Drean):</strong><br>
<a href="{C505}" rel="nofollow">Manual de instrucciones Drean Concept 5.05 V1 (drean.com.ar)</a>: instalación de la manguera de descarga (pág. 6 y 7), Plancha fácil (pág. 10), limpieza del filtro de pelusas (pág. 14), medidas de seguridad (pág. 15), detección de averías (pág. 18) y certificado de garantía (pág. 21).<br>
<a href="{C505B}" rel="nofollow">Manual de Lavarropas Drean Concept 505v1 (blog.drean.com.ar)</a>.<br>
<a href="{DST}" rel="nofollow">Servicio técnico Drean</a> (repuestos genuinos y 90 días de garantía en reparaciones).</p>''',
crumb='Drean Concept 5.05 V1: bomba de desagote',pub=N,mod=N,faq=[
('¿Cómo sé si la bomba de desagote de mi Drean Concept está rota?','Primero descartá la manguera: según el manual, tiene que estar sin dobleces, a entre 70 y 90 cm del piso y sin prolongación. Si sigue sin desagotar, el manual indica llamar al service, que es quien confirma si es la bomba.'),
('¿Qué luces muestra el Concept 5.05 V1 cuando no desagota?','Según el manual, Algodón EEE + Plancha fácil + 1/2 Carga indican manguera de desagote obstruida o mal ubicada. Al presionar Inicio intenta de nuevo.'),
('¿Qué bomba lleva el Drean Concept 5.05 V1?','El manual oficial no indica el código ni la marca de la bomba. Consultalo con el service oficial de Drean, que trabaja con repuestos genuinos.'),
('¿Sirve una bomba Emicol para el Drean Concept 5.05 V1?','No lo podemos confirmar: Drean no publica qué bomba lleva el equipo. La compatibilidad tiene que confirmarla el vendedor o el service con tu modelo exacto.'),
('¿Puedo cambiar la bomba yo?','No conviene. Es una pieza eléctrica dentro del gabinete y, según el manual, la manipulación interna la tiene que hacer el service oficial para tener derecho a la garantía.'),
('¿Por qué la bomba del lavarropas no para nunca?','El manual no cubre ese caso. Si la bomba arranca sola al enchufar, no compres repuestos: llamá al service.'),
('¿Dónde está el filtro del Drean Concept 5.05 V1?','El manual describe un filtro de pelusas en el recirculador de agua, dentro de la cuba: se saca destrabándolo desde arriba, se lava bajo la canilla y se vuelve a poner.'),
('¿Si está en garantía, me cambian la bomba gratis?','El certificado del manual da 12 meses de garantía desde la compra para reparar o reponer piezas con defectos de fabricación, sin cargo. Se anula, entre otros casos, si el equipo fue intervenido por personal ajeno al service autorizado.')])

# ---- 2026-11-10: briefs del 09/11 (Gold Eco, LCFDR SB/LB, Whirlpool WCS60ZB)
D='2026-11-10'
GOLD='https://drean.com.ar/medias/Manual-Lavarropas-Gold-Drean.pdf?context=bWFzdGVyfGltYWdlc3wzMDYwNTg4fGFwcGxpY2F0aW9uL3BkZnxhRE5tTDJnM1l5OHhNVFE0TWprd05qYzFOVEV3TWk5TllXNTFZV3d0VEdGMllYSnliM0JoY3kxSGIyeGtMVVJ5WldGdUxuQmtaZ3w4NzY1OWYwYWU2MjlkM2QwZjU5OTMyYTEzY2RlZWM0MGI5NjNjYzJkNGUwMTdjYTExNDExZTZlZGUzZTA0N2Fm'
GOLDB='https://blog.drean.com.ar/manual-de-lavarropas-drean-gold/'
LTDR='https://drean.com.ar/medias/Manual-lavarropas-Drean-LTDR0610PB0.pdf?context=bWFzdGVyfGltYWdlc3wzMDYxMTM2fGFwcGxpY2F0aW9uL3BkZnxhR0k0TDJnME5DOHhNakE0T0RZek16UTFPRGN4T0M5TllXNTFZV3d0YkdGMllYSnliM0JoY3kxRWNtVmhiaTFNVkVSU01EWXhNRkJDTUM1d1pHWXxhMzFjZDMyOGMzMzhjYmIwNmJiNDI2ODVjMjcxMDU4Y2Y0MDI4NWU3MzA2NjY5YjhjOWY3NzEyY2Y4NTU1YjY1'
LCF='https://drean.com.ar/medias/Manual-LCFDR0610LB1.pdf?context=bWFzdGVyfGltYWdlc3wyMzQxOTQyfGFwcGxpY2F0aW9uL3BkZnxhR0ZsTDJoak55OHhNelF4TnpReU16WTJOekl6TUM5TllXNTFZV3d0VEVOR1JGSXdOakV3VEVJeExuQmtaZ3wzNGY2Zjc4MzJmMGQyNDNjNjY1MzA1OTc3MDE0ZDY2ZmZjZjA5YWI1ZGY2YWMyOWE3MmM5MGVhNjhhNGE3YjYy'
WCS='https://descargas.whirlpool.com.ar/Lavado/Lavarropas/WCS60ZB/WCS60ZB_manual_usuario.pdf'
WST='https://www.whirlpool.com.ar/servicio-tecnico'
WAC='https://www.whirlpool.com.ar/atencion-clientes'

page('drean-gold-eco-codigos-de-error/','Códigos de error Drean Gold Eco: Err 1 a 9 y destellos',
'Qué significa cada código del lavarropas Drean Gold Eco según el manual oficial: Err 1 a Err 9, destellos, qué revisar vos y cuándo llamar al service.',
f'''<h1>Drean Gold Eco: tabla de códigos de error (Err 1 a Err 9) y destellos</h1>
<div class="box"><strong>Respuesta corta:</strong> en el Drean Gold Eco el error se ve como <span class="code">Err 1</span> a <span class="code">Err 9</span> en el display (modelos 10·8 SI, 10·8 y 10.6) o como destellos de los 3 LEDs de funciones (modelo 8·6). Según el manual oficial (pág. 21), solo Err 1 (bomba), Err 2 (carga de agua) y Err 5 (puerta) tienen una revisión que podés hacer vos. Para el resto, llamá al service.</div>
<div class="box warn">Agua y 220 V: desenchufá el lavarropas y cerrá la canilla antes de revisar filtros o mangueras. Al abrir el filtro sale agua (puede estar caliente si el ciclo fue en caliente): poné trapos y un recipiente. No abras el gabinete ni la placa: según el manual, la manipulación interna la tiene que hacer el service oficial para tener derecho a la garantía.</div>
<h2>Cómo saber qué modelo tenés y cómo muestra el error</h2>
<p>Este manual cubre los <strong>Gold Eco 10·8 SI, 10·8, 10.6 y 8·6</strong>. Fijate el modelo en la etiqueta del equipo (el manual no describe dónde está pegada). Si tu lavarropas es un Next, los códigos son otros: <a href="/drean-next-error-6/">si tu lavarropas es un Next (Er 6 / E6), esta es la página</a>.</p>
<h3>10·8 SI, 10·8 y 10.6</h3>
<p>El display muestra <span class="code">Err 1</span> a <span class="code">Err 9</span>. Si hay demasiada espuma, muestra <span class="code">o o</span>.</p>
<h3>8·6 (sin "Err" en el display)</h3>
<p>El número de error es la <strong>cantidad de destellos de los 3 LEDs de los pulsadores de funciones</strong>: 5 destellos = error 5. La espuma se indica con un destello escalonado en los 3 LEDs de velocidad de centrifugado. En foros el 8·6 aparece como "Gold Blue 8.6": si la etiqueta dice 8·6, esta tabla aplica. El manual no nombra la variante "Gold Blue", así que no la generalices a otros modelos.</p>
<h2>Tabla de códigos Drean Gold Eco (manual oficial, pág. 21)</h2>
<table>
<tr><th>Cómo se ve</th><th>Qué significa (manual Drean)</th><th>¿Vos o service?</th></tr>
<tr><td class="code">Err 1 / 1 destello</td><td>Bomba bloqueada</td><td>Vos: limpiar el filtro (pág. 16). Si sigue, service.</td></tr>
<tr><td class="code">Err 2 / 2 destellos</td><td>Tiempo de carga de agua excedido o electroválvula defectuosa</td><td>Vos: revisar la presión de la conexión hidráulica. Si sigue, service.</td></tr>
<tr><td class="code">Err 3 / 3 destellos</td><td>Error de resistencia</td><td>Service.</td></tr>
<tr><td class="code">Err 4 / 4 destellos</td><td>Sensor de temperatura (NTC)</td><td>Service.</td></tr>
<tr><td class="code">Err 5 / 5 destellos</td><td>Error de puerta</td><td>Vos: cerrar bien la puerta. Si sigue, service.</td></tr>
<tr><td class="code">Err 6 / 6 destellos</td><td>Motor bloqueado / Protector abierto / Tacómetro abierto</td><td>Service.</td></tr>
<tr><td class="code">Err 7 / 7 destellos</td><td>Error de overflow</td><td>Service.</td></tr>
<tr><td class="code">Err 8 / 8 destellos</td><td>Triac cortocircuitado</td><td>Service.</td></tr>
<tr><td class="code">Err 9 / 9 destellos</td><td>Relé de alimentación de resistencia dañado</td><td>Service.</td></tr>
<tr><td class="code">Destello escalonado en los 3 LEDs de funciones</td><td>Tensión de alimentación fuera de rango (admisible entre 180 V y 245 V)</td><td>Service.</td></tr>
<tr><td class="code">o o (8·6: destello escalonado en los LEDs de centrifugado)</td><td>Generación excesiva de espuma</td><td>Vos: dejar que siga el programa y revisar la dosis de jabón la próxima vez.</td></tr>
</table>
<p>Ojo: en el Gold Eco el manual no distingue 6A, 6B o 6C como en el Next. No mezcles las tablas de las dos líneas.</p>
<h2>Qué podés revisar vos sin riesgo</h2>
<h3>Err 1 / 1 destello (bomba bloqueada)</h3>
<p>El manual indica revisar y limpiar el filtro de la electrobomba de desagote (pág. 16):</p>
<ol>
<li>Desenchufá el lavarropas.</li>
<li>Poné un recipiente para recoger el agua.</li>
<li>Retirá el zócalo.</li>
<li>Desenroscá el filtro y tirá hacia afuera.</li>
<li>Sacá el filtro y limpialo.</li>
<li>Volvé a colocarlo repitiendo los pasos en orden inverso.</li>
</ol>
<p>Además, para "no descarga agua o no centrifuga" (pág. 19), el manual pide comprobar que la manguera de desagote no esté estrangulada ni taponada y que esté bien instalada. El manual recomienda limpiar este filtro cada 100 lavados aproximadamente.</p>
<h3>Err 2 / 2 destellos (carga de agua)</h3>
<p>El manual indica revisar que la conexión hidráulica tenga la presión adecuada. Para "no carga agua" (pág. 19) suma: canilla bien abierta, filtro de ingreso de agua sin obstruir y manguera de entrada sin estrangular. Para limpiar el filtro de ingreso (pág. 16): desenchufá, cerrá la llave de agua, desenroscá la manguera de entrada en la parte posterior, sacá el filtro con una pinza de punta plana, limpialo y volvé a conectar la manguera.</p>
<h3>Err 5 / 5 destellos (error de puerta)</h3>
<p>Según el manual: controlá que la puerta esté bien cerrada y cerrala de nuevo; el error desaparece y el lavarropas empieza el lavado. Si continúa, service.</p>
<h3>Espuma ("o o" o destello escalonado en los LEDs de centrifugado)</h3>
<p>El manual dice que dejes que siga el programa: va a hacer un enjuague adicional. En los próximos lavados revisá la dosis de jabón.</p>
<h2>Destello escalonado en los 3 LEDs de funciones</h2>
<p>Indica tensión de alimentación fuera de rango (el rango admisible es de 180 V a 245 V). El manual indica comunicarse con el Servicio de Asistencia Técnica y no trae un reset. Tené en cuenta que el certificado de garantía excluye los daños por excesos o caídas de tensión eléctrica.</p>
<h2>Cuándo llamar al service</h2>
<ul>
<li><strong>Vos:</strong> Err 1, Err 2, Err 5 y el aviso de espuma, solo con las acciones del manual.</li>
<li><strong>Service:</strong> Err 3, 4, 6, 7, 8, 9, tensión fuera de rango, y cualquier código que vuelva después de la revisión.</li>
</ul>
<p>Teléfonos, WhatsApp y horarios: <a href="/servicio-tecnico-drean/">servicio técnico oficial Drean</a>. Si el problema es de desagote en otro modelo: <a href="/drean-concept-5-05-v1-bomba-de-desagote/">Drean Concept 5.05 V1 que no desagota</a>. Otra línea Drean con display: <a href="/drean-lcfdr-clr-fltr-codigos-de-error/">Drean LCFDR (CLR FLTR, E2, E4)</a>.</p>
<h2>¿Y si el modelo de la etiqueta es LTDR0810, LTDR0610 o LTDR0608?</h2>
<p>El <a href="{LTDR}" rel="nofollow">manual oficial de los LTDR0810PI0, LTDR0810PB0, LTDR0610PB0 y LTDR0608PB0</a> trae la misma tabla en su pág. 21: Err 1 a Err 9 en el display de los LTDR0810 y LTDR0610, y destellos en el LTDR0608PB0. Podés usar esta misma tabla.</p>''' + f'''
<p class="src"><strong>Fuentes (oficiales, Drean, revisadas el 10/11/2026):</strong><br>
<a href="{GOLD}" rel="nofollow">Manual de instrucciones Lavarropas Gold Eco 10.8 SI, 10.8, 10.6 y 8.6 (drean.com.ar)</a>: limpieza de filtros (pág. 16), medidas de seguridad (pág. 18), causas y posibles soluciones (pág. 19), listado de errores (pág. 21) y certificado de garantía (pág. 22 y 23).<br>
<a href="{GOLDB}" rel="nofollow">Manual de uso Lavarropas Drean Gold (blog.drean.com.ar)</a>.<br>
<a href="{LTDR}" rel="nofollow">Manual Lavarropas Drean LTDR0810PI0, LTDR0810PB0, LTDR0610PB0, LTDR0608PB0 (drean.com.ar)</a>: listado de errores (pág. 21).<br>
<a href="{DST}" rel="nofollow">Servicio técnico Drean</a>.</p>''',
crumb='Drean Gold Eco: códigos de error',pub=D,mod=D,faq=[
('¿Qué significa Err 1 en un Drean Gold Eco?','Según el manual oficial, Err 1 (o 1 destello en el 8·6) es bomba bloqueada. Revisá y limpiá el filtro de la electrobomba de desagote con el equipo desenchufado; si sigue, llamá al service.'),
('¿Qué es el error 5 / Err 5 del Gold (error de puerta)?','Es error de puerta. El manual indica controlar que la puerta esté bien cerrada y cerrarla de nuevo: el error desaparece y el lavado comienza. Si continúa, service.'),
('¿Cómo se lee el error en el Gold 8.6, que parpadea con 3 luces?','En el 8·6 el número de error es la cantidad de destellos de los 3 LEDs de los pulsadores de funciones. Por ejemplo, 5 destellos equivalen a Err 5 (error de puerta).'),
('¿Qué significa Err 6 en el Gold Eco?','Según el manual: motor bloqueado, protector abierto o tacómetro abierto. El manual indica comunicarse con el Servicio de Asistencia Técnica.'),
('¿El Gold Blue 8.6 usa esta tabla?','Si la etiqueta del equipo dice 8·6, sí: es uno de los modelos del manual Gold Eco. El manual no nombra la variante comercial "Gold Blue", así que confirmá el modelo en la etiqueta.'),
('¿A qué teléfono llamo?','Al service oficial de Drean: los canales están en nuestra página de servicio técnico Drean. El certificado del manual da 12 meses de garantía desde la compra y se anula, entre otros casos, si el equipo fue intervenido por personal ajeno al service autorizado.')])

page('drean-lcfdr-clr-fltr-codigos-de-error/','Códigos de error Drean LCFDR: CLR FLTR, E2 y E4',
'¿Tu Drean LCFDR muestra CLR FLTR, E2 o E4? Qué dice el manual oficial, qué revisar vos sin riesgo y cuándo llamar al service. Solo línea SB/LB.',
f'''<h1>Drean LCFDR: qué significan CLR FLTR, E2 y E4, y tabla de códigos</h1>
<div class="box"><strong>Respuesta corta:</strong> en los Drean LCFDR de la línea SB/LB, el display puede mostrar CLR FLTR, E2, E4, E8, F3, F4, F7, FA o FC0 a FC2. Según el manual oficial (pág. 24), <span class="code">CLR FLTR</span> es un error de drenaje: limpiá el filtro de la bomba y revisá la manguera. <span class="code">E2</span> es error de bloqueo: cerrá bien la puerta. <span class="code">E4</span> es que no llega el nivel de agua: revisá grifo, presión y mangueras. El resto va al service.</div>
<div class="box warn">Esta tabla es solo para los modelos SB/LB del manual citado. Si tu equipo es un Next o un LCFDR…TG, no copies estos significados. Antes de tocar nada, desenchufá el lavarropas y cerrá la canilla; al abrir el filtro queda agua (puede estar caliente). No abras el gabinete ni la placa.</div>
<h2>Cómo saber si este manual es el tuyo</h2>
<p>El manual cubre estos modelos: <strong>LCFDR0608LB1, LCFDR0610LB1, LCFDR0710SB1, LCFDR0814SB1, LCFDR0814SG1 y LCFDR1012SB1</strong>. Fijate el modelo en la etiqueta del equipo (el manual no describe dónde está pegada). El LCFDR1012TG tiene otro manual oficial con otra tabla (ERROR 1, 6A, 6B, 6C), parecida a la del Next: <a href="/drean-next-error-6/">si tu modelo es un Next, los códigos son Er / E, no CLR FLTR</a>.</p>
<h2>Qué significa CLR FLTR</h2>
<p>Según la pág. 24 del manual: <strong>"Error de drenaje, el agua no se drena completamente en 6 min."</strong> La solución oficial: limpiar el filtro de la bomba y verificar la instalación de la manguera de drenaje. Los pasos del filtro están más abajo.</p>
<h2>E2 y E4</h2>
<h3>E2, error de bloqueo</h3>
<p>El manual indica: "Cierre bien la puerta." Si sigue, service.</p>
<h3>E4, no se alcanza el nivel de agua</h3>
<p>Según el manual, revisá que:</p>
<ul>
<li>El grifo esté completamente abierto y la presión de agua sea normal.</li>
<li>La manguera de entrada no esté doblada ni obstruida.</li>
<li>El filtro de la entrada de agua al producto no esté obstruido.</li>
<li>La manguera de desagote esté bien instalada y no esté haciendo sifón.</li>
</ul>
<h2>Tabla completa de códigos de pantalla (manual oficial, pág. 24)</h2>
<table>
<tr><th>Código</th><th>Qué indica el manual</th><th>¿Vos o service?</th></tr>
<tr><td class="code">CLR FLTR</td><td>Error de drenaje: el agua no se drena completamente en 6 min. Limpiar el filtro de la bomba y verificar la manguera de drenaje.</td><td>Vos; si sigue, service.</td></tr>
<tr><td class="code">E2</td><td>Error de bloqueo. Cerrar bien la puerta.</td><td>Vos; si sigue, service.</td></tr>
<tr><td class="code">E4</td><td>No se alcanza el nivel de agua. Grifo, presión, manguera de entrada, filtro de entrada y manguera de desagote sin sifón.</td><td>Vos; si sigue, service.</td></tr>
<tr><td class="code">E8</td><td>Error de nivel de protección de agua.</td><td>Service.</td></tr>
<tr><td class="code">F3</td><td>Error del sensor de temperatura.</td><td>Service.</td></tr>
<tr><td class="code">F4</td><td>Error de calentamiento.</td><td>Service.</td></tr>
<tr><td class="code">F7</td><td>Error del motor.</td><td>Service.</td></tr>
<tr><td class="code">FA</td><td>Error del sensor de nivel de agua.</td><td>Service.</td></tr>
<tr><td class="code">FC0, FC1, FC2</td><td>Error de comunicación anormal.</td><td>Service.</td></tr>
</table>
<p>Ojo: <a href="/whirlpool-wcs60zb-codigos-de-error/">FA en un Whirlpool WCS60ZB no significa lo mismo</a> (allá es error de desagüe).</p>
<p>La misma pág. 24 lista "códigos de información" del ciclo: tiempo restante, inicio diferido, bloqueo para niños, lavado terminado, puerta trabada por nivel o temperatura del agua o centrifugado, y medición de la carga. <strong>No son errores</strong>: el manual dice "No es necesario realizar ninguna acción."</p>
<h2>Problemas sin código en el display (pág. 25)</h2>
<table>
<tr><th>Problema</th><th>Qué revisar según el manual</th></tr>
<tr><td>No funciona</td><td>Que el programa esté iniciado, la puerta bien cerrada, la máquina encendida, que haya energía y que no esté activado el bloqueo para niños.</td></tr>
<tr><td>No se llena de agua</td><td>Grifo, manguera de entrada sin doblar, filtro de la manguera de entrada, presión del agua (no menos de 0,04 MPa) y puerta bien cerrada.</td></tr>
<tr><td>Se vacía mientras carga</td><td>Manguera de drenaje a no menos de 70 cm de altura y con el extremo fuera del agua.</td></tr>
<tr><td>Falla de drenaje</td><td>Manguera de drenaje sin bloquear, filtro de la bomba limpio y extremo de la manguera a no más de 90 cm.</td></tr>
</table>
<h2>Qué podés revisar vos</h2>
<p>El manual empieza el apartado de cuidado y limpieza con: "Desenchufe el lavarropas antes de realizar cualquier tarea de mantenimiento."</p>
<h3>Filtro de la electrobomba de desagote (pág. 19)</h3>
<ol>
<li>Abrí la tapa con un elemento plástico para no dañar la pintura.</li>
<li>Antes de desenroscar, poné una bandeja y/o un trapo debajo: queda agua en el filtro.</li>
<li>Desenroscá la tapa en sentido antihorario hasta liberarla.</li>
<li>Sacá el conjunto tapa-rejilla y limpialo.</li>
<li>Volvé a colocarlo enroscando en sentido horario hasta el tope. Asegurate de que la tapa quede bien ajustada para evitar pérdidas de agua.</li>
</ol>
<p>El manual recomienda limpiar este filtro cada 100 lavados aproximadamente.</p>
<h3>Filtro de ingreso de agua (pág. 19)</h3>
<ol>
<li>Cerrá la llave de agua.</li>
<li>Desenroscá la manguera de entrada de la parte posterior del lavarropas.</li>
<li>Sacá el filtro con una pinza de punta plana y limpialo.</li>
<li>Volvé a conectar la manguera haciendo lo mismo a la inversa.</li>
</ol>
<h2>Cuándo llamar al service</h2>
<ul>
<li><strong>Vos:</strong> CLR FLTR, E2 y E4, solo con las revisiones del manual, y las comprobaciones sin código que no exigen abrir el gabinete.</li>
<li><strong>Service:</strong> E8, F3, F4, F7, FA, FC0 a FC2, y cualquier código que vuelva después de la revisión.</li>
</ul>
<p>Canales del service: <a href="/servicio-tecnico-drean/">servicio técnico oficial Drean</a>. Otras líneas Drean: <a href="/drean-gold-eco-codigos-de-error/">tabla del Gold Eco (otra línea)</a>. Problemas de desagote en otro modelo: <a href="/drean-concept-5-05-v1-bomba-de-desagote/">Drean Concept 5.05 V1</a>.</p>
<p class="src"><strong>Fuentes (oficiales, Drean, revisadas el 10/11/2026):</strong><br>
<a href="{LCF}" rel="nofollow">Manual de instrucciones Lavarropas LCFDR0608LB1, LCFDR0610LB1, LCFDR0710SB1, LCFDR0814SB1, LCFDR0814SG1 y LCFDR1012SB1 (drean.com.ar)</a>: cuidado y limpieza (pág. 19), códigos de información y de pantalla (pág. 24), problemas sin código (pág. 25) y certificado de garantía (desde la pág. 26).<br>
<a href="{DST}" rel="nofollow">Servicio técnico Drean</a>.</p>''',
crumb='Drean LCFDR: CLR FLTR, E2 y E4',pub=D,mod=D,faq=[
('¿Qué significa CLR FLTR en un lavarropas Drean LCFDR?','Según el manual oficial de la línea SB/LB, es un error de drenaje: el agua no se drena completamente en 6 minutos. Hay que limpiar el filtro de la bomba y verificar la instalación de la manguera de drenaje.'),
('¿Qué es el error E2?','En estos modelos, E2 es error de bloqueo. El manual indica cerrar bien la puerta. Si sigue, service.'),
('¿Qué significa E4?','Que no se alcanza el nivel de agua. El manual pide revisar que el grifo esté abierto con presión normal, la manguera de entrada, el filtro de entrada y que la manguera de desagote no haga sifón. Este significado vale solo para los modelos de este manual.'),
('¿Qué hago si aparece F7 o FA?','F7 es error del motor y FA es error del sensor de nivel de agua. Para los dos, el manual indica contactar al servicio de postventa.'),
('¿Esta tabla sirve para un Drean Next o para un LCFDR…TG?','No. El Next y el LCFDR1012TG tienen otros manuales y otra tabla de códigos.'),
('¿Cuál es el teléfono del service Drean?','Los canales oficiales están en nuestra página de servicio técnico Drean. El certificado del manual da 12 meses de garantía desde la compra y se anula, entre otros casos, si el equipo fue intervenido por personal ajeno al service autorizado.')])

page('whirlpool-wcs60zb-codigos-de-error/','Whirlpool WCS60ZB: error FA, F09, Fod y limpie la bomba',
'Qué significan FA, F09, Fod, «válvula cerrada» y «limpie la bomba» en el Whirlpool WCS60ZB, según el manual oficial, y cuándo llamar al service.',
f'''<h1>Whirlpool WCS60ZB: qué significan FA, F09, Fod y «limpie la bomba»</h1>
<div class="box"><strong>Respuesta corta:</strong> en el Whirlpool WCS60ZB, según el manual oficial argentino (pág. 11 y 17), «válvula cerrada» es falta de entrada de agua y «limpie la bomba» es que no puede vaciar: revisá tubo y filtro. <span class="code">FA</span> es error de desagüe. <span class="code">F09</span> es nivel de agua demasiado alto. <span class="code">Fod</span> es exceso de espuma. <span class="code">F02</span> a <span class="code">F35</span>, salvo F09, son error de módulo eléctrico. Esta tabla vale solo para este modelo.</div>
<div class="box warn">Los códigos de Whirlpool cambian según el modelo y el país. Esta página transcribe el manual del WCS60ZB: no la uses para otro modelo. F05 o F06, si aparecieran en este equipo, caen en el grupo F02 a F35 (excepto F09) de este manual; en otros Whirlpool pueden significar otra cosa. Agua y 220 V: apagá y desconectá el lavarropas antes de limpiar el filtro, y no abras el gabinete. Según el manual, las reparaciones las tiene que hacer un técnico cualificado.</div>
<h2>Cómo confirmar que es un WCS60ZB</h2>
<p>El manual se titula "Manual de usuario - Modelo: WCS60ZB". Al llamar al service, el manual (pág. 18) pide el tipo y el modelo exacto del aparato y el número de service de la placa. El manual no describe con una frase dónde está pegada esa etiqueta. Podés descargar el <a href="{WCS}" rel="nofollow">manual oficial en descargas.whirlpool.com.ar</a>.</p>
<h2>Indicadores del panel (pág. 11)</h2>
<ul>
<li><strong>Válvula cerrada:</strong> ausencia de entrada de agua o entrada insuficiente.</li>
<li><strong>Limpie la bomba:</strong> no puede vaciarse el agua; el filtro de agua puede estar obstruido.</li>
<li><strong>Asistencia:</strong> llame al Servicio Postventa. Consultá la resolución de problemas y, si el indicador sigue encendido, llamá.</li>
</ul>
<h2>Códigos en pantalla (pág. 17, "Descripción de los indicadores de error")</h2>
<table>
<tr><th>Indicación</th><th>Qué indica el manual</th><th>¿Vos o service?</th></tr>
<tr><td class="code">Válvula cerrada</td><td>Ausencia de entrada de agua o entrada insuficiente.</td><td>Vos; si se repite, service.</td></tr>
<tr><td class="code">Limpie la bomba</td><td>El agua residual no se descarga; el filtro puede estar obstruido.</td><td>Vos; si se repite, service.</td></tr>
<tr><td class="code">bdd</td><td>Solapas del tambor abiertas: el aparato se para.</td><td>Vos; si persiste, service.</td></tr>
<tr><td class="code">F02 a F35 (excepto F09)</td><td>Error de módulo eléctrico.</td><td>Pulsar Cancelar/Vaciado 3 s; si persiste, service.</td></tr>
<tr><td class="code">F09</td><td>Nivel de agua demasiado alto (después de cancelar un programa o de un funcionamiento fallido).</td><td>Pulsar Cancelar/Vaciado 3 s; si persiste, service.</td></tr>
<tr><td class="code">FA</td><td>Error de desagüe.</td><td>Vos los pasos del manual; service si el agua entra sola o el error sigue.</td></tr>
<tr><td class="code">Fod</td><td>Exceso de espuma: se interrumpió el programa.</td><td>Vos; si persiste, service.</td></tr>
</table>
<p>Ojo: <a href="/drean-lcfdr-clr-fltr-codigos-de-error/">FA en un Drean LCFDR significa otra cosa</a> (sensor de nivel de agua).</p>
<h2>Qué podés revisar vos</h2>
<h3>Válvula cerrada</h3>
<p>Según el manual, comprobá que:</p>
<ul>
<li>El grifo esté completamente abierto y la presión de agua sea suficiente.</li>
<li>La manguera de entrada no esté doblada.</li>
<li>El filtro de malla de la manguera de suministro no esté obstruido.</li>
<li>La manguera no esté congelada.</li>
<li>Si tu manguera de suministro tiene ventana de inspección en la válvula de seguridad, que no esté roja. Si está roja, el manual indica sustituir la manguera a través del Servicio Postventa o del distribuidor autorizado.</li>
</ul>
<p>Después, reiniciá el programa con «Inicio/Pausa». Si se repite, service.</p>
<h3>Limpie la bomba</h3>
<p>Desconectá el lavarropas y comprobá que el tubo de desagüe no esté doblado ni congelado y que el filtro o la bomba no estén obstruidos (limpieza del filtro, abajo). Esperá a que el agua se haya enfriado antes de drenar. Después, pulsá «Cancelar/Vaciado» al menos 3 segundos para vaciar el agua. Si se repite, service.</p>
<h3>FA (error de desagüe)</h3>
<ol>
<li>Apagá el aparato, desenchufalo y cerrá el grifo.</li>
<li>Inclinalo con cuidado hacia delante para que salga el agua acumulada por la parte inferior.</li>
<li>Volvé a enchufarlo.</li>
<li>Abrí el grifo. Si el agua entra enseguida sin que hayas iniciado el aparato, hay un error: cerrá el grifo y avisá al Servicio Postventa.</li>
<li>Volvé a seleccionar e iniciar el programa.</li>
</ol>
<h3>Cómo limpiar el filtro de agua y drenar el agua residual (pág. 14)</h3>
<ol>
<li>Apagá y desconectá el lavarropas. Si usaste un programa de agua caliente, esperá a que el agua se enfríe.</li>
<li>Abrí la cubierta del filtro con una moneda.</li>
<li>Poné un recipiente bajo y ancho debajo del filtro.</li>
<li>Girá el filtro despacio en sentido antihorario, sin sacarlo, hasta que salga el agua. Cuando el recipiente se llene, cerrá el filtro en sentido horario, vacialo y repetí hasta que no salga más.</li>
<li>Poné un paño de algodón debajo y sacá el filtro girándolo hacia la izquierda.</li>
<li>Limpiá los residuos y lavalo con agua corriente.</li>
<li>Volvé a ponerlo girando en sentido horario hasta el tope, con el agarre en vertical. Echá aproximadamente un litro de agua por el tambor, comprobá que no pierda por el filtro y cerrá la cubierta.</li>
</ol>
<p>El manual pide limpiar el filtro a menudo, sobre todo si el aparato no se vacía bien o no centrifuga bien.</p>
<h3>Fod (exceso de espuma)</h3>
<p>Seleccioná e iniciá el programa «Aclarado + Centrifugado». Después, volvé a iniciar el programa que querías usando menos detergente.</p>
<h3>bdd (solapas del tambor abiertas)</h3>
<p>Pulsá «Cancelar/Vaciado» al menos 3 segundos y esperá a que se encienda el indicador de «Puerta abierta». Abrí la tapa, cerrá las solapas del tambor y volvé a seleccionar e iniciar el programa. Si persiste, service.</p>
<h3>F09 y F02 a F35</h3>
<p>Pulsá «Cancelar/Vaciado» al menos 3 segundos. Si el error persiste, el manual indica desconectar el aparato, cerrar el grifo y contactar al Servicio Postventa.</p>
<h2>Cuándo llamar al service Whirlpool Argentina</h2>
<p>Antes de llamar, el manual (pág. 18) pide probar las recomendaciones de resolución de problemas y apagar y volver a encender el aparato. Llamá si el error persiste después de eso, si en un FA el agua entra sola al abrir el grifo, si hay que cambiar la manguera con ventana roja o para cualquier reparación interna. El manual dice que no hagas reparaciones ni sustituciones que no estén indicadas en él.</p>
<p>Según <a href="{WST}" rel="nofollow">whirlpool.com.ar/servicio-tecnico</a>, la línea gratuita de atención al consumidor es el <strong>0800-666-6266</strong>. Sobre el horario, el sitio oficial muestra dos datos distintos: "Lunes a Viernes de 9 a 18hs" en <a href="{WAC}" rel="nofollow">Atención al Cliente</a> y "Lunes a Sábado de 9 a 19 hs." en el pie de página; confirmalo al llamar. La garantía figura en la cartilla que viene con el equipo; el manual no la transcribe. El manual también menciona whirlpool.eu: para Argentina, usá los canales de whirlpool.com.ar.</p>
<p>Otros errores de desagote: <a href="/longvie-lavarropas-error-e03/">errores de desagote en Longvie</a>. Service de otras marcas: <a href="/servicio-tecnico-drean/">servicio técnico Drean</a>.</p>
<p class="src"><strong>Fuentes (oficiales, Whirlpool Argentina, revisadas el 10/11/2026):</strong><br>
<a href="{WCS}" rel="nofollow">Manual de usuario Whirlpool WCS60ZB (descargas.whirlpool.com.ar)</a>: guía de seguridad, indicadores (pág. 11), limpieza del filtro de agua (pág. 14), resolución de problemas (pág. 16), descripción de los indicadores de error (pág. 17) y servicio postventa (pág. 18).<br>
<a href="{WST}" rel="nofollow">Servicio técnico oficial Whirlpool Argentina</a> y <a href="{WAC}" rel="nofollow">Atención al Cliente Whirlpool Argentina</a> (0800-666-6266 y horarios).</p>''',
crumb='Whirlpool WCS60ZB: códigos de error',pub=D,mod=D,faq=[
('¿Qué significa FA en el Whirlpool WCS60ZB?','Según el manual oficial, FA es error de desagüe. No lo confundas con el FA del Drean LCFDR, que es el sensor de nivel de agua.'),
('¿Qué es el aviso «limpie la bomba»?','Que el agua no puede vaciarse; el filtro puede estar obstruido. Desconectá el aparato, revisá el tubo de desagüe y el filtro (con el agua fría) y pulsá Cancelar/Vaciado al menos 3 segundos.'),
('¿Qué significan F09 y Fod?','F09 es nivel de agua demasiado alto y Fod es exceso de espuma. Para F09 el manual indica pulsar Cancelar/Vaciado 3 segundos; para Fod, hacer un Aclarado + Centrifugado y volver a lavar con menos detergente.'),
('¿Qué hago si aparece un código F02, F05 o F35?','En el WCS60ZB, de F02 a F35 (excepto F09) es error de módulo eléctrico. Pulsá Cancelar/Vaciado al menos 3 segundos; si sigue, llamá al service. No uses significados de otros modelos o países.'),
('¿Esta tabla sirve para cualquier lavarropas Whirlpool?','No. Es solo del WCS60ZB. Otros manuales de Whirlpool Argentina no traen esta tabla o la tienen distinta.'),
('¿Cuál es el teléfono del service Whirlpool en Argentina?','Según whirlpool.com.ar, la línea gratuita es el 0800-666-6266. El sitio muestra dos horarios distintos (lunes a viernes de 9 a 18 y lunes a sábado de 9 a 19), así que confirmalo al llamar.')])
