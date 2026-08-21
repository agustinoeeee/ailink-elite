# Tracker de ventas

> Recurso de L8 (F4 Cierra). El cuaderno de bitácora de tus llamadas de venta: una fila por reunión agendada, rellenada al colgar. **Cópialo hoy a Google Sheets o Notion** — en Notion pega las tablas tal cual; en Sheets, una pestaña para la tabla diaria y otra para los totales. Es el hermano de tu tracker de captación de F3: aquel mide cómo entran las reuniones; este mide qué haces con ellas.

## LA REGLA 30 (imprímela encima del tracker)

> **Nada de tu proceso de ventas se juzga antes de 30 llamadas REALIZADAS.** Realizadas, no agendadas: reuniones donde te sentaste con el dueño del negocio. Por la regresión a la media (F0-L7): puedes encadenar 20-25 noes seguidos y cerrar 5 seguidas después — con menos de 30, tu close rate no es un dato, es una anécdota. Hasta la llamada 30: registrar, analizar cada llamada con Claude, practicar… y volver a llamar. Ni "mi oferta no funciona", ni "voy a rehacer mi framework". Volumen.

Y cuando tengas las 30, el marco Más/Mejor/Nuevo (F0, de Alex Hormozi) decide:

| Tu situación tras 30 realizadas | Decisión |
|---|---|
| Close rate en benchmark del programa (20-25%) o mejor | **MÁS**: más reuniones. No toques nada — retocar un proceso que cierra es la forma más cara de procrastinar |
| Close rate por debajo, con un patrón claro en los motivos del no | **MEJOR**: una sola mejora, entrenada en llamadas de práctica, y otras 30 llamadas para medirla |
| Tentación de cambiar de oferta, de nicho o de método | **NUEVO no existe en esta fase.** Eso es el síndrome del objeto brillante con corbata |

## Tabla diaria — una fila por reunión

| Fecha | Origen (ads / email / LinkedIn / llamada) | ¿Realizada? (sí / no-show) | Nivel de discovery alcanzado (1-3) | Resultado (cierre / no / 2ª con socio) | Motivo del no | Aprendizaje (1 frase) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

Cómo rellenarla sin mentirte:

- **¿Realizada?**: un no-show también se apunta — alimenta tu show rate y te avisa si el setting de L3 se está aflojando.
- **Nivel de discovery**: 1 superficie (datos) · 2 acción (emoción, los porqués) · 3 transformación (identidad). Sé honesto; si dudas entre 2 y 3, es 2. El análisis de Claude de cada llamada te lo confirma con citas.
- **Resultado**: "2ª con socio" solo vale si la segunda llamada quedó agendada EN la llamada, con fecha y con ambos. "Ya me dirá algo" no es un resultado: es un no que aún no ha llegado.
- **Motivo del no**: usa los 5 tipos de L7 — dinero, miedo, confianza, momento, socio — o "no apto" si lo descartaste tú. "No sé" está prohibido: para eso está la transcripción.
- **Aprendizaje**: una frase, la que te llevas a la siguiente llamada. Sale sola del análisis con Claude.

## Totales semanales

| Semana | Agendadas | Realizadas | Show rate (realizadas ÷ agendadas) | Cierres | Close rate (cierres ÷ realizadas) | Motivo del no más repetido | Aprendizaje de la semana |
|---|---|---|---|---|---|---|---|
| S1 | | | | | | | |
| S2 | | | | | | | |
| S3 | | | | | | | |
| S4 | | | | | | | |

Benchmarks del programa para leerlos (no promesas): show rate 60-70% en B2B templado con la confirmación de L3 bien hecha · close rate razonable 20-25% de las reuniones realizadas · en torno a 20 conversaciones para el primer cliente. ¿Chocan el 20-25% y las ~20 conversaciones? No: las ~20 conversaciones son el escenario honesto del principiante — tus primeras 10-15 llamadas cerrarán por debajo del 20-25% mientras entrenas; ese benchmark es tu tasa en régimen, no en el arranque. Si tu show rate cojea, el problema es de F4-L3 (setting), no de tu cierre.

## Prompt de análisis mensual con Claude

Una vez al mes — o al cruzar las 30 realizadas, lo que llegue antes — copia tu tracker completo (tabla diaria + totales) y pégaselo a Claude con esto:

```
Eres el coach de ventas del programa AILINK Élite. Te pego mi tracker
de ventas del último mes. Contexto: vendo soluciones de IA (software y
automatizaciones con Claude Code) a negocios españoles; mi proceso es
rapport → marco → discovery (3 niveles: superficie, acción,
transformación) → pitch con demo en vivo → cierre con enlace de pago
en la propia llamada. Una llamada por lead (única excepción:
segunda llamada con el socio decisor, agendada en vivo).

Benchmarks del programa: show rate 60-70% · close rate razonable
20-25% sobre reuniones REALIZADAS · nada se juzga antes de 30
llamadas realizadas.

Analiza y respóndeme exactamente esto, en este orden:

1) VALIDEZ: ¿tengo ya 30 llamadas realizadas? Si NO, tu análisis
   termina aquí con una sola palabra: "continuar". No juzgues tasas
   con muestra insuficiente aunque yo te lo pida.
2) MIS NÚMEROS: show rate y close rate del periodo, comparados con
   el benchmark. Señala también la tendencia semana a semana.
3) EL PATRÓN DE LOS NOES: qué motivo del no se repite más y qué
   nivel de discovery alcanzo en las llamadas que pierdo.
4) CORRELACIÓN NIVEL-RESULTADO: compara mi close rate cuando llego
   al nivel 3 frente a cuando me quedo en 1-2, y dime qué implica.
5) SHOW RATE: si está bajo 60%, el problema es mi setting
   (confirmación, reunión a menos de 24-48h), no mi cierre — dímelo.
6) DECISIÓN MÁS/MEJOR/NUEVO: según todo lo anterior, ¿me toca MÁS
   volumen sin tocar nada, o MEJORAR una sola cosa concreta? Si es
   mejorar: cuál exactamente, cómo la entreno en llamadas de
   práctica y qué dato del tracker me dirá el mes que viene si ha
   funcionado. Recuerda: NUEVO no es una opción en esta fase.

Reglas: básate solo en los datos que te paso, sin inventar; si una
columna está vacía o inconsistente, señálalo como problema de
registro; sé directo, sin ánimos genéricos — quiero el análisis que
me daría un director comercial exigente.

MI TRACKER:
[PEGA AQUÍ LA TABLA DIARIA Y LOS TOTALES SEMANALES]
```

Tres reglas para el análisis:

- **Sin muestra mínima, el veredicto es una palabra: continuar.** No dejes que nadie — ni Claude, ni tu ansiedad a las 2 de la mañana — juzgue tu proceso con 12 llamadas.
- **Este prompt lee el bosque; el de `guia-llamadas-practica.md` lee el árbol.** Transcripción de una llamada → prompt de la guía. Mes entero de datos → este. No los mezcles.
- **Las tasas de TU tracker son TUS benchmarks personales.** Las cifras de ejemplo de las lecciones son ilustrativas; estas son de verdad, porque son tuyas.
