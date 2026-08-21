# Adjuntos del alumno, listos para subir a Skool

> Una carpeta por curso, en el mismo orden que el Classroom. Dentro, cada archivo lleva delante la lección a la que se sube: `L04-F0-manifiesto-90-dias.pdf` → lección 4.
>
> **Todo lo que hay aquí se sube tal cual.** Nada de esta carpeta es material interno.

## Estado

| # | Carpeta | Curso | Archivos listos | Faltan |
|---|---|---|---|---|
| 1 | `1-bienvenido` | F0 Bienvenido | 7 | — |
| 2 | `2-domina` | F1 Domina | 7 | 3 PDF |
| 3 | `3-construye` | F2 Construye | 5 | — |
| 4 | `4-lanza` | F3 Lanza | 7 (los CSV) | 7 PDF |
| 5 | `5-cierra` | F4 Cierra | 2 (los CSV) | 6 PDF |
| 6 | `6-entrega` | F5 Entrega | 1 (el CSV) | 6 PDF |
| 7 | `7-escala` | F6 Escala | 2 (los CSV) | 6 PDF |

**F0 y F2 están completos** (12 archivos): esos dos cursos se pueden montar y grabar enteros. F0 se cerró el 21/08/2026 con el Bloque 1 de diseño, que trajo `F0-norte-personal` y rehizo lo que había caducado.

A **F1 le faltan 3 entregables** de las lecciones nuevas (`F1-inventario-ventajas`, `F1-catalogo-oportunidades`, `F1-revision-oferta`), y **sus otras piezas están caducadas**: siguen siendo la versión anterior a la ampliación, así que no se graba ni se sube con ellas hasta que llegue el Bloque 2. La lista exacta está en `diseno/03-REENCARGOS-PENDIENTES.md`.

De F3 a F6 están todos los CSV y faltan **25 PDF** que Claude Design aún no ha producido — el encargo está en `diseno/PROMPT-CONTINUACION.md`. **Total pendiente: 28 adjuntos.**

Cada carpeta lleva su `_LEEME.md` con la tabla lección por lección: qué adjunto va, con qué nombre está aquí y en qué estado.

## Las cuatro reglas al subirlos

1. **Un archivo se sube una sola vez en todo el programa**, a la lección donde aparece por primera vez. El prefijo `L##` te dice cuál es. Cuando otra lección lo reutiliza —incluso desde otro curso, como el tracker de ventas de F4 que F5 vuelve a usar— la descripción lo menciona con «(ya lo tienes en LX)» y no se vuelve a subir.
2. **Los formularios no son archivos.** Van como enlace de Tally dentro de la descripción (F0-L2 y F5-L2). Móntalos con las guías de `entregables-listos/formularios/`.
3. **Los CSV se suben tal cual**, sin convertir a PDF: su sitio es una hoja de cálculo. Las fórmulas que el alumno tiene que pegar están en `entregables-listos/csv/README-F0-F3.md` y `README-F4-F6.md` — ese texto va **en la descripción de la lección**, no como archivo suelto.
4. **Las pizarras no se suben.** Están en `pizarras-grabacion/` y son tuyas, para grabar.

## Si cambias una cifra `[BORRADOR]`

Los rangos de precio (piloto 500-1.500€, proyecto 2.000-6.000€, retainer 300-1.500€/mes) están **impresos** en `2-domina/L06-F1-calculadora-pricing.pdf`. Si los cierras distintos, hay que rehacer ese PDF y la pizarra de F1-L7. Lo mismo con las demás cifras pendientes de `02-INDICE-MAESTRO.md`.

## Cómo se regeneró esto

Claude Design entrega `.dc.html`, que no sirven como adjunto: dependen de una carpeta `_ds/` y se rompen al moverlos. Se convirtieron a PDF con Chrome (los A4 salen A4, los horizontales salen horizontales) y se repartieron por lección desde `skool/contenido-skool.json`, que es el mapa que manda. Si vuelves a recibir material de diseño, el circuito son dos órdenes: `python3 herramientas/convertir.py "<carpeta que te haya dejado>"` y después `python3 herramientas/componer.py`.
