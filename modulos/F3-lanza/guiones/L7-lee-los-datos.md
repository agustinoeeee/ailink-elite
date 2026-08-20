# L7 | Lee los datos como un profesional

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F3 Lanza | 12-16 min | recursos/kpis-ads-benchmarks.md |

**Objetivo:** el alumno decide con datos —matar, mantener o escalar— usando el tablero mínimo, las reglas de decisión del programa y el análisis de cuellos de botella con Claude.

## Gancho (0:00-0:20)

"La mayoría de la gente no fracasa con los anuncios por mala estrategia. Fracasa porque decide con sensaciones: un día flojo, pánico, tres ediciones — y campaña muerta. Hoy instalamos lo contrario: un tablero de seis números, cinco reglas y un método para que cada decisión salga de los datos. Esta es la lección que separa a quien quema presupuesto de quien construye una máquina."

[PANTALLA: el tracker de captación de L1 con los primeros 7 días de datos de la campaña de L6]

## Sección 1 — El tablero mínimo: seis números y nada más

- El administrador de anuncios te enseña doscientas métricas para que te pierdas. Tú miras SEIS, una vez al día, apuntadas en tu tracker:
  1. **Gasto** — cuánto ha salido.
  2. **CPM** (coste por mil impresiones) — benchmark del programa: sano entre 40-100€.
  3. **CTR link** (porcentaje de quienes ven el anuncio y hacen clic hacia tu funnel) — benchmark del programa: ≥1,5%.
  4. **Conversión de landing** (de visitante a lead) — benchmark del programa: 5-10%.
  5. **Coste por reunión agendada** — rango orientativo B2B del programa: 50-150€.
  6. **Coste por reunión REALIZADA** — el que de verdad importa: una reunión a la que no vienen no vale nada. Con el show rate en benchmark (60-70%, B2B templado), agendada y realizada van de la mano; si se separan, hay fuga.
- Se apunta siempre el día completo de ayer, nunca el de hoy a medias. Una vez al día. No diez.

## Sección 2 — Las cinco reglas de decisión (grábalas a fuego)

[PANTALLA: las cinco reglas en tarjetas, apareciendo una a una]

- **Regla 1 — Muestra mínima:** nada se juzga antes de 50 eventos o 5-7 días, lo que llegue antes. Apagar un anuncio con dos días de vida y cero reservas no es disciplina: es ansiedad. Los leads llegan en olas; un día flojo no es una señal.
- **Regla 2 — Matar:** con muestra suficiente, un creativo cuyo coste por resultado está en ≥2x tu objetivo se apaga. Y la muerte anticipada: si ha gastado 3x tu coste objetivo sin UNA sola conversión, no es mala suerte — es un anuncio roto, y ese no espera la muestra.
- **Regla 3 — La zona intermedia:** entre 1x y 2x del objetivo, ni matar ni escalar: o más datos, o diagnóstico (Sección 3).
- **Regla 4 — NUNCA editar un anuncio o adset activo.** Ni el copy, ni el enlace, ni "solo una palabra". Editar reinicia el aprendizaje y funde todo lo pagado. ¿Quieres cambiar algo? DUPLICA, cambia UNA variable en la copia y deja el original en paz. Una variable, literal: si cambias hook, audiencia y presupuesto a la vez y mejora, no sabes por qué — no estás testeando, estás adivinando.
- **Regla 5 — Escalar:** si tras la muestra mínima el coste por reunión está en objetivo y las reuniones se realizan, sube el presupuesto **+20-30% cada 2-3 días**. Ni más ni más rápido: subirlo de golpe rompe el aprendizaje y el anuncio rentable deja de serlo.

## Sección 3 — La jerarquía de diagnóstico

- Cuando algo no cuadra, no mires todo a la vez: baja por el funnel en orden, porque cada métrica enferma señala a su culpable.
  - **¿CPM por encima de 100€?** → creativo débil o página fría: a Meta no le compensa empujar tu anuncio. Revisa L5 (creativo) y L4 (calentamiento).
  - **¿CTR link por debajo de 1,5%?** → te ven pero no hacen clic: mensaje u hook. Recuerda la regla de L5 — dentro del creativo, el hook es el 80%.
  - **¿Landing por debajo del 5%?** → hacen clic pero no dejan sus datos: congruencia anuncio↔titular o fricción del formulario (L2).
  - **¿Agendan pero no se presentan (show rate <60%)?** → eso ya no es un problema de ads: es F4 — recordatorios y pre-llamada; se trabaja allí.
- El orden importa: retocar la landing cuando el problema es el hook es pintar las puertas de una casa sin cimientos.

## Sección 4 — El análisis de cuellos de botella con Claude (el método del programa)

- Aquí es donde juegas con ventaja: no interpretas los datos solo. Abre Claude, pégale la tabla de benchmarks del recurso de esta lección y, debajo, tus métricas del tracker. Pídele el diagnóstico: cuál es el cuello de botella, qué regla del programa se aplica y qué ÚNICA variable cambiar.

[PANTALLA: demo del análisis — el prompt del recurso con métricas pegadas y Claude señalando el cuello de botella y la variable a testear]

- Ejemplo con cifras ilustrativas: CPM en benchmark, CTR flojo, landing convirtiendo bien → el diagnóstico apunta al hook. Decisión: duplicar el adset, entrar con dos hooks nuevos sobre el creativo ganador y esperar la muestra mínima. Media hora de trabajo en lugar de una semana de angustia.
- El prompt completo, listo para copiar, está en `recursos/kpis-ads-benchmarks.md`. Y recuerda: los benchmarks marcan el suelo; tus datos mandan.

## Sección 5 — ¿Te acuerdas de la plantilla de tests?

- En F0 te di una plantilla de tests y te dije que se estrenaba más adelante. Es aquí. Cada duplicado es un test con todas sus piezas: hipótesis ("el cuello de botella es el hook"), variable única, muestra mínima, resultado, decisión. Apuntado, cada euro gastado te enseña algo que reutilizas; sin apuntar, repites errores carísimos con cara de sorpresa.

## Sección 6 — Ruta outreach: mismas reglas, otras columnas

- Si tu canal es el email o la llamada, esta lección es igual de tuya. Cambian las columnas del tracker —envíos o llamadas en lugar de gasto, respuestas en lugar de clics— pero el final es el mismo: reuniones agendadas y realizadas.
- Mismas reglas: muestra mínima antes de juzgar (300 toques / 30 llamadas — la regla de F0), una variable por test (¿asunto o primera línea? elige una), y a lo que funciona, MÁS volumen antes de inventar nada nuevo. La tabla equivalente está en el recurso.

## Cierre + CTA

- Recap en 2 frases: "Seis números una vez al día, muestra mínima de 50 eventos o 5-7 días, matar a 2x del objetivo, nunca editar en activo —duplicar y una variable—, escalar +20-30% cada 2-3 días. Y ante cualquier duda, análisis de cuellos de botella con Claude: los datos deciden, tú ejecutas."
- **Acción del alumno AHORA:** abre `recursos/kpis-ads-benchmarks.md`, copia el prompt de análisis y pásale a Claude los datos que ya tengas en el tracker — aunque la muestra aún no esté completa, el hábito se instala hoy.
- **KPI de esta lección:** tracker con 7 días de datos reales + primer análisis de cuellos de botella hecho con Claude.
- Puente: "Tu máquina de ads ya se pilota con reglas, no con nervios. Ahora vamos a por el canal de las rutas low-budget: el email frío que no da vergüenza — y que cumple."
