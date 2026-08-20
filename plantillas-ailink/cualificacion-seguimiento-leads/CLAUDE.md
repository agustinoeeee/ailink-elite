# CLAUDE.md — Demo: Cualificación y seguimiento de leads (Fincas Alcaraz)

## Qué es este proyecto
Demo comercial web de cualificación y seguimiento de leads para inmobiliarias. UN solo archivo (`index.html`, construido a partir de `BRIEF.md`), sin dependencias externas, desplegable tal cual. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el "lead" solo responde pulsando botones (chips). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el chat libre y las integraciones reales llegan en el piloto, no en la demo).
- **Datos ficticios y verosímiles**: nombres de leads, calles, precios y franjas creíbles en español de España. Nada de "Lead 1" ni lorem ipsum. Los contadores de partida son ilustrativos. Orígenes de lead genéricos ("portal inmobiliario", "web propia", "recomendación"): sin marcas reales de portales.
- **El movimiento de tarjetas es el corazón de la demo**: cada avance de la conversación mueve la tarjeta de columna EN DIRECTO, con una transición visible. Si el cliente no VE la tarjeta subir, la demo no vende.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** (columnas, etiquetas, contadores y conversaciones) — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px (columnas con scroll horizontal o apiladas).
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).
- No uses logos ni marcas reales de WhatsApp: la estética del simulador es "reconocible", no oficial.

## Los 8 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel con 4 columnas: Nuevo → Contactado → Cualificado → Cita, con tarjetas de leads (nombre, inmueble con precio, origen, tiempo de espera).
2. Contadores visibles: "leads cualificados este mes" y "visitas agendadas".
3. Pulsar un lead en "Nuevo" abre el simulador de conversación, que saluda al lead por su nombre citando su inmueble exacto.
4. Flujo guiado: saludo → presupuesto (opciones) → plazos (opciones) → 2 franjas de visita → elección → confirmación con día y hora.
5. La tarjeta sube de columna en directo según avanza la conversación; al llegar a "Cita", los contadores suben y la tarjeta muestra día y hora.
6. El lead frío ("sin respuesta desde hace 2 días") muestra la secuencia de seguimiento automático que lo rescata y también avanza de columna.
7. "Reiniciar demo" restaura todo.
8. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio, leads y su interés (inmueble → curso/tratamiento/asunto), preguntas de cualificación y sus opciones, franjas de cita, copy y colores. Las 4 columnas, el flujo y la estructura no se tocan.
