# Plantilla base de tests

> Recurso de F0 · vinculado a la lección «Cómo se decide aquí: datos, no sensaciones».
> Copia la tabla a Google Sheets o Notion y trabaja siempre ahí. Esta es tu máquina de decisiones: aquí no se opina, se testea.

## Cómo se usa (5 líneas)

1. Antes de lanzar nada, rellena una fila entera: UNA variable a cambiar, el resto constantes, métricas y KPI definidos.
2. Lanza y no toques nada hasta completar la muestra Y la duración. Apunta las métricas cada día, no al final.
3. Al terminar, escribe el Resultado y compáralo con el KPI objetivo.
4. Decisión: ¿en KPI o cerca? → ESCALAR (más volumen, cero cambios). ¿Por debajo? → ITERAR: nueva versión cambiando una sola variable.
5. Si la nueva versión empeora, VOLVER A V ANTERIOR y cambiar otra cosa distinta desde ahí.

> Esta plantilla se copia AHORA (para tenerla lista) y se estrena en F3, con tu primera campaña de captación. No necesitas usarla antes.

## Las 2 reglas de validez (benchmark del programa)

- [ ] **300 toques de outreach** como mínimo antes de juzgar un canal, un mensaje o una lista.
- [ ] **30 llamadas de venta realizadas** (no agendadas: realizadas) como mínimo antes de juzgar tu tasa de cierre.

Cualquier métrica con menos muestra NO es un dato: es ruido. Con ruido no se decide nada.

## La tabla (cópiala tal cual a Sheets/Notion)

| Test | Versión | Hipótesis | Variable que cambio | Constantes | Métrica primaria | Métrica secundaria | KPI objetivo | Tamaño de muestra | Duración | Resultado | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |

**La columna Decisión solo admite 3 valores:**

| Decisión | Cuándo | Qué haces |
|---|---|---|
| **Escalar** | Resultado en KPI o rozándolo | Repite exactamente lo mismo con más volumen. Ni un cambio. |
| **Iterar** | Resultado por debajo de KPI | Crea la siguiente versión cambiando UNA sola variable. |
| **Volver a V anterior** | La nueva versión empeoró | Recupera la versión anterior y cambia otra cosa desde ella. |

## Ejemplo relleno — outreach de email frío B2B (clínicas dentales)

| Test | Versión | Hipótesis | Variable que cambio | Constantes | Métrica primaria | Métrica secundaria | KPI objetivo | Tamaño de muestra | Duración | Resultado | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Email frío dentales | V1 | Un asunto con el nombre de la clínica logrará ≥3% de respuesta positiva | Asunto del email | Lista (misma fuente), cuerpo, firma, dominio, horario de envío, secuencia de 4 seguimientos | Tasa de apertura | Respuesta positiva | Apertura ≥40% · Respuesta ≥3% | 300 emails | 3 días de envío + 14 de seguimientos | Apertura 44% · Respuesta 1,8% | Iterar → V2 |
| Email frío dentales | V2 | Una primera línea con un dato del negocio del lead subirá la respuesta a ≥3% | Primera línea del cuerpo | Todo igual que V1, incluido el asunto de V1 (que ya cumplió su KPI de apertura: 44% ≥ 40%) | Tasa de apertura | Respuesta positiva | Apertura ≥40% · Respuesta ≥3% | 300 emails | 3 días + 14 días | Apertura 43% · Respuesta 1,1% | Volver a V anterior (V1) |
| Email frío dentales | V2 bis (desde V1) | Una CTA de «vídeo demo de 3 min» en vez de «llamada de 30 min» subirá la respuesta a ≥3% | CTA final | Todo igual que V1 | Tasa de apertura | Respuesta positiva | Apertura ≥40% · Respuesta ≥3% | 300 emails | 3 días + 14 días | Apertura 45% · Respuesta 3,4% | Escalar |

Lectura del ejemplo en 3 frases: V1 se quedó corta en respuesta → se iteró UNA variable. V2 empeoró → no se construye una V3 sobre ella: se vuelve a V1 y se cambia otra cosa. La nueva versión entra en KPI → se escala: el mismo email, a más volumen.

> Las cifras del ejemplo (apertura 40%, respuesta 3%) son ilustrativas, no benchmarks del programa; los KPIs reales de cada canal se dan en F3.

## Checklist: ¿fue un test válido? (marca las 5 antes de decidir)

- [ ] Nada técnico se rompió a mitad (links, calendario de reservas, dominio).
- [ ] No toqué nada durante el test (cero cambios emocionales a mitad).
- [ ] Registré las métricas cada día, con precisión.
- [ ] No cambié ninguna constante.
- [ ] Dejé completarse la muestra Y la duración (seguimientos incluidos).

Si falta una sola casilla, el test no vale: se repite, no se interpreta.
