# Tracker de captación

> Recurso de L1 (F3 Lanza). Tu cuaderno de bitácora diario hasta el primer cliente: aquí se apunta cada toque, cada día, en el canal de tu ruta. **Cópialo hoy a Google Sheets o Notion** — en Notion, pega las tablas tal cual (las convierte solas); en Sheets, crea una pestaña por canal con estas mismas columnas. El tracker no vive en tu memoria: vive por escrito, y es la materia prima del análisis con Claude de L7.

## Reglas de validez (léelas antes de juzgar NADA)

1. **300 toques antes de emitir un veredicto sobre un canal de outreach** — regla del programa, de F0. Una llamada ES un toque, igual que un email o un mensaje de LinkedIn. Con menos muestra no tienes un resultado: tienes una anécdota. (Las **30 llamadas de venta realizadas** validan otra cosa: tu tasa de cierre — eso se trabaja en F4.)
2. **En ads, nada se juzga antes de 50 eventos o 5-7 días** (benchmark del programa). Las reglas completas de matar/mantener/escalar están en L7 y en `recursos/kpis-ads-benchmarks.md`.
3. **Speed to lead: todo lead entrante se responde en menos de 5 minutos** (benchmark del programa; lead = persona que ha dejado sus datos o respondido a tu mensaje). El primero en responder se lleva la mayoría de las ventas.
4. **El tracker se rellena al terminar el bloque diario**, no a final de semana de memoria. El día sin actividad también se apunta: un 0 es un dato; una casilla vacía es una mentira por omisión.
5. **Un cambio de variable a la vez** (tu plantilla de tests de F0). Si cambias el asunto del email y el guion de la llamada la misma semana, no sabrás cuál de los dos movió el dato.

## Tu matemática de actividad (se rellena en L1)

| Campo | Tu cifra |
|---|---|
| Objetivo de los 90 días | 10.000€ acumulados (o el tuyo) |
| Valor de un cliente (calculadora de F1: piloto + proyecto + retainer) | ______ € |
| Clientes necesarios | ______ |
| Reuniones realizadas necesarias | ______ |
| Reuniones agendadas necesarias | ______ |
| Toques totales | ______ |
| Toques por día laborable | ______ |
| **Valor de cada toque (objetivo ÷ toques totales)** | ______ € |

> Esa última cifra, escríbela donde la veas cada mañana. Cada email sin respuesta y cada llamada que nadie coge también la están cobrando.

## Tabla diaria — Email frío

| Fecha | Envíos | Respuestas | Reuniones agendadas | Reuniones realizadas | Notas |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| **TOTAL SEMANA** | | | | | |

## Tabla diaria — Llamadas

| Fecha | Llamadas | Conversaciones con decisor | Reuniones agendadas | Reuniones realizadas | Notas |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| **TOTAL SEMANA** | | | | | |

## Tabla diaria — LinkedIn

| Fecha | Conexiones/mensajes enviados | Conversaciones iniciadas | Reuniones agendadas | Reuniones realizadas | Notas |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| **TOTAL SEMANA** | | | | | |

## Tabla diaria — Meta ads

| Fecha | Gasto (€) | Impresiones | CPM (€) | Clics en el enlace | CTR link (%) | Leads (formulario) | Reuniones agendadas | Reuniones realizadas | Notas |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| **TOTAL SEMANA** | | | | | | | | | |

> Cómo se derivan las dos columnas nuevas: **CPM = gasto ÷ impresiones × 1.000** · **CTR link = clics en el enlace ÷ impresiones × 100**. El administrador de anuncios te las da hechas, pero saber de dónde salen te obliga a mirar los datos de verdad. Con el total semanal calculas tu coste por reunión agendada: gasto ÷ reuniones agendadas. Los benchmarks para leerlo todo están en `recursos/kpis-ads-benchmarks.md` (L7).

## Semanal por creativo (solo ruta ads)

Una fila por creativo, rellenada cada semana con los datos por anuncio del administrador. Esta tabla alimenta directamente el análisis de cuellos de botella de L7; las reglas de decisión completas están en `recursos/kpis-ads-benchmarks.md`.

| Creativo (nombre/ID) | Gasto (€) | Resultados (leads o reuniones) | Coste por resultado (€) | Decisión (matar / mantener / escalar) |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Resumen semanal (todas las rutas)

| Semana | Canal | Toques totales / Gasto | Respuestas / Clics | CPM / CTR link (solo ads) | Agendadas | Realizadas | Show rate (realizadas ÷ agendadas) | Aprendizaje de la semana (1 frase) |
|---|---|---|---|---|---|---|---|---|
| S1 | | | | | | | | |
| S2 | | | | | | | | |
| S3 | | | | | | | | |

## Mini-guía: cómo pasarle esto a Claude para el análisis

Cada semana, con 7 días de datos en las tablas (o antes, si alcanzas la muestra mínima), copia tu tracker completo y pégaselo a Claude con este prompt:

```
Aquí tienes mi tracker de captación de la semana [X] y los benchmarks
del programa [pega aquí la tabla de recursos/kpis-ads-benchmarks.md].

Dime:
1) Mi cuello de botella principal (uno solo).
2) Qué me toca hacer según las reglas de decisión: matar, mantener,
   escalar — o seguir acumulando muestra sin tocar nada.
3) UNA sola cosa que cambiar la semana que viene, y qué dato me dirá
   si ha funcionado.

Recuerda las reglas de validez: 300 toques en outreach (una llamada
es un toque), 50 eventos o 5-7 días en ads, y un cambio de variable
a la vez.
```

Tres reglas para el análisis:

- **Si no hay muestra mínima, el análisis de la semana es una sola palabra: continuar.** No dejes que nadie — ni Claude, ni tu ansiedad — juzgue con 40 emails.
- **Las tasas que salen de TU tracker son TUS benchmarks personales.** Las cifras de ejemplo de las lecciones son ilustrativas; estas son de verdad, porque son tuyas.
- **Apunta el aprendizaje semanal en una frase.** Dentro de un mes, esa columna leída de arriba abajo es la historia de cómo tu máquina pasó de fría a rentable.
