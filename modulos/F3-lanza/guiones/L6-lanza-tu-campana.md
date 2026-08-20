# L6 | Lanza tu campaña

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F3 Lanza | 12-16 min | recursos/kpis-ads-benchmarks.md (aquí, su checklist pre-lanzamiento; la tabla de datos se estrena en L7) |

**Objetivo:** campaña activa (ruta ads): estructura mínima montada, pixel instalado y probado con Claude Code, checklist pre-lanzamiento completa — y el compromiso de no tocar nada durante 7 días.

## Gancho (0:00-0:20)

"Hoy pulsas el botón. La oferta de F1, la demo de F2, el funnel, el VSL y los creativos de las últimas lecciones: todo lo que has construido converge en una pantalla del administrador de anuncios. Y te aviso ya: montar la campaña es la parte fácil de esta lección. La difícil viene después — no tocar nada durante siete días. Vamos por partes."

[PANTALLA: administrador de anuncios abierto, campaña en borrador con el nombre del nicho del alumno]

## Sección 1 — La estructura mínima: 1 → 1 → 2-4

- La complejidad no es profesional: es ruido. La estructura del programa: **1 campaña → 1 adset → 2-4 creativos**. Adset (conjunto de anuncios): el nivel intermedio donde se definen presupuesto, audiencia y evento de optimización; los creativos viven dentro.
- ¿Por qué UN solo adset? Porque cada adset reparte la señal. Si divides tu presupuesto entre cinco, ninguno acumula datos suficientes para aprender; con uno, Meta concentra la señal y aprende antes.
- Presupuesto: **30-50€/día por adset (benchmark del programa); mínimo absoluto 20€/día**. Por debajo del mínimo, el aprendizaje del algoritmo se alarga tanto que la campaña nunca llega a demostrar nada. Si arrancas en el mínimo, ajusta expectativas: menos datos por semana y decisiones más lentas.
- La regla de testeo: cada creativo necesita **10-20€/día propios** para probarse de forma justa. Por eso con 30-50€/día caben 2-4 creativos — los que hiciste en L5. No metas ocho "por si acaso": los matarías de hambre a todos.

## Sección 2 — Targeting 2026: tu creativo ES el targeting

- La idea que lo cambia todo: ya no le explicas a Meta a quién buscar apilando intereses; se lo dice tu anuncio. Si tu creativo habla de "clínicas que pierden llamadas", Meta encuentra a quien reacciona a eso. El mensaje segmenta mejor que cualquier filtro.
- Lo único que configuras: edad y género razonables del dueño de tu nicho, ubicación geográfica (España entera, o tu provincia + radio si tu oferta es local) y ubicaciones de anuncio (placements) SOLO Facebook e Instagram — el resto de ubicaciones dan clics baratos y de mala calidad.
- Todo lo demás, abierto. Tu targeting de verdad lo hiciste en L5 cuando escribiste el hook.

## Sección 3 — El evento de optimización y el pixel

- Meta optimiza hacia lo que tú le señales. Tu evento ideal es la **reserva de reunión**: es exactamente lo que quieres que se repita. Regla del programa: optimiza por el evento más profundo del funnel para el que tengas volumen. Si estás en presupuesto mínimo y las reservas van a ser pocas, optimiza por lead (formulario enviado): le das a Meta señal suficiente para aprender, y subes a reserva cuando haya volumen.
- Para que Meta se entere de lo que pasa tras el clic necesita el **pixel**: un fragmento de código instalado en tu funnel que le avisa de cada visita, cada formulario enviado y cada reserva confirmada.
- Y aquí llega tu ventaja de F2: como tu funnel lo construiste con Claude Code, instalar el pixel te cuesta un prompt: "Instala el pixel de Meta con este ID en mi funnel: dispara un evento de lead cuando se envía el formulario y un evento de reserva cuando se confirma cita en el calendario." La reserva se captura escuchando el evento del widget embebido del calendario o con una página de gracias tras reservar — si el evento no dispara en el test, pídele a Claude Code exactamente eso.

[PANTALLA: el prompt en Claude Code y, al lado, el administrador de eventos de Meta registrando lead y reserva durante el test]

- Después, pruébalo TÚ: recorre el funnel entero como si fueras un cliente y verifica en el administrador de eventos que los dos eventos se disparan. Sin este check no hay lanzamiento.
- Recordatorio legal: el pixel solo puede dispararse tras el consentimiento de cookies — lo tienes resuelto en el bloque legal de tu checklist del funnel (L2); en el test, acepta el aviso primero.

## Sección 4 — Checklist pre-lanzamiento

[PANTALLA: la checklist completa en pantalla]

- La misma disciplina que la checklist pre-demo de F2, aplicada ahora al lanzamiento — la tienes como checklist con casillas al final de `recursos/kpis-ads-benchmarks.md`:
  1. **Congruencia anuncio↔titular:** lo que promete el ad es lo primero que se lee en la landing (L2).
  2. **Todos los enlaces funcionan:** del anuncio a la landing, de la landing a la demo, del formulario al calendario.
  3. **Pixel probado:** los dos eventos disparando en el test.
  4. **Calendario funcionando:** reserva de prueba hecha desde el móvil.
  5. **Avisos de speed to lead activos:** cuando entre un lead, tu móvil suena y respondes en <5 minutos (benchmark del programa: el primero en responder se lleva la mayoría de las ventas).
  6. **Creativos cargados:** un creativo por anuncio, copy revisado, cero faltas.
- ¿Todo marcado? Entonces —y solo entonces— se programa el lanzamiento.

## Sección 5 — Lanza a medianoche y suelta el ratón

- Programa la campaña para arrancar a las 00:00: le das a Meta el día completo para repartir el gasto, en lugar de un arranque a media tarde con el presupuesto comprimido en pocas horas.
- Y ahora la parte difícil de verdad: durante los próximos 7 días, **NO TOCAS NADA**. Los leads llegan en olas — dos días sin nada y de pronto tres seguidos es normal, no una señal. La campaña está en fase de aprendizaje (learning phase: el periodo en el que Meta aún está averiguando a quién mostrar tu anuncio), y cada edición la reinicia: vuelves a la casilla de salida, pagando.
- La única excepción: algo ROTO. Un enlace caído o el calendario fallando se arreglan en el funnel, no editando anuncios. La regla completa de cambios (duplicar, nunca editar el activo) la vemos en L7 con los datos delante.
- Tu único trabajo esta semana: responder a cada lead en <5 minutos y apuntar los datos una vez al día en el tracker de L1.

## Sección 6 — Si tu ruta es outreach

- Esta lección también es tuya, y no como cultura general: la ejecutarás tal cual cuando reinviertas tus primeros ingresos en ads — con el funnel, el VSL y la página ya calientes, llevarás medio camino hecho. De momento, guarda la checklist y céntrate en tu canal en L8-L9: la matemática de actividad de L1 es la misma, solo cambia el grifo.

## Cierre + CTA

- Recap en 2 frases: "Estructura mínima —1 campaña, 1 adset, 2-4 creativos a 30-50€/día—, el creativo como targeting, pixel probado con Claude Code y lanzamiento programado a medianoche. Después, siete días sin tocar nada: los leads llegan en olas y cada edición reinicia el aprendizaje."
- **Acción del alumno AHORA:** completa la checklist pre-lanzamiento punto por punto, programa la campaña para las 00:00 y publica la checklist marcada en la comunidad.
- **KPI de esta lección (ruta ads):** campaña activa + checklist pre-lanzamiento completa publicada.
- Puente: "Dentro de unos días tu panel estará lleno de números. En la próxima lección aprendes a leerlos como un profesional: matar, mantener o escalar — con reglas, no con sensaciones."
