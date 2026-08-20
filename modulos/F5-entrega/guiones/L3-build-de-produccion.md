# L3 | El build: de demo a producción

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F5 Entrega | 10-14 min | plantilla-brief-solucion.md (recurso de F2-Construye — se amplía aquí; F5 no añade recurso propio) |

**Objetivo:** el piloto real construido con los datos del cliente en ≤5 días de trabajo (sobre los 7 comprometidos en la llamada de arranque).

## Gancho (0:00-0:20)

"Llamada de arranque hecha, alcance leído en voz alta, accesos recibidos (L2). Ahora toca lo que el cliente ha pagado: construir de verdad. Y empiezo por la mejor noticia del módulo — no empiezas de cero. Empiezas de tu demo."

[PANTALLA: pantalla partida — a la izquierda, la demo de F2 funcionando; a la derecha, la carpeta del proyecto real recién creada a partir de ella]

## Sección 1 — Qué cambia de demo a producción

- La frase que ordena toda la lección: **la demo convence; la producción trabaja.** Son tres saltos, y solo tres:
  1. **Datos reales.** Los del formulario de arranque, no los inventados de tu brief de F2. El panel ya no enseña a "Lucía Ferrer": enseña a los clientes de tu cliente.
  2. **Usuarios reales.** Ya no la maneja tu cuñado en el test de F2: la manejará la recepcionista, el gestor, el dueño — cada día, sin ti delante.
  3. **Integraciones reales.** El ejemplo de F2 lo dice todo: la demo dental simulaba la conversación de WhatsApp dentro de la web; el piloto la envía de verdad al móvil del paciente.
- Y con los datos reales llega una responsabilidad nueva: te han confiado accesos e información del negocio. Trátalos con confidencialidad, usa solo lo necesario para el proyecto y deja su uso pactado en el acuerdo (L2). Y la coletilla de la casa: esto es orientación práctica, no asesoría legal — valida tu proceso con un profesional.

## Sección 2 — El brief de producción: tu plantilla de F2, ampliada

- No hay herramienta nueva que aprender: es la plantilla de brief de F2-L3 — la misma que dirigió tu demo — con **dos secciones nuevas al final**:
  - **7. Datos reales del cliente:** qué te ha llegado del formulario de arranque, en qué formato está y qué falta por pedir. Si falta algo, se pide HOY, no el día 4.
  - **8. Integraciones que entran:** solo las que figuran en el alcance ENTRA. Ni una más, por bien que quede.
- La regla de oro sigue intacta: describe QUÉ debe pasar y PARA QUIÉN, nunca cómo programarlo.

[PANTALLA: la plantilla de F2 abierta, con las secciones 7 y 8 añadiéndose en directo sobre el ejemplo dental]

## Sección 3 — Las integraciones reales, a nivel de flujo

- **WhatsApp de verdad:** elige un proveedor actual de WhatsApp Business API y deja que Claude Code te guíe en la integración — cuenta, número del cliente, plantillas de mensaje, conexión con tu solución. El proveedor concreto cambia con el tiempo; el flujo, no.
- **Chat libre:** se conecta con la API de Anthropic. Recuerda la decisión de F2: ese coste por uso se repercute al cliente como coste operativo — no lo absorbes tú. Y si no quedó dicho en la venta, se pacta AHORA, en la llamada de arranque, y se recoge en el acuerdo (hay una línea para ello): un coste sorpresa en la primera factura destruye más confianza que el coste mismo.
- **Si la solución es pública** (una web que recoge datos de clientes finales): necesita política de privacidad enlazada, aviso de cookies antes de disparar cualquier pixel y casilla de consentimiento en los formularios — pídeselo a Claude Code al construirla. Misma coletilla de siempre.

## Sección 4 — Construye en pasos, empezando por tu demo

- El método es el de F2-L3, sin cambiar una coma: el brief de producción entero como primera instrucción → **una petición = un cambio** → probar entre pasos → los errores se pegan, no se pelean.
- La diferencia es el punto de partida: abres el repo de tu demo y construyes encima. Los datos de ejemplo salen, los datos reales entran, el simulador se sustituye por la integración. "El amateur empieza de cero; tú empiezas de tu demo."
- El calendario (días ilustrativos, ajústalo a tu solución): día 1, datos reales dentro y flujo principal funcionando; días 2-3, integraciones; día 4, casos límite del negocio real; día 5, margen y pulido. Comprometiste 7 días (L2, con la infrapromesa del ~30%); planificas 5. Ese margen no es pereza: es tu seguro contra imprevistos — y tu oportunidad de entregar antes de lo prometido.
- Cada día del build debe producir algo enseñable — una captura, un vídeo corto, un "míralo aquí". Guárdalo: es la materia prima del plan de comunicación de L4.

[PANTALLA: Claude Code sustituyendo el simulador de WhatsApp de la demo dental por la integración real, con la prueba del primer mensaje llegando a un móvil]

## Sección 5 — Imprevistos y la regla de alcance

- **Los atascos se comunican, no se esconden.** Si algo te bloquea más de medio día, el cliente lo sabe por ti ANTES de preguntar: qué ha pasado, qué estás haciendo y cuándo tendrás noticias. En L4 verás el mensaje exacto; aquí queda la regla.
- **Lo que no está en ENTRA no se construye.** A mitad de build se te ocurrirán mejoras, y al cliente también. La respuesta es siempre la misma que en L2: "lo apunto para la fase 2". Cada extra gratis alarga tu entrega, encoge tu margen y devalúa lo pactado — los criterios de aceptación que pactasteis en L2 no crecen a mitad de partido.

## Cierre + CTA

- Recap en 2 frases: "De demo a producción hay tres saltos —datos reales, usuarios reales, integraciones reales— y un solo método: el de F2, construyendo encima de tu demo. Comprometes 7 días, planificas 5, y lo que no está en ENTRA se apunta para la fase 2."
- **Acción del alumno AHORA:** amplía tu brief de F2 con las secciones 7 y 8, comprueba que tienes todos los datos del formulario de arranque y dale a Claude Code la primera instrucción del build hoy mismo.
- **KPI de esta lección:** piloto funcionando con datos reales del cliente en ≤5 días de trabajo (sobre 7 comprometidos).
- Puente: "Mientras tú construyes, tu cliente solo percibe una de dos cosas: progreso o silencio. En la próxima lección montamos el plan para que cada día vea progreso — sin robarte ni media hora de build."
