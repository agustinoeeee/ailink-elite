# CLAUDE.md — Demo: Gestión documental (Gestoría Ferrándiz)

## Qué es este proyecto
Demo comercial web de gestión documental para gestorías y asesorías. UN solo archivo (`index.html`), sin dependencias externas, desplegable tal cual. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el "cliente" de la gestoría solo responde pulsando botones (chips). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el cerebro real llega en el piloto, en F5).
- **La demo NO lee documentos**: el adjunto de la conversación es visual (icono + nombre de archivo) y el documento se marca como "recibido" sin procesarse. No añadas subida real de archivos, OCR ni extracción de datos — eso es el corazón del piloto real (F5), no de la demo.
- **Datos ficticios y verosímiles**: clientes, trámites y documentos creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Las cifras (minutos ahorrados por documento, contadores) son ilustrativas.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en la función de reinicio.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).
- No uses logos ni marcas reales de WhatsApp: la estética es "reconocible", no oficial.

## Los 7 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel de expedientes: cliente, trámite, documentos requeridos con estado (recibido / pendiente) y estado del expediente (completo / incompleto).
2. Contadores visibles: expedientes completos + horas de persecución ahorradas (minutos por documento configurables; cifra ilustrativa).
3. Cada documento pendiente tiene un botón "Reclamar" que abre el simulador de conversación.
4. Flujo: recordatorio amable del documento que falta → el cliente responde por botón → adjunto simulado → confirmación de recepción.
5. El documento pasa a "recibido"; si era el último, el expediente pasa a "completo" con distintivo visual y los contadores suben.
6. "Reiniciar demo" restaura todo.
7. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio y avatar, clientes y trámites de los datos iniciales, nombres de los documentos, copy de los mensajes y colores. El flujo de reclamación y la estructura no se tocan.
