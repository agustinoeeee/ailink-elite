# F2 | Construye — Blueprint del módulo (contrato de producción)

> Semanas 3-4 del alumno. El módulo FLAGSHIP del programa: la habilidad core (construir soluciones de IA con Claude Code). Objetivo del módulo: salir con **la solución demo construida, desplegada en una URL y con guion de presentación de 3 minutos** (hito maestro fin S4) — el activo que hace innegable la oferta V1 de F1.
>
> ⚠️ MÓDULO DE CREACIÓN ORIGINAL: no hay chunk fuente (el equivalente en el curso fuente enseñaba Meta Ads; aquí la habilidad core es otra). Se hereda solo el ESQUELETO de un módulo flagship: filosofía → flujo general → componentes → build en directo → disciplina de testeo → benchmarks. Todo el contenido técnico sale de este blueprint — seguirlo con precisión.
>
> Leer también `../../01-BIBLIA.md`. El alumno llega de F1 con: nicho elegido, avatar, oferta V1 redactada y precios fijados. Puede tener CERO experiencia técnica (bandera del formulario de F0) — TODO se explica para no técnicos, sin condescendencia.

## Decisión de diseño central (borrador — validar con Agustín)

**En F2 todo es web.** La demo del alumno vive en una URL: se construye en días, se enseña en cualquier llamada y no depende de terceros. Las integraciones reales (WhatsApp Business API, telefonía) llegan en F5 con el primer piloto pagado — meterse en verificaciones de Meta Business en la semana 4 ahogaría al alumno sin necesidad: la demo web simula el flujo de WhatsApp visualmente y vende igual.

**Stack del programa (borrador):** Claude Code (núcleo) · GitHub (guardar el código) · Vercel (desplegar con URL) · Supabase (datos, cuando haga falta). Coste de arranque orientativo: la suscripción de Claude (~20€/mes, consultar precio actual) — el resto tiene capa gratuita suficiente para demos. `[STACK: pendiente de validación de Agustín — si cambia, cambia solo aquí y en L2/L4]`

**Plantillas AILINK** = el equivalente a "clonar un sistema ya montado": repos base por tipo de solución que el alumno clona y personaliza con Claude Code. `[PLANTILLAS AILINK: pendientes de construir — los guiones las referencian como recurso del programa; ver notas-fuente]`

## Reglas de estilo (heredan F0+F1 y sus auditorías)

1. Español de España, tuteo. Glosario Biblia 3.5 actualizado (lead y no-show permitidos; follow-up→seguimiento; "no aplica" prohibido). Términos técnicos nuevos SIEMPRE glosados en primera mención: repo(sitorio), deploy (desplegar/publicar), terminal, prompt.
2. Cero rastro del curso fuente. "Benchmark del programa" solo sobre cifras de Biblia/blueprint. Cifras de ejemplo → "ilustrativas". SIN cifras de precios de servicios (viven en F1); el coste del stack sí, marcado como orientativo.
3. Plantilla canónica de guion (la de F1, con "**KPI de esta lección:**" obligatorio en el cierre). SIN timestamps en títulos de sección (solo el Gancho 0:00-0:20). Mínimo 3 `[PANTALLA: …]` por guion, repartidas. 600-1.200 palabras (L5 hasta 1.500 por ser la demo).
4. Tono anti-miedo técnico constante: "no necesitas saber programar; necesitas saber DIRIGIR" — pero sin prometer magia: las cosas fallan, se itera (método de F0-L7).
5. Referencias hacia atrás sin re-explicar: la oferta V1 (F1-L8), el catálogo de soluciones (F1-R1), "una demo que falla delante del cliente = credibilidad muerta" (F0-L6, error 6), Más/Mejor/Nuevo.

## Especificación por pieza

### L1 | Tu arsenal: por qué Claude Code lo cambia todo — `guiones/L1-tu-arsenal.md` (5-8 min)
- **Objetivo:** el alumno entiende qué es Claude Code, por qué es su ventaja competitiva y cuál es su papel (director, no programador).
- **Contenido obligatorio:** (a) qué es Claude Code en lenguaje de resultado: "un desarrollador senior que trabaja para ti por [coste orientativo]/mes, no se cansa y construye en días lo que una agencia tradicional presupuesta en meses"; (b) la inversión de papeles: tú no programas — describes, revisas y decides; la máquina teclea; (c) por qué esto es LA ventaja del modelo AILINK: entregar en días permite el piloto barato y rápido que hace irresistible tu oferta (conectar con la red de seguridad de F1-L5); (d) el estándar del programa: simple y entregado > complejo y eterno (eco del error 4 de F0-L6) — tu demo no es tu obra maestra, es tu herramienta de venta; (e) mapa de F2: setup → dirigir → catálogo → construir → testear → demo vendible.
- **Recurso vinculado:** — (la acción aterriza en L2; anotar la excepción de ADN aquí en el blueprint: L1 es apertura de módulo).

### L2 | Setup del stack en una tarde — `guiones/L2-setup-stack.md` (10-15 min, práctica con pantalla)
- **Objetivo:** stack operativo: Claude Code instalado y funcionando, cuentas de GitHub/Vercel creadas, y un "hola mundo" desplegado en una URL propia.
- **Contenido obligatorio:** (a) desdramatizar el terminal: "una ventana donde escribes órdenes; usarás cuatro"; (b) pasos EN PANTALLA: cuenta de Claude → instalar Claude Code (macOS y Windows, ambos) → primera conversación → cuenta GitHub (glosar: "donde vive tu código, tu copia de seguridad") → cuenta Vercel (glosar deploy: "publicar tu web en una URL") → pedirle a Claude Code un "hola mundo" con el nombre de su agencia y desplegarlo; (c) momento psicológico clave: "acabas de publicar software en internet. Hace una hora no sabías qué era un terminal"; (d) costes honestos del stack (orientativos, marcar "consulta precios actuales"); (e) resolución de atascos: qué hacer si algo falla (pegarle el error a Claude Code y pedirle que lo arregle — esa ES la habilidad).
- **Recurso vinculado:** `recursos/checklist-setup-stack.md`.
- **KPI:** URL del "hola mundo" publicada en la comunidad.

### L3 | Cómo dirigir a Claude Code — `guiones/L3-dirigir-claude-code.md` (10-14 min)
- **Objetivo:** el alumno sabe escribir un brief que produce lo que quiere, iterar en pasos pequeños y no romper lo que funciona.
- **Contenido obligatorio:** (a) la regla de oro: la calidad de lo construido = la calidad del brief — "describe QUÉ debe pasar y PARA QUIÉN, nunca cómo programarlo"; (b) la plantilla de brief del programa (recurso): contexto del negocio, usuario, qué debe hacer (lista numerada), qué NO entra, aspecto, datos de ejemplo; (c) iterar en pasos pequeños: una petición = un cambio; probar antes de pedir el siguiente (es el método científico de F0-L7 aplicado a construir); (d) el archivo CLAUDE.md del proyecto: las instrucciones fijas que Claude Code lee siempre (qué es el proyecto, reglas, qué no tocar); (e) los 5 errores del no-técnico: pedirlo todo de golpe, no probar entre cambios, aceptar sin revisar, pelearse con el error en vez de pegárselo a Claude, y cambiar de idea a mitad sin actualizar el brief; (f) frase ancla: "si sabes explicárselo a un becario brillante, sabes construir software".
- **Recurso vinculado:** `recursos/plantilla-brief-solucion.md`.

### L4 | El catálogo por dentro — `guiones/L4-catalogo-por-dentro.md` (8-12 min)
- **Objetivo:** el alumno sabe qué es técnicamente cada solución del catálogo, cuál es demo-able en web ya, y elige la suya (la de su oferta V1).
- **Contenido obligatorio:** (a) recorrer las 8 soluciones del catálogo de F1 con rayos X: qué hace por dentro, qué necesita (solo web / datos / integración externa), dificultad 1-3; (b) la distinción clave del programa: DEMO (web, se construye en F2, simula el flujo — p.ej. un simulador visual de WhatsApp dentro de la web) vs PILOTO REAL (integraciones de verdad, llega en F5 con el cliente pagando — y muchas veces el piloto real también empieza en web); (c) matriz en pantalla: dificultad × potencia de demo; recomendación para primera demo: recepcionista/recuperación de citas o chatbot web cualificador (máximo efecto visual, mínima complejidad); (d) acción: elegir SU solución (la que su oferta V1 promete — cruzar con el cuaderno de F1).
- **Recurso vinculado:** `recursos/catalogo-tecnico-soluciones.md`.

### L5 | DEMO EN DIRECTO: construye tu solución — `guiones/L5-demo-en-directo.md` (15-20 min, LA demo del módulo, hasta 1.500 palabras)
- **Objetivo:** el alumno ve construir una demo completa de principio a fin y replica el proceso con la suya.
- **Contenido obligatorio:** (a) marcar como demo real del programa: Agustín construye EN DIRECTO la demo dental (coherente con la demo de F1-L8: recuperación de citas para clínicas dentales) usando la plantilla de brief; estructura con bloques `[DEMO: …]` por paso: 1) rellenar el brief en pantalla (2 min), 2) dárselo a Claude Code y comentar lo que va pasando mientras construye, 3) primera versión: probarla, encontrar un fallo A PROPÓSITO y enseñarle a arreglarlo pegando el error ("esto no es un tropiezo, es EL método"), 4) iterar 2 mejoras pequeñas (datos de ejemplo realistas del nicho, un toque visual), 5) deploy a URL y probarla desde el móvil; (b) qué debe tener la demo resultante: panel simple + simulador del flujo (mensajes recuperando una cita) + datos de ejemplo del nicho; (c) el alumno replica con SU solución y SU nicho — con permiso explícito para que le salga peor a la primera: "mi tercera demo fue la primera decente" `[PRUEBA SOCIAL: experiencia real de Agustín]`; (d) mención de las plantillas AILINK como atajo `[PLANTILLAS AILINK: referenciar sin detallar — pendientes de construir]`.
- **Recurso vinculado:** `recursos/plantilla-brief-solucion.md` (reutilizado de L3 — anotarlo).
- **KPI:** tu demo V1 construida y desplegada en URL (aunque sea fea).

### L6 | Testea como un profesional — `guiones/L6-testea-como-profesional.md` (6-10 min)
- **Objetivo:** demo a prueba de directo: el alumno la rompe él antes de que la rompa un cliente.
- **Contenido obligatorio:** (a) recuperar el error 6 de F0-L6: "una demo que falla delante del cliente = credibilidad muerta" — el testeo no es opcional, es parte de construir; (b) la checklist pre-demo (recurso): flujo completo probado 3 veces, probado EN MÓVIL, datos de ejemplo realistas del nicho (nada de "Lorem ipsum" ni "Cliente 1"), qué pasa si el usuario escribe algo raro, URL que carga rápido, y el "test del cuñado": que alguien sin contexto la use delante de ti sin ayuda; (c) cómo pedirle a Claude Code que teste por ti (pedirle casos límite y arreglos) — pero el test del cuñado no lo sustituye nada; (d) regla del programa: nadie enseña una demo a un cliente sin la checklist completa.
- **Recurso vinculado:** `recursos/checklist-pre-demo.md`.

### L7 | Tu demo vendible — `guiones/L7-tu-demo-vendible.md` (8-12 min)
- **Objetivo:** HITO MAESTRO S4: demo construida + desplegada + guion de presentación de 3 minutos + vídeo de respaldo.
- **Contenido obligatorio:** (a) de demo técnica a activo de venta: personalizada con datos del nicho (nombres de negocio inventados pero verosímiles), el flujo cuenta una historia ("mira: este paciente canceló… y mira lo que pasa"); (b) el guion de 3 minutos (recurso): dolor → "mira esto" (demo) → resultado en unidad contable → siguiente paso; regla: enseñas el RESULTADO, no la tecnología (eco del wording de F1-L5 — "las palmeras, no el vuelo"); (c) grabar un vídeo-demo de 2-3 min como respaldo (si el directo falla en una llamada, compartes pantalla del vídeo) — con cualquier grabador de pantalla; (d) dónde vivirá la demo: URL compartible que en F3 irá en tu funnel y en F4 se enseña en llamada — "esta URL es tu credencial: no me creas, míralo funcionar"; (e) cierre de fase: recap de F2 y puente a F3 ("ya tienes oferta y prueba; ahora, tráfico").
- **Recursos vinculados:** `recursos/guion-demo-3-min.md`.
- **KPI (hito maestro):** demo desplegada + guion de 3 min escrito + vídeo de respaldo grabado — los tres publicados en la comunidad.

### R1 | `recursos/checklist-setup-stack.md`
Checklist secuencial con checkboxes y tiempo estimado: cuenta Claude → instalar Claude Code (rutas macOS/Windows) → verificar que responde → cuenta GitHub → cuenta Vercel → hola mundo desplegado (con la orden sugerida para pedírselo a Claude Code, literal y copiable) → URL publicada en comunidad. + Sección "si algo falla": los 3 atascos típicos de instalación y la instrucción universal (pegar el error a Claude Code). Costes orientativos del stack con nota "consulta precios actuales".

### R2 | `recursos/plantilla-brief-solucion.md`
La plantilla de brief rellenable: (1) contexto (mi negocio cliente es… su cliente final es…), (2) qué debe hacer — lista numerada de comportamientos observables, (3) qué NO entra (alcance del piloto de F1), (4) datos de ejemplo (tabla mínima), (5) aspecto (2-3 referencias), (6) cómo sabré que funciona (los checks de la demo). + Ejemplo COMPLETO relleno (demo dental, coherente con L5) + las 3 reglas de dirección (una petición = un cambio; probar entre pasos; errores se pegan, no se pelean).

### R3 | `recursos/catalogo-tecnico-soluciones.md`
Las 8 soluciones del catálogo (mismos nombres canónicos que F1-R1) con ficha cada una: qué hace por dentro (3-4 líneas sin jerga) · qué necesita (solo web / web+datos / integración externa en F5) · dificultad 1-3 · potencia de demo 1-3 · demo web recomendada (qué simular). + Matriz dificultad×potencia + recomendación de primera demo + regla: "tu demo = la solución de tu oferta V1 (cuaderno de F1)".

### R4 | `recursos/checklist-pre-demo.md`
Checklist con checkboxes: flujo completo ×3 · móvil · datos realistas del nicho · entradas raras probadas · carga rápida · test del cuñado hecho (nombre y fecha) · vídeo de respaldo grabado. + campo firma/fecha "apta para enseñar". Regla en cabecera: sin checklist completa, la demo no se enseña a nadie.

### R5 | `recursos/guion-demo-3-min.md`
Plantilla del guion de presentación: minuto 1 — el dolor en SUS palabras (de las reseñas/avatar de F1-L4); minuto 2 — "mira esto" (pasos exactos de qué enseñar y en qué orden, terminando en el resultado); minuto 3 — la unidad contable + siguiente paso (sin precio: eso es F4). + 3 reglas (resultado antes que tecnología; silencio después del momento "wow"; jamás improvisar una función no testeada) + campos rellenables por el alumno.

## Archivos que NO escriben los redactores (los hace Claude principal)
- `kpis.md` — KPIs del módulo (alumno + operador)
- `notas-fuente.md` — qué se hereda del esqueleto flagship, qué es creación original, pendientes de Agustín (stack, plantillas AILINK, prueba social de L5)
