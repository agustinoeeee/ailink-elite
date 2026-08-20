# Catálogo técnico de soluciones AILINK

> Recurso de L4 (F2 Construye). Las 8 soluciones del catálogo AILINK — mismos nombres canónicos que conociste en F1 — vistas por dentro: qué hacen, qué necesitan y qué simular en tu demo web. Recuerda la distinción de L4: la **DEMO** es web, se construye ahora en F2 y simula el flujo; el **PILOTO REAL** con integraciones (conectar con sistemas de fuera: el WhatsApp del negocio, su calendario, su teléfono, Google) llega en F5, con cliente pagando — y muchas veces también empieza en web.
>
> **Regla del programa: tu demo = la solución de tu oferta V1 (cuaderno de F1).**

**Leyenda de las fichas**
- **Qué necesita**: `solo web` · `web + datos` (datos del negocio: tarifas, citas, documentos de ejemplo) · `integración externa en F5` (la demo sigue siendo solo web: simula la integración).
- **Dificultad 1-3**: lo que cuesta construir la demo dirigiendo a Claude Code (1 = una tarde buena).
- **Potencia de demo 1-3**: el tamaño del "quiero eso" cuando la enseñas al cliente.

---

## 1. Recepcionista IA (WhatsApp/llamadas)

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Integración externa en F5 (demo: solo web) | 1 | 3 |

**Qué hace por dentro:** una conversación que atiende como lo haría la persona de recepción: saluda, responde las dudas de siempre (horarios, ubicación, cómo funciona el servicio), propone huecos libres y apunta la cita en una agenda. El cerebro es la IA con las instrucciones y datos del negocio; la memoria, una agenda y una lista de preguntas frecuentes.

**Demo web recomendada:** un simulador visual de WhatsApp dentro de la web — la pantalla del móvil dibujada en la página — donde el visitante hace de cliente eligiendo entre respuestas sugeridas (botones) y ve a la recepcionista responder y cerrar una cita; al lado, un mini-panel donde la cita aparece al instante. Es una conversación guiada: el flujo está guionizado, como el simulador de la demo dental.

**Nota honesta:** el piloto real conecta el cerebro de IA de verdad (API de Anthropic, coste por uso repercutible al cliente) — eso llega en F5.

## 2. Recuperación de no-shows y citas

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Integración externa en F5 (demo: web + datos) | 1 | 3 |

**Qué hace por dentro:** vigila una agenda, detecta citas canceladas y no-shows, y lanza una secuencia de mensajes amable para reagendar. Cada respuesta del cliente actualiza la agenda sola; lo que no se recupera queda en una lista para que el negocio llame. En el piloto real se conecta a la agenda y al canal de mensajes del cliente (F5).

**Demo web recomendada:** un panel con la agenda de un negocio inventado pero verosímil del nicho; marcas una cita como cancelada y, a la derecha, un simulador de conversación muestra los mensajes de recuperación hasta que la cita vuelve a la agenda. Es la demo que se construye en directo en L5.

## 3. Cualificación y seguimiento de leads

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Integración externa en F5 (demo: web + datos) | 2 | 3 |

**Qué hace por dentro:** recibe leads, les hace las preguntas que separan curiosos de compradores, les pone nota y programa seguimientos automáticos a los que se enfrían. El negocio ve un panel claro: quién está caliente, quién espera respuesta y a quién se recontacta hoy. En real se conecta a las fuentes de leads (formularios, portales, campañas) y al canal de mensajes (F5).

**Demo web recomendada:** panel de leads de ejemplo con columnas por estado + un simulador de conversación de cualificación; cuando el lead responde bien, su tarjeta sube de columna en directo delante del cliente.

## 4. Presupuestos automáticos

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Web + datos (tarifas del negocio) | 2 | 3 |

**Qué hace por dentro:** un formulario o chat recoge los datos del trabajo (qué, cuánto, dónde), aplica las tarifas y reglas del negocio y genera en segundos un presupuesto presentable, con desglose por partidas, listo para enviar. La memoria son las tarifas; el cerebro convierte la petición en partidas. Suele vivir en web incluso en el piloto real.

**Demo web recomendada:** rellenas 4-5 campos de un trabajo típico del nicho y aparece el presupuesto desglosado con el logo de un negocio inventado. El salto de "esto me lleva dos días" a "esto tarda 30 segundos" se explica solo.

## 5. Gestión documental

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Web + datos (documentos de ejemplo); integración con el software de la gestoría, si hace falta, en F5 | 3 | 2 |

**Qué hace por dentro:** recibe documentos (facturas, nóminas, contratos), lee cada uno, extrae los datos que importan (importes, fechas, identificadores), los clasifica y los vuelca ordenados en una tabla. Lo dudoso lo marca para revisión humana en vez de inventárselo. Es la única dificultad 3 del catálogo: leer documentos variados sin equivocarse es lo más delicado de construir.

**Demo web recomendada:** arrastras una factura de ejemplo a la página y ves sus datos aparecer extraídos y clasificados en la tabla. Demo sobria — pero a una gestoría en campaña de impuestos le brillan los ojos.

## 6. Automatización de reseñas Google

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Integración externa en F5 (demo: web + datos) | 2 | 2 |

**Qué hace por dentro:** después de cada servicio envía al cliente un mensaje pidiendo reseña; al satisfecho lo lleva a Google y al insatisfecho lo desvía a un formulario privado antes de que la queja se haga pública. Además prepara borradores de respuesta para las reseñas que van llegando. En real se conecta al perfil de Google del negocio y a su canal de mensajes (F5).

**Demo web recomendada:** simulador del flujo completo: servicio terminado → mensaje al cliente → dos caminos (contento / descontento) → panel de reseñas con la respuesta propuesta por la IA lista para aprobar.

## 7. Chatbot web cualificador

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Solo web — también en el piloto real | 1 | 3 |

**Qué hace por dentro:** un chat instalado en la web del negocio que atiende visitas 24/7, responde dudas con la información del negocio y cualifica: pregunta qué necesita el visitante, recoge sus datos y entrega el contacto ya filtrado, avisando de los urgentes. La joya oculta del catálogo: es 100% web incluso en el piloto real — se instala en la página del cliente y ya está funcionando.

**Demo web recomendada:** una web inventada pero verosímil del nicho (un despacho, una academia) con el chat en la esquina; el cliente potencial recorre la conversación eligiendo entre respuestas sugeridas (botones) — el flujo está guionizado, como el simulador de la demo dental — y, al terminar, ve su lead cualificado entrar en el panel.

**Nota honesta:** el piloto real conecta el cerebro de IA de verdad (API de Anthropic, coste por uso repercutible al cliente) — eso llega en F5.

## 8. Informes automáticos

| Qué necesita | Dificultad | Potencia de demo |
|---|---|---|
| Web + datos (tabla de ejemplo; en real, los datos del cliente — un volcado o una conexión ligera, en F5 si hace falta) | 2 | 2 |

**Qué hace por dentro:** toma los datos del negocio (ventas, citas, horas), calcula las métricas que el dueño mira de verdad y redacta un informe periódico en lenguaje claro: qué ha pasado, qué destaca y dónde conviene mirar. De la tabla de datos al informe legible sin que nadie toque nada.

**Demo web recomendada:** panel con datos de ejemplo del nicho y un botón "generar informe del mes": el informe aparece redactado y con sus gráficas, delante del cliente.

---

## Matriz dificultad × potencia de demo

| | Potencia 1 | Potencia 2 | Potencia 3 |
|---|---|---|---|
| **Dificultad 1** | — | — | Recepcionista IA (WhatsApp/llamadas) · Recuperación de no-shows y citas · Chatbot web cualificador |
| **Dificultad 2** | — | Automatización de reseñas Google · Informes automáticos | Cualificación y seguimiento de leads · Presupuestos automáticos |
| **Dificultad 3** | — | Gestión documental | — |

**Lectura:** arriba a la derecha está la esquina de oro — fácil de construir y espectacular de enseñar. Cuanto más abajo, más disciplina de brief e iteración pide (no más miedo: más pasos pequeños).

## Recomendación de primera demo

Si tu oferta V1 te deja margen, la primera demo recomendada del programa es **Recuperación de no-shows y citas** o **Recepcionista IA (WhatsApp/llamadas)** — y si tu nicho vive de su página web, **Chatbot web cualificador**. Máximo efecto visual, mínima complejidad: exactamente lo que necesita tu primera vez.

## Tu elección (la regla que manda)

**Tu demo = la solución de tu oferta V1 (cuaderno de F1).** La matriz orienta; tu oferta manda. Dos casos frecuentes:

1. **Tu oferta combina dos soluciones** (p. ej. recepcionista + recuperación): para la demo construye UNA, la de más potencia; la otra la cuentas de palabra en la llamada.
2. **Tu solución es dificultad 3**: no cambies de oferta — simplifica la primera versión de la demo. Simple y entregado gana a complejo y eterno.

**Si tu solución de la lista de F1 no aparece literal entre las 8 fichas, búscala aquí:**

| Lo que dice tu lista de F1 | Su ficha en este catálogo |
|---|---|
| Gestión/chatbot de reservas (restaurantes, fisioterapia) | Recepcionista IA o Chatbot web cualificador |
| Atención de huéspedes (alojamientos) | Chatbot web cualificador |
| Agenda de visitas (inmobiliarias) | Cualificación y seguimiento de leads |

| Campo | |
|---|---|
| **Mi solución (nombre canónico del catálogo)** | ______________________ |
| **Qué simulará mi demo (una frase)** | ______________________ |
| **Mi nicho (cuaderno de F1)** | ______________________ |
