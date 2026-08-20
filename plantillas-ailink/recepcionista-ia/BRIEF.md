# Brief de solución — Recepcionista IA (clínica veterinaria)

> Formato de F2-R2, RELLENO para el nicho típico de esta solución. Se entrega entero a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …") y a partir de la primera versión se itera con las 3 reglas de dirección del final. Si tu nicho es otro, adapta los datos ANTES de construir.

**Solución del catálogo:** Recepcionista IA (WhatsApp/llamadas) · **Nicho:** clínicas veterinarias

### 1. Contexto

- **Mi negocio cliente es:** una clínica veterinaria independiente en España, 2 veterinarios y una auxiliar que además hace de recepción. El teléfono se satura en horas punta y fuera de horario nadie contesta: las llamadas perdidas se apuntan en un pósit, cuando se apuntan. Nombre inventado pero verosímil para la demo: **Clínica Veterinaria La Dehesa** (Calle del Olivar 22 · consulta L-V 9:30–20:00, sábados 10:00–14:00).
- **Su cliente final es:** dueños de mascotas (perros y gatos sobre todo) que llaman para vacunas, revisiones y dudas — clientes recurrentes durante toda la vida del animal — y que, si nadie les coge el teléfono, prueban en la clínica de dos calles más allá.
- **El dolor que esta demo enseña resuelto:** teléfono saturado y urgencias mezcladas con citas rutinarias; cada llamada perdida es una cita que se escapa y, a veces, un cliente de años que se pierde.
- **Quién usará la pantalla en la demo:** el veterinario propietario (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web se ve, a un lado, un mini-panel de recepción con dos bloques: "Llamadas perdidas de hoy" (hora, dueño, mascota, estado) y "Agenda de hoy y mañana" (hora, mascota, dueño, motivo); al otro lado, un simulador visual de conversación tipo WhatsApp — dentro de la web, no WhatsApp real — donde la recepcionista IA se presenta.
2. Sobre el panel, dos contadores bien visibles: "citas apuntadas por la recepcionista este mes" y "facturación estimada" (calculada con una consulta media configurable; cifra ilustrativa).
3. Al pulsar una llamada perdida, el simulador reproduce la atención mensaje a mensaje: la recepcionista escribe al dueño ("Hola, soy la asistente de la Clínica La Dehesa — hemos visto tu llamada…") y el dueño responde eligiendo entre respuestas sugeridas (botones dentro del simulador: conversación guiada, sin texto libre).
4. La recepcionista responde las dudas de siempre con los datos del negocio (horario, dirección, precio orientativo de la consulta) y propone 2 huecos libres reales de la agenda; el dueño elige uno con un botón y recibe confirmación con día, hora y nombre de la mascota.
5. Si el motivo es una urgencia (la llamada de Ana Beltrán: su perro lleva horas vomitando), la recepcionista NO da cita: muestra un aviso de urgencia con el teléfono directo de la clínica y la llamada queda marcada en el panel como "Urgencia derivada", en rojo.
6. Al confirmarse una cita, aparece al instante en la agenda del panel con la etiqueta "atendida por la recepcionista", la llamada perdida pasa a estado "convertida en cita" y los dos contadores suben.
7. Un botón "reiniciar demo" devuelve todos los datos a su estado inicial, para repetir el flujo en cada llamada de venta.
8. Todo el flujo es usable desde el móvil.

### 3. Qué NO entra

- WhatsApp de verdad ni llamadas de voz reales: todo es una simulación visual dentro de la web. La integración con el WhatsApp y el teléfono del negocio llega en F5, con el piloto pagado.
- Cerebro de IA real (API): la conversación es guiada y guionizada. El cerebro de verdad llega en F5.
- Conexión con el programa de gestión de la clínica: los datos de la demo son de ejemplo.
- Historiales clínicos ni fichas de las mascotas.
- Usuarios, contraseñas y pagos.
- Más de una clínica (la demo es mono-clínica).

### 4. Datos de ejemplo

Consulta media para el contador: 40€ (cifra ilustrativa, configurable). Contadores base al abrir: 26 citas · 1.040€. Precios orientativos para las respuestas: consulta general 35€, vacuna anual 45€ (ilustrativos). Teléfono de urgencias para la derivación: 618 402 275 (ficticio).

**Llamadas perdidas de hoy:**

| Hora | Dueño | Mascota | Qué pasa al pulsarla |
|---|---|---|---|
| 9:12 | Laura Cano | Rocky (perro, 4 años) | Quiere la vacuna anual: pregunta precio y termina con cita |
| 13:47 | Sergio Puente | Nala (gata, 7 años) | Pregunta el horario del sábado y pide cita de revisión |
| 20:35 | Ana Beltrán | Coco (perro, 11 meses) | Urgencia: lleva horas vomitando → derivación al teléfono, sin cita |

**Agenda de hoy y mañana:**

| Cita | Mascota | Dueño | Motivo |
|---|---|---|---|
| Hoy 10:00 | Duque (pastor alemán) | Miguel Antón | Vacuna polivalente |
| Hoy 12:30 | Misha (gata europea) | Rosa Peñalver | Revisión anual |
| Hoy 19:00 | Golfo (beagle) | Elena Sanchís | Control postoperatorio |
| Mañana 9:30 | Trufa (gata persa) | David Roldán | Desparasitación |

Huecos libres para ofrecer en la conversación: hoy 17:00 · hoy 18:30 · mañana 10:15 · mañana 12:00.

### 5. Aspecto

- **Estilo general:** cálido pero profesional; debe transmitir "software serio de clínica veterinaria", no "proyecto de fin de semana".
- **Referencias:** el panel, como una app moderna de citas (tarjetas, mucho blanco, estados con color: pendiente / convertida en cita / urgencia derivada); el simulador, reconocible al instante como una conversación de WhatsApp (burbujas verdes y blancas), sin usar logos oficiales.
- **Colores / sensación:** blanco y verde suave, con el rojo reservado para la urgencia; una huella de pata como icono del negocio; tipografía grande y legible — el veterinario lo verá a veces desde el móvil.

### 6. Cómo sabré que funciona

- [ ] El flujo completo (pulsar llamada perdida → conversación → cita en la agenda → contadores suben) se reproduce en menos de 1 minuto sin explicar nada.
- [ ] El camino de urgencia se distingue a la primera: rojo, sin cita, teléfono directo en pantalla.
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] El botón "reiniciar demo" deja todo listo para repetir el flujo.
- [ ] Todos los datos parecen de una clínica real: dueños, mascotas, motivos, precios y horas verosímiles.
- [ ] La URL carga rápido a la primera.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
