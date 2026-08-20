# CLAUDE.md — Demo: Recepcionista IA (Clínica Veterinaria La Dehesa)

## Qué es este proyecto
Demo comercial web de Recepcionista IA (WhatsApp/llamadas) para clínicas veterinarias: llamadas perdidas que se convierten en citas mediante una conversación simulada. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

**Estado actual:** esta carpeta llega SIN `index.html`. La primera tarea es construir la demo siguiendo `BRIEF.md` al pie de la letra, usando `../recuperacion-citas-dental/index.html` (la plantilla insignia, completa y funcionando) como referencia estructural: misma anatomía panel + simulador + contadores + reiniciar.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el "dueño de la mascota" solo responde pulsando botones (chips). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el cerebro real llega en F5, con el piloto pagado).
- **Datos ficticios y verosímiles**: dueños, mascotas, motivos y horas creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Las cifras (consulta media, precios, contadores base) son ilustrativas.
- **La urgencia NUNCA acaba en cita**: el camino de urgencia deriva al teléfono directo y marca la llamada en rojo. Es el momento de más credibilidad de la demo — no lo "arregles" convirtiéndolo en cita.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).
- No uses logos ni marcas reales de WhatsApp: la estética es "reconocible", no oficial.

## Los 8 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel de recepción con "Llamadas perdidas de hoy" y "Agenda de hoy y mañana", junto al simulador de conversación.
2. Contadores visibles: citas apuntadas por la recepcionista + facturación estimada (consulta media configurable).
3. Pulsar una llamada perdida arranca la conversación de atención en el simulador.
4. Flujo: la recepcionista escribe al dueño → responde dudas con datos del negocio → propone 2 huecos reales → elección por botón → confirmación con día, hora y mascota.
5. El motivo "urgencia" deriva al teléfono directo, sin cita, y marca la llamada como "Urgencia derivada" en rojo.
6. La cita confirmada aparece en la agenda como "atendida por la recepcionista", la llamada perdida pasa a "convertida en cita" y los contadores suben.
7. "Reiniciar demo" restaura todo.
8. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio y avatar, mascotas→vehículos/pacientes/mesas, motivos de llamada, datos del negocio (horario, dirección, precios orientativos), datos de las tablas de ejemplo, huecos, copy de los mensajes y colores. El flujo y la estructura no se tocan.
