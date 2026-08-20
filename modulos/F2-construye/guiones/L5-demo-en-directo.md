# L5 | DEMO EN DIRECTO: construye tu solución

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F2 Construye | 15-20 min | recursos/plantilla-brief-solucion.md (reutilizada de L3) |

**Objetivo:** al terminar, el alumno ha visto construir una demo completa de principio a fin —del brief a la URL en el móvil— y replica el proceso con su solución y su nicho.

## Gancho (0:00-0:20)

"En esta lección no te explico nada: construyo. Una demo completa para una clínica dental, desde una página en blanco hasta una URL funcionando en mi móvil. Y todo lo que voy a hacer lo puedes repetir esta misma tarde, sin escribir una sola línea de código."

[PANTALLA: pantalla dividida — a la izquierda, la plantilla de brief en blanco; a la derecha, el terminal con Claude Code esperando]

## Sección 1 — Las reglas de esta demo

- Marcar la lección: "Esta es LA demo del módulo. Aquí converge todo F2: el stack de L2, la dirección de L3 y la solución que elegiste en L4. Si aún no la has elegido, para el vídeo y hazlo — esta lección se trabaja, no se mira."
- El proyecto: la misma oferta que construimos en directo en F1-L7 — recuperación de citas para clínicas dentales, del catálogo "Recuperación de no-shows y citas". "En F1 escribimos la promesa. Hoy construimos la prueba."
- Anunciar qué vamos a levantar, para que lo reconozcas al verlo nacer: un panel simple con las citas de la clínica, un simulador visual del flujo de mensajes que recupera una cita caída, y datos de ejemplo del nicho. Recuerda la distinción de L4: esto es DEMO, no piloto — el flujo de WhatsApp se simula dentro de la web; las integraciones reales llegan en F5, con un cliente pagando.
- Cómo trabajar el vídeo: yo construyo con mi nicho; tú pausas en cada paso y replicas con el tuyo.

## Sección 2 — Paso 1: el brief, los dos minutos que lo deciden todo

[DEMO: rellenar la plantilla de brief en pantalla, en directo y sin cortes — objetivo: unos 2 minutos]

- Lo que se rellena es EL ejemplo de `recursos/plantilla-brief-solucion.md`, TAL CUAL está escrito — los 7 comportamientos observables completos, los contadores de "citas recuperadas" y "facturación recuperada" y el botón "reiniciar demo" incluidos. A cámara se recorre campo a campo pensando en voz alta, pero de la lista solo se leen los 3 comportamientos más ilustrativos:
  - **Contexto:** "Mi cliente es una clínica dental de barrio — la llamaré Clínica Dental Ensanche, inventada pero verosímil. Su dolor: citas que se caen y nadie recupera."
  - **Qué debe hacer** (los 3 que se leen en voz alta): 1) un panel con las citas del día y su estado; 2) cuando una cita pasa a "cancelada", se abre la conversación que la recupera en un simulador con aspecto de WhatsApp; 3) cuando el paciente acepta, la cita vuelve a la agenda en su hueco nuevo.
  - **Qué NO entra:** WhatsApp real, pagos, cuentas de usuario — el mismo alcance acotado que definiste en tu piloto de F1.
  - **Datos de ejemplo y aspecto:** pacientes y tratamientos creíbles; diseño limpio, que se vea bien en móvil.
- Insistir en la regla de oro de L3: "describe QUÉ debe pasar y PARA QUIÉN. Cómo programarlo no es asunto tuyo."

## Sección 3 — Paso 2: Claude Code construye y tú diriges

[DEMO: pegar el brief completo en Claude Code con una orden en lenguaje natural: "Construye una web siguiendo este brief. Cuando termines, dime cómo verla en mi navegador." Comentar en voz alta lo que va ocurriendo mientras construye]

- Narrar sin dramatismo lo que se ve en pantalla: lee el brief, propone un plan, crea los archivos, avisa cuando hay algo que mirar. "Tu trabajo ahora es exactamente este: leer lo que te cuenta y decidir. Eso es dirigir. Fíjate en que yo no toco el código en ningún momento."
- Gestionar la expectativa: esto tarda minutos, no segundos. "Una agencia tradicional te presupuestaría esto en semanas. Tú vas a protestar porque tarda cinco minutos. Ponlo en perspectiva."

[PANTALLA: la primera versión abierta en el navegador — el panel de citas existe, todavía con datos genéricos]

## Sección 4 — Paso 3: el primer fallo, y por qué es buena noticia

[DEMO: probar la primera versión buscando el fallo A PROPÓSITO — por ejemplo, cancelar una cita y que el simulador no se abra, o que aparezca un error visible en pantalla. Plan B si nada falla a la primera: prueba un caso que el brief no cubre —marca dos citas como canceladas a la vez, o pulsa "reiniciar demo" en mitad del flujo— hasta provocar un comportamiento roto; o pide una mejora deliberadamente ambigua y usa el resultado inesperado como el fallo]

- Probarla delante del alumno hasta que algo se rompa. Y celebrarlo: "Esto no es un tropiezo. Esto es EL método. Hipótesis, prueba, dato, ajuste — el mismo ciclo que firmaste en F0."
- Enseñar el gesto exacto: copiar el error tal cual —el mensaje rojo, el pantallazo, lo que sea— y pegárselo a Claude Code con una frase: "Al cancelar una cita pasa esto: [error pegado]. Arréglalo."
- Lo que NO se hace (los errores del no-técnico de L3): pelearte con el error, intentar descifrarlo tú, o aprovechar el arreglo para colar tres cambios más. Una petición = un cambio, y se prueba antes de pedir el siguiente.

## Sección 5 — Paso 4: dos mejoras pequeñas, no veinte

[DEMO: iteración 1 — datos realistas. Pedirle: "Sustituye los datos de ejemplo por pacientes y tratamientos verosímiles de una clínica dental española: limpiezas, endodoncias, revisiones, ortodoncia. Nombres y apellidos normales, citas de esta semana." Probar el resultado antes de seguir]

[DEMO: iteración 2 — un toque visual. Pedirle: "Dale aspecto de producto: colores sobrios de clínica, el nombre Clínica Dental Ensanche en la cabecera y estados de cita con color — verde confirmada, rojo cancelada, azul recuperada." Probar el resultado]

- La lección detrás de cada mejora: los datos realistas son los que harán que un dentista se reconozca — "'Cliente 1' no vende; 'endodoncia, jueves a las 18:30' sí" —, y el toque visual separa "un experimento" de "un producto".
- Y freno: dos mejoras y paramos. "Tu demo no es tu obra maestra, es tu herramienta de venta. Simple y entregada gana a compleja y eterna — siempre."

## Sección 6 — Paso 5: deploy y prueba de fuego en el móvil

[DEMO: pedir el deploy en lenguaje natural: "Publica esta web en internet con su URL pública, igual que el hola mundo de L2." Abrir la URL en el móvil, a cámara, y recorrer el flujo entero: cita cancelada → conversación del simulador → cita recuperada en el panel]

[PANTALLA: el móvil en mano — la conversación del simulador recuperando la cita, mensaje a mensaje, y la cita reapareciendo en la agenda]

- El momento: "Esta URL abre en cualquier parte: en una llamada, en la consulta del dentista, en su propio móvil mientras te mira. Esto es lo que en F1 llamamos 'no me creas: míralo funcionar'."

## Sección 7 — Ahora tú, con permiso para que salga regular

- La réplica: mismo proceso, mismos cinco pasos, con TU solución —la que promete tu oferta V1, la que elegiste en L4— y TU nicho. Brief → construir → romper y arreglar → dos mejoras → deploy.
- Permiso explícito para la imperfección: "Te saldrá peor que a mí a la primera. A mí también me pasó: mi tercera demo fue la primera decente. Las dos anteriores cumplieron su función, que era enseñarme a dirigir." `[PRUEBA SOCIAL: experiencia real de Agustín — validar antes de grabar]`
- El atajo del programa: las plantillas AILINK — repos base (proyectos ya montados) por tipo de solución, para clonar y personalizar con Claude Code en vez de partir de cero. Mencionarlas como acelerador, sin entrar en detalle. `[PLANTILLAS AILINK: referenciar sin detallar — pendientes de construir]`
- El estándar de hoy: fea pero funcionando y en una URL. "En L6 la blindamos para que no falle delante de nadie, y en L7 la vestimos para vender."

## Cierre + CTA

- Recap en 2 frases: "Has visto el ciclo completo cinco veces más rápido de lo que crees que es posible: brief de dos minutos, construcción dirigida, un fallo convertido en método, dos mejoras con freno y una URL que abre en el móvil. Ese ciclo es tu oficio a partir de hoy."
- **Acción del alumno AHORA:** abre `recursos/plantilla-brief-solucion.md`, rellénala con tu solución y tu nicho, y ejecuta los cinco pasos hasta tener una URL que abre en tu móvil.
- **KPI de esta lección:** tu demo V1 construida y desplegada en una URL — aunque sea fea.
- Puente: "Tienes una demo que funciona cuando la usas tú. En la próxima lección vamos a intentar romperla a conciencia — porque el siguiente en usarla podría ser un cliente."
