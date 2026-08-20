# Plantillas CSV — F0 (tests) y F3 (captación)

Estos CSV son la versión lista para importar de dos recursos del programa:

- `modulos/F0-bienvenido/recursos/plantilla-base-de-tests.md` → **F0-plantilla-tests.csv**
- `modulos/F3-lanza/recursos/tracker-captacion.md` → los siete ficheros `F3-*`

| Fichero | Para qué |
|---|---|
| `F0-plantilla-tests.csv` | Tu máquina de decisiones. Viene con las 3 filas del ejemplo del recurso (email frío a clínicas dentales) + 10 filas vacías. |
| `F3-matematica-actividad.csv` | Tu matemática de actividad, la que se rellena en L1. Campos fijos: solo rellenas la columna «Tu cifra». |
| `F3-tracker-email.csv` | Tabla diaria de la ruta email frío. |
| `F3-tracker-llamadas.csv` | Tabla diaria de la ruta llamadas. |
| `F3-tracker-linkedin.csv` | Tabla diaria de la ruta LinkedIn. |
| `F3-tracker-ads.csv` | Tabla diaria de la ruta Meta ads. |
| `F3-tracker-creativos.csv` | Semanal por creativo (solo ruta ads). |
| `F3-tracker-resumen-semanal.csv` | Resumen semanal, todas las rutas. Trae S1, S2 y S3 puestas. |

Los CSV **no llevan fórmulas a propósito**: el separador de fórmulas cambia según el idioma de la hoja y se rompen al importar. Las fórmulas están más abajo, para que las pegues tú.

## Cómo importarlo a Google Sheets en 3 pasos

1. Abre una hoja nueva en [sheets.new](https://sheets.new) y ve a **Archivo → Importar → Subir**. Suelta ahí el CSV.
2. En el diálogo elige **Insertar nueva hoja** (así vas metiendo un CSV por pestaña en el mismo documento) y **Tipo de separador: coma**. Deja desmarcado «Convertir texto a números y fechas» si no quieres que te reformatee las fechas a su manera.
3. Pulsa **Importar datos**. Renombra la pestaña con el nombre del canal, congela la fila 1 (**Ver → Inmovilizar → 1 fila**) y ya estás listo para escribir.

Repite con cada CSV que necesites: de F3 solo te hace falta la pestaña del canal de **tu** ruta, más el resumen semanal.

> Si trabajas en Notion en vez de Sheets, no uses estos CSV: pega las tablas del `.md` directamente, que Notion las convierte solas.

## Qué significa cada columna

### F0-plantilla-tests.csv

- **Test** — el nombre del experimento (el mismo en todas sus versiones).
- **Versión** — V1, V2, V2 bis… la iteración concreta que estás midiendo.
- **Hipótesis** — qué crees que va a pasar, con su número: «logrará ≥3% de respuesta positiva».
- **Variable que cambio** — UNA sola cosa. Si aquí hay dos, el test no vale.
- **Constantes** — todo lo que dejas quieto durante el test.
- **Métrica primaria** — el dato que decide.
- **Métrica secundaria** — el dato de apoyo, para entender el porqué.
- **KPI objetivo** — el listón, escrito ANTES de lanzar.
- **Tamaño de muestra** — cuántos toques necesitas para que sea un dato y no ruido.
- **Duración** — cuánto tiempo lo dejas correr, seguimientos incluidos.
- **Resultado** — lo que salió de verdad, apuntado a diario, no al final.
- **Decisión** — solo 3 valores: Escalar, Iterar, Volver a V anterior.

### F3-matematica-actividad.csv

- **Campo** — el concepto (ya viene escrito, no lo toques).
- **Tu cifra** — tu número. La última fila, el valor de cada toque, es objetivo ÷ toques totales.

### F3-tracker-email.csv

- **Fecha** — el día. También se apunta el día a 0: un 0 es un dato, una casilla vacía es una mentira por omisión.
- **Envíos** — emails enviados ese día.
- **Respuestas** — respuestas recibidas.
- **Reuniones agendadas** — las que quedan en el calendario.
- **Reuniones realizadas** — las que ocurren de verdad.
- **Notas** — qué cambiaste, qué rompió, qué te llamó la atención.
- Fila **TOTAL SEMANA** — el cierre semanal (fórmulas abajo).

### F3-tracker-llamadas.csv

- **Fecha** · **Llamadas** (marcadas ese día; una llamada ES un toque) · **Conversaciones con decisor** (has hablado con quien decide, no con recepción) · **Reuniones agendadas** · **Reuniones realizadas** · **Notas** · **TOTAL SEMANA**.

### F3-tracker-linkedin.csv

- **Fecha** · **Conexiones/mensajes enviados** · **Conversaciones iniciadas** (te han contestado y hay hilo) · **Reuniones agendadas** · **Reuniones realizadas** · **Notas** · **TOTAL SEMANA**.

### F3-tracker-ads.csv

- **Fecha** — el día.
- **Gasto (€)** — lo gastado ese día.
- **Impresiones** — veces que se mostró el anuncio.
- **CPM (€)** — coste por mil impresiones: gasto ÷ impresiones × 1.000.
- **Clics en el enlace** — clics en el enlace, no clics totales.
- **CTR link (%)** — clics en el enlace ÷ impresiones × 100.
- **Leads (formulario)** — personas que han dejado sus datos.
- **Reuniones agendadas** · **Reuniones realizadas** · **Notas** · **TOTAL SEMANA**.

El administrador de anuncios te da CPM y CTR hechos, pero saber de dónde salen te obliga a mirar los datos de verdad.

### F3-tracker-creativos.csv

- **Creativo (nombre/ID)** — una fila por creativo, rellenada cada semana con los datos por anuncio del administrador.
- **Gasto (€)** — lo gastado por ese creativo.
- **Resultados (leads o reuniones)** — lo que ha producido.
- **Coste por resultado (€)** — gasto ÷ resultados.
- **Decisión (matar / mantener / escalar)** — las reglas completas están en `recursos/kpis-ads-benchmarks.md` (L7).

### F3-tracker-resumen-semanal.csv

- **Semana** — S1, S2, S3… (las tres primeras ya vienen puestas).
- **Canal** — el canal de tu ruta.
- **Toques totales / Gasto** — toques si es outreach, gasto si es ads.
- **Respuestas / Clics** — respuestas si es outreach, clics si es ads.
- **CPM / CTR link (solo ads)** — se deja vacía en las rutas de outreach.
- **Agendadas** · **Realizadas** — reuniones.
- **Show rate (realizadas ÷ agendadas)** — cuánta gente aparece de verdad.
- **Aprendizaje de la semana (1 frase)** — una frase. Leída de arriba abajo dentro de un mes, esa columna es la historia de cómo tu máquina pasó de fría a rentable.

## Fórmulas recomendadas (pégalas tú)

> **Aviso importante:** si tu Google Sheets está en **español**, el separador de argumentos es **punto y coma (`;`)** y la función se llama `SUMA`. Si está en **inglés**, es **coma (`,`)** y `SUM`. Abajo tienes las dos versiones: usa la que corresponda a tu hoja. Además, en una hoja en español los decimales se escriben con coma (`3,4`), no con punto.

### Totales de las tablas diarias (email, llamadas, LinkedIn)

Datos en las filas 2 a 11, fila de totales la 12. En **B12**:

```
=SUMA(B2:B11)     ← hoja en español
=SUM(B2:B11)      ← hoja en inglés
```

Arrastra esa celda hacia la derecha hasta **E12** para cubrir las cuatro columnas numéricas. La columna **Notas** no se suma.

### Tabla de ads

Datos en las filas 2 a 11, totales en la 12.

CPM en **D2** (arrastra hasta D11):

```
=B2/C2*1000
```

CTR link en **F2** (arrastra hasta F11), formateado como número, no como porcentaje:

```
=E2/C2*100
```

Totales en la fila 12, solo en las columnas que se suman (**B, C, E, G, H, I**):

```
=SUMA(B2:B11)     /     =SUM(B2:B11)
```

**CPM y CTR no se suman nunca.** Se vuelven a calcular con los totales de la semana, en **D12** y **F12**:

```
=B12/C12*1000
=E12/C12*100
```

Y con el total semanal sacas tu **coste por reunión agendada**, en una celda libre debajo de la tabla:

```
=B12/H12
```

### Tabla por creativo

Coste por resultado en **D2** (arrastra hasta D11):

```
=B2/C2
```

### Resumen semanal

Show rate en **H2** (arrastra hacia abajo), y luego dale formato de porcentaje:

```
=G2/F2
```

### Matemática de actividad

Si en **B2** escribes tu objetivo como número limpio (`10000`, sin el símbolo del euro ni el punto de los miles) y en **B7** tus toques totales, el valor de cada toque sale solo en **B9**:

```
=B2/B7
```

Esa cifra, escríbela donde la veas cada mañana. Cada email sin respuesta y cada llamada que nadie coge también la están cobrando.

### F0 — plantilla de tests: validación en vez de fórmula

La columna **Decisión** solo admite 3 valores, así que en vez de una fórmula ponle una lista desplegable: selecciona **L5:L14** → **Datos → Validación de datos** → **Lista de elementos** y escribe:

```
Escalar, Iterar, Volver a V anterior
```

| Decisión | Cuándo | Qué haces |
|---|---|---|
| **Escalar** | Resultado en KPI o rozándolo | Repite exactamente lo mismo con más volumen. Ni un cambio. |
| **Iterar** | Resultado por debajo de KPI | Crea la siguiente versión cambiando UNA sola variable. |
| **Volver a V anterior** | La nueva versión empeoró | Recupera la versión anterior y cambia otra cosa desde ella. |

## Reglas de uso (las que ya traen los recursos)

### Reglas de validez del programa

1. **300 toques de outreach** como mínimo antes de juzgar un canal, un mensaje o una lista. Una llamada ES un toque, igual que un email o un mensaje de LinkedIn.
2. **30 llamadas de venta realizadas** (realizadas, no agendadas) como mínimo antes de juzgar tu tasa de cierre. Eso se trabaja en F4.
3. **En ads, nada se juzga antes de 50 eventos o 5-7 días.** Las reglas completas de matar/mantener/escalar están en L7 y en `recursos/kpis-ads-benchmarks.md`.
4. **Speed to lead: todo lead entrante se responde en menos de 5 minutos.** Lead = persona que ha dejado sus datos o respondido a tu mensaje. El primero en responder se lleva la mayoría de las ventas.
5. **El tracker se rellena al terminar el bloque diario**, no a final de semana de memoria. El día sin actividad también se apunta.
6. **Un cambio de variable a la vez.** Si cambias el asunto del email y el guion de la llamada la misma semana, no sabrás cuál de los dos movió el dato.

Cualquier métrica con menos muestra NO es un dato: es ruido. Con ruido no se decide nada.

### Cómo se usa la plantilla de tests

1. Antes de lanzar nada, rellena una fila entera: UNA variable a cambiar, el resto constantes, métricas y KPI definidos.
2. Lanza y no toques nada hasta completar la muestra Y la duración. Apunta las métricas cada día, no al final.
3. Al terminar, escribe el Resultado y compáralo con el KPI objetivo.
4. Decisión: ¿en KPI o cerca? → ESCALAR (más volumen, cero cambios). ¿Por debajo? → ITERAR: nueva versión cambiando una sola variable.
5. Si la nueva versión empeora, VOLVER A V ANTERIOR y cambiar otra cosa distinta desde ahí.

La plantilla se copia AHORA (para tenerla lista) y se estrena en F3, con tu primera campaña de captación.

> Las cifras del ejemplo que viene relleno en el CSV (apertura 40%, respuesta 3%) son ilustrativas, no benchmarks del programa; los KPIs reales de cada canal se dan en F3. Cuando empieces a usarlo de verdad, borra esas tres filas o déjalas arriba como referencia.

### Checklist: ¿fue un test válido? (marca las 5 antes de decidir)

- [ ] Nada técnico se rompió a mitad (links, calendario de reservas, dominio).
- [ ] No toqué nada durante el test (cero cambios emocionales a mitad).
- [ ] Registré las métricas cada día, con precisión.
- [ ] No cambié ninguna constante.
- [ ] Dejé completarse la muestra Y la duración (seguimientos incluidos).

Si falta una sola casilla, el test no vale: se repite, no se interpreta.

### Antes de pedirle el análisis a Claude

- **Si no hay muestra mínima, el análisis de la semana es una sola palabra: continuar.** No dejes que nadie —ni Claude, ni tu ansiedad— juzgue con 40 emails.
- **Las tasas que salen de TU tracker son TUS benchmarks personales.** Las cifras de ejemplo de las lecciones son ilustrativas; estas son de verdad, porque son tuyas.
- **Apunta el aprendizaje semanal en una frase.**

El prompt exacto para pasarle el tracker a Claude está en `modulos/F3-lanza/recursos/tracker-captacion.md`, en la sección «Mini-guía».
