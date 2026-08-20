# Plantilla AILINK — Cualificación y seguimiento de leads (inmobiliarias)

> **Kit de brief.** Esta plantilla no trae la demo construida: trae el brief COMPLETO relleno y las reglas de proyecto para que construyas TU demo dirigiendo a Claude Code — esa ES la habilidad de F2. Tu referencia estructural es la plantilla insignia (`../recuperacion-citas-dental/`): ábrela y pruébala antes de empezar, porque el nivel de acabado que ves ahí es el que se te pide aquí.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `BRIEF.md` | El brief completo relleno para el nicho típico (inmobiliarias), en el formato de F2-R2 — se lo das ENTERO a Claude Code como primera instrucción |
| `CLAUDE.md` | Las instrucciones de proyecto para Claude Code: reglas y comportamientos innegociables de esta solución |
| `README.md` | Este archivo |

## Qué hace la demo que vas a construir

Un mini-panel de leads entrantes con columnas por estado (Nuevo → Contactado → Cualificado → Cita) y un simulador de conversación de cualificación al lado. Cuando el lead responde bien pulsando respuestas sugeridas, su tarjeta sube de columna EN DIRECTO delante del cliente; y un lead que se enfrió muestra la secuencia de seguimiento automático que lo rescata (ficha 3 del catálogo técnico de F2-L4).

## Cómo se usa (alumno)

1. **Prueba la insignia**: abre `../recuperacion-citas-dental/index.html`, reproduce su flujo completo y fíjate en el acabado. Es tu referencia estructural (un archivo, datos verosímiles, botón reiniciar, móvil).
2. **Lee `BRIEF.md` entero** antes de tocar nada. Si tu nicho no es inmobiliario, adapta primero los datos (negocio, leads, preguntas de cualificación) manteniendo el flujo.
3. **Abre esta carpeta con Claude Code** y dale el brief entero como primera instrucción: *"construye esta demo web siguiendo este brief: …"*. Objetivo: UN solo `index.html`, sin dependencias.
4. **Itera con las 3 reglas de dirección** (final del `BRIEF.md`): una petición = un cambio · probar entre pasos · los errores se pegan, no se pelean.
5. **Despliégala** en tu hosting (F2-L2) y tendrás tu URL compartible.
6. **No la enseñes a nadie** sin pasar la checklist pre-demo de F2-L6.

## Qué NO es

- No es una demo hecha: el `index.html` lo construyes tú a partir del brief.
- No es el piloto real: la conversación es un simulador visual guiado por botones, sin texto libre ni APIs de IA, y no hay conexión con portales ni WhatsApp de verdad (decisión del programa: el cerebro real y las integraciones llegan en F5, con el piloto pagado).
- No guarda datos: todo vive en la página y se reinicia con el botón (a propósito: cada llamada de venta empieza limpia).

## Adaptación rápida a otros nichos (mismo esqueleto)

Academias y centros de formación (lead = solicitud de matrícula; cita = entrevista o clase de prueba), clínicas de medicina estética (lead = interesado en un tratamiento; cita = valoración gratuita), despachos de abogados (lead = consulta web; cita = primera visita): cambia leads → tus contactos, el inmueble → el curso/tratamiento/asunto, las preguntas de cualificación y el copy. El panel de columnas y el flujo conversación → tarjeta que sube son idénticos.
