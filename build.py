import os
B="https://codigos-error.onrender.com"
FOOT='''<footer><p><strong>Guía independiente.</strong> Este sitio no está afiliado, patrocinado ni avalado por Drean, Longvie, Whirlpool, BGH ni ninguna otra marca. Los nombres y marcas pertenecen a sus dueños. La información se transcribe de manuales oficiales enlazados en cada página; ante cualquier duda, manda el manual de tu modelo y el service oficial.</p><p>Si el equipo tiene riesgo eléctrico o de gas, no lo abras: llamá a un técnico matriculado o al service oficial.</p><p>Última revisión: 23/10/2026.</p></footer>'''
def page(path,title,desc,body,back=True):
    hdr='<a href="/">← Códigos de error · guía independiente</a>' if back else '<a href="/">Códigos de error · guía independiente</a>'
    html=f'''<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{B}/{path}"><link rel="stylesheet" href="/style.css"></head><body>
<header>{hdr}</header>
<main>
{body}
</main>
{FOOT}
</body></html>
'''
    d=path.rstrip('/') or '.'
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w').write(html)

ECO='https://drean.com.ar/medias/Manual-Drean-Next-ECO-LFDRI0710SB0.pdf?context=bWFzdGVyfGltYWdlc3wxODg4NDUyfGFwcGxpY2F0aW9uL3BkZnxhRFU0TDJnM01pOHhNakU0TnpnNE1EUXlNelExTkM5TllXNTFZV3d0UkhKbFlXNHRUbVY0ZEMxRlEwOHRURVpFVWtrd056RXdVMEl3TG5Ca1pnfDY5Zjk2NTllMmIyZWZjNTU1YmY5NDE4Y2VjYjE5ZDc0ODdiMzFlMWMzNmFkODU4MDk2ZjM0ZDM4Zjg3OTMyNjY'
TOUCH='https://drean.com.ar/medias/Manual-Drean-Next-Touch-ECO.pdf?context=bWFzdGVyfGltYWdlc3wyNDU4MDY5fGFwcGxpY2F0aW9uL3BkZnxhREJtTDJnNE15OHhNVFE0TWprd05qVTFPRFE1TkM5TllXNTFZV3d0UkhKbFlXNHRUbVY0ZEMxVWIzVmphQzFGUTA4dWNHUm18NDMxY2EyN2Y0ZDQ4OWQxN2UwZmVmZmM4ZjU4YjMzMzA0ZDBjMjhiZjcxYmJiNDY5Y2YyNTA0YjMxNDkxYjg4YQ'
LV='https://longvie-gestion.appsinnovategroup.com/api/uploads/7494468/13280-V6.pdf'
WCCR='https://portal.bgh.com.ar/wp-content/uploads/2023/07/UM-BGH-Minisplit-OnOff-BS_WCCR-ES-MAR23.pdf'
WCEW='https://portal.bgh.com.ar/wp-content/uploads/2025/10/UM-BGH-Minisplit-OnOff-WCEW-ES-SEP25.pdf'
BSI='https://portal.bgh.com.ar/wp-content/uploads/2026/06/Manual-BSI106WCAW-1.pdf'
AYUDA='https://www.bgh.com.ar/institucional/ayuda'

page('','Códigos de error de lavarropas y aires acondicionados (Drean, Longvie, BGH)',
'Guía independiente de códigos de error de lavarropas Drean y Longvie y aires acondicionados BGH, transcriptos de los manuales oficiales con la fuente enlazada.',
'''<h1>Códigos de error de electrodomésticos en Argentina</h1>
<p>Qué significa cada código según el <strong>manual oficial</strong> del fabricante, qué podés revisar vos sin riesgo y cuándo llamar al service. Cada página enlaza el manual del que sale la información. Si un código no está en el manual, lo decimos.</p>
<h2>Lavarropas</h2>
<ul class="cards">
<li><a href="/drean-next-codigos-de-error/">Drean Next: tabla de códigos de error (Er 1 a Er 11, error 6)</a></li>
<li><a href="/longvie-lavarropas-error-e20/">Longvie lavarropas error E20: qué dice el manual oficial</a></li>
</ul>
<h2>Aire acondicionado</h2>
<ul class="cards">
<li><a href="/bgh-aire-acondicionado-codigos-de-error/">Aire acondicionado BGH: qué significa "CF" y tabla de códigos de error</a></li>
</ul>''',back=False)

page('drean-next-codigos-de-error/','Drean Next error 6 (Er 6 / E6): tabla de códigos de error del manual',
'Qué significa el error 6 del lavarropas Drean Next (Er 6, E6A, E6b, E6C) y la tabla completa de códigos Er 1 a Er 11 según el manual oficial de Drean.',
f'''<h1>Drean Next: error 6 y tabla de códigos de error</h1>
<div class="box"><strong>Respuesta corta:</strong> en el Drean Next, el <span class="code">Er 6</span> (o <span class="code">E6</span>, y en algunos modelos <span class="code">Er 6A</span>, <span class="code">Er 6b</span>, <span class="code">Er 6C</span>) significa <strong>"problema en el motor de lavado"</strong>. Para este código el manual oficial indica <strong>llamar al Servicio Técnico</strong>; no trae una solución casera.</div>
<div class="box warn">El motor y la placa funcionan con 220 V. No desarmes el lavarropas: desenchufalo y llamá al service oficial o a un técnico matriculado.</div>
<h2>Cómo se muestra el error según tu modelo</h2>
<ul>
<li><strong>Next con display (perilla):</strong> 10·12, 8·14, 8·12, LFDRI0710SB y 7·10 muestran <span class="code">Er</span> + número. En 10·12P y 8·14 el error 6 aparece como <span class="code">Er 6A</span>, <span class="code">Er 6b</span> o <span class="code">Er 6C</span>.</li>
<li><strong>Next sin display (con LEDs):</strong> 8·10, 7·09, 6·09, 6·08 y 6·06 indican el error con la cantidad de destellos de las 3 luces de los botones de función (por ejemplo, 6 destellos = error 6). Un <em>destello escalonado</em> indica tensión fuera de rango.</li>
<li><strong>Next Touch ECO (WiFi):</strong> 10·12 WCR/WCRG ECO y 8·14 WCR/WCRG ECO muestran <span class="code">E1</span> a <span class="code">E11</span> (E6A/E6B/E6C para el motor).</li>
</ul>
<h2>Tabla de códigos de error Drean Next (según manual oficial)</h2>
<table>
<tr><th>Código</th><th>Significado (manual Drean)</th><th>Qué indica hacer el manual</th></tr>
<tr><td class="code">Er 1 / E1</td><td>Circuito de desagüe obstruido</td><td>Revisar el filtro y la manguera de desagote y limpiarlos. Si continúa, llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 2 / E2</td><td>Tiempo de carga de agua excedido</td><td>Verificar presión de agua, que el grifo esté abierto, el filtro de entrada y la instalación de la manguera de desagote. Si continúa, Servicio Técnico.</td></tr>
<tr><td class="code">Er 3 / E3</td><td>Resistencia de calentamiento averiada</td><td>Llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 4 / E4</td><td>Problema en el sensor de temperatura</td><td>Llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 5 / E5</td><td>Error de puerta</td><td>Llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 6 / E6 (6A, 6b, 6C)</td><td>Problema en el motor de lavado</td><td>Llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 7 / E7</td><td>Sobrenivel de agua</td><td>Llamar al Servicio Técnico.</td></tr>
<tr><td class="code">Er 8 / E8</td><td>Falla en el control del motor</td><td>Reiniciar el ciclo. Si continúa, Servicio Técnico.</td></tr>
<tr><td class="code">Er 9 / E9</td><td>Sobrecalentamiento del agua</td><td>Verificar que el lavarropas no esté conectado a agua caliente. Si continúa, Servicio Técnico.</td></tr>
<tr><td class="code">E10</td><td>Tensión fuera de rango (figura en el manual Next Touch ECO)</td><td>—</td></tr>
<tr><td class="code">Er 11 / E11</td><td>Error en el circuito de medición de nivel</td><td>Llamar al Servicio Técnico.</td></tr>
</table>
<h2>Qué podés revisar vos sin riesgo</h2>
<p>Solo para los errores en los que el manual sugiere una revisión (1, 2, 8 y 9): con el equipo <strong>desenchufado</strong>, revisá que el grifo esté abierto, que las mangueras no estén dobladas y que los filtros de entrada y de desagote estén limpios. Para el resto de los códigos, incluido el 6, el manual deriva al service.</p>
<h2>Service oficial Drean</h2>
<p>Teléfonos que figuran en los manuales oficiales: <strong>CABA y GBA (011) 5246-8663</strong> · <strong>Interior 0800-345-6580</strong>.</p>
<p class="src"><strong>Fuentes (manuales oficiales en drean.com.ar):</strong><br>
<a href="{ECO}" rel="nofollow">Manual Drean Next ECO (perilla): 10.12, 8.14, 8.12, 8.10, LFDRI0710SB, 7.10, 7.09, 6.09, 6.08, 6.06</a>, códigos de error (pág. 25).<br>
<a href="{TOUCH}" rel="nofollow">Manual Drean Next Touch ECO (WiFi): 10·12 y 8·14 WCR/WCRG ECO</a>, lista de errores (pág. 27 del manual).</p>''')

page('longvie-lavarropas-error-e20/','Longvie lavarropas error E20: qué dice el manual oficial',
'¿Tu lavarropas Longvie marca E20? Revisamos el manual oficial: E20 no figura. Acá está la tabla de errores que sí trae el manual (2, 3, 4 y service) y qué revisar.',
f'''<h1>Longvie lavarropas error E20: qué dice el manual oficial</h1>
<div class="box"><strong>Respuesta honesta:</strong> el código <span class="code">E20</span> <strong>no figura en el manual oficial</strong> de Longvie que revisamos (lavarropas L16508, L16510, L18010, L18012/C/P y lavasecarropas LS18012/C/P, edición 02-2026). No vamos a inventarle un significado. Si tu equipo muestra E20, anotá el modelo exacto (está en la etiqueta del equipo) y consultá al service oficial de Longvie.</div>
<div class="box warn">Un lavarropas combina agua y 220 V. Antes de tocar cualquier cosa, desenchufalo. No abras paneles ni la placa: eso es trabajo del service oficial o de un técnico matriculado.</div>
<h2>Códigos de error que sí trae el manual Longvie</h2>
<table>
<tr><th>Error Nº</th><th>Qué indica el manual</th></tr>
<tr><td class="code">2</td><td>No se llena de agua. Revisar que el grifo esté abierto, que el selector esté bien posicionado y que el filtro de la electroválvula no esté tapado.</td></tr>
<tr><td class="code">3</td><td>No descarga el agua. Revisar que el tubo de desagote no esté doblado y que no haya cuerpos extraños en el filtro de la bomba.</td></tr>
<tr><td class="code">4</td><td>Demasiada agua. Cerrar la llave del agua y llamar al service.</td></tr>
<tr><td class="code">0, 1, 5, 7, 8, 9</td><td>Dirigirse al Servicio de Asistencia Técnica.</td></tr>
<tr><td class="code">E20</td><td><strong>No figura en el manual.</strong></td></tr>
</table>
<h2>Limpieza del filtro de la bomba (según el manual)</h2>
<ol>
<li>Desenchufá el lavarropas y cerrá la canilla de agua.</li>
<li>Tené a mano un trapo y un recipiente bajo: va a salir agua.</li>
<li>Abrí la tapa inferior del frente.</li>
<li>Girá el filtro en sentido antihorario para sacarlo y limpialo.</li>
<li>Volvé a colocarlo girando en sentido horario y cerrá la tapa.</li>
</ol>
<h2>Service oficial Longvie</h2>
<p>Dato que figura en el manual oficial: <strong>Laprida 4851 (1603) Villa Martelli, Buenos Aires · Tel. (011) 4709-8501</strong>.</p>
<p class="src"><strong>Fuente:</strong> <a href="{LV}" rel="nofollow">Manual oficial Longvie 13280-V6 (L16508, L16510, L18010, L18012, LS18012)</a>, sección "Posibles causas de desperfectos". Si tu modelo es otro, buscá su manual en el sitio de Longvie: la tabla puede ser distinta.</p>''')

page('bgh-aire-acondicionado-codigos-de-error/','Aire acondicionado BGH error CF: qué significa y tabla de códigos',
'¿Tu aire BGH muestra CF? Según el manual oficial no es una falla: indica la función Hot Start en calefacción. Además, tabla de códigos de error E1, E0, EC y más.',
f'''<h1>Aire acondicionado BGH: qué significa "CF" y tabla de códigos de error</h1>
<div class="box"><strong>Respuesta corta:</strong> en los splits BGH cuyo manual lo describe, <span class="code">cF</span> en el display <strong>no es un código de falla</strong>: se muestra cuando la función <strong>Hot Start</strong> se activa en modo calefacción. El ventilador interior arranca recién cuando el radiador está lo suficientemente caliente, para no tirar aire frío al ambiente. Es normal que dure unos minutos al encender en calor.</div>
<p>Esto figura en la sección "Display" de los manuales oficiales BGH Silent Air BS26/35/52/53/65 WCCR-WFCR y BS26/35/52/65 WCEW. En esos mismos manuales, <span class="code">dF</span> indica descongelamiento (DEFROST), <span class="code">SC</span> autolimpieza (opcional) y <span class="code">FP</span> calefacción de 8 °C (opcional). Si tu modelo es otro, revisá su manual: no todos los equipos usan los mismos indicadores.</p>
<div class="box warn">El aire acondicionado trabaja con 220 V y gas refrigerante a presión (en modelos R32, inflamable). BGH aclara que los códigos de falla son para el servicio técnico especializado y que no intentes repararlo vos. Ante un código de falla, llamá al service oficial o a un técnico matriculado.</div>
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
<p>Servicio técnico de Climatización (según <a href="{AYUDA}" rel="nofollow">bgh.com.ar/institucional/ayuda</a> y los manuales): <strong>0810-222-1244</strong>.</p>
<p class="src"><strong>Fuentes (manuales oficiales en portal.bgh.com.ar):</strong><br>
<a href="{WCCR}" rel="nofollow">Manual BGH Silent Air On/Off BS26/35/53 WFCR y BS26/35/52/65 WCCR (MAR23)</a>: display "cF" (pág. 6) y códigos de fallas (sección 7).<br>
<a href="{WCEW}" rel="nofollow">Manual BGH On/Off BS26/35/52/65 WCEW (SEP25)</a>: display y códigos de fallas (sección 7).<br>
<a href="{BSI}" rel="nofollow">Manual BGH BSI106WCAW</a>: códigos de fallas unidad interior (sección 7).</p>''')
