# F3 | Lanza — Blueprint del módulo (contrato de producción)

> Semanas 3-7 del alumno. Objetivo del módulo: **máquina de demanda encendida** — funnel publicado, VSL grabado y, según su ruta (asignada en la kick-off), campaña de Meta ads activa O sistema de outreach en marcha. Hito maestro: **primeras reuniones agendadas (S6-7)**.
>
> Leer `../../01-BIBLIA.md`. El alumno llega con: oferta V1 (F1), demo desplegada + guion 3 min + vídeo (F2), y su ruta por presupuesto decidida en la kick-off: <500€ → outreach orgánico · 500-2.000€ → outreach sistematizado · +2.000€ → Meta ads. Las TRES rutas ven todo el módulo (la teoría de ads les servirá al escalar), pero ejecutan la suya.

## Fuentes por chunk (transcripción del curso fuente)

| Chunk | Contenido a extraer |
|---|---|
| 01 (Meta Ads A) | Awareness levels, componentes del ad, oferta del ad, hooks (80%), creativos, copy, funnels vs lead forms, fricción, speed to lead |
| 02 (Meta Ads B) | Campaña en vivo, pixel, KPIs/benchmarks, reglas de escalado, kill/keep/scale, cadencia de testeo, nunca editar ads activos, bottleneck analysis, ad math |
| 05 (VSL) | Estructura de los 2 VSLs, "no me creas, verifícame", producción simple |
| 06 (FB warmup) | Página con nombre personal, campaña de engagement 5€/día |
| 17 (daily workflow) | El estándar de trabajo 0→20K |
| 18 (cold SMS) | La ESTRUCTURA del sistema (HPF hook/pitch/follow-up, drip, llamar al reply) — el canal cambia a email |
| 19 (cold calling) | Mindset, tonalidad, urgencia, guion, $6/marcación (reverse engineering), tie-down de agenda |

## Adaptaciones estructurales clave (los redactores las siguen a rajatabla)

1. **Solo captación B2B del alumno.** El curso fuente usa ads en dos direcciones (captar clientes B2B + servir a clientes B2C); aquí SOLO existe la primera: anuncios dirigidos a dueños de negocio del micro-nicho del alumno para agendar reuniones. Nada de price-anchoring B2C ni ads de servicio.
2. **El funnel se construye con Claude Code** (no con herramientas de terceros): el alumno acaba de aprenderlo en F2 y su funnel es en sí mismo una demo de lo que vende. Estructura: página con VSL + demo enlazada + formulario corto cualificador + calendario embebido (Cal.com/Calendly de F0-L9).
3. **La prueba del principiante es la DEMO, no los casos de éxito.** El "no me creas, verifícame" del VSL fuente (que enseña clientes con teléfono) se adapta honesta: "no me creas — mira la solución funcionando" (URL de la demo + vídeo). PROHIBIDO sugerir testimonios inventados o prueba social prestada; hueco `[PRUEBA SOCIAL: cuando tengas tu primer caso, va aquí]`.
4. **Cold SMS masivo NO existe en España** (RGPD/LSSI). Su estructura (HPF, drip, llamar al que responde) se trasplanta al **email frío B2B**. WhatsApp en frío: NO (contra RGPD y las condiciones de WhatsApp). Llamada fría B2B: sí con matices.
5. **Marco legal — regla editorial estricta**: las afirmaciones legales se dan a nivel de flujo, SIN citar artículos concretos, SIEMPRE con la coletilla "esto es orientación práctica, no asesoría legal — valida tu proceso con un profesional". Línea autorizada: "el email comercial en frío está regulado en España (LSSI/RGPD): dirígete a buzones corporativos, personaliza de verdad, justifica el interés legítimo B2B, ofrece baja clara en cada email, jamás compres bases de datos turbias; la llamada en frío a EMPRESAS está permitida con matices (a particulares rige la Lista Robinson)". **Ampliación (ronda de corrección, 20/08): "tu funnel recoge datos personales y usa el pixel: necesita política de privacidad enlazada, aviso/consentimiento de cookies ANTES de disparar el pixel y casilla de consentimiento en el formulario — pídeselo a Claude Code al construirlo"** (misma coletilla). Nada más específico que esto.

### Enmiendas post-verificación (20/08)
- "Marcaciones" es calco/uso latinoamericano → **"llamadas"** en todo el módulo (incluido este blueprint: "50 llamadas").
- La secuencia de email se llama **"hook → pitch → seguimiento"** (nunca HPF: la F delataría follow-up, término traducido).
- Seguimientos: **2 + 1 opcional de cierre** ("última vez que te escribo").
- Validez canónica (de F0/Biblia, sin redefinir): **300 toques = validez de un canal de outreach (una llamada ES un toque); 30 llamadas DE VENTA realizadas = validez de tu tasa de cierre (materia de F4)**.
- En outreach, el pitch y los seguimientos enlazan **EL FUNNEL** (que ya contiene VSL + demo + calendario), no la demo suelta: un solo activo, un solo mensaje.
- **Ruta "sistematizado" (500-2.000€) definida**: el presupuesto va a herramienta de secuencias de email con buena entregabilidad + verificación de emails + datos de contacto + más volumen semanal, y a adelantar el primer test de ads al mínimo (20€/día) cuando la muestra orgánica valide el mensaje.
- Creativos: los prompts de imagen son portables a **cualquier generador de imágenes con IA actual** (F2 NO enseña generación de imágenes — no afirmar que sí); el concepto "captura de la demo" no necesita generador.
- La checklist pre-lanzamiento vive como recurso (sección final de `kpis-ads-benchmarks.md`), no solo dentro del guion de L6.

## Benchmarks autorizados en este módulo (únicos números permitidos, etiquetables como "benchmark del programa")

- Presupuesto de ads: **recomendado 30-50€/día; mínimo absoluto 20€/día** (con menos, el aprendizaje del algoritmo se alarga) — `[BORRADOR: validar con Agustín, que opera Meta ads]`
- Testeo: **10-20€/día por creativo** → con 30-50€/día, 2-4 creativos a la vez
- CTR link único ≥1,5% · CPM sano 40-100€ `[heredado, validar]` · conversión de landing 5-10% · show rate 60-70% (B2B templado)
- Coste por reunión agendada B2B: rango orientativo 50-150€ `[heredado, validar con datos reales]`
- Reglas de decisión: no juzgar antes de 50 eventos o 5-7 días · matar a ≥2x el coste objetivo (muerte anticipada: 3x gastado sin conversión) · NUNCA editar un ad/adset activo (duplicar) · un cambio de variable a la vez · escalar +20-30% cada 2-3 días si es rentable
- Campaña de engagement: 5€/día por adset
- Email frío: 200-400 envíos/semana sostenibles con personalización real; las tasas del ejemplo SIEMPRE ilustrativas (los KPIs propios salen de su tracker)
- Llamada fría: la matemática de actividad se enseña con la calculadora inversa (toques → reuniones → clientes), sin prometer tasas
- Regla de validez transversal: **300 toques / 30 llamadas** (de F0-L7)
- Speed to lead: responder a un lead entrante en **<5 minutos** (benchmark heredado: el primero en responder se lleva la mayoría de las ventas — sin inventar el % exacto; decir "la mayoría")

## Reglas de estilo

Las de F1/F2 (plantilla canónica con "**KPI de esta lección:**", sin timestamps en títulos de sección, recaps entrecomillados, mínimo 3 `[PANTALLA]` repartidas, 600-1.200 palabras — L6 y L7 hasta 1.400 por ser prácticas, glosario Biblia, cero rastro de la fuente, cifras de ejemplo "ilustrativas", sin precios de servicios fuera de los rangos ya enseñados en F1). Términos nuevos glosados en primera mención: adset (conjunto de anuncios), CPM, CTR, pixel, learning phase (fase de aprendizaje).

## Especificación por pieza

### L1 | La máquina de demanda — `guiones/L1-maquina-de-demanda.md` (6-9 min)
- **Objetivo:** el alumno entiende el mapa completo del módulo, confirma su ruta y asume la matemática de actividad.
- **Contenido:** (a) la verdad incómoda: oferta + demo sin tráfico = cero; F3 enciende el grifo; (b) las 3 rutas por presupuesto (de su kick-off) — las tres llevan al mismo sitio: reuniones en el calendario; qué ve y qué ejecuta cada ruta; (c) la matemática de actividad (reverse engineering del chunk 19, adaptada y en €): del objetivo de la promesa hacia atrás → clientes → reuniones realizadas → reuniones agendadas → toques; cada toque VALE dinero (la idea "cada llamada son X€" adaptada sin inventar la cifra: se calcula con SU calculadora); (d) el mapa de lecciones; (e) regla: la máquina no se juzga sin muestra (300/30).
- **Recurso:** `recursos/tracker-captacion.md`.

### L2 | Tu funnel: de clic a reunión — `guiones/L2-tu-funnel.md` (10-14 min, práctica)
- **Objetivo:** funnel publicado, construido con Claude Code.
- **Contenido:** (a) anatomía del funnel book-a-call: titular congruente con tu oferta → VSL → "mira la demo funcionando" (URL de F2) → formulario corto cualificador (2-4 preguntas: sector, tamaño, qué le duele) → calendario embebido; (b) el principio de FRICCIÓN (metáfora de la tubería del chunk 01): menos preguntas = más reuniones de menos calidad; empezar con poca fricción y añadir según calidad; (c) congruencia anuncio↔titular (si el ad dice X, la página abre con X); (d) velocidad de carga y mobile-first (checklist); (e) construirlo con Claude Code: brief del funnel (plantilla de F2-L3 aplicada) — "tu funnel ES una demo de lo que vendes"; (f) speed to lead: <5 min a cualquier lead entrante — configura avisos al móvil.
- **Recurso:** `recursos/checklist-funnel.md`.
- **KPI:** funnel publicado en URL propia + prueba completa hecha desde el móvil (formulario → reserva de test).

### L3 | Tu VSL: "no me creas, míralo funcionar" — `guiones/L3-tu-vsl.md` (8-12 min)
- **Objetivo:** VSL de 3-5 min grabado y montado en el funnel.
- **Contenido:** (a) qué es un VSL (glosar: vídeo de venta que trabaja por ti 24/7) y por qué multiplica el show rate: el que agenda ya sabe quién eres; (b) la estructura adaptada (del chunk 05): 1) a quién ayudo y con qué dolor, 2) "no me creas — mira esto" (la demo funcionando, el momento central), 3) cómo trabajo (piloto acotado, entrega en días, sin humo), 4) qué pasa al agendar (llamada corta, sin compromiso), 5) CTA al calendario; (c) producción simple: cámara del móvil + luz de ventana + el guion; se puede regrabar mil veces; (d) qué NO hacer: inventar casos de éxito, salir leyendo, prometer cifras; hueco `[PRUEBA SOCIAL: tu primer caso irá aquí — de momento, la demo ES tu prueba]`.
- **Recurso:** `recursos/guion-vsl.md`.

### L4 | Tu página y el calentamiento — `guiones/L4-pagina-calentamiento.md` (6-9 min)
- **Objetivo:** página de Facebook/Instagram creada (nombre personal) y campaña de engagement activa.
- **Contenido:** (a) por qué PERSONA > logo para vender a dueños de negocio locales: confían en alguien con cara, no en "otra agencia" (del chunk 06); (b) crear la página (nombre y apellido, foto real profesional, bio corta de resultado); (c) la campaña de calentamiento: engagement a 5€/día con contenido simpático/curioso — objetivo: seguidores y señales para bajar CPMs futuros; qué es CPM (glosar); (d) advertencia: no crear cuenta publicitaria y página el mismo día a toda prisa (restricciones); calentar 1-2 semanas mientras se ejecutan L2-L3; (e) para rutas low-budget: la página también da credibilidad cuando te buscan tras un email o llamada — se hace igual.
- **KPI:** página creada + campaña de engagement activa a 5€/día.

### L5 | Anatomía de un anuncio B2B — `guiones/L5-anatomia-anuncio-b2b.md` (10-14 min)
- **Objetivo:** primer lote de 2-4 creativos listos.
- **Contenido:** (a) los 4 componentes: oferta del ad, creativo, copy, destino — y la regla: **el creativo es el 80%; dentro del creativo, el hook es el 80%** (0,1 segundos para decidir si te miran); (b) la oferta del ad vende SOLO el siguiente paso (la reunión), no el proyecto entero; (c) niveles de consciencia del dueño de negocio (adaptado): la mayoría es consciente del problema ("pierdo llamadas, la IA existe") pero no del vehículo — tu ángulo: enseñar el resultado concreto en SU sector + la demo; (d) creativos de imagen con IA (F2 ya les dio la herramienta): 3 conceptos que funcionan — la cara del alumno con texto de resultado, captura real de la demo con titular, "antes/después" del proceso del negocio; prompts en el recurso; (e) copy: llamada al nicho → dolor → resultado → CTA (fórmula corta); (f) investigar en la biblioteca de anuncios de Meta: los ads activos +6 meses son ganadores — inspirarse, no copiar.
- **Recurso:** `recursos/banco-creativos-b2b.md`.
- **KPI:** 2-4 creativos generados + copy escrito para cada uno.

### L6 | Lanza tu campaña — `guiones/L6-lanza-tu-campana.md` (12-16 min, práctica, hasta 1.400 palabras)
- **Objetivo:** campaña activa (ruta ads).
- **Contenido:** (a) estructura mínima: 1 campaña → 1 adset (glosar) → 2-4 creativos; presupuesto por adset 30-50€/día (mínimo 20€ con expectativas ajustadas); (b) targeting 2026: el creativo ES el targeting — solo edad/género razonables del dueño del nicho + ubicación (España o su provincia+radio) + placements solo Facebook/Instagram; (c) evento de optimización: la reserva de reunión (o el lead si el volumen es bajo — regla del chunk 02 adaptada); pixel: pedirle a Claude Code que lo instale en el funnel `[PANTALLA]`; (d) checklist pre-lanzamiento (congruencia, links, pixel probado, calendario funcionando, avisos de speed to lead); (e) lanzar a medianoche; (f) qué esperar los primeros 7 días: NO TOCAR NADA (los leads llegan en olas; tocar reinicia el aprendizaje); (g) las rutas low-budget ven esta lección igual: la ejecutarán al reinvertir sus primeros ingresos.
- **KPI (ruta ads):** campaña activa + checklist pre-lanzamiento completa publicada.

### L7 | Lee los datos como un profesional — `guiones/L7-lee-los-datos.md` (12-16 min, hasta 1.400 palabras)
- **Objetivo:** el alumno decide con datos: matar, mantener o escalar.
- **Contenido:** (a) el tablero mínimo: gasto, CPM, CTR link, conversión de landing, coste por reunión agendada, coste por reunión REALIZADA; benchmarks de la tabla autorizada; (b) las reglas de decisión (del chunk 02, casi verbatim): nada se juzga antes de 50 eventos o 5-7 días · kill a ≥2x del objetivo · muerte anticipada a 3x gastado sin conversión · NUNCA editar un ad activo (duplicar y cambiar UNA variable) · escalar +20-30% cada 2-3 días si es rentable — "subirlo de golpe rompe el aprendizaje"; (c) jerarquía de diagnóstico: ¿CPM alto? → creativo débil/página fría · ¿CTR bajo? → hook/mensaje · ¿landing no convierte? → congruencia/fricción · ¿agendan pero no se presentan? → eso es F4; (d) **el análisis de cuellos de botella con Claude**: pega tus métricas + los benchmarks y pídele el diagnóstico `[PANTALLA: demo del análisis]` — el método del programa; (e) conexión con la plantilla de tests de F0 ("te dije que se estrenaba aquí"); (f) para outreach: MISMAS reglas con sus métricas (envíos, respuestas, reuniones) en el tracker.
- **Recurso:** `recursos/kpis-ads-benchmarks.md`.
- **KPI:** tracker con 7 días de datos reales + primer análisis de cuellos de botella hecho con Claude.

### L8 | Email frío B2B que no da vergüenza (y cumple) — `guiones/L8-email-frio-b2b.md` (10-14 min)
- **Objetivo (rutas low-budget):** sistema de email en marcha: lista propia + secuencia + cadencia semanal.
- **Contenido:** (a) marco legal con la LÍNEA AUTORIZADA del blueprint (regla editorial 5) — ni más ni menos; (b) construir la lista SIN comprar bases turbias: Google Maps del nicho + web del negocio + criterios de la checklist de F1 (100-300 negocios de arranque); (c) la estructura HPF adaptada del sistema fuente: email 1 = Hook (pregunta corta y específica del dolor, 3-4 líneas, cero pitch) → si responde, Pitch (la oferta en 2 frases + demo) → seguimientos 2-3 espaciados (valor, no insistencia); personalización real (una línea que demuestre que has mirado SU negocio — con Claude Code puedes preparar la investigación en lote); (d) al que responde: llamada corta ese mismo día (speed to lead) para agendar la reunión; (e) cadencia: 200-400 envíos/semana sostenibles; regla 300 antes de juzgar; (f) higiene: baja clara, buzones corporativos, nada de adjuntos pesados.
- **Recursos:** `recursos/plantillas-email-frio.md` + `recursos/rgpd-captacion.md`.
- **KPI:** lista de 100+ negocios validados + secuencia cargada + primeros 50 envíos hechos.

### L9 | LinkedIn y la llamada que agenda — `guiones/L9-linkedin-llamada.md` (10-14 min)
- **Objetivo (rutas low-budget):** segundo canal activo: LinkedIn con criterio + llamada B2B para agendar.
- **Contenido:** (a) LinkedIn: perfil orientado a resultado (titular = tu oferta en 8 palabras), conexión sin pitch en el primer mensaje, conversación → demo → agenda; constancia > volumen; (b) la llamada fría B2B (permitida con matices — recordar la línea legal y la Lista Robinson para particulares): mindset del chunk 19 adaptado — nadie te conoce, el no es gratis, cada marcación es un ladrillo de tu matemática de actividad; (c) tonalidad y marco (sonríe, habla como persona, baja el ritmo); (d) el guion corto: apertura honesta ("te llamo en frío, 30 segundos y decides") → el dolor del nicho en una frase → la pregunta → si hay interés: agendar EN la llamada (tie-down del chunk 19: email confirmado en vivo, invitación aceptada antes de colgar); (e) urgencia sin trucos: la agenda del piloto es limitada de verdad (solo puedes entregar N pilotos a la vez — cierto por capacidad); (f) registro en el tracker.
- **Recurso:** `recursos/guion-llamada-b2b.md`.
- **KPI:** 50 marcaciones O 30 conversaciones de LinkedIn registradas en el tracker.

### L10 | El estándar: tu día en captación — `guiones/L10-el-estandar.md` (5-8 min)
- **Objetivo:** instalar el estándar de trabajo hasta el primer cliente.
- **Contenido:** (a) del chunk 17 casi verbatim, adaptado: en fase de captación tu día es UNA cosa — conseguir reuniones y cerrarlas; 80% captación / 20% resto; la analogía del avión (el despegue quema el 90% del combustible); (b) el bloque diario según ruta (ads: revisar datos 1 vez al día — NO 10 — y producir creativos; outreach: bloque de envíos/llamadas a primera hora); (c) Más/Mejor/Nuevo aplicado: si funciona, MÁS volumen — no montes el segundo canal hasta exprimir el primero; (d) puente a F4: "las reuniones ya caen; ahora, a convertirlas — y eso es una habilidad, no un talento".
- **KPI:** bloque diario de captación en el calendario (captura) + 7 días seguidos cumplidos en el tracker.

### R1 | `recursos/tracker-captacion.md` — tabla diaria por canal (fecha, toques/gasto, respuestas/clics, reuniones agendadas, realizadas, notas) + fila semanal de totales + las reglas de validez impresas arriba + mini-guía "cómo pasarle esto a Claude para el análisis". Formato para copiar a Sheets/Notion.
### R2 | `recursos/checklist-funnel.md` — congruencia ad↔titular · carga <3s · mobile-first · VSL arriba · demo enlazada y funcionando · formulario 2-4 preguntas · calendario embebido probado · aviso de lead al móvil configurado (speed to lead <5 min) · prueba completa desde el móvil con reserva de test. Checkboxes + campos.
### R3 | `recursos/guion-vsl.md` — la estructura de 5 bloques con frases sugeridas y campos rellenables + reglas de producción (móvil, luz, regrabar) + lista de NOs (casos inventados, leer, cifras prometidas) + hueco `[PRUEBA SOCIAL]`.
### R4 | `recursos/banco-creativos-b2b.md` — los 3 conceptos de creativo con un prompt de generación de imagen COMPLETO cada uno (adaptable por nicho), fórmula de copy con 2 ejemplos rellenos (ilustrativos), guía de 5 min de la biblioteca de anuncios de Meta (buscar el nicho, filtrar activos antiguos, qué mirar), y la regla "inspirarse, no copiar".
### R5 | `recursos/kpis-ads-benchmarks.md` — la tabla completa de benchmarks autorizados + reglas kill/keep/scale + reglas de cambios (nunca editar activo, una variable, +20-30%) + el prompt sugerido para el análisis de cuellos de botella con Claude + tabla equivalente para email/llamada.
### R6 | `recursos/plantillas-email-frio.md` — secuencia HPF completa: email 1 (hook, 2 variantes), pitch de respuesta, 2 seguimientos, con campos [nicho]/[dolor]/[demo] + reglas de personalización + recordatorio legal corto remitiendo a R8.
### R7 | `recursos/guion-llamada-b2b.md` — guion esqueleto de la llamada (apertura honesta → dolor → pregunta → agenda en vivo con tie-down) + 6-8 respuestas a objeciones de agenda típicas ("mándame un email" → "te lo mando ahora mismo y lo vemos juntos 15 min, ¿jueves o viernes?") + reglas de tonalidad.
### R8 | `recursos/rgpd-captacion.md` — la línea legal autorizada desarrollada en tabla práctica: canal → qué sí / qué no / matiz — email B2B, llamada B2B, llamada B2C (Robinson), WhatsApp frío (NO), LinkedIn, compra de bases (NO) — con el disclaimer de "orientación práctica, no asesoría legal; valida tu proceso con un profesional" arriba Y abajo.

## Archivos que NO escriben los redactores (los hace Claude principal)
- `kpis.md` · `notas-fuente.md`
