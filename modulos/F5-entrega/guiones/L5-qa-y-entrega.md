# L5 | QA de producción y entrega

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F5 Entrega | 10-14 min | recursos/checklist-entrega-produccion.md |

**Objetivo:** entrega ejecutada: QA pasado, cliente formado, criterios de aceptación firmados.

## Gancho (0:00-0:20)

"En F2 aprendiste una ley: una demo que falla delante del cliente es credibilidad muerta. Hoy esa ley sube de categoría, porque ya no hay demo — hay un cliente que ha pagado. Una entrega rota destruye en 5 minutos la confianza que has construido en 3 semanas. Así que hoy no entregamos todavía: hoy primero rompemos."

[PANTALLA: la frase "UNA ENTREGA ROTA DESTRUYE EN 5 MINUTOS LA CONFIANZA DE 3 SEMANAS" en grande]

## Sección 1 — El QA de producción: tu checklist de F2, con apuestas reales

- QA —el control de calidad: probarlo todo antes de que lo pruebe otro— no es nuevo para ti: es la checklist pre-demo de F2-L6, la que ya te salvó de aprender fallos delante de un cliente. La checklist de entrega (recurso) es su hermana mayor: misma disciplina, cinco checks subidos de nivel.
  - **Flujo completo, tres veces, con datos reales.** Entero y desde el principio, con los datos del cliente dentro — no con los de ejemplo. Si a la tercera asoma algo raro, no estaba arreglado: estaba escondido.
  - **El usuario real delante.** La versión producción del test del cuñado: la persona que lo usará cada día —la recepcionista, el gestor— lo recorre delante de ti, sin ayuda. Donde se atasque ella hoy, se atascará cada mañana cuando tú no estés.
  - **Casos límite del negocio real.** Ya no son solo entradas raras: son las cosas que pasan de verdad en ese negocio. El cliente que escribe a las 3 de la madrugada, el nombre con acentos, la cita cancelada dos veces, el mes sin datos. Pídele a Claude Code la lista pensando en ESE negocio, y pruébalos uno a uno.
  - **Errores dignos.** Las integraciones fallan a veces: WhatsApp que no responde, una API caída. La pregunta no es si fallará, sino qué verá el usuario cuando falle: un mensaje claro y humano ("no hemos podido enviar el mensaje, lo reintentamos en unos minutos"), nunca una pantalla rota llena de jerga.
  - **Móvil, siempre.** Con la URL real y datos móviles. Tu cliente vive en su móvil; su solución también.

[PANTALLA: recursos/checklist-entrega-produccion.md abierta, bloque a bloque]

## Sección 2 — La regla intacta

- La misma de F2, palabra por palabra: **nada se entrega sin la checklist completa.** Ni "es solo el piloto", ni "esto se lo enseño ya y lo pulo mañana". La checklist termina en una firma, y esa firma es tu permiso para entregar.
- No es burocracia: es la diferencia entre un profesional y un aficionado con prisa. El cliente no recordará las diez cosas que funcionaron; recordará la pantalla en blanco.

## Sección 3 — Formación: el vídeo y el traspaso

- Dos piezas, ninguna opcional:
  1. **El vídeo de uso (2-3 min).** Grabación de pantalla, en el lenguaje del cliente, sin jerga: cómo se usa la solución en el día a día. Queda para siempre — para el empleado nuevo, para el "¿cómo era esto?" del mes que viene.
  2. **La sesión de traspaso al cliente (20-30 min, en directo).** Y aquí, la regla de oro de la lección: **el CLIENTE maneja la solución delante de ti — no tú delante de él.** Si conduces tú, él asiente, no aprende, y en dos semanas no lo usa. Y un software que el cliente no usa es un proyecto muerto con la factura pagada — y un retainer que no llegará.
- Tu papel en el traspaso: mirar, apuntar dónde se atasca y solo intervenir si se bloquea. Cada atasco suyo es un arreglo tuyo antes de cerrar — o una línea del vídeo de uso que faltaba.

## Sección 4 — El cierre formal: "terminado" se firma juntos

- Los criterios de aceptación —la lista de checks que pactasteis en la llamada de arranque como definición de "terminado" (L2)— existen para este momento exacto. Se repasan uno a uno, en la misma sesión de traspaso, y se marcan JUNTOS, en voz alta, delante del cliente.
- Sin este ritual, el proyecto no acaba nunca: siempre habrá "una cosita más", y un proyecto que no acaba es un piloto que no cobra su final ni propone su retainer. Con el ritual, el final es un hecho compartido, no una opinión tuya.
- Lo que surja nuevo durante el repaso no reabre la lista: se apunta para la fase 2 — y acabas de encontrar el primer contenido de tu propuesta de retainer (eso es materia de F6).

[PANTALLA: los criterios de aceptación del proyecto marcándose uno a uno, con el último check en verde]

## Sección 5 — Documenta lo entregado (15 minutos que valen doble)

- Antes de cerrar el día: dos párrafos —qué hace la solución y qué necesita para funcionar— más la lista de accesos entregados. Nada más.
- Esos 15 minutos alimentan dos negocios: tu fábrica de plantillas (L7 — el segundo cliente te costará la mitad) y la propuesta de mantenimiento que verás en F6.

## Cierre + CTA

- Recap en 2 frases: "El QA de producción es tu checklist de F2 con apuestas reales: datos reales, usuario real, errores dignos, móvil — y nada se entrega sin ella completa. La entrega no acaba cuando el software funciona: acaba cuando el cliente lo maneja solo y los criterios de aceptación están firmados juntos."
- **Acción del alumno AHORA:** pasa entera la checklist de entrega con tu piloto, agenda la sesión de traspaso con tu cliente y graba el vídeo de uso de 2-3 minutos.
- **KPI de esta lección:** checklist de entrega completa y firmada + criterios de aceptación marcados "terminado" junto al cliente.
- Puente: "Tu cliente acaba de ver su solución funcionando y lo ha manejado él mismo: está en su pico de emoción. La próxima lección va de aprovechar ese pico — cobrar el final, capturar la prueba y encadenar el siguiente paso."
