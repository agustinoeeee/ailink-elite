# Reencargos pendientes a Claude Design

> Dos cosas viven aquí: las **piezas nuevas** que nunca se han diseñado y las **piezas ya diseñadas cuyo PDF contradice a la fuente** porque el copy cambió después de entregarlas. Mientras estén en esta lista, ese PDF está caducado: no se graba con él ni se sube al alumno.
>
> Se vacía sola: cuando una pieza se rehace, se convierte y se reparte, se borra su fila.
>
> Estado a 20/08/2026 · **7 piezas nuevas · 19 piezas a rehacer · 12 archivos a renombrar (sin rediseñar)**.

## Qué ha cambiado (los cambios que provocan todo esto)

1. **La promesa.** +10.000€ → **+5.000€** de facturación acumulada a 90 días, y de 2-4 clientes a **1-3**. Decisión de Agustín, ya en la Biblia.
2. **Los ejemplos de micro-nicho.** Ahora llevan criterio de volumen: "Clínicas dentales en España que atienden +20 pacientes al día" e "Inmobiliarias de lujo que facturan +100K al mes".
3. **La anatomía de la oferta.** De 6 componentes a **7**: "red de seguridad" pasa a llamarse **garantía** y entra **urgencia**. La antigua sección de la red de seguridad AILINK la sustituye "el error que mata a la mayoría de agencias de IA".
4. **F0.** Hitos maestros movidos (primeras reuniones **S6-7**, primer cliente **S7-10**, retainer **S11-12**), el setup ya no obliga a Stripe (**método de pago** con dos condiciones) y el antídoto del error nº1 añade "sé resiliente".
5. **Tres lecciones nuevas y la renumeración que traen** (20/08/2026). F0 pasa de 8 a 9 lecciones y F1 de 7 a 9:
   - **F0-L3 «Tu norte»** — propósito, los 7 criterios de diseño del negocio y la escalera del valor.
   - **F1-L2 «Tu inventario de ventajas»** — va antes de elegir nicho; produce los candidatos que entran en la checklist.
   - **F1-L9 «De la oferta al resto del negocio»** — cierra el módulo con el scorecard y la derivación de activos.
6. **Regla nueva para los recursos del alumno:** las lecciones se citan **por nombre, nunca por número**. Es la razón por la que varias piezas caducan ahora — y la garantía de que una futura renumeración no vuelva a hacerlo.

---

## Paso 0 — Renombrar antes de nada (12 archivos, en el Mac)

Estos `.dc.html` **no se rediseñan: se renombran**. Hay que hacerlo **en orden descendente** para no pisar un archivo con otro, y **antes** de encargar las piezas nuevas — porque `F0-L03` y `F1-L02` van a pasar a ser lecciones distintas.

```
F0-L08-pizarra  →  F0-L09-pizarra
F0-L07-pizarra  →  F0-L08-pizarra
F0-L06-pizarra  →  F0-L07-pizarra
F0-L05-pizarra  →  F0-L06-pizarra
F0-L04-pizarra  →  F0-L05-pizarra
F0-L03-pizarra  →  F0-L04-pizarra

F1-L07-pizarra  →  F1-L08-pizarra
F1-L06-pizarra  →  F1-L07-pizarra
F1-L05-pizarra  →  F1-L06-pizarra
F1-L04-pizarra  →  F1-L05-pizarra
F1-L03-pizarra  →  F1-L04-pizarra
F1-L02-pizarra  →  F1-L03-pizarra
```

Los PDF del **material del alumno** no hay que renombrarlos: su prefijo de lección lo pone `componer.py` a partir del orden del JSON, así que se recolocan solos.

---

## Prioridad 1 — Piezas NUEVAS (nunca diseñadas)

### Entregables del alumno

| Pieza | Fuente | Qué es |
|---|---|---|
| `F0-norte-personal.pdf` | `modulos/F0-bienvenido/recursos/norte-personal.md` | A4, 2 páginas. Las 5 preguntas del contexto de vida, la tabla de los 7 criterios con columna «implicación para mi oferta», la escalera del valor y la declaración de propósito |
| `F1-inventario-ventajas.pdf` | `modulos/F1-domina/recursos/inventario-ventajas.md` | A4, 2 páginas. Inventario de hechos, los seis cajones, la matriz de 6 factores con su tabla de candidatos y la frase de ventaja |
| `F1-catalogo-oportunidades.pdf` | `modulos/F1-domina/recursos/catalogo-oportunidades.md` | A4, 2-3 páginas. Las 8 capas, las 8 áreas de oportunidad por tipo de negocio, la anatomía del proceso y «cuándo no automatizar todavía» |
| `F1-scorecard-oferta.pdf` | `modulos/F1-domina/recursos/scorecard-oferta.md` | A4, 2 páginas. Los 14 criterios a 0/1/2, la barra de lectura de puntuación, la tabla de derivación y los tres activos |

### Pizarras de grabación (16:9)

| Pieza | Fuente | Diapos |
|---|---|---|
| `F0-L03-pizarra.pdf` | `F0-bienvenido/pizarras/L3.md` | 5 — D2, D3 y D4 son los mismos bloques del A4 del norte personal: reutiliza la composición |
| `F1-L02-pizarra.pdf` | `F1-domina/pizarras/L2.md` | 6 — D4 (los seis cajones) y D5 (la matriz) reutilizan la composición del worksheet |
| `F1-L09-pizarra.pdf` | `F1-domina/pizarras/L9.md` | 5 — D1 es un diagrama radial; D4 reutiliza la barra de lectura del scorecard |

## Prioridad 2 — Material del alumno a rehacer

*(el nombre de archivo que se sube lo recalcula `componer.py`; aquí van los nombres de origen)*

| PDF a sustituir | Fuente | Qué ha cambiado |
|---|---|---|
| `F0-roadmap-90-dias` | `F0-bienvenido/recursos/roadmap-90-dias.md` | Los 3 hitos con semanas nuevas, la nota del hito 4 y **las filas S6 a S10** de la tabla semana a semana (los 🏆 se mueven a S7, S10 y S12) |
| `F0-checklist-setup-negocio` | `F0-bienvenido/recursos/checklist-setup-negocio.md` | El paso 4 pasa de "Stripe" a **método de pago**, con las dos condiciones (enlace de pago + guardar el método). La cabecera y el comprobante final citan la lección por nombre |
| `F0-manifiesto-90-dias` | `F0-bienvenido/recursos/manifiesto-90-dias.md` | **Cambio mínimo:** la cabecera decía «Vinculado a la lección F0-L3» y ahora dice «la lección de señal vs ruido». Nada más |
| `F0-plantilla-base-de-tests` | `F0-bienvenido/recursos/plantilla-base-de-tests.md` | **Cambio mínimo:** la cabecera cita la lección por nombre, sin número |
| `F1-checklist-validacion-nicho` | `F1-domina/recursos/checklist-validacion-nicho.md` | "te bastan **1-3 clientes**" · bloque nuevo al principio con las tres puntuaciones que trae el candidato desde la matriz de ventajas · señal de alarma nueva («elegido porque tiene dinero», la lista pasa de 3 a 4) |
| `F1-avatar-cliente-ideal` | `F1-domina/recursos/avatar-cliente-ideal.md` | **Rehecho casi entero.** Parte 1 nueva (los cuatro roles) · dos campos nuevos en el avatar y uno en el negocio · el test de la escena · **Parte 4 nueva: la brecha y el disparador** · las 8 preguntas de descubrimiento · la escala de evidencia · checklist de cierre ampliada a 7 casillas |
| `F1-calculadora-pricing` | `F1-domina/recursos/calculadora-pricing.md` | **Pasa de 5 a 6 pasos:** entra el **Paso 3, el suelo** (coste de diagnóstico, construcción, herramientas, imprevistos y soporte + margen) con su bloque en el ejemplo relleno y en la calculadora en blanco. Los pasos 3-5 antiguos se desplazan a 4-6 |
| `F1-worksheet-oferta` | `F1-domina/recursos/worksheet-oferta.md` | Paso 5 es **Garantía** y suma dos campos (qué pone el cliente, qué revisa una persona) · Paso 4 suma «primera señal de que funciona» · **Paso 8 — Urgencia** con la alternativa actual · Paso 9 con «el siguiente paso» · tres casillas nuevas en la checklist de calidad |
| `F1-ejemplos-ofertas` | `F1-domina/recursos/ejemplos-ofertas.md` | "garantía" en lugar de "red de seguridad" · referencias por nombre · **bloque nuevo al final: el caso completo de ingeniería inversa**, de «hago chatbots» a una oferta concreta, en cinco pasos |
| `F1-lista-micro-nichos-espana` | `F1-domina/recursos/lista-micro-nichos-espana.md` | **Cambio mínimo:** la cabecera cita la lección por nombre |
| `F1-cuaderno-f1` | `F1-domina/recursos/cuaderno-f1.md` | Las tres secciones se titulan por el nombre de su lección y la cabecera menciona el inventario de ventajas entre los worksheets del módulo |

## Prioridad 3 — Pizarras de grabación a rehacer

*(numeración **nueva**: renombra primero, según el paso 0, y rehaz después)*

| PDF a sustituir | Fuente | Qué ha cambiado |
|---|---|---|
| `F0-L01-pizarra` | `F0-bienvenido/pizarras/L1.md` | D3: **+5.000 €** |
| `F0-L06-pizarra` *(era L05)* | `F0-bienvenido/pizarras/L6.md` | D5: "Aguantar la fase fea. **Sé resiliente.**" |
| `F0-L08-pizarra` *(era L07)* | `F0-bienvenido/pizarras/L8.md` | D3: los tres hitos con semanas nuevas |
| `F0-L09-pizarra` *(era L08)* | `F0-bienvenido/pizarras/L9.md` | D2, pieza 4: **método de pago (Stripe, PayPal, Wise…)** |
| `F1-L01-pizarra` | `F1-domina/pizarras/L1.md` | D5: el mapa del módulo pasa de 4 a **5 pasos** — VENTAJA → NICHO → AVATAR → OFERTA → PRECIO, con la numeración de lección nueva |
| `F1-L03-pizarra` *(era L02)* | `F1-domina/pizarras/L3.md` | D2: los dos ejemplos de micro-nicho · D4: promesa 5.000€ → 1-3 clientes, y el pie |
| `F1-L04-pizarra` *(era L03)* | `F1-domina/pizarras/L4.md` | **Pasa de 4 a 6 diapos:** D2 nueva (quién es quién) · D3 suma la escalera de la escena en letra pequeña · **D5 nueva (la brecha y el disparador)** |
| `F1-L05-pizarra` *(era L04)* | `F1-domina/pizarras/L5.md` | D4: **7 componentes** y letra pequeña nueva sobre contra quién compites · D5: nueva frase B · **D6 entera** es otra ("el error que mata a la mayoría de agencias IA") |
| `F1-L06-pizarra` *(era L05)* | `F1-domina/pizarras/L6.md` | D3: "el piloto ES tu **garantía**" · D5: letra pequeña nueva sobre precios prémium |
| `F1-L07-pizarra` *(era L06)* | `F1-domina/pizarras/L7.md` | **Pasa de 6 a 7 diapos: D5 nueva, «suelo y techo»** — la barra con el suelo (coste + margen) a un lado y el techo (valor ÷ 5) al otro |
| `F1-L08-pizarra` *(era L07)* | `F1-domina/pizarras/L8.md` | D1: sin pie y con la pantalla real a **8 pasos** (garantía y urgencia dentro) |
| `F3-L01-pizarra` | `F3-lanza/pizarras/L1.md` | D3: la cadena entera — `5.000 € → 2 clientes → 8 realizadas → 12-13 agendadas → ~600 toques → 10-12 toques al día` |

### Avisos de encaje para el diseñador

- **F1-L03 D2**: las dos líneas de ejemplo son ahora bastante más largas (107 y 93 caracteres, antes 79 y 72). Las tarjetas estaban calculadas para dos líneas de 42 px.
- **F1-L05**: D4 pasa de 6 a 7 ítems con su línea de apoyo cada uno, y D6 es un bloque de texto más largo que la media del sistema.
- **F1-inventario-ventajas**: la tabla de hechos necesita filas altas —el alumno escribe frases, no palabras— y la matriz de candidatos tiene que caber entera en una página, sin partirse.
- **F1-scorecard-oferta**: las casillas 0/1/2 tienen que poder marcarse a bolígrafo y el total sobre 28 verse desde lejos.

Si algo no cabe, la regla de siempre: se señala en la entrega, **no se recorta el copy**.

## Lo que NO hay que rehacer

- **`F0-L02`, `F0-L04`, `F0-L05`, `F0-L07`, `F1-L02`… en su versión antigua**: las pizarras que solo cambian de número **se renombran y ya está** (paso 0). Su copy es idéntico.
- **`F0-framework-mas-mejor-nuevo`**: no cita ninguna lección por número y su copy no ha cambiado.
- **`F4-L06`** (Stripe enviando el Payment Link) y las demás pantallas reales con Stripe: la grabación se hace con Stripe, que sigue siendo la pasarela recomendada. El copy de las diapos no dice que sea obligatoria.
- **El tracker de captación de F3**: su objetivo de 90 días ya está a 5.000€, pero se entrega en CSV y ese archivo ya está regenerado. No tiene PDF.
- **La propuesta de retainer de F6**: se ha matizado "(Stripe o la pasarela que uses)", pero es un `.md` sin PDF asociado.

---

## Cómo se reencarga

Mismo flujo que `01-COMO-ENCARGARLO.md`. Adjunta `00-SISTEMA-VISUAL.md`, el brief del módulo (`F*-pizarras.md` o `F*-entregables.md`) y los `.md` de las piezas afectadas — los de este repo, que ya están corregidos.

Para las **piezas nuevas**, encargo normal. Para las que se rehacen, este prompt:

```
Eres diseñador gráfico de AILINK Élite. Ya diseñaste estas piezas; el copy
ha cambiado y hay que rehacerlas.

Adjunto: 00-SISTEMA-VISUAL.md (la constitución de marca), el brief del módulo
y los archivos fuente ya corregidos.

TAREA: rehaz SOLO las piezas que te indico, con el mismo sistema visual y el
mismo formato que las anteriores (pizarra = PDF 16:9 1920×1080 con revelado
paso a paso; entregable = PDF A4).

INNEGOCIABLES:
- El copy es literal: no reescribes, no resumes, no añades frases. Si algo no
  cabe, lo señalas en la entrega; no lo cambias.
- Mantén la composición de la versión anterior salvo donde el cambio de copy
  obligue a reflotar. No es un rediseño: es una corrección.
- Devuelve los PDF con el mismo nombre de archivo que tenían.
```

Después, en local:

```bash
python3 herramientas/convertir.py "~/Desktop/AILINK Élite. Formación visual"
```

```bash
python3 herramientas/componer.py
```

> ⚠️ **`componer.py` borra y rehace `adjuntos-skool/` y `pizarras-grabacion/` enteras a partir de `pdf-convertidos/`.** Ejecútalo solo en la máquina que tenga esa carpeta con TODOS los PDF; si la carpeta está incompleta, te quedas sin los adjuntos que ya estaban repartidos.
