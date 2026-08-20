# AILINK Élite — el programa completo

Programa high ticket de 90 días que enseña a montar una agencia que vende **soluciones de IA hechas con Claude Code** (software y automatizaciones) a negocios españoles. Modelo de **entregables** —proyecto + retainer—, no de resultados.

**Promesa canónica:** +10.000€ de facturación acumulada al final de los 90 días (total, no mensual).

Este repositorio contiene el programa entero: los 54 guiones de vídeo, los 45 recursos del alumno, las 54 pizarras de grabación, los trackers, los formularios y la maqueta del aula. Falta grabar los vídeos y diseñar 25 PDF.

---

## Empieza por aquí

Si acabas de entrar, lee estos tres archivos **en este orden** y ya tendrás el mapa completo:

1. **[`01-BIBLIA.md`](01-BIBLIA.md)** — la autoridad. Las decisiones que valen para todo el programa: la promesa, el modelo de negocio, los precios y dónde se enseñan, el glosario (qué se dice en inglés y qué está prohibido decir), las reglas de España y RGPD. **Ante cualquier duda o contradicción, manda la Biblia.**
2. **[`02-INDICE-MAESTRO.md`](02-INDICE-MAESTRO.md)** — el mapa navegable: las 7 fases, las 54 lecciones, el estado de cada carpeta y los **17 pendientes que solo puede cerrar Agustín**.
3. **[`skool/00-MONTAJE-SKOOL.md`](skool/00-MONTAJE-SKOOL.md)** — cómo se traduce todo esto a la plataforma: cursos, lecciones, adjuntos, drip.

Para ver el aula montada sin instalar nada: abre **[`skool/aula-ailink.html`](skool/aula-ailink.html)** a doble clic. Es una réplica navegable del Skool con las 54 lecciones, sus descripciones y sus adjuntos, y un botón para copiar cada cosa.

---

## Las 7 fases

| Fase | Curso en Skool | Semanas | Lecciones | Hito |
|---|---|---|---|---|
| F0 | **Bienvenido** — onboarding | 1 | 8 | Kick-off + setup + manifiesto firmado |
| F1 | **Domina** — nicho, oferta, precio | 2-3 | 7 | Oferta V1 redactada |
| F2 | **Construye** — Claude Code | 3-4 | 7 | Demo desplegada + vídeo de respaldo |
| F3 | **Lanza** — máquina de demanda | 5-7 | 10 | Primeras reuniones agendadas |
| F4 | **Cierra** — ventas consultivas | 6-9 | 8 | Primer cliente cobrado en la llamada |
| F5 | **Entrega** — del cobro a la entrega | 8-11 | 7 | Primera entrega con criterios firmados |
| F6 | **Escala** — retención y MRR | 11-13 | 7 | Primer retainer con cobro automático |

El contenido se abre en orden; el trabajo se solapa a partir de Lanza.

---

## Qué hay en cada carpeta

| Carpeta | Qué es | ¿Lo ve el alumno? |
|---|---|---|
| `modulos/F0…F6/` | El corazón. Por módulo: `00-plan-modulo.md` (contrato de producción), `guiones/` (los 54 guiones de vídeo), `recursos/` (los 45 entregables en Markdown), `pizarras/` (guion de diapositivas, uno por lección), `kpis.md`, `notas-fuente.md` | Solo `recursos/`, y en PDF |
| `adjuntos-skool/` | **Lo que se sube a Skool**, ya repartido por curso y lección (`L03-F0-manifiesto-90-dias.pdf` → lección 3) | Sí |
| `pizarras-grabacion/` | Las 54 pizarras en PDF 16:9, con revelado paso a paso | ⛔ No — es material de grabación |
| `entregables-listos/` | 13 CSV de trackers + guías para montar los 2 formularios en Tally | Los CSV sí |
| `diseno/` | El sistema visual, los briefs por módulo y los prompts para Claude Design | No |
| `skool/` | Plan de montaje + la maqueta navegable del aula + su generador | No |
| `plantillas-ailink/` | La demo dental funcionando (HTML autocontenido) + 7 kits de brief para las demás soluciones | La demo sí |
| `herramientas/` | Los dos scripts que convierten el material de Claude Design y lo reparten por lección | No |
| `_grok/` | Carril de auditoría paralelo, histórico. No se produce desde aquí | No |
| `fuente/` | La transcripción del curso que se usó de esqueleto. **No está en el repo** (material de terceros) | No |

---

## Reglas de trabajo

Si vas a escribir o corregir contenido, estas cinco no se negocian:

1. **La Biblia manda.** Antes de decidir nada transversal —una cifra, un término, un precio—, compruébalo en `01-BIBLIA.md`. Si falta, se añade ahí primero y luego se propaga.
2. **Español de España, tuteo.** El glosario de la Biblia marca qué anglicismos se quedan (hook, funnel, retainer, close rate, kick-off…) y cuáles están **prohibidos** — el más importante: *prospect/prospecto* no se usa nunca; es «lead» o «el dueño».
3. **Los precios solo se enseñan en F1.** Ningún otro módulo cita rangos.
4. **Nada marcado `⛔ NO PUBLICAR` llega al alumno.** Guiones, `kpis.md`, `notas-fuente.md`, `00-plan-modulo.md`, los briefs de diseño y `F0-bienvenido/guia-interna-operador.md` son material interno.
5. **Lo que está `[BORRADOR]` no se da por bueno.** Son las cifras que Agustín aún no ha cerrado; están listadas en `02-INDICE-MAESTRO.md`. Si cambian, hay que propagarlas y rehacer los PDF afectados.

El estándar de cada tipo de pieza está escrito: el de los guiones de vídeo, en `01-BIBLIA.md`; el de las pizarras, en `diseno/02-ESTANDAR-GUION-DIAPOS.md`; el de los PDF, en `diseno/00-SISTEMA-VISUAL.md`.

---

## Estado a 20/08/2026

**Hecho:**
- Los 7 módulos escritos, verificados y corregidos: 54 guiones + 45 recursos + guía interna del operador.
- Las 54 pizarras diseñadas y convertidas a PDF.
- 17 de los 45 entregables diseñados (F0, F1 y F2 completos) y repartidos por lección.
- Los 13 CSV de trackers, con sus README de fórmulas.
- Las guías de montaje de los 2 formularios.
- La maqueta del aula, con las 54 descripciones escritas y listas para copiar.

**Falta:**
- **Grabar los 54 vídeos.**
- **25 PDF de F3, F4, F5 y F6** — el encargo está escrito en `diseno/PROMPT-CONTINUACION.md`.
- Los 17 pendientes de Agustín en `02-INDICE-MAESTRO.md`: cerrar las 7 cifras `[BORRADOR]`, montar los formularios en Tally, grabar la llamada modelo y pasar el esqueleto de contrato por un abogado.
- Las 7 demos de plantilla que aún son solo brief (`plantillas-ailink/`).

---

## Cuando llegue material nuevo de Claude Design

Claude Design entrega `.dc.html`, que no valen como adjunto: dependen de la carpeta `_ds/` que los acompaña y se rompen en cuanto se mueven. El circuito es de dos pasos:

```bash
python3 herramientas/convertir.py "~/Desktop/carpeta que te haya dejado"
python3 herramientas/componer.py
```

El primero los rasteriza a PDF con Chrome respetando el formato de cada pieza (A4, A4 horizontal o 16:9) y los deja en `pdf-convertidos/`. El segundo los reparte: material del alumno a `adjuntos-skool/`, pizarras a `pizarras-grabacion/`, y reescribe el `_LEEME.md` de cada carpeta y el `skool/estado-adjuntos.json`. Después, regenera la maqueta para que los sellos se actualicen.

## Cómo regenerar la maqueta

La maqueta del aula no se edita a mano: se genera.

```bash
cd skool && python3 build.py
```

Lee `contenido-skool.json` (las 54 lecciones con su descripción y sus adjuntos) y `estado-adjuntos.json` (qué archivo existe ya), y escribe `aula-ailink.html` —autocontenido, se abre a doble clic— y `aula-ailink-web.html`. Para cambiar un texto de una lección, se toca el JSON y se vuelve a generar.
