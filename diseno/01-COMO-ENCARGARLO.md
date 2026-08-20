# Cómo encargar el diseño (para Agustín)

> Manual de uso de esta carpeta. Aquí está el flujo, los prompts listos para pegar y el orden en que conviene pedir las cosas para poder empezar a grabar cuanto antes.

## El flujo en 4 pasos

```
0. GUION DE DIAPOS        1. ENCARGO           2. DISEÑO            3. GRABACIÓN
   (un L*.md por          adjuntas 3-4         Claude Design        abres el PDF a
   lección, diapo         archivos y pegas     devuelve PDFs        pantalla completa
   a diapo)               el prompt                                 y hablas
```

**El paso 0 es la clave y es el que casi todo el mundo se salta.** Claude Design no debe decidir qué va en cada diapositiva: eso es contenido, y el contenido ya está cerrado. Por eso cada lección necesita antes un `L*.md` con el desglose **D1, D2, D3…** (como los que ya tienes en `F0-bienvenido/pizarras/`). Sin ese archivo, el diseñador inventa frases y se rompe la regla de oro del programa.

> **Estado:** F0 ya tiene sus 8 guiones de diapos. Para F1–F6 hay que generarlos (46 lecciones). Se hacen a partir de los guiones de cada lección: son un extracto, no una reescritura.

## Qué adjuntas en cada encargo

| Encargo | Adjuntas |
|---|---|
| **Pizarras de un módulo** | `00-SISTEMA-VISUAL.md` · `F*-pizarras.md` (el brief del módulo) · la carpeta `pizarras/` con los `L*.md` |
| **Entregables de un módulo** | `00-SISTEMA-VISUAL.md` · `F*-entregables.md` · la carpeta `recursos/` con los `.md` |

Nunca las dos cosas a la vez: son piezas distintas y se mezclan solas si van juntas.

---

## Prompt 1 — Pizarras de un módulo

```
Eres diseñador gráfico. Trabajas para AILINK Élite, un programa de formación
para dueños de negocio en España.

Adjunto tres cosas:
1) 00-SISTEMA-VISUAL.md — la constitución de marca y las reglas. Léela primero
   y respétala al pie de la letra, en especial la sección 4 (reglas de la pizarra)
   y la sección 7 (lista negra).
2) F[X]-pizarras.md — el brief de este módulo: qué lecciones llevan pizarra,
   cuántas diapositivas y cuál es la pieza visual clave de cada una.
3) Los archivos L1.md, L2.md… — el guion de diapositivas de cada lección,
   ya cerrado.

TAREA: diseña un PDF 16:9 (1920×1080) por lección, siguiendo exactamente el
desglose de diapositivas de su L*.md.

INNEGOCIABLES:
- El copy es literal. No reescribes, no resumes, no añades frases, no traduces
  a español neutro. Si algo no cabe, lo señalas en la entrega; no lo cambias.
- Estas slides se ven detrás de una cara en un vídeo: deja libre la esquina
  superior derecha (480×480 px) y no bajes de 28 px en ningún texto.
- Una idea por diapositiva. Un héroe visual por diapositiva.
- Cero capturas de software, cero stock, cero degradados, cero iconos 3D.

ENTREGA: un PDF por lección, nombrados F[X]-L1-pizarra.pdf, F[X]-L2-pizarra.pdf…
(Si tu herramienta exporta imágenes, PNG a 1920×1080 y las junto yo.)
Al final, una tabla: archivo de salida ↔ L*.md de origen.

Empieza por las lecciones marcadas como prioritarias en el brief y enséñame
la primera antes de seguir con el resto.
```

## Prompt 2 — Entregables de un módulo

```
Eres diseñador editorial. Trabajas para AILINK Élite, un programa de formación
para dueños de negocio en España.

Adjunto tres cosas:
1) 00-SISTEMA-VISUAL.md — la constitución de marca y las reglas. Léela primero,
   en especial la sección 5 (reglas del entregable) y la 7 (lista negra).
2) F[X]-entregables.md — el brief de este módulo: qué recurso es cada archivo,
   en qué formato sale, cuántas páginas y qué tiene que verse.
3) Los .md de la carpeta recursos/ — el contenido, ya cerrado.

TAREA: maqueta cada recurso en el formato que indica el brief (PDF A4 salvo que
diga otra cosa). Son documentos que el alumno imprime, cuelga en la pared y
rellena a bolígrafo.

INNEGOCIABLES:
- El copy es literal y completo. Si no cabe, subes a 2 páginas; no recortas.
- Rellenable de verdad: líneas de ≥8 mm, checkboxes de ≥4 mm, campos de
  formulario en el PDF si puedes.
- Funciona impreso en blanco y negro: el color refuerza, nunca es la única señal.
- Los archivos marcados "spec-no-diseñar" o "interno" NO se maquetan.

ENTREGA: un archivo por recurso, nombrados F[X]-nombre-del-recurso.pdf.
Al final, una tabla: archivo de salida ↔ .md de origen.

Empieza por los marcados como prioritarios y enséñame el primero antes de
seguir con el resto.
```

## Prompt 3 — Tablas (trackers y plantillas de hoja de cálculo)

```
Adjunto 00-SISTEMA-VISUAL.md y el .md de una plantilla de tabla del programa
AILINK Élite.

TAREA doble:
1) Un CSV listo para importar a Google Sheets: fila 1 = encabezados exactos
   del .md, fila 2 = la fila de ejemplo ya rellena que aparece en el documento,
   filas 3-12 vacías.
2) Un PDF A4 de una sola página con las reglas de uso y los benchmarks que
   acompañan a la tabla en el .md (las cajas que el alumno no puede saltarse),
   pensado para imprimir y tener al lado.

No maquetes la tabla entera como póster: su sitio es la hoja de cálculo.
Nombres: F[X]-nombre.csv y F[X]-nombre.pdf.
```

---

## Orden recomendado (para grabar antes)

1. **Pizarras de F0** ✅ (ya tienes el brief y los guiones de diapos).
2. **Entregables de F0**: manifiesto → framework → roadmap → checklist → tests.
3. **Pizarras de F1**, y grabas F1 mientras se diseñan las de F2. A partir de aquí, encadenado: mientras grabas un módulo, se diseña el siguiente.
4. Los entregables de cada módulo pueden ir un paso por detrás: el alumno los descarga, no los ves tú en cámara.

**Regla práctica:** lo que te bloquea para grabar son las pizarras. Los entregables no. Pide siempre pizarras primero.

## Cómo revisar lo que te llegue (2 minutos por pieza)

1. Abre el PDF **en el móvil**, a un palmo de la cara. ¿Se lee todo? Si entrecierras los ojos, está mal.
2. Pon un dedo sobre la esquina superior derecha. ¿Sigue entendiéndose la slide? Ahí irá tu cara.
3. Busca una frase al azar en el `.md` de origen. ¿Está literal?
4. Si es entregable: imprímelo en blanco y negro y rellena una línea a bolígrafo.

Si falla algo, no pidas "mejóralo": di exactamente qué regla del sistema visual se ha incumplido (sección y número). Es lo que hace que la segunda versión venga bien.

## Un aviso sobre el alcance

No pidas "hazme todo el programa" en un solo encargo. Módulo a módulo, y dentro del módulo, primero una pieza de muestra. Un lote de 50 PDFs mal calibrados cuesta más de arreglar que de rehacer.
