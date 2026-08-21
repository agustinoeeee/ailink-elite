# Reencargos pendientes a Claude Design

> Dos cosas viven aquí: las **piezas nuevas** que nunca se han diseñado y las **piezas ya diseñadas cuyo PDF contradice a la fuente** porque el copy cambió después de entregarlas. Mientras estén en esta lista, ese PDF está caducado: no se graba con él ni se sube al alumno.
>
> Se vacía sola: cuando una pieza se rehace, se convierte y se reparte, se borra su fila.
>
> Estado a 21/08/2026 · **5 piezas nuevas · 14 piezas a rehacer**. El renombrado (paso 0) está hecho y el Bloque 1 · F0 está entregado, convertido y repartido.

## Qué ha cambiado (los cambios que provocan todo esto)

1. **La promesa.** +10.000€ → **+5.000€** de facturación acumulada a 90 días, y de 2-4 clientes a **1-3**. Decisión de Agustín, ya en la Biblia.
2. **Los ejemplos de micro-nicho.** Ahora llevan criterio de volumen: "Clínicas dentales en España que atienden +20 pacientes al día" e "Inmobiliarias de lujo que facturan +100K al mes".
3. **La anatomía de la oferta.** De 6 componentes a **7**: "red de seguridad" pasa a llamarse **garantía** y entra **urgencia**. La antigua sección de la red de seguridad AILINK la sustituye "el error que mata a la mayoría de agencias de IA".
4. **F0.** Hitos maestros movidos (primeras reuniones **S6-7**, primer cliente **S7-10**, retainer **S11-12**), el setup ya no obliga a Stripe (**método de pago** con dos condiciones) y el antídoto del error nº1 añade "sé resiliente".
5. **Tres lecciones nuevas y la renumeración que traen** (20/08/2026). F0 pasa de 8 a 9 lecciones y F1 de 7 a 9:
   - **F0-L3 «Tu norte»** — propósito, los 7 criterios de diseño del negocio y la escalera del valor.
   - **F1-L2 «Tu inventario de ventajas»** — va antes de elegir nicho; produce los candidatos que entran en la checklist.
   - **F1-L9 «De la oferta al resto del negocio»** — cierra el módulo con la revisión de la oferta y la derivación de activos.
6. **Regla nueva para los recursos del alumno:** las lecciones se citan **por nombre, nunca por número**. Es la razón por la que varias piezas caducan ahora — y la garantía de que una futura renumeración no vuelva a hacerlo.

---

## Paso 0 — Renombrar (HECHO el 21/08/2026)

Los 12 archivos se renombraron en orden descendente en la carpeta de trabajo, dejando libres `F0-L3`, `F1-L2` y `F1-L9`. Verificado que el contenido de cada uno casa con su número nuevo. Copia de seguridad previa en `~/Desktop/formacion-visual-ANTES-de-renumerar.tgz`.

---

## Prioridad 1 — Piezas NUEVAS (nunca diseñadas)

### Entregables del alumno

| Pieza | Fuente | Qué es |
|---|---|---|
| `F1-inventario-ventajas.pdf` | `modulos/F1-domina/recursos/inventario-ventajas.md` | A4, 2 páginas. Inventario de hechos, los seis cajones, la matriz de 6 factores con su tabla de candidatos y la frase de ventaja |
| `F1-catalogo-oportunidades.pdf` | `modulos/F1-domina/recursos/catalogo-oportunidades.md` | A4, 2-3 páginas. Las 8 capas, las 8 áreas de oportunidad por tipo de negocio, la anatomía del proceso y «cuándo no automatizar todavía» |
| `F1-revision-oferta.pdf` | `modulos/F1-domina/recursos/revision-oferta.md` | A4, 2 páginas. Los 14 criterios a 0/1/2, la barra de lectura de puntuación, la tabla de derivación y los tres activos |

### Pizarras de grabación (16:9)

| Pieza | Fuente | Diapos |
|---|---|---|
| `F1-L02-pizarra.pdf` | `F1-domina/pizarras/L2.md` | 6 — D4 (los seis cajones) y D5 (la matriz) reutilizan la composición del worksheet |
| `F1-L09-pizarra.pdf` | `F1-domina/pizarras/L9.md` | 5 — D1 es un diagrama radial; D4 reutiliza la barra de lectura de la puntuación |

## Prioridad 2 — Material del alumno a rehacer

*(el nombre de archivo que se sube lo recalcula `componer.py`; aquí van los nombres de origen)*

| PDF a sustituir | Fuente | Qué ha cambiado |
|---|---|---|
| `F1-checklist-validacion-nicho` | `F1-domina/recursos/checklist-validacion-nicho.md` | "te bastan **1-3 clientes**" · bloque nuevo al principio con las tres puntuaciones que trae el candidato desde la matriz de ventajas · señal de alarma nueva («elegido porque tiene dinero», la lista pasa de 3 a 4) |
| `F1-avatar-cliente-ideal` | `F1-domina/recursos/avatar-cliente-ideal.md` | **Rehecho casi entero.** Parte 1 nueva (los cuatro roles) · dos campos nuevos en el avatar y uno en el negocio · el test de la escena · **Parte 4 nueva: la brecha y el disparador** · las 8 preguntas de descubrimiento · la escala de evidencia · checklist de cierre ampliada a 7 casillas |
| `F1-worksheet-oferta` | `F1-domina/recursos/worksheet-oferta.md` | Paso 5 es **Garantía** y suma dos campos (qué pone el cliente, qué revisa una persona) · Paso 4 suma «primera señal de que funciona» · **Paso 8 — Urgencia** con la alternativa actual · Paso 9 con «el siguiente paso» · tres casillas nuevas en la checklist de calidad |
| `F1-ejemplos-ofertas` | `F1-domina/recursos/ejemplos-ofertas.md` | "garantía" en lugar de "red de seguridad" · referencias por nombre · **bloque nuevo al final: el caso completo de ingeniería inversa**, de «hago chatbots» a una oferta concreta, en cinco pasos |
| `F1-lista-micro-nichos-espana` | `F1-domina/recursos/lista-micro-nichos-espana.md` | **Cambio mínimo:** la cabecera cita la lección por nombre |
| `F1-cuaderno-f1` | `F1-domina/recursos/cuaderno-f1.md` | Las tres secciones se titulan por el nombre de su lección y la cabecera menciona el inventario de ventajas entre los worksheets del módulo |

## Prioridad 3 — Pizarras de grabación a rehacer

*(numeración **nueva**: renombra primero, según el paso 0, y rehaz después)*

| PDF a sustituir | Fuente | Qué ha cambiado |
|---|---|---|
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
- **F1-revision-oferta**: las casillas 0/1/2 tienen que poder marcarse a bolígrafo y el total sobre 28 verse desde lejos.

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
