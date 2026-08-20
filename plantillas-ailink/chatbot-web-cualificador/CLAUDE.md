# CLAUDE.md — Demo: Chatbot web cualificador (Inmobiliaria Alameda)

## Qué es este proyecto
Demo comercial web de Chatbot web cualificador para inmobiliarias: una web de agencia inventada con el chat en la esquina que cualifica interesados en vivienda (zona, presupuesto, financiación, plazo) y entrega el lead etiquetado en un mini-panel. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

**Estado actual:** esta carpeta llega SIN `index.html`. La primera tarea es construir la demo siguiendo `BRIEF.md` al pie de la letra, usando `../recuperacion-citas-dental/index.html` (la plantilla insignia, completa y funcionando) como referencia estructural: misma anatomía de simulador guiado + panel que reacciona + reiniciar.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el visitante solo responde pulsando botones (chips). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el cerebro real llega en F5, con el piloto pagado).
- **Sin formularios reales**: los datos del visitante entran con el botón "Enviar mis datos", que usa el interesado de ejemplo del brief (Carlos Navarro). Nunca pidas teclear nombre ni teléfono.
- **La etiqueta de temperatura se calcula con las respuestas** (regla del brief), no está fijada a mano: si cambias las respuestas en la conversación, la etiqueta del lead debe cambiar. Es la prueba de credibilidad de la demo.
- **Datos ficticios y verosímiles**: viviendas, precios, zonas y nombres creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Fotos: bloques de color o ilustraciones, nunca fotos reales de inmuebles. Las cifras son ilustrativas.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px, y la burbuja del chat no puede tapar el contenido.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).

## Los 8 comportamientos que NO se pueden romper (del BRIEF.md)
1. Página de inmobiliaria verosímil (marca + 4 fichas de vivienda) con burbuja de chat abajo a la derecha.
2. La burbuja saluda sola a los 2-3 segundos; el chat abre con 3 opciones de intención (comprar / vender / solo mirar) — todo por botones.
3. Camino comprador: 4 preguntas de cualificación por botones — zona, presupuesto, financiación, plazo.
4. El chat propone la vivienda (o dos) de la cartera que encaja y ofrece visita con 2 huecos por botón.
5. El lead entra en el mini-panel "Leads del chat" con todo lo recogido y su etiqueta de temperatura calculada (caliente / templado / frío); los calientes se destacan con "avisar al comercial ya".
6. Los caminos "vender" y "solo mirar" también terminan bien (lead de valoración / alerta de novedades).
7. "Reiniciar demo" restaura todo (chat cerrado, panel con solo los 2 leads de ejemplo).
8. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: marca y colores del negocio, viviendas→servicios/cursos/alojamientos, las 4 preguntas de cualificación y su regla de temperatura, los datos de las tablas de ejemplo, huecos de visita y copy de los mensajes. El flujo y la estructura no se tocan.
