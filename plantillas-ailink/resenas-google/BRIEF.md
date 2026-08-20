# Brief de la demo — Automatización de reseñas Google (restaurantes)

> Brief COMPLETO relleno (formato de F2-R2) para el nicho típico de esta solución. Se entrega entero a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …"); a partir de la primera versión, se itera con las 3 reglas de dirección del final.

**Solución del catálogo:** Automatización de reseñas Google · **Nicho:** restaurantes

### 1. Contexto

- **Mi negocio cliente es:** un asador familiar en Zaragoza con buen volumen (dos turnos llenos los fines de semana, grupos y celebraciones). Nombre inventado pero verosímil para la demo: **Asador La Carrasca**. Su nota media lleva más de un año clavada en 4,2 mientras el competidor de la misma calle luce un 4,6 — y la gente elige restaurante por la nota.
- **Su cliente final es:** comensales que acaban de pagar la cuenta. La mayoría sale contenta y no deja reseña porque nadie se lo pide en el momento; el que sale enfadado sí escribe — y en público.
- **El dolor que esta demo enseña resuelto:** las reseñas deciden reservas y nadie del equipo tiene tiempo (ni sistema) para pedirlas una a una; las quejas que se habrían arreglado con una llamada acaban publicadas en Google bajando la nota.
- **Quién usará la pantalla en la demo:** el dueño del restaurante (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve un panel del restaurante con los servicios terminados de hoy: cliente, mesa, hora y estado (pendiente de pedir valoración / valoración pedida / reseña publicada / queja privada).
2. Sobre el panel, tres marcadores bien visibles: **"nota media"** (empieza en 4,2 con 187 reseñas), **"reseñas nuevas este mes"** (empieza en 3) y **"quejas desviadas en privado"** (empieza en 1). Cifras ilustrativas.
3. Al pulsar "pedir valoración" en un servicio, se abre al lado un simulador visual de conversación tipo WhatsApp — dentro de la web, no WhatsApp real — con un mensaje de agradecimiento y la petición de valoración de 1 a 5 estrellas: el cliente responde pulsando las estrellas (botones dentro del simulador: conversación guiada, sin texto libre).
4. **Camino contento:** si pulsa 4 o 5 estrellas, el mensaje le da las gracias y le lleva a dejar la reseña pública: dentro del simulador aparece una mini-pantalla "Deja tu reseña" genérica (estrellas y texto, sin logos oficiales de Google) donde elige uno de los 3 textos de reseña sugeridos pulsando un botón. Al publicarla, la reseña aparece en el panel de "reseñas recientes" con sus estrellas, **la nota media sube en pantalla** (de 4,2 a 4,3 tras un par de reseñas de 5) y el contador de reseñas del mes suma una.
5. **Camino descontento:** si pulsa 1, 2 o 3 estrellas, la conversación NO le lleva a la reseña pública: le pide disculpas y le pregunta qué ha fallado con 3 motivos como botones; al elegir uno, confirma que el responsable le llamará hoy mismo. La queja aparece SOLO en la bandeja **"Quejas privadas — solo las ves tú"** del panel, con cliente y motivo. La nota media no baja y el contador de quejas desviadas suma una.
6. Cada reseña pública nueva llega al panel con un **borrador de respuesta ya redactado** (simulado, guionizado) y un botón "Aprobar y publicar respuesta"; al pulsarlo, la respuesta queda visible bajo la reseña como "Respuesta del propietario".
7. Un botón "reiniciar demo" devuelve todos los datos, marcadores y conversaciones a su estado inicial, para repetir el flujo en cada llamada de venta.
8. Todo el flujo es usable desde el móvil.

### 3. Qué NO entra

- Google de verdad: no se conecta al perfil de Google del restaurante ni publica reseñas reales; la pantalla de reseña es una simulación genérica sin logos ni interfaz oficial. La integración real llega en F5, con el piloto pagado.
- WhatsApp de verdad: la conversación es una simulación visual dentro de la web.
- Texto libre: reseñas, quejas y respuestas van con opciones guiadas y borradores guionizados (el cerebro de IA real llega en F5).
- Borrar o filtrar reseñas ya publicadas en Google: la solución actúa ANTES de que la queja se publique, no después.
- Más de un local, usuarios, contraseñas y pagos.

### 4. Datos de ejemplo

Marcadores iniciales: nota media **4,2** (187 reseñas) · reseñas nuevas este mes: **3** · quejas desviadas en privado: **1** (cifras ilustrativas).

| Cliente | Mesa | Hora | Estado inicial |
|---|---|---|---|
| Sergio Antón | Mesa 4 (2 pers.) | Comida 14:30 | Pendiente de pedir valoración |
| Nuria Esteban | Mesa 9 (4 pers.) | Comida 15:00 | Pendiente de pedir valoración |
| Familia Cabrera | Mesa 12 (6 pers.) | Comida 15:15 | Valoración pedida |
| Íñigo Zabala | Mesa 2 (2 pers.) | Cena 21:30 | Pendiente de pedir valoración |
| Rosa Peñalver | Mesa 6 (3 pers.) | Cena 22:00 | Pendiente de pedir valoración |

Textos de reseña sugeridos (camino contento, el cliente elige uno):
- "El chuletón, espectacular, y el servicio de diez. Volveremos seguro."
- "Buen producto y trato cercano. El flan casero, imprescindible."
- "Perfecto para ir en familia: rapidez y raciones generosas."

Motivos de queja (camino descontento, el cliente elige uno): "La comida tardó demasiado" · "El plato llegó frío" · "El trato en sala no fue el esperado".

Reseñas ya publicadas en el panel al abrir (para que no empiece vacío):
- Marisa Gil — 5 estrellas — "Celebramos ahí el cumpleaños de mi padre y todo perfecto." (hace 3 días, con respuesta del propietario ya publicada)
- Álvaro Pinto — 4 estrellas — "Muy buen asado, aunque el postre flojeó un poco." (hace 6 días, sin responder — con su borrador de respuesta pendiente de aprobar)

Ejemplo de borrador de respuesta guionizado: "¡Mil gracias, Sergio! Nos alegra que disfrutarais del chuletón. Os esperamos muy pronto — el equipo de Asador La Carrasca."

### 5. Aspecto

- **Estilo general:** panel limpio tipo herramienta de reputación online; debe transmitir "software serio que vigila mi nota", no "proyecto de fin de semana".
- **Referencias:** el panel, como una app moderna de reputación (tarjetas, estados con color, estrellas grandes); el simulador, reconocible al instante como una conversación de WhatsApp (burbujas verdes y blancas) sin logos oficiales; la pantalla de reseña, una ficha genérica de valoraciones — estrellas y texto — sin imitar la interfaz de Google.
- **Colores / sensación:** blanco con acentos granate y madera (asador) y estrellas en ámbar; tipografía grande y legible — el dueño lo verá a veces desde el móvil en la barra.

### 6. Cómo sabré que funciona

- [ ] Los dos caminos completos (4-5 estrellas → reseña pública y marcadores subiendo; 1-3 estrellas → queja privada) se reproducen en menos de 2 minutos sin explicar nada.
- [ ] La nota media y el contador del mes suben EN PANTALLA al publicarse una reseña — ese es el momento "quiero eso".
- [ ] Una queja privada jamás aparece en el panel de reseñas públicas ni baja la nota media.
- [ ] No hay logos oficiales de Google ni de WhatsApp en ninguna pantalla.
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] El botón "reiniciar demo" deja todo listo para repetir el flujo.
- [ ] Todos los datos parecen de un restaurante real: nombres, mesas, horas y reseñas verosímiles.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
