# Checklist de entrega de producción

> Recurso de L5 (F5 Entrega). **Regla del programa: no se agenda la sesión de traspaso sin el Bloque 1 completo** (salvo el check del usuario real, que se hace EN el propio traspaso), **y la firma de "entregado" solo llega con los 4 bloques cerrados.** Ni "es solo el piloto", ni "lo pulo mañana": una entrega rota destruye en 5 minutos la confianza de 3 semanas. Esta checklist es la hermana mayor de tu checklist pre-demo de F2-L6 — misma disciplina, apuestas reales.

| | |
|---|---|
| **Cliente / proyecto** | ______________________ |
| **Solución entregada** | ______________________ |
| **URL / entorno de producción** | ______________________ |
| **Fecha comprometida al cliente** | ______________________ |
| **Fecha planificada (con margen, L3)** | ______________________ |

## Bloque 1 — QA con datos reales

- [ ] **Flujo completo probado 3 veces con datos reales.** Entero y desde el principio, con los datos del cliente dentro — no con los de ejemplo. Tres pasadas seguidas sin un solo fallo; si a la tercera asoma algo raro, no estaba arreglado: estaba escondido. Arreglas, y las tres pasadas empiezan de cero.
- [ ] **El usuario real lo ha recorrido delante de ti.** La versión producción del test del cuñado: la persona del cliente que lo usará cada día lo recorre sin ayuda mientras tú miras y apuntas. Donde se atasque hoy, se atascará cada mañana cuando tú no estés.
- [ ] **Casos límite del negocio real probados.** No solo entradas raras: lo que pasa de verdad en ese negocio — mensajes fuera de horario, nombres con acentos, cancelaciones dobles, campos vacíos, periodos sin datos. Pídele a Claude Code la lista pensando en ESE negocio y pruébalos uno a uno.
- [ ] **Errores dignos.** Desconecta o fuerza el fallo de cada integración (WhatsApp, API) y mira qué ve el usuario: un mensaje claro y humano, nunca una pantalla rota con jerga. La integración puede fallar; tu solución no puede parecer rota.
- [ ] **Probado EN MÓVIL con la URL real.** Y al menos una vez con datos móviles en lugar de wifi. Tu cliente vive en su móvil; su solución también.
- [ ] **Carga rápida con la URL real.** Primera carga en frío, con datos móviles, sin espera incómoda: en producción el que la sufre es el cliente final del negocio, cada día.

## Bloque 2 — Formación

- [ ] **Vídeo de uso grabado y enviado.** 2-3 minutos de grabación de pantalla, en el lenguaje del cliente, sin jerga: cómo se usa en el día a día.
- [ ] **Sesión de traspaso hecha.** 20-30 minutos en directo con el cliente (o con quien usará la solución cada día).
- [ ] **El cliente la manejó SOLO.** De principio a fin, delante de ti, sin que tocaras tú. Si condujiste tú, el traspaso no cuenta: repítelo.

## Bloque 3 — Cierre

- [ ] **Criterios de aceptación repasados y firmados JUNTOS.** La lista pactada en la llamada de arranque (L2), uno a uno, en voz alta, marcando "terminado" con el cliente delante. Lo nuevo que surja no reabre la lista: se apunta para la fase 2.
- [ ] **Documentación entregada.** Dos párrafos —qué hace la solución y qué necesita para funcionar— más la lista de accesos. Copia para el cliente y copia para tu biblioteca (L7).

## Bloque 4 — Post-entrega

- [ ] **Cobro final enviado el día de la entrega.** Si es proyecto: el 50% restante `[BORRADOR]` — el mejor día para cobrar es el día del "wow" (L6).
- [ ] **Testimonio pedido en el pico.** Hoy, no "más adelante": guía y preguntas en L6 y su recurso.
- [ ] **Tracker actualizado.** Proyecto marcado como entregado, fechas reales apuntadas.

## Firma: entregado

| Campo | |
|---|---|
| **Todos los checks marcados** | Sí / No |
| **Firma** | ______________________ |
| **Fecha de entrega real** | ______________________ |

> Al firmar declaras el proyecto **entregado**: QA pasado, cliente formado, criterios de aceptación cerrados. Si entre la firma y la entrega cambias cualquier cosa de la solución —lo que sea—, la firma caduca y el Bloque 1 se pasa de nuevo. Y al terminar, no cierres el ordenador todavía: los 30 minutos que convierten esta entrega en plantilla son L7.
