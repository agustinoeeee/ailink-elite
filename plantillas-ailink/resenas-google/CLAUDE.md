# CLAUDE.md — Demo: Automatización de reseñas Google (Asador La Carrasca)

## Qué es este proyecto
Demo comercial web de automatización de reseñas Google para restaurantes. El objetivo es UN solo archivo (`index.html`), sin dependencias externas, desplegable tal cual, construido a partir de `BRIEF.md`. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final. La referencia estructural de calidad es la plantilla insignia `../recuperacion-citas-dental/index.html`.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Conversación GUIADA**: el "cliente" solo responde pulsando botones (estrellas, chips de respuesta sugerida). JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (el cerebro real llega en F5, con el piloto pagado). El "borrador de respuesta redactado por la IA" es un texto guionizado.
- **Los dos caminos son sagrados**: 4-5 estrellas → pantalla de reseña pública; 1-3 estrellas → queja desviada a la bandeja privada del dueño. Una queja NUNCA aparece en el panel de reseñas públicas ni baja la nota media, y una valoración de 1-3 NUNCA lleva a la pantalla de reseña pública.
- **Sin logos oficiales de Google** (ni de WhatsApp): la pantalla de reseña es genérica — estrellas, texto, "Deja tu reseña" — reconocible pero sin imitar la interfaz ni las marcas oficiales. Mencionar "Google" en el copy comercial está bien; usar sus logos o su estética calcada, no.
- **Datos ficticios y verosímiles**: nombres de comensales, mesas, horas y textos de reseña creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Las cifras (nota media, número de reseñas) son ilustrativas.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** — cada llamada de venta empieza limpia. Si añades estado nuevo (una reseña publicada, una queja, una respuesta aprobada), inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).

## Los 8 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel con los servicios terminados de hoy (cliente, mesa, hora, estado).
2. Tres marcadores visibles: nota media, reseñas nuevas del mes, quejas desviadas en privado.
3. "Pedir valoración" abre el simulador de conversación con la petición de 1-5 estrellas por botones.
4. Camino contento (4-5 estrellas): pantalla de reseña genérica → el cliente elige un texto sugerido → la reseña aparece en el panel público, la nota media sube y el contador del mes suma una.
5. Camino descontento (1-3 estrellas): disculpa → motivo por botones → la queja aparece SOLO en la bandeja privada del dueño; la nota media no baja.
6. Cada reseña pública nueva trae un borrador de respuesta guionizado con botón "Aprobar y publicar respuesta".
7. "Reiniciar demo" restaura todo.
8. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio y avatar, mesas/servicios → los trabajos del nicho, datos de la tabla de servicios, textos de reseña sugeridos, motivos de queja, copy de los mensajes y colores. Los dos caminos, los marcadores y la estructura no se tocan.
