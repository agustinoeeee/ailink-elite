# Montaje en Skool — plan de la plataforma

> Cómo se traduce el programa a la estructura de Skool, decisión a decisión. La maqueta navegable enseña cómo queda cada lección; este documento dice cómo montarlo.
>
> **Maqueta publicada:** https://claude.ai/code/artifact/3820ff59-224a-40f0-8716-bd4bb2801059 (privada hasta que la compartas). En local: `aula-ailink.html` (autocontenido, se abre a doble clic). Se regenera con `python3 build.py` a partir de `contenido-skool.json`.

## 1. La equivalencia

| En el programa | En Skool | Cantidad |
|---|---|---|
| Fase (F0…F6) | **Curso** (tarjeta del Classroom) | 7 |
| Lección | **Lección** dentro del curso | 54 |
| Guion | El **vídeo** de la lección | 54 |
| Recurso (PDF/CSV) | **Adjunto** de la lección | 45 |
| Formulario | **Enlace** en la descripción (Tally), no adjunto | 2 |

Cada lección lleva tres cosas: **vídeo + descripción + adjuntos**. La descripción de las 54 está escrita — se copia y se pega.

## 2. Las 7 tarjetas del Classroom

Hoy tienes 5 y con la nomenclatura antigua. La nueva estructura son 7:

| # | Palabra de portada | Título de la tarjeta | Semanas |
|---|---|---|---|
| 1 | **Bienvenido** | Onboarding — Empieza aquí | 1 |
| 2 | **Domina** | F1 · Nicho y oferta | 2-3 |
| 3 | **Construye** | F2 · Tu solución con Claude Code | 3-4 |
| 4 | **Lanza** | F3 · Máquina de demanda | 5-7 |
| 5 | **Cierra** | F4 · Ventas consultivas | 6-9 |
| 6 | **Entrega** | F5 · Del cobro a la entrega | 8-11 |
| 7 | **Escala** | F6 · Retención y MRR | 11-13 |

**Qué cambia respecto a lo que tienes montado:** entran dos cursos nuevos (**Construye** y **Escala**), y las tarjetas actuales de Lanza/Planea/Escala se renombran y reordenan. Los nombres de portada que ya tienes hechos se reaprovechan: Bienvenido, Domina, Lanza y Escala siguen existiendo, solo cambian de posición o de subtítulo.

## 3. El desbloqueo (drip)

Dos capas, y conviene no confundirlas:

- **El contenido se abre en orden.** Cada curso se desbloquea al completar el anterior.
- **El trabajo se solapa** a partir de Lanza: el alumno capta, vende y entrega a la vez. Por eso **nunca se bloquea el acceso hacia atrás**: tiene que poder volver a F3 mientras ejecuta F5.

En Skool: desbloqueo por completado (no por días), y los cursos ya completados quedan siempre accesibles. Es exactamente lo que L1 de Bienvenido le explica al alumno.

## 4. Reglas de los adjuntos

1. **Un adjunto se sube una sola vez en todo el programa**, a la lección donde se usa por primera vez. Si otra lección lo reutiliza —aunque sea de otro curso, como el tracker de ventas de F4 que F5 vuelve a usar—, se menciona en la descripción con "(ya lo tienes en LX)" en vez de volver a subirlo.
2. **Los formularios no se adjuntan**: van como enlace a Tally en la descripción. Un PDF de un formulario no sirve para nada.
3. **Los trackers van en CSV**, no en PDF: su sitio es una hoja de cálculo. El PDF que los acompaña (cuando lo hay) es solo la hoja de reglas.
4. **Nunca se suben**: guiones, `kpis.md`, `notas-fuente.md`, `00-plan-modulo.md`, los briefs de diseño ni la guía interna del operador. Es material tuyo.

## 5. Orden de montaje recomendado

1. Crea los 7 cursos con sus portadas y descripciones (30 min).
2. Crea las lecciones **vacías** de un curso, en orden, con su título y emoji.
3. Pega la descripción de cada lección (ya escritas — cópialas de la maqueta).
4. Sube los adjuntos de ese curso.
5. Sube los vídeos según los vayas grabando.

Los pasos 1-4 se pueden hacer HOY, sin un solo vídeo grabado. Así el aula queda montada y solo vas rellenando huecos de vídeo conforme grabas.

**Atajo para los pasos 2-4:** en la maqueta, dentro de cada curso, el botón **«Copiar el curso entero»** te deja en el portapapeles las lecciones de ese curso seguidas, cada una con su título, su duración de vídeo, su descripción y la lista de adjuntos que hay que subir. Pégalo en un bloc de notas al lado y vas montando de arriba abajo sin volver a la maqueta.

## 5 bis. Dónde están los archivos

Todo lo que se sube está en **`adjuntos-skool/`**, una carpeta por curso en el orden del Classroom, y cada archivo con la lección delante del nombre (`L03-F0-manifiesto-90-dias.pdf` → lección 3). Cada carpeta lleva su `_LEEME.md` con la tabla lección por lección.

| Curso | Archivos listos | Faltan |
|---|---|---|
| 1 Bienvenido · 2 Domina · 3 Construye | **18 — completos** | — |
| 4 Lanza | 7 CSV | 7 PDF |
| 5 Cierra | 2 CSV | 6 PDF |
| 6 Entrega | 1 CSV | 6 PDF |
| 7 Escala | 2 CSV | 6 PDF |

Los 25 PDF que faltan son la segunda tanda de Claude Design: el encargo está escrito en `diseno/PROMPT-CONTINUACION.md`.

**Los CSV no dependen del diseño** — su sitio es una hoja de cálculo, no un PDF. Están todos. Las fórmulas que el alumno pega al importarlos están en `entregables-listos/csv/README-F0-F3.md` y `README-F4-F6.md`: ese texto va **en la descripción de la lección**, no como archivo.

**Las pizarras no se suben.** Las 54 están en `pizarras-grabacion/`, en PDF 16:9 y con revelado paso a paso: se avanzan con la flecha mientras grabas.

## 6. Antes de abrirlo a alumnos

- [ ] Los 2 formularios montados en Tally y sus enlaces pegados (Bienvenido L2, Entrega L2).
- [ ] El enlace de tu calendario de reservas pegado en Bienvenido L2.
- [ ] Los `[PRUEBA SOCIAL]` de los vídeos, resueltos o retirados.
- [ ] El desbloqueo configurado y probado con una cuenta de prueba.
- [ ] Los adjuntos abiertos desde el móvil: que se descarguen y se lean.
