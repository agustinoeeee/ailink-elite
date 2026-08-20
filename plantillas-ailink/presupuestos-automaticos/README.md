# Plantilla AILINK — Presupuestos automáticos (empresas de reformas)

> **Kit de brief.** Esta plantilla no trae la demo construida: trae el brief COMPLETO relleno y las reglas de proyecto para que construyas TU demo dirigiendo a Claude Code — esa ES la habilidad de F2. Tu referencia estructural es la plantilla insignia (`../recuperacion-citas-dental/`): ábrela y pruébala antes de empezar, porque el nivel de acabado que ves ahí es el que se te pide aquí.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `BRIEF.md` | El brief completo relleno para el nicho típico (empresas de reformas), en el formato de F2-R2 — se lo das ENTERO a Claude Code como primera instrucción |
| `CLAUDE.md` | Las instrucciones de proyecto para Claude Code: reglas y comportamientos innegociables de esta solución |
| `README.md` | Este archivo |

## Qué hace la demo que vas a construir

El cliente final elige opciones guiadas — tipo de trabajo, tamaño, extras — y sale un presupuesto orientativo al instante en pantalla, con desglose por partidas, total destacado y el aviso "orientativo, sujeto a visita técnica". El salto de "esto me lleva dos días" a "esto tarda 30 segundos" se explica solo (ficha 4 del catálogo técnico de F2-L4).

## Cómo se usa (alumno)

1. **Prueba la insignia**: abre `../recuperacion-citas-dental/index.html`, reproduce su flujo completo y fíjate en el acabado. Es tu referencia estructural (un archivo, datos verosímiles, botón reiniciar, móvil).
2. **Lee `BRIEF.md` entero** antes de tocar nada. Si tu nicho no es reformas, adapta primero los datos (negocio, servicios, tarifas) manteniendo el flujo.
3. **Abre esta carpeta con Claude Code** y dale el brief entero como primera instrucción: *"construye esta demo web siguiendo este brief: …"*. Objetivo: UN solo `index.html`, sin dependencias.
4. **Itera con las 3 reglas de dirección** (final del `BRIEF.md`): una petición = un cambio · probar entre pasos · los errores se pegan, no se pelean.
5. **Despliégala** en tu hosting (F2-L2) y tendrás tu URL compartible.
6. **No la enseñes a nadie** sin pasar la checklist pre-demo de F2-L6.

## Qué NO es

- No es una demo hecha: el `index.html` lo construyes tú a partir del brief.
- No es el piloto real: el configurador es un flujo guiado por botones, sin texto libre ni APIs de IA (decisión del programa: el cerebro real y el envío del presupuesto en PDF llegan en F5, con el piloto pagado). Las tarifas son ilustrativas — las de verdad se cargan con el cliente.
- No guarda datos: todo vive en la página y se reinicia con el botón (a propósito: cada llamada de venta empieza limpia).

## Adaptación rápida a otros nichos (mismo esqueleto)

Talleres mecánicos (tipo de intervención → revisión, frenos, embrague, distribución; tamaño → cilindrada o gama del coche), carpinterías e instaladores (armarios, ventanas, pérgolas), empresas de pintura o pladur, jardinería: cambia tipos de trabajo → tus servicios, las tarifas, las partidas del desglose y el copy. El flujo elegir → elegir → elegir → presupuesto en pantalla es idéntico.
