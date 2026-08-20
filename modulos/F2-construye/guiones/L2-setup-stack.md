# L2 | Setup del stack en una tarde

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F2 Construye | 10-15 min (práctica con pantalla) | recursos/checklist-setup-stack.md |

**Objetivo:** al terminar, el alumno tiene el stack operativo: Claude Code instalado y respondiendo, cuentas de GitHub y Vercel creadas, y un "hola mundo" con el nombre de su agencia desplegado en una URL propia y publicada en la comunidad.

## Gancho (0:00-0:20)

"Hoy vas a publicar software en internet. Tú. Esta tarde. Aunque nunca hayas abierto un terminal ni sepas lo que es. De hecho, si no lo sabes, mejor: vas a comprobar en primera persona que el muro técnico que te imaginabas… no existe."

[PANTALLA: pantalla partida — a la izquierda un terminal vacío con el cursor parpadeando; a la derecha un navegador mostrando una web sencilla con el rótulo "TU AGENCIA — Soluciones de IA". Entre ambos, una flecha: "de aquí a aquí, hoy"]

## Sección 1 — El terminal no muerde

- Desactiva el miedo antes de que aparezca: el **terminal** es, simplemente, una ventana donde escribes órdenes a tu ordenador con texto en vez de con clics. Nada más.
- La parte que nadie te cuenta: no vas a aprender "comandos de terminal". Vas a usar cuatro cosas contadas — abrirlo, arrancar Claude Code, escribir en español y pegar errores. Todo lo demás lo teclea la máquina.
- Conecta con L1: tu papel es dirigir, no programar. El terminal es la puerta del despacho donde trabaja tu desarrollador: entras, das instrucciones, revisas.
- Regla de la tarde: no memorices nada. Para eso está la checklist del recurso — casilla a casilla y en una tarde estás operativo.

## Sección 2 — Las cuatro piezas de tu stack (y lo que cuestan de verdad)

[PANTALLA: diagrama de 4 cajas conectadas — Claude Code ("construye") → GitHub ("guarda") → Vercel ("publica") → Supabase ("datos, más adelante") — con el coste orientativo debajo de cada una]

- **Claude Code**: el núcleo. Tu desarrollador. Lo único con coste fijo: la suscripción de Claude, en torno a 20€/mes — consulta precios actuales antes de contratar.
- **GitHub**: donde vive tu código. Piénsalo como tu **repositorio** (o "repo"): la carpeta oficial de cada proyecto, con copia de seguridad e historial de todos los cambios. Capa gratuita de sobra para todo F2.
- **Vercel**: donde tu web se hace pública. Aquí aparece la palabra **deploy** (desplegar): publicar tu web en una URL que cualquiera puede abrir. Su capa gratuita cubre tus demos sin pagar un euro — ojo: esa capa gratuita es para uso no comercial; para enseñar demos a clientes y ponerla en tu funnel revisa sus condiciones actuales, porque es probable que te toque su plan de pago (coste orientativo, consúltalo).
- **Supabase**: la base de datos, para más adelante. Hoy ni la tocas.
- Coste de arranque: una suscripción y tres cuentas gratuitas. "Una agencia tradicional necesita nóminas para construir software. Tú, menos de lo que cuesta una cena para dos. Esa asimetría ES el modelo AILINK."

## Sección 3 — Manos a la obra: Claude Code respondiendo

[PANTALLA: proceso completo en directo — crear la cuenta de Claude, descargar e instalar Claude Code siguiendo el instalador oficial en macOS y después en Windows, abrir el terminal y arrancarlo por primera vez]

- Paso 1 — cuenta de Claude: te registras en la web oficial de Claude y activas la suscripción. Dos minutos.
- Paso 2 — instalar Claude Code: sigue el instalador oficial para tu sistema — te enseño el camino en macOS y en Windows. Nada de tutoriales de terceros: la fuente oficial siempre está actualizada; los tutoriales, casi nunca.
- Paso 3 — primera conversación: abre el terminal, arranca Claude Code, inicia sesión con tu cuenta y escríbele tu primer **prompt** — la petición que le escribes a la IA — en español normal: preséntate y pregúntale qué puede hacer por ti. Lee la respuesta con calma. Acabas de conocer a tu desarrollador.

## Sección 4 — GitHub y Vercel: cinco minutos cada una

- Cuenta de GitHub: registro estándar con tu email. Un consejo de futuro: usa el email de tu negocio, no uno personal de hace quince años — esto es infraestructura de tu agencia.
- Cuenta de Vercel: regístrate usando tu cuenta de GitHub cuando te lo ofrezca. Así quedan conectadas desde el primer día y los despliegues fluyen solos.
- No configures nada más en ninguna de las dos. Cuentas creadas y sesión iniciada: listo. Claude Code se encargará del resto cuando llegue el momento.

## Sección 5 — Tu "hola mundo" en una URL

[PANTALLA: en el terminal, se escribe la orden en lenguaje natural; Claude Code construye la página, la sube a GitHub y la despliega en Vercel; se abre la URL final en el navegador Y en un móvil]

- La orden no es un conjuro técnico: es un brief — un encargo por escrito de lo que quieres — en español. Del estilo: "Crea una página web sencilla de una sola pantalla con el nombre de mi agencia y el texto 'Soluciones de IA para [tu nicho]', con diseño limpio y profesional. Cuando esté lista, súbela a GitHub y despliégala en Vercel para que tenga una URL pública. Si necesitas que yo haga algo, guíame paso a paso." La versión copiable está en la checklist.
- Nota cómo dirijo: describo el QUÉ y dejo el CÓMO a la máquina. En L3 convertimos esto en método.
- Claude Code te irá pidiendo permisos y algún inicio de sesión: es normal — léelo y confirma. No va más rápido quien no lee.
- Y ahora, el momento. Abre la URL en tu móvil. Mírala. **"Acabas de publicar software en internet. Hace una hora no sabías qué era un terminal."** Guarda ese momento: es la prueba, con fecha de hoy, de que la barrera técnica era mentira.

## Sección 6 — Si algo falla (bienvenido a la habilidad)

- Va a pasar. Hoy o el jueves. Un mensaje rojo, algo que no carga. Reacción del programa: cero drama, un solo movimiento — **copia el error completo y pégaselo a Claude Code con "esto ha fallado, arréglalo"**. Explicará qué pasa y lo resolverá o te dirá qué tocar.
- Si el que falla es el propio instalador y Claude Code aún no arranca, mismo gesto en otra ventanilla: pega el error en el chat de Claude del navegador.
- Caso distinto: si en plena sesión Claude Code te dice que has alcanzado el límite de uso, no es un fallo ni es culpa tuya — los planes tienen límites por franjas; el propio mensaje te dice cuándo se restablece. Si te pasa, la tarde se convierte en dos bloques; está previsto.
- Esto no es un apaño de emergencia: es EL método — el mismo bucle de probar, fallar y corregir que firmaste en F0; aquí solo cambia quién teclea. Los atascos típicos de instalación y su salida están en la checklist.

## Cierre + CTA

- Recap en 2 frases: "Cuatro piezas — Claude Code construye, GitHub guarda, Vercel publica, Supabase espera su turno — por el coste orientativo de una suscripción. Y tu primera web ya existe: la barrera técnica cayó esta misma tarde."
- **Acción del alumno AHORA:** abre `checklist-setup-stack.md`, complétala casilla a casilla de arriba abajo y no la cierres hasta la última: tu URL compartida en la comunidad.
- **KPI de esta lección:** URL del "hola mundo" desplegada y publicada en la comunidad.
- Puente: "Ya tienes el arma en la mano. En la próxima lección aprendes a apuntar: cómo escribir briefs que consiguen exactamente lo que quieres — la diferencia entre dirigir y cruzar los dedos."
