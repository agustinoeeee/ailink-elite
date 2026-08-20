# Plantilla AILINK — Chatbot web cualificador (inmobiliarias)

> **Kit de brief.** Esta plantilla trae todo lo necesario para que construyas TU demo de Chatbot web cualificador con Claude Code: el brief completo relleno, las reglas de proyecto y este manual. No trae la demo construida — por diseño: construirla a partir del brief ES la habilidad que entrenas en F2. Tu referencia estructural es la plantilla insignia (`../recuperacion-citas-dental/`), que sí está completa y funcionando.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `BRIEF.md` | El brief COMPLETO relleno para el nicho típico (inmobiliaria — cualificar interesados en vivienda), en el formato de F2-R2. Listo para dárselo entero a Claude Code como primera instrucción. |
| `CLAUDE.md` | Las instrucciones de proyecto para Claude Code: qué es esta demo, sus reglas innegociables y qué no tocar mientras la construyes y la personalizas. |
| `README.md` | Este manual. |

## La solución (ficha del catálogo: Chatbot web cualificador)

Un chat instalado en la web del negocio que atiende visitas 24/7, responde dudas y cualifica: pregunta qué necesita el visitante, recoge sus datos y entrega el contacto ya filtrado, avisando de los urgentes. **La joya oculta del catálogo**: es 100% web incluso en el piloto real — se instala en la página del cliente y ya está funcionando. La demo lo enseña sobre una web inmobiliaria inventada: el visitante responde presupuesto, zona y financiación con botones, y su lead cualificado (caliente / templado / frío) entra en el mini-panel delante del cliente.

Dificultad 1, potencia de demo 3: la esquina de oro del catálogo, junto a la insignia.

## Cómo se usa (alumno)

1. **Lee `BRIEF.md` entero** antes de abrir Claude Code. Es tu herramienta de dirección: describe QUÉ debe pasar, nunca cómo programarlo.
2. **Abre y prueba la insignia** (`../recuperacion-citas-dental/index.html`): simulador guiado + panel que reacciona + contadores + reiniciar. Aquí la anatomía es la misma con otra piel: web del negocio + chat en la esquina + panel de leads.
3. **Abre ESTA carpeta con Claude Code** y dale el brief entero como primera instrucción: "construye esta demo web siguiendo este brief" + el contenido de `BRIEF.md`. Objetivo: UN solo archivo `index.html`, sin dependencias.
4. **Itera con las 3 reglas de dirección** (al final del brief): una petición = un cambio; probar entre pasos; los errores se pegan, no se pelean.
5. **Pasa los checks** de la sección 6 del brief. Lo que no has probado, no existe.
6. **Despliégala** en tu hosting (F2-L2) y tendrás tu URL compartible.
7. **No la enseñes a nadie** sin pasar la checklist pre-demo de F2-L6.

## Qué NO es

- No es el piloto real: la conversación es guiada (botones, sin texto libre, sin APIs de IA — decisión del programa). El cerebro de IA de verdad llega en F5 con el piloto pagado — aunque esta solución, incluso en real, sigue siendo 100% web.
- No se instala en la web real del cliente: la demo trae su propia página inventada. En el piloto sí se instala en la web real — ese es su superpoder de venta.
- No guarda datos: todo vive en la página y se reinicia con el botón (a propósito: cada llamada de venta empieza limpia).
- No es una demo genérica: está rellena para inmobiliaria. Si tu oferta V1 es otro nicho, adapta el brief ANTES de construir (abajo).

## Adaptación rápida a otros nichos (mismo esqueleto)

Despachos de abogados (consultas sin filtrar que devoran horas facturables), academias y centros de formación (matrículas que se enfrían), alojamientos turísticos (preguntas de huéspedes 24/7): cambia viviendas→servicios/cursos/alojamientos y las 4 preguntas de cualificación (área legal y urgencia, curso y fecha de inicio, fechas y nº de personas). El flujo chat guiado → lead etiquetado en el panel es idéntico.
