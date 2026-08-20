# CLAUDE.md — Demo: Recuperación de citas (Clínica Dental Ensanche)

## Qué es este proyecto
Demo comercial web de recuperación de no-shows y citas para clínicas dentales. UN solo archivo (`index.html`), sin dependencias externas, desplegable tal cual. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el "paciente" solo responde pulsando botones (chips). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el chat libre llega en el piloto real, no en la demo).
- **Datos ficticios y verosímiles**: nombres, tratamientos y horas creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Las cifras (ticket medio, contadores base) son ilustrativas.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).
- No uses logos ni marcas reales de WhatsApp: la estética es "reconocible", no oficial.

## Los 7 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel con citas de hoy/mañana (paciente, tratamiento, hora, estado).
2. Contadores visibles: citas recuperadas + facturación recuperada (ticket medio configurable).
3. Marcar cancelada/no-show abre el simulador de conversación.
4. Flujo: lamento → 2 huecos reales → elección por botón → confirmación.
5. La cita reaparece en su nuevo hueco como "recuperada" y los contadores suben.
6. "Reiniciar demo" restaura todo.
7. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio y avatar, tratamientos→servicios, datos de la tabla `DATOS_INICIALES`, huecos, copy de los mensajes y colores. El flujo y la estructura no se tocan.
