# BRIEF — Recuperación de no-shows y citas · Clínicas dentales

> El brief que produjo la demo de esta plantilla (`index.html`). Es el ejemplo canónico del programa (F2-R2 y F2-L5). Para personalizarlo a TU nicho: cambia contexto, datos y copy — los 7 comportamientos y el flujo no se tocan. La plantilla rellenable en blanco vive en el recurso F2-R2 del programa.

**Solución del catálogo:** Recuperación de no-shows y citas · **Nicho:** clínicas dentales

## 1. Contexto

- **Mi negocio cliente es:** una clínica dental independiente en España, 3 sillones, con una recepcionista saturada en horas punta. Nombre inventado pero verosímil para la demo: **Clínica Dental Ensanche**.
- **Su cliente final es:** pacientes recurrentes (higienes, revisiones, tratamientos) que cancelan o no se presentan (no-show) y a los que nadie tiene tiempo de perseguir por teléfono.
- **El dolor que esta demo enseña resuelto:** cada sillón vacío es facturación perdida; las citas caídas no se recuperan porque recuperarlas exige perseguir una a una y no hay manos.
- **Quién usará la pantalla en la demo:** el dentista propietario (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

## 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve un panel con las citas de hoy y de mañana: paciente, tratamiento, hora y estado (confirmada / cancelada / no-show / recuperada).
2. Sobre el panel, dos contadores bien visibles: "citas recuperadas este mes" y "facturación recuperada" (calculada con un ticket medio configurable; cifra ilustrativa).
3. Al marcar una cita como "cancelada" o "no-show", se abre al lado un simulador visual de conversación tipo WhatsApp — dentro de la web, no WhatsApp real — que reproduce la recuperación mensaje a mensaje.
4. La conversación simulada sigue este flujo: mensaje al paciente lamentando la cancelación → propuesta de 2 huecos libres reales del panel → el paciente elige uno pulsando una respuesta sugerida (botones dentro del simulador: conversación guiada, sin texto libre) → confirmación con día y hora.
5. Al confirmarse, la cita reaparece en el panel en su nuevo hueco con estado "recuperada", y los dos contadores suben.
6. Un botón "reiniciar demo" devuelve todos los datos a su estado inicial, para repetir el flujo en cada llamada de venta.
7. Todo el flujo es usable desde el móvil.

## 3. Qué NO entra

- WhatsApp de verdad: la conversación es una simulación visual dentro de la web. La integración real llega en F5, con el piloto pagado.
- Conexión con el programa de gestión de la clínica: los datos de la demo son de ejemplo.
- Recordatorios por SMS o por llamada de voz.
- Usuarios, contraseñas y pagos.
- Más de una clínica (la demo es mono-clínica).

## 4. Datos de ejemplo

Ticket medio para el contador: 120€ (cifra ilustrativa, configurable).

| Paciente | Tratamiento | Cita | Estado inicial |
|---|---|---|---|
| Lucía Ferrer | Higiene dental | Hoy 10:00 | Confirmada |
| Jorge Lamas | Endodoncia | Hoy 11:30 | No-show |
| Marta Ruiz | Revisión | Hoy 12:15 | Cancelada |
| Andrés Molina | Empaste | Hoy 16:00 | Confirmada |
| Carmen Ortega | Blanqueamiento | Mañana 9:30 | Confirmada |
| Pablo Ibáñez | Higiene dental | Mañana 11:00 | Cancelada |

Huecos libres para ofrecer en la conversación: hoy 13:00 · hoy 17:30 · mañana 10:15 · mañana 12:30.

## 5. Aspecto

- **Estilo general:** limpio y sanitario; debe transmitir "software serio de clínica", no "proyecto de fin de semana".
- **Referencias:** el panel, como una app moderna de citas médicas (tarjetas, mucho blanco, estados con color); el simulador, reconocible al instante como una conversación de WhatsApp (burbujas verdes y blancas), sin usar logos oficiales.
- **Colores / sensación:** blanco y azul claro; tipografía grande y legible — el dentista lo verá a veces desde el móvil.

## 6. Cómo sabré que funciona

- [ ] El flujo completo (marcar no-show → conversación → cita recuperada → contadores suben) se reproduce en menos de 1 minuto sin explicar nada.
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] El botón "reiniciar demo" deja todo listo para repetir el flujo.
- [ ] Todos los datos parecen de una clínica real: nombres, tratamientos y horas verosímiles.
- [ ] La URL carga rápido a la primera.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
