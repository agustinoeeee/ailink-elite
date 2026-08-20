# Segunda tanda para Claude Design — los 25 entregables que faltan

> **Qué ya entregó:** las 54 pizarras (F0-F6, completas) y 17 entregables (F0, F1 y F2, completos). Todo eso está validado y convertido a PDF.
>
> **Qué falta:** los entregables de F3, F4, F5 y F6. Nada más.
>
> Ábrele otra vez la carpeta `programa-ia` entera. Pega el prompt tal cual.

```
Seguimos con AILINK Élite. Ya me entregaste las 54 pizarras y los entregables
de F0, F1 y F2 — están validados, no hay que tocarlos. Falta la segunda mitad
de los entregables: F3, F4, F5 y F6. Mismas reglas de siempre.

ANTES DE EMPEZAR
Relee diseno/00-SISTEMA-VISUAL.md. Lo que hiciste en F0-F2 es la referencia:
misma retícula, misma tipografía, mismos colores, mismo tratamiento de las
líneas para rellenar a mano. Esto tiene que parecer el mismo programa.

QUÉ DISEÑAR (25 piezas, todas ENTREGABLE A4 — ninguna es pizarra)

F3 Lanza — brief en diseno/F3-entregables.md · contenido en modulos/F3-lanza/recursos/
  F3-checklist-funnel.pdf        (A4, 2 pág)
  F3-guion-vsl.pdf               (A4, 3 pág)
  F3-banco-creativos-b2b.pdf     (A4, 6 pág)
  F3-kpis-ads-benchmarks.pdf     (A4 HORIZONTAL, 4 pág)
  F3-plantillas-email-frio.pdf   (A4, 4 pág)
  F3-guion-llamada-b2b.pdf       (A4, 4 pág)
  F3-rgpd-captacion.pdf          (A4 HORIZONTAL, 3 pág)

F4 Cierra — brief en diseno/F4-entregables.md · contenido en modulos/F4-cierra/recursos/
  F4-rutina-estado.pdf · F4-checklist-setting-show.pdf · F4-framework-llamada.pdf
  F4-guia-discovery.pdf · F4-guia-objeciones.pdf · F4-guia-llamadas-practica.pdf

F5 Entrega — brief en diseno/F5-entregables.md · contenido en modulos/F5-entrega/recursos/
  F5-guion-llamada-arranque.pdf · F5-acuerdo-servicios-esqueleto.pdf
  F5-plan-comunicacion-build.pdf · F5-checklist-entrega-produccion.pdf
  F5-guia-testimonio-referido.pdf · F5-biblioteca-plantillas.pdf

F6 Escala — brief en diseno/F6-entregables.md · contenido en modulos/F6-escala/recursos/
  F6-cadencia-retencion.pdf · F6-guion-llamada-quincenal.pdf
  F6-propuesta-retainer.pdf · F6-guiones-rescate.pdf
  F6-guia-referidos-upsells.pdf · F6-mapa-post-programa.pdf

El brief de cada módulo trae, pieza a pieza, el formato, las páginas y la
dirección de arte. El número de páginas es orientativo: si el contenido pide
una más, la pones; lo que no se toca es el copy.

LAS REGLAS QUE NO CAMBIAN
- El copy es literal, sale del .md. No reescribes, no resumes, no acortas, no
  "mejoras" el tono. Español de España, tuteo. Si algo no cabe, lo señalas en
  la entrega; no lo cambias.
- Entregable = A4 que el alumno imprime y rellena a bolígrafo: líneas ≥8 mm,
  checkboxes ≥4 mm, legible en blanco y negro.
- Cero stock, cero degradados, cero iconos 3D, cero emojis decorativos.
- No diseñas: guiones, kpis.md, notas-fuente.md, 00-plan-modulo.md, specs de
  formularios, prompts para copiar, ni nada marcado como interno o NO PUBLICAR.
- Tres piezas llevan aviso legal y va literal, sin recortar: F3-rgpd-captacion
  (los dos disclaimers de "orientación práctica, no asesoría legal", arriba y
  abajo de cada página) y F5-acuerdo-servicios-esqueleto (es un esqueleto, no
  un contrato: tiene que verse que hay que pasarlo por un abogado).
- En F3-banco-creativos-b2b y F3-kpis-ads-benchmarks hay prompts para copiar:
  van en bloque monoespaciado, tal cual, sin maquetar como arte.

CÓMO ENTREGAS
Módulo a módulo, en este orden: F4 → F5 → F3 → F6.
(F4 y F5 primero porque son los que el alumno usa antes en su calendario real.)
Al cerrar cada módulo, tabla de dos columnas: archivo de salida ↔ .md de origen.
Si una pieza te obliga a incumplir una regla del sistema visual, no la
incumplas: entrégala igual y dime qué regla chocaba y por qué.
```

## Cuando te lo entregue

Los `.dc.html` no sirven como adjunto de Skool: dependen de la carpeta `_ds/` y se rompen al moverlos. Hay que convertirlos a PDF y repartirlos por lección — es lo que hicieron `convertir.py` y `componer.py` con la primera tanda. Déjame la carpeta nueva en el escritorio y lo hago igual.

## Lo que no depende de él

- Los 12 CSV de trackers: hechos, en `entregables-listos/csv/`.
- Los 2 formularios: guía de montaje hecha, en `entregables-listos/formularios/`. Se montan en Tally.
- Las 54 pizarras: hechas, en `pizarras-grabacion/`.
