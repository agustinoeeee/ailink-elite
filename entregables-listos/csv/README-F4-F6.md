# Plantillas CSV — F4 (ventas) y F6 (dashboard de dueño)

Estos CSV son la versión lista para importar de dos recursos del programa:

- `modulos/F4-cierra/recursos/tracker-ventas.md` → los dos ficheros `F4-*`
- `modulos/F6-escala/recursos/dashboard-agencia.md` → los dos ficheros `F6-*`

| Fichero | Para qué |
|---|---|
| `F4-tracker-ventas.csv` | Tabla diaria: una fila por reunión agendada, rellenada al colgar. |
| `F4-tracker-ventas-totales-semanales.csv` | Totales semanales. Trae S1, S2, S3 y S4 puestas. |
| `F6-dashboard-agencia.csv` | Los 6 números, con sus columnas «Este mes» y «Mes anterior». Los seis vienen escritos: solo rellenas las dos columnas de cifras. |
| `F6-decisiones-mes.csv` | La decisión del mes (histórico): una fila por mes. |

Los CSV **no llevan fórmulas a propósito**: el separador de fórmulas cambia según el idioma de la hoja y se rompen al importar. Las fórmulas están más abajo, para que las pegues tú.

## Cómo importarlo a Google Sheets en 3 pasos

1. Abre una hoja nueva en [sheets.new](https://sheets.new) y ve a **Archivo → Importar → Subir**. Suelta ahí el CSV.
2. En el diálogo elige **Insertar nueva hoja** (así metes un CSV por pestaña en el mismo documento) y **Tipo de separador: coma**.
3. Pulsa **Importar datos**. Renombra la pestaña, congela la fila 1 (**Ver → Inmovilizar → 1 fila**) y ya estás listo para escribir.

Los dos CSV de F4 van en el mismo documento, en dos pestañas: llámalas **`Diaria`** y **`Totales`**, que es como las nombran las fórmulas de abajo. Los dos de F6, igual, en otro documento.

> Si trabajas en Notion en vez de Sheets, no uses estos CSV: pega las tablas del `.md` directamente, que Notion las convierte solas.

## Qué significa cada columna

### F4-tracker-ventas.csv (pestaña `Diaria`)

- **Fecha** (A) — el día de la reunión.
- **Origen (ads / email / LinkedIn / llamada)** (B) — por dónde entró esa reunión.
- **¿Realizada? (sí / no-show)** (C) — el no-show también se apunta: alimenta tu show rate y te avisa si el setting de L3 se está aflojando.
- **Nivel de discovery alcanzado (1-3)** (D) — 1 superficie (datos) · 2 acción (emoción, los porqués) · 3 transformación (identidad). Si dudas entre 2 y 3, es 2.
- **Resultado (cierre / no / 2ª con socio)** (E) — «2ª con socio» solo vale si quedó agendada EN la llamada, con fecha y con ambos. «Ya me dirá algo» no es un resultado: es un no que aún no ha llegado.
- **Motivo del no** (F) — los 5 tipos de L7: dinero, miedo, confianza, momento, socio; o «no apto» si lo descartaste tú. «No sé» está prohibido: para eso tienes la transcripción.
- **Aprendizaje (1 frase)** (G) — la frase que te llevas a la siguiente llamada. Sale sola del análisis con Claude.

### F4-tracker-ventas-totales-semanales.csv (pestaña `Totales`)

- **Semana** (A) — S1, S2, S3, S4 (ya vienen puestas).
- **Agendadas** (B) · **Realizadas** (C) — reuniones.
- **Show rate (realizadas ÷ agendadas)** (D) — cuánta gente aparece de verdad.
- **Cierres** (E) — filas con resultado «cierre».
- **Close rate (cierres ÷ realizadas)** (F) — sobre realizadas, nunca sobre agendadas.
- **Motivo del no más repetido** (G) — el patrón de la semana.
- **Aprendizaje de la semana** (H) — una frase.

### F6-dashboard-agencia.csv

- **#** (A) y **Número** (B) — los 6 números, ya escritos. No los toques.
- **Qué es (en una línea)** (C) — la definición. Ahí está la unidad: € en MRR, facturación y LTV medio; % en churn y referral; ratio en LTGP:CAC.
- **De dónde sale** (D) — el tracker o la herramienta de la que lo copias.
- **Este mes** (E) y **Mes anterior** (F) — escribe **solo el número limpio** (`1200`, sin símbolo del euro ni punto de los miles) y dale formato a la columna con **Formato → Número → Moneda** o **Porcentaje**. Así las fórmulas funcionan.

### F6-decisiones-mes.csv

- **Mes** (A) — el mes que cierras.
- **Número atacado** (B) — cuál de los 6 estaba peor respecto a su benchmark.
- **Decisión (Más/Mejor/Nuevo)** (C) — UNA decisión escrita, con el marco de F0-L4.
- **Resultado al mes siguiente** (D) — se rellena 30 días después, cuando ya tienes el dato.

## Fórmulas recomendadas (pégalas tú)

> **Aviso importante:** si tu Google Sheets está en **español**, el separador de argumentos es **punto y coma (`;`)** y las funciones se llaman `SI`, `CONTAR.SI`, `CONTAR.SI.CONJUNTO`… Si está en **inglés**, es **coma (`,`)** y `IF`, `COUNTIF`, `COUNTIFS`. Abajo tienes las dos versiones: usa la que corresponda a tu hoja. Además, en una hoja en español los decimales se escriben con coma (`3,4`), no con punto.

### Show rate y close rate (pestaña `Totales`)

Show rate en **D2** (arrastra hasta D5) y luego dale formato de porcentaje:

```
=SI(B2="";"";C2/B2)     ← hoja en español
=IF(B2="","",C2/B2)     ← hoja en inglés
```

Close rate en **F2** (arrastra hasta F5), también en formato de porcentaje:

```
=SI(C2="";"";E2/C2)     /     =IF(C2="","",E2/C2)
```

### Rellenar la semana contando desde la tabla diaria

Escribe en dos celdas libres el lunes y el domingo de esa semana (por ejemplo **J2** y **K2**) y usa, en B2, C2 y E2:

```
Agendadas   =CONTAR.SI.CONJUNTO(Diaria!$A$2:$A;">="&$J2;Diaria!$A$2:$A;"<="&$K2)
Realizadas  =CONTAR.SI.CONJUNTO(Diaria!$A$2:$A;">="&$J2;Diaria!$A$2:$A;"<="&$K2;Diaria!$C$2:$C;"sí")
Cierres     =CONTAR.SI.CONJUNTO(Diaria!$A$2:$A;">="&$J2;Diaria!$A$2:$A;"<="&$K2;Diaria!$E$2:$E;"cierre")
```

En inglés, `COUNTIFS` y comas:

```
=COUNTIFS(Diaria!$A$2:$A,">="&$J2,Diaria!$A$2:$A,"<="&$K2,Diaria!$C$2:$C,"sí")
```

Escribe «sí» y «cierre» exactamente como están en la tabla: si pones «si» sin tilde, el recuento no lo ve.

### Celdas de control (en cualquier hueco de `Totales`)

```
Realizadas acumuladas   =CONTAR.SI(Diaria!C:C;"sí")           /  =COUNTIF(Diaria!C:C,"sí")
Semáforo Regla 30       =SI(CONTAR.SI(Diaria!C:C;"sí")>=30;"Ya son datos";"Continuar")
                        =IF(COUNTIF(Diaria!C:C,"sí")>=30,"Ya son datos","Continuar")
Show rate global        =CONTAR.SI(Diaria!C:C;"sí")/CONTARA(Diaria!A2:A)
                        =COUNTIF(Diaria!C:C,"sí")/COUNTA(Diaria!A2:A)
Close rate global       =CONTAR.SI(Diaria!E:E;"cierre")/CONTAR.SI(Diaria!C:C;"sí")
                        =COUNTIF(Diaria!E:E,"cierre")/COUNTIF(Diaria!C:C,"sí")
```

Motivo del no más repetido de todo el tracker:

```
=SI.ERROR(INDICE(FILTRAR(Diaria!$F$2:$F;Diaria!$F$2:$F<>"");MODA(COINCIDIR(FILTRAR(Diaria!$F$2:$F;Diaria!$F$2:$F<>"");FILTRAR(Diaria!$F$2:$F;Diaria!$F$2:$F<>"");0)));"")

=IFERROR(INDEX(FILTER(Diaria!$F$2:$F,Diaria!$F$2:$F<>""),MODE(MATCH(FILTER(Diaria!$F$2:$F,Diaria!$F$2:$F<>""),FILTER(Diaria!$F$2:$F,Diaria!$F$2:$F<>""),0))),"")
```

### Correlación nivel-resultado (el punto 4 del análisis mensual)

Dos celdas libres, formato de porcentaje:

```
Close rate llegando a nivel 3
=CONTAR.SI.CONJUNTO(Diaria!D:D;3;Diaria!E:E;"cierre")/CONTAR.SI.CONJUNTO(Diaria!D:D;3;Diaria!C:C;"sí")
=COUNTIFS(Diaria!D:D,3,Diaria!E:E,"cierre")/COUNTIFS(Diaria!D:D,3,Diaria!C:C,"sí")

Close rate quedándote en 1-2
=CONTAR.SI.CONJUNTO(Diaria!D:D;"<3";Diaria!E:E;"cierre")/CONTAR.SI.CONJUNTO(Diaria!D:D;"<3";Diaria!C:C;"sí")
=COUNTIFS(Diaria!D:D,"<3",Diaria!E:E,"cierre")/COUNTIFS(Diaria!D:D,"<3",Diaria!C:C,"sí")
```

### F6 — variación contra el mes anterior

En una columna libre **G** (arrastra de G2 a G7) y con formato de porcentaje:

```
=SI(F2="";"";E2/F2-1)     /     =IF(F2="","",E2/F2-1)
```

### F6 — los cálculos del recurso, en celdas sueltas debajo de la tabla

```
LTV medio   =SUMA(total_cobrado_por_cliente)/CONTAR(total_cobrado_por_cliente)
            =SUM(total_cobrado_por_cliente)/COUNT(total_cobrado_por_cliente)
LTGP        =LTV_medio-lo_que_te_cuesta_servirle
CAC         =gasto_de_captacion_del_periodo/clientes_cerrados_del_periodo
LTGP:CAC    =LTGP/CAC
```

El resultado de LTGP:CAC se escribe como **número limpio** (10) en la fila del número 6, que en la hoja es la fila 7, y se le da **Formato → Número → Formato personalizado** `0,0" : 1"` para que se lea `10,0 : 1`. Si lo escribes como texto («10 : 1»), el semáforo de más abajo da luz verde siempre —en una hoja de cálculo cualquier texto es mayor que cualquier número— y la variación mensual devuelve `#¡VALOR!`. Churn y referral, tal como los define su columna «Qué es»:

```
Churn de retainers  =retainers_que_se_fueron_este_mes/retainers_activos_al_empezar_el_mes
Referral %          =clientes_nuevos_por_referido/clientes_nuevos_del_mes
```

Semáforo del suelo 3:1, en una celda libre (siendo E7 tu LTGP:CAC de este mes):

```
=SI(E7>=3;"Puedes reinvertir";"Por debajo del suelo 3:1")
=IF(E7>=3,"Puedes reinvertir","Por debajo del suelo 3:1")
```

## Reglas de uso (las que ya traen los recursos)

### LA REGLA 30 (imprímela encima del tracker)

**Nada de tu proceso de ventas se juzga antes de 30 llamadas REALIZADAS.** Realizadas, no agendadas: reuniones donde te sentaste con el dueño del negocio. Por la regresión a la media (F0-L6) puedes encadenar 20-25 noes seguidos y cerrar 5 seguidas después: con menos de 30, tu close rate no es un dato, es una anécdota. Hasta la llamada 30 toca registrar, analizar cada llamada con Claude, practicar… y volver a llamar. Ni «mi oferta no funciona», ni «voy a rehacer mi framework». Volumen.

Y cuando tengas las 30, decides con Más/Mejor/Nuevo:

| Tu situación tras 30 realizadas | Decisión |
|---|---|
| Close rate en benchmark del programa (20-25%) o mejor | **MÁS**: más reuniones. No toques nada — retocar un proceso que cierra es la forma más cara de procrastinar |
| Close rate por debajo, con un patrón claro en los motivos del no | **MEJOR**: una sola mejora, entrenada en llamadas de práctica, y otras 30 llamadas para medirla |
| Tentación de cambiar de oferta, de nicho o de método | **NUEVO no existe en esta fase.** Eso es el síndrome del objeto brillante con corbata |

### Benchmarks de F4 (para leerlos, no son promesas)

Show rate 60-70% en B2B templado con la confirmación de L3 bien hecha · close rate razonable 20-25% de las reuniones realizadas · en torno a 20 conversaciones para el primer cliente. ¿Chocan el 20-25% y las ~20 conversaciones? No: las ~20 conversaciones son el escenario honesto del principiante — tus primeras 10-15 llamadas cerrarán por debajo del 20-25% mientras entrenas; ese benchmark es tu tasa en régimen, no en el arranque. **Si tu show rate cojea, el problema es de F4-L3 (setting), no de tu cierre.**

### El análisis mensual con Claude

Una vez al mes —o al cruzar las 30 realizadas, lo que llegue antes— copia el tracker completo (tabla diaria + totales) y pégaselo a Claude con el prompt exacto de `modulos/F4-cierra/recursos/tracker-ventas.md`. Tres reglas:

- **Sin muestra mínima, el veredicto es una palabra: continuar.** No dejes que nadie —ni Claude, ni tu ansiedad a las 2 de la mañana— juzgue tu proceso con 12 llamadas.
- **Ese prompt lee el bosque; el de `guia-llamadas-practica.md` lee el árbol.** Transcripción de una llamada → prompt de la guía. Mes entero de datos → el del tracker. No los mezcles.
- **Las tasas de TU tracker son TUS benchmarks personales.** Las cifras de ejemplo de las lecciones son ilustrativas; estas son de verdad, porque son tuyas.

### Benchmarks de F6

Churn **< 5%/mes** · referral % **>** churn % · **LTGP:CAC ≥ 3:1** (el suelo). El ideal al que apuntar (benchmark heredado): **captación financiada por el cliente** — que el piloto de un cliente nuevo pague el CAC del siguiente.

### El ritual mensual de F6 (30 min, día 1)

- [ ] Día 1 del mes: dashboard relleno con los trackers (F3 captación, F4 ventas, fichas F6).
- [ ] Comparado con el mes anterior: ¿qué número es el PEOR respecto a su benchmark?
- [ ] UNA decisión escrita, con Más/Mejor/Nuevo (F0-L4).
- [ ] La decisión convertida en acción con fecha en tu calendario.
- [ ] (Si toca) señal de alarma detectada → llamada de rescate agendada (F6-L4).

Cada decisión, a una fila de `F6-decisiones-mes.csv`. Rellena el dashboard en el mismo bloque en el que preparas los informes de tus clientes: 30 minutos, seis números, UNA decisión.

### Síntoma → número → palanca

No va en CSV porque es tabla de consulta, no de registro:

| Síntoma | Número que mirar | Palanca (y dónde vive) |
|---|---|---|
| «Facturo pero no crezco» | Churn de retainers | Sistema de retención y rescates → F6-L2 / F6-L4 |
| «Crezco pero sin beneficio» | LTGP:CAC | Precios con casos (F1-L6) · coste de captación (F3-L7) |
| «Todo depende de mí» | Horas por entrega | Tu fábrica de plantillas → F5-L7 |
| «Entran pocos clientes nuevos» | Referral % y CAC | Referidos en cada quincenal (F6-L5) · volumen del canal (F3) |
| «Cada mes empieza en cero» | MRR | La propuesta de retainer → F6-L3 |
| «No sé qué me pasa» | Los 6 en fila | El tramo estrecho de la tubería → F6-L7 |

> Todas las cifras de ejemplo de los recursos (los 7.600 €, el 10:1) son ilustrativas.
