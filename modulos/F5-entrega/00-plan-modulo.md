# F5 | Entrega — Blueprint del módulo (contrato de producción)

> Semanas 8-11 del alumno (solapado con F3/F4: entrega mientras sigue captando). Objetivo del módulo: **piloto entregado en ≤7 días, proyecto en ≤21, cliente encantado y listo para el retainer**. Hito maestro: primera entrega completada con criterios de aceptación firmados.
>
> Leer `../../01-BIBLIA.md`. El alumno llega con: primer cliente cobrado en la llamada (F4), demo guiada (F2), plantilla de brief (F2-L3), checklist pre-demo (F2-L6), tarjeta del cliente guardada en Stripe (F0-L8/F4-L6).
>
> **Frontera con F6**: F5 cubre la comunicación DURANTE el build y la entrega (días); F6 cubre la relación DURANTE el retainer (meses). No pisarse.

## Fuentes por chunk

| Chunk | Contenido a extraer |
|---|---|
| 09 (fulfillment overview) | Viaje del cliente, cero tiempo muerto post-pago, buyer's remorse (80% en las primeras 24h — benchmark heredado), the two tracks (trabajo real + experiencia percibida), "haz visible el trabajo invisible" |
| 10 (onboarding & launch) | Formulario post-venta, guion de onboarding call (incl. RE-VENDER), acuerdo, messaging framework día a día (el ejemplo real: foto → "CRM casi listo" → vídeo → lanzamiento → primera victoria "más rápido de lo que esperaba") |
| 12 (service delivery) | Native delivery (infraestructura reutilizable → aquí: plantillas propias), expectativas (infraprometer), primeros 7 días |
| 01 (proof capturing SOP, dentro de Meta Ads A) | Capturar prueba en el pico emocional, crudo > pulido, muchos mini-testimonios > uno grande, preguntas del testimonio, documentar el viaje desde el día 1 |

## Adaptaciones estructurales clave

1. **El "launch de ads" de la fuente = la "entrega del build" aquí.** El cliente de Owen esperaba leads; el de AILINK espera software funcionando. Mismo principio: velocidad + visibilidad del progreso.
2. **De demo guiada a producción**: en F5 llegan las integraciones REALES — WhatsApp Business API vía proveedor, chat libre con API de Anthropic (coste por uso, repercutido al cliente como coste operativo — decisión de F2), datos reales del negocio. Nivel de flujo, sin tutoriales de proveedor concretos: "elige un proveedor actual de WhatsApp Business API; Claude Code te guía en la integración".
3. **Cobros [BORRADOR — validar con Agustín]**: piloto ya cobrado por adelantado (F4). Proyecto: **50% al arrancar / 50% a la entrega**. El retainer se PROPONE en la entrega y arranca el mes siguiente (la venta completa es materia de F6-L3).
4. **Acuerdo de servicios**: se entrega un ESQUELETO estructural (partes, alcance ENTRA/NO ENTRA, precio y pagos, plazos, propiedad del entregable, datos y confidencialidad, cancelación) marcado en cabecera y pie: **"borrador estructural — pásalo por un abogado antes de usarlo con un cliente; esto no es asesoría legal"**. PROHIBIDO redactarlo como contrato definitivo o con lenguaje pseudo-jurídico denso.
5. **Infraprometer plazos**: comprometer 7 días y entregar en 5. Los plazos comprometidos al cliente llevan margen SIEMPRE.
6. **Datos del cliente = responsabilidad**: al recibir accesos y datos reales, una línea de flujo — trátalos con confidencialidad, solo lo necesario, acuerda su uso en el acuerdo — con la coletilla de la casa. Sin desarrollar RGPD más allá (la línea autorizada de la Biblia).
7. **La fábrica**: el "native delivery" de Owen (misma infraestructura para todos) se convierte en: cada entrega termina convertida en plantilla reutilizable → el segundo cliente cuesta la mitad. Las `[PLANTILLAS AILINK]` crecen con cada proyecto del alumno.

## Benchmarks autorizados

- Piloto entregado **≤7 días** desde el cobro · proyecto **≤21 días** (ya en Biblia)
- Buyer's remorse: el 80% ocurre en las primeras 24h (heredado) → primer contacto post-pago **el mismo día**, primera prueba visible de trabajo **<24h**
- Comunicación durante el build: **1 toque visible al día mínimo** (foto/captura/Loom/mensaje)
- Cobro del proyecto 50/50 `[BORRADOR]`
- Regla de infrapromesa: margen del ~30% en todo plazo comprometido (comprometes 7, planificas 5)
- Testimonio: se pide EN el pico emocional (el día de la entrega o la primera victoria), nunca "más adelante"

## Reglas de estilo

Las canónicas (plantilla con **KPI de esta lección**, único timestamp en Gancho, recap entrecomillado, ≥3 `[PANTALLA]` repartidas, 600-1.200 palabras, recursos con blockquote, glosario Biblia — lead/no-show/MRR ok, seguimiento no follow-up, "se aplica" no "aplica" —, cero rastro de la fuente, cifras de ejemplo "ilustrativas", huecos `[PRUEBA SOCIAL]`/`[DEMO]` en vez de inventos). Términos nuevos glosados: onboarding ya está en glosario; "criterios de aceptación" se explica en primera mención (la lista de checks que el cliente firma como "terminado").

## Especificación por pieza

### L1 | Cobrado ≠ terminado: el viaje de tu cliente — `guiones/L1-viaje-del-cliente.md` (6-9 min)
- **Objetivo:** entender el mapa completo post-cobro y las 24h críticas.
- **Contenido:** (a) la verdad: el 80% del arrepentimiento de compra ocurre en las primeras 24h — **cero tiempo muerto post-pago**: el formulario de arranque le llega ANTES de que se enfríe la llamada; (b) el viaje completo en pantalla: cobro → formulario → llamada de arranque → build (días) → entrega y traspaso → cobro final → propuesta de retainer (F6); (c) **the two tracks**: el trabajo real (invisible) y la experiencia percibida — "el cliente no ve tu esfuerzo: ve lo que le enseñas"; haz visible el invisible; (d) el estándar de plazos con infrapromesa (~30% de margen); (e) mapa del módulo.

### L2 | La llamada de arranque — `guiones/L2-llamada-de-arranque.md` (10-14 min)
- **Objetivo:** onboarding del cliente ejecutado: formulario recibido, llamada hecha, acuerdo firmado, alcance cerrado.
- **Contenido:** (a) el formulario de arranque (recurso): datos del negocio, accesos necesarios, contacto operativo, datos para la solución; se envía EN cuanto paga; (b) el guion de la llamada (30-45 min, recurso): 1) RE-VENDER (recordarle por qué esto va a funcionar — el cliente recién pagado necesita reafirmación, no silencio), 2) alcance ENTRA/NO ENTRA leído en voz alta (del worksheet de F1/piloto), 3) **criterios de aceptación** (glosar): la lista de checks que definirá "terminado" — se pactan AHORA, no al final, 4) accesos y datos (con la línea de confidencialidad y su coletilla), 5) fechas con infrapromesa, 6) canal de comunicación único y expectativa de updates diarios, 7) firma del acuerdo; (c) el acuerdo-esqueleto (recurso, con su doble disclaimer legal); (d) qué NO hacer: prometer extras fuera de alcance en caliente ("lo apunto para la fase 2").
- **Recursos:** `recursos/formulario-arranque-cliente.md` + `recursos/guion-llamada-arranque.md` + `recursos/acuerdo-servicios-esqueleto.md`.

### L3 | El build: de demo a producción — `guiones/L3-build-de-produccion.md` (10-14 min)
- **Objetivo:** el piloto real construido con datos del cliente en ≤5 días de trabajo (7 comprometidos).
- **Contenido:** (a) diferencia demo ↔ producción: datos reales, usuarios reales, integraciones reales; (b) el brief de producción: la plantilla de F2-L3 con dos secciones nuevas — datos reales del cliente y qué integraciones entran (solo las del alcance); (c) integraciones reales a nivel de flujo: WhatsApp Business API vía proveedor actual, chat libre conectando la API de Anthropic (recordar la decisión de F2: este coste por uso se repercute al cliente como coste operativo — se dijo en la propuesta), el pixel/aviso legal si la solución es pública; (d) construir en pasos con Claude Code (el método de F2: una petición = un cambio, probar entre pasos), empezando por la plantilla de su demo — "no empiezas de cero: empiezas de tu demo"; (e) gestión de imprevistos: si algo se atasca >medio día, se comunica al cliente ANTES de que pregunte (siembra de L4); (f) regla de alcance: lo que no está en ENTRA no se construye — se anota para la fase 2.

### L4 | Haz visible el invisible — `guiones/L4-haz-visible-el-invisible.md` (8-12 min)
- **Objetivo:** plan de comunicación del build activo: 1 toque visible al día.
- **Contenido:** (a) el principio: los clientes no se van por malos resultados en la semana 1 — se van por SILENCIO; la percepción de trabajo importa tanto como el trabajo; (b) el messaging framework día a día (recurso, con el patrón de la fuente adaptado a builds): día 0 "arrancamos" + foto del brief → día 1 captura del progreso → día 2 Loom de 60s enseñando algo funcionando → entrega parcial → "ya está desplegado, pruébalo" — cada mensaje corto, visual, sin jerga; (c) celebrar hitos con el cliente (primera respuesta del bot, primer dato real procesado) — la emoción del cliente en esos momentos es materia prima del testimonio (siembra de L6); (d) qué hacer si el cliente se pone nervioso o pide extras: responder el mismo día, recentrar en el alcance, nunca defenderse — datos y siguiente paso; (e) [PANTALLA] con el hilo de mensajes modelo completo.
- **Recurso:** `recursos/plan-comunicacion-build.md`.

### L5 | QA de producción y entrega — `guiones/L5-qa-y-entrega.md` (10-14 min)
- **Objetivo:** entrega ejecutada: QA pasado, cliente formado, criterios de aceptación firmados.
- **Contenido:** (a) el QA de producción (recurso): la checklist pre-demo de F2-L6 ampliada — con datos reales, con el usuario real del cliente delante, casos límite del negocio real, qué pasa si falla la integración (mensajes de error dignos), móvil; (b) la regla intacta: **nada se entrega sin la checklist completa** — "una entrega rota destruye en 5 minutos la confianza de 3 semanas"; (c) formación al cliente: vídeo corto de uso (2-3 min, grabación de pantalla) + sesión de traspaso en directo (20-30 min): el CLIENTE maneja la solución delante de ti, no tú delante de él; (d) el cierre formal: repasar los criterios de aceptación uno a uno y marcar "terminado" JUNTOS — sin esto, el proyecto no acaba nunca; (e) documentar lo entregado (2 párrafos + accesos) — alimenta la plantilla (L7) y el retainer (F6).
- **Recurso:** `recursos/checklist-entrega-produccion.md`.

### L6 | Cobra, captura y encadena — `guiones/L6-cobra-captura-encadena.md` (8-12 min)
- **Objetivo:** cobro final hecho, testimonio capturado en el pico, siguiente paso propuesto.
- **Contenido:** (a) el cobro final (50% restante si es proyecto `[BORRADor]`) se envía el día de la entrega — el mejor día para cobrar es el día del "wow"; (b) **capturar la prueba EN el pico emocional** (del proof capturing de la fuente): el día de la entrega o de la primera victoria, no "más adelante" — crudo > pulido, un audio de WhatsApp del cliente vale más que un vídeo producido; las 4 preguntas del testimonio (recurso); mini-testimonios continuos > un testimonial épico; ese material llena los huecos [PRUEBA SOCIAL] de F3 (VSL, funnel, creativos) — "tu máquina de F3 se hace más fuerte con cada entrega"; (c) pedir el referido en caliente: "¿a qué otro [nicho] que conozcas le vendría bien esto?" — una frase, cero presión; (d) sembrar el retainer: "esto necesita mantenimiento y puede crecer — te preparo la propuesta de acompañamiento mensual" (la venta completa del retainer es F6-L3); (e) actualizar el tracker y celebrar TU hito en la comunidad.
- **Recurso:** `recursos/guia-testimonio-referido.md`.

### L7 | Tu fábrica: cada entrega te hace más rápido — `guiones/L7-tu-fabrica.md` (6-9 min)
- **Objetivo:** la entrega convertida en plantilla; el segundo cliente cuesta la mitad.
- **Contenido:** (a) el principio de infraestructura reutilizable: el amateur empieza cada proyecto de cero; la fábrica convierte cada entrega en plantilla (repo base + brief tipo + checklist del nicho); (b) qué se guarda de cada proyecto: el repo limpio de datos del cliente, el brief final, los atascos y sus soluciones, los mensajes que mejor funcionaron; (c) la biblioteca del alumno (recurso): estructura mínima de una plantilla propia; (d) efecto compuesto: piloto 1 = 5 días → piloto 3 del mismo nicho = 2 días → margen y capacidad crecen sin subir horas; esa capacidad es la que te deja escalar (puente a F6); (e) `[PLANTILLAS AILINK: las del programa te dan el arranque; tu biblioteca personal te da el negocio]`.
- **Recurso:** `recursos/biblioteca-plantillas.md`.

### R1 | `recursos/formulario-arranque-cliente.md` — spec del formulario post-pago (para Typeform/Tally o doc): datos del negocio, contacto operativo, accesos necesarios (lista por tipo de solución), datos para la solución (los de la tabla del brief), horario/canal preferido, "¿algo que deba saber?". Se envía automáticamente tras el pago (o a mano el mismo día). Con nota de confidencialidad + coletilla.
### R2 | `recursos/guion-llamada-arranque.md` — los 7 pasos de L2 en esqueleto con frases sugeridas, tiempos orientativos y checkboxes; el momento RE-VENDER desarrollado (2-3 frases modelo); tabla ENTRA/NO ENTRA rellenable; sección de criterios de aceptación con 5 campos.
### R3 | `recursos/acuerdo-servicios-esqueleto.md` — esqueleto estructural por secciones con lenguaje llano y campos: partes · objeto y alcance (ENTRA/NO ENTRA) · precio y calendario de pagos · plazos (con margen) · propiedad del entregable al pago completo · datos y confidencialidad · criterios de aceptación · cancelación y qué pasa con lo pagado. **Cabecera Y pie: "Borrador estructural: pásalo por un abogado antes de usarlo con un cliente. Esto no es asesoría legal."**
### R4 | `recursos/plan-comunicacion-build.md` — el messaging framework día a día en tabla (día, qué envías, formato, ejemplo de mensaje literal) para un build de 5-7 días + reglas (1 toque visible/día, responder el mismo día, celebrar hitos, comunicar atascos antes de que pregunte) + 6 mensajes modelo copiables.
### R5 | `recursos/checklist-entrega-produccion.md` — checkboxes en 4 bloques: QA con datos reales (flujo ×3, usuario real, casos límite del negocio, errores dignos, móvil) · formación (vídeo de uso grabado, sesión de traspaso hecha, el cliente lo manejó solo) · cierre (criterios de aceptación repasados y firmados juntos, documentación entregada) · post (cobro final enviado, testimonio pedido, tracker actualizado). Regla en cabecera: nada se entrega sin la checklist completa.
### R6 | `recursos/guia-testimonio-referido.md` — cuándo pedir (el pico: entrega o primera victoria), cómo (el audio de WhatsApp, el vídeo selfie de 30s, la reseña escrita — de menor a mayor fricción), las 4 preguntas (¿cómo era antes? ¿por qué confiaste? ¿qué ha pasado? ¿a quién se lo recomendarías?), dónde usarlo (huecos [PRUEBA SOCIAL] de F3: VSL, funnel, creativos, LinkedIn), y la frase del referido + seguimiento del referido en el tracker.
### R7 | `recursos/biblioteca-plantillas.md` — estructura de la plantilla personal (repo limpio, brief tipo del nicho, checklist de entrega del nicho, atascos y soluciones, mensajes que funcionaron) + el ritual post-entrega de 30 min para alimentarla + campos de inventario (mis plantillas: nicho, solución, veces reutilizada, tiempo del último build).

## Archivos que NO escriben los redactores (los hace Claude principal)
- `kpis.md` · `notas-fuente.md`
