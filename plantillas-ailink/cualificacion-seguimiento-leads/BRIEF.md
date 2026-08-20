# BRIEF — Cualificación y seguimiento de leads (inmobiliarias)

> Brief completo relleno para el nicho típico de esta solución (formato de F2-R2). **Cómo se usa:** se lo das ENTERO a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …") y, a partir de la primera versión, iteras con las 3 reglas de dirección del final. Si tu nicho es otro, cambia negocio, leads y preguntas de cualificación — el flujo es el mismo.

**Solución del catálogo:** Cualificación y seguimiento de leads · **Nicho:** inmobiliarias

### 1. Contexto

- **Mi negocio cliente es:** una inmobiliaria de barrio en España, 4 agentes, con cartera de venta y alquiler, que recibe cada semana decenas de contactos desde los portales inmobiliarios y su web. Hoy los leads se apuntan donde se puede y se responden cuando alguien tiene un hueco: muchos se enfrían sin que nadie los persiga. Nombre inventado pero verosímil para la demo: **Fincas Alcaraz** (Murcia).
- **Su cliente final es:** compradores e inquilinos que preguntan por un inmueble concreto y esperan respuesta inmediata; el que no la recibe escribe a la agencia de enfrente con el mismo piso guardado en favoritos.
- **El dolor que esta demo enseña resuelto:** responder tarde regala la operación a la competencia, y nadie tiene tiempo de separar curiosos de compradores ni de insistir a los que dejan de contestar.
- **Quién usará la pantalla en la demo:** el gerente de la inmobiliaria (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve un panel "Leads — Fincas Alcaraz" con 4 columnas: **Nuevo → Contactado → Cualificado → Cita**. Cada tarjeta muestra: nombre del lead, inmueble por el que pregunta (con precio), origen (portal inmobiliario / web propia / recomendación) y cuánto tiempo lleva esperando.
2. Sobre el panel, dos contadores bien visibles: "leads cualificados este mes" y "visitas agendadas" (cifras ilustrativas de partida).
3. Al pulsar la tarjeta de Laura Cifuentes (columna Nuevo), se abre al lado un simulador visual de conversación tipo WhatsApp — dentro de la web, no WhatsApp real — donde el asistente saluda a Laura por su nombre citando el inmueble exacto por el que preguntó.
4. La conversación es guiada: el lead responde pulsando respuestas sugeridas (botones dentro del simulador, sin texto libre). Flujo: saludo con el inmueble → pregunta de presupuesto (3 opciones) → pregunta de plazos ("¿para entrar a vivir ya o mirando sin prisa?") → propuesta de 2 franjas de visita → elección por botón → confirmación con día y hora.
5. La tarjeta se mueve de columna EN DIRECTO según avanza la conversación: a "Contactado" con el primer mensaje, a "Cualificado" al responder presupuesto y plazos, a "Cita" al confirmar la franja — y en ese momento los dos contadores suben y la tarjeta muestra el día y la hora de la visita.
6. La tarjeta de Nerea Garmendia (columna Contactado) lleva la etiqueta "sin respuesta desde hace 2 días". Al pulsarla, el simulador muestra la secuencia de seguimiento automático ya enviada — mensaje inicial (día 0) y recordatorio amable (día 2) — y Nerea contesta al segundo toque: retoma el flujo de cualificación con botones y su tarjeta también avanza hasta "Cita". Esto enseña el "seguimiento" del nombre de la solución: el sistema insiste solo, sin que nadie de la agencia se acuerde.
7. Un botón "reiniciar demo" devuelve todos los datos a su estado inicial (columnas, etiquetas, contadores y conversaciones), para repetir el flujo en cada llamada de venta.
8. Todo el flujo es usable desde el móvil (columnas con scroll horizontal o apiladas, sin perder el movimiento de tarjetas).

### 3. Qué NO entra

- Conexión real con los portales inmobiliarios ni con WhatsApp: todo es una simulación visual dentro de la web. Las integraciones reales llegan en F5, con el piloto pagado.
- Texto libre ni cerebro de IA real: la conversación está guionizada (decisión del programa).
- Envío real de emails o SMS de seguimiento: la secuencia se muestra simulada.
- CRM real y persistencia: los datos viven en la página y se reinician con el botón.
- Fichas de inmuebles, valoraciones ni portal de propiedades: solo el flujo de leads.
- Usuarios, contraseñas y pagos.
- Más de una oficina (la demo es mono-agencia).

### 4. Datos de ejemplo

Contadores de partida (ilustrativos): leads cualificados este mes **23** · visitas agendadas **11**.

| Lead | Inmueble por el que pregunta | Origen | Estado inicial |
|---|---|---|---|
| Laura Cifuentes | Piso 3 hab. en C/ Alfareros 12 — 235.000€ | Portal inmobiliario | Nuevo (hace 4 min) |
| Miguel Ángel Soria | Ático en Av. Libertad 8 — 310.000€ | Portal inmobiliario | Nuevo (hace 26 min) |
| Nerea Garmendia | Adosado en Urb. Los Fresnos — 289.000€ | Web propia | Contactado — sin respuesta desde hace 2 días |
| Ricardo Peña | Piso 2 hab. en C/ Cervantes 4 — 168.000€ | Portal inmobiliario | Cualificado (presupuesto ok, entrar en menos de 3 meses) |
| Sonia Vidal | Local comercial en C/ Mayor 21 — 1.200€/mes | Recomendación | Cita — jueves 17:00 |

Opciones de presupuesto en la conversación de Laura: "Hasta 240.000€ con hipoteca preaprobada" · "Necesitaría financiación" · "Solo estoy mirando". Opciones de plazos: "Para entrar a vivir cuanto antes" · "En los próximos 6 meses" · "Sin prisa, comparando".

Franjas de visita para ofrecer: miércoles 17:30 · sábado 11:00.

### 5. Aspecto

- **Estilo general:** panel tipo tablero de columnas moderno y limpio, como un CRM sencillo de agencia — debe transmitir "software serio de inmobiliaria", no "proyecto de fin de semana".
- **Referencias:** el panel, como un tablero kanban de una app de gestión actual (tarjetas blancas, columnas con cabecera y contador, transición visible al mover); el simulador, reconocible al instante como una conversación de WhatsApp (burbujas verdes y blancas), sin usar logos oficiales.
- **Colores / sensación:** blanco y azul oscuro; un color por estado (gris = nuevo, ámbar = contactado, azul = cualificado, verde = cita); tipografía grande y legible — el gerente lo verá a veces desde el móvil.

### 6. Cómo sabré que funciona

- [ ] El flujo estrella (pulsar lead nuevo → conversación → tarjeta subiendo de columna → cita → contadores suben) se reproduce en menos de 1 minuto sin explicar nada.
- [ ] El caso de seguimiento (Nerea) se entiende sin narrarlo: se VE que el sistema insistió solo y rescató un lead que se había enfriado.
- [ ] El botón "reiniciar demo" restaura columnas, etiquetas, contadores y conversaciones exactos.
- [ ] Funciona igual en el móvil que en el ordenador, y el movimiento de tarjetas se sigue viendo.
- [ ] Todos los datos parecen de una agencia real: nombres, calles, precios y franjas verosímiles.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
