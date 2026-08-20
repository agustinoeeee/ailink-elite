# Guía de montaje — Formulario de arranque del cliente

> Fuente: `modulos/F5-entrega/recursos/formulario-arranque-cliente.md`
> Montaje estimado: 15 minutos en Tally o Typeform (el recurso da 30-45 min contando la conexión al pago y la prueba del circuito).

## Para qué sirve

Es el formulario post-pago. Hace dos trabajos a la vez: te da todo lo necesario para empezar a construir sin perseguir a nadie, y le manda al cliente la señal que necesita en sus 24 horas frágiles — "esto ya está en marcha".

**Quién lo rellena:** el cliente que acaba de pagar (idealmente con su contacto operativo delante, la persona que usará la solución cada día).

**Cuándo se envía:** **el mismo día del cobro**, sin excepción. Automáticamente si lo conectas como redirección de tu enlace de pago (Payment Link de Stripe), o a mano con el mensaje modelo. Se pide relleno **antes** de la llamada de arranque, que va agendada a 24-48 horas vista.

**Cuándo lo montas tú:** en cuanto desbloquees F5, **antes de tener cliente**. F4 corre en paralelo y tu primer cobro puede caer en cualquier reunión de esta semana; el kit se necesita ESE día.

---

## Ajustes generales

- **Título del formulario:** Formulario de arranque del cliente
- **Una pregunta por pantalla:** no. Aquí conviene lo contrario: **una pantalla por bloque**, con los campos agrupados. Son datos operativos, el cliente los tiene a mano y quiere terminar rápido. Objetivo de respuesta: 5-10 minutos.
- **Bloques:** 6, en este orden. Mantén el orden: empieza por lo fácil (datos del negocio) y termina por lo abierto.
- **Mensaje de bienvenida:** el .md no trae copy de pantalla de bienvenida. Lo que sí trae es el **mensaje de envío** (va por WhatsApp/email, fuera del formulario) — está en "Conexiones", al final de esta guía.
- **Obligatoriedad:** el .md no marca campo a campo qué es obligatorio. Lo que va abajo es una propuesta práctica — obligatorio todo lo imprescindible para construir y facturar, opcional el resto. Ajústala a tu caso.
- **Regla de oro del recurso:** adapta los campos a TU solución y **borra todo lo que no vayas a usar**. Cada campo de más es fricción de menos respuestas.
- **Pie del formulario** (copy literal, visible para el cliente):

  > "Los datos y accesos que compartas aquí se usan exclusivamente para construir tu solución. Pedimos solo lo necesario, los tratamos con confidencialidad y su uso queda recogido en el acuerdo de servicios que firmaremos."

---

## Bloque 1 · Datos del negocio

### 1.1

- **Enunciado:** Nombre comercial del negocio
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### 1.2

- **Enunciado:** Nombre fiscal y NIF/CIF (para el acuerdo y la factura)
- **Tipo de campo:** texto corto (o dos campos cortos: nombre fiscal / NIF-CIF)
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna. Alimenta directamente el acuerdo de servicios y la factura.

### 1.3

- **Enunciado:** Web y redes sociales (enlaces)
- **Tipo de campo:** texto largo (un enlace por línea)
- **Obligatoria:** no
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### 1.4

- **Enunciado:** Dirección / zona de actuación
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### 1.5

- **Enunciado:** Horario de atención al público
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

---

## Bloque 2 · Contacto operativo

**Descripción del bloque** (copy literal, va bajo el título del bloque):

> La persona que usará la solución cada día (recepción, administración, el propio dueño…).

### 2.1

- **Enunciado:** Nombre y cargo
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### 2.2

- **Enunciado:** Email y móvil
- **Tipo de campo:** dos campos — **email** + **teléfono**
- **Obligatoria:** sí (los dos)
- **Texto de ayuda:** —
- **Lógica:** ninguna. El teléfono te sirve además para el canal único si eligen WhatsApp (bloque 5).

### 2.3

- **Enunciado:** ¿Estará en la llamada de arranque?
- **Tipo de campo:** opción única
- **Opciones:**
  - Sí
  - No
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** si responde **No**, salta tu aviso: escribe al cliente y pídele que invite a esa persona a la llamada. Quien va a usar la herramienta tiene que estar.

---

## Bloque 3 · Accesos necesarios

**Cómo montarlo:** incluye **SOLO** los campos de tu tipo de solución y borra el resto de filas. Los accesos concretos dependen de tu stack; Claude Code te guía en cada integración. Todos estos campos son de **texto largo** y **obligatorios** para tu tipo de solución: sin ellos no hay build.

| Tipo de solución | Campos a montar (accesos típicos a pedir) |
|---|---|
| Chatbot de citas | Calendario del negocio (invitación de acceso) · número de teléfono para WhatsApp Business API (vía el proveedor que uses) · acceso a la web si va widget insertado |
| Automatización de facturación/documentos | Plantillas actuales de factura/documento · carpeta compartida donde llegan/salen los documentos · acceso al programa de facturación si lo hay |
| Dashboard | Fuentes de datos: hojas de cálculo, CRM, exportaciones · quién debe poder verlo |
| Agente de atención | Preguntas frecuentes reales de clientes · catálogo de servicios y precios públicos · tono de la marca (2-3 ejemplos de respuestas suyas) |

- **Tipo de campo:** texto largo, uno por acceso (usa el texto de la celda tal cual como enunciado del campo).
- **Obligatoria:** sí, salvo los que el propio texto marca como condicionales ("si va widget insertado", "si lo hay") — esos, opcionales.
- **Lógica:** lo que no llegue por aquí se pide **en la llamada de arranque**, compartiendo pantalla (paso 4 del guion). El formulario no bloquea el arranque, lo adelanta.
- **Aviso:** pide SOLO lo necesario para el flujo y trátalo con confidencialidad. La nota de confidencialidad del pie cubre este bloque.

---

## Bloque 4 · Datos para la solución

**Cómo montarlo:** los datos que pide la tabla de tu **brief de F2** (`plantilla-brief-solucion.md`), convertidos en preguntas. Los de abajo son **ejemplos ilustrativos** — sustitúyelos por los de tu solución.

### 4.1 (ejemplo)

- **Enunciado:** Lista de servicios con duración y precio
- **Tipo de campo:** texto largo
- **Obligatoria:** sí
- **Lógica:** ninguna.

### 4.2 (ejemplo)

- **Enunciado:** Las 10 preguntas que más os hacen los clientes (y cómo las respondéis hoy)
- **Tipo de campo:** texto largo
- **Obligatoria:** sí
- **Lógica:** ninguna.

### 4.3 (ejemplo)

- **Enunciado:** ¿Qué debe pasar cuando la solución no sepa responder? (derivar a un humano: ¿a quién?)
- **Tipo de campo:** texto largo
- **Obligatoria:** sí
- **Lógica:** ninguna. La respuesta suele acabar en un criterio de aceptación de la llamada de arranque.

### 4.4 (ejemplo)

- **Enunciado:** Textos legales de vuestra web (política de privacidad, aviso legal), si la solución es pública
- **Tipo de campo:** texto largo (enlaces o texto pegado)
- **Obligatoria:** no
- **Lógica:** monta este campo solo si tu solución es pública (accesible por los clientes finales del negocio). Si no lo es, bórralo.

---

## Bloque 5 · Comunicación

### 5.1

- **Enunciado:** Canal preferido para el día a día
- **Tipo de campo:** opción única
- **Opciones:**
  - WhatsApp
  - Email
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** una sola opción, y es el **canal único del proyecto**. Nada de multi-selección: toda la comunicación del build va por ahí, con 1 toque visible al día mínimo.

### 5.2

- **Enunciado:** Mejor franja horaria para mensajes
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### 5.3

- **Enunciado:** ¿Quién responde las dudas del negocio durante el build?
- **Tipo de campo:** texto corto
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

---

## Bloque 6 · Campo abierto

### 6.1

- **Enunciado:** ¿Algo que deba saber antes de empezar? (fechas señaladas, vacaciones, campañas en marcha, peculiaridades del negocio…)
- **Tipo de campo:** texto largo
- **Obligatoria:** no
- **Texto de ayuda:** —
- **Lógica:** ninguna.

---

## Pantalla final

El .md **no trae copy de pantalla final**, así que no se inventa aquí: escribe la tuya o deja el mensaje por defecto de Tally/Typeform. Lo que sí es literal y obligatorio es la nota de confidencialidad al pie del formulario (ver "Ajustes generales").

**Qué pasa después (del propio recurso):**

- La respuesta te llega a ti y tiene que estar **antes de la llamada de arranque**.
- Si a las 24h no lo ha rellenado, recordatorio amable (copy literal): *"[Nombre], para llegar a la llamada del [día] con todo preparado necesito el formulario hoy — son 5-10 minutos. ¿Te viene bien ahora?"*
- En la llamada, el paso 4 del guion repasa lo que llegó por el formulario y pide lo que falte compartiendo pantalla.

---

## Conexiones

- **Dónde se enlaza dentro del programa:** es el recurso de la lección **L2 "La llamada de arranque"** de F5 Entrega (`modulos/F5-entrega/guiones/L2-llamada-de-arranque.md`). El alumno lo encuentra en los recursos de esa lección junto al guion de la llamada y al esqueleto del acuerdo.
- **A qué se conecta después (lo importante):** la URL del formulario se pega como **página de redirección del enlace de pago** (Payment Link de Stripe). Así el cliente aterriza en el formulario justo después de pagar, sin tiempo muerto. Si no lo automatizas, se envía a mano el mismo día del cobro.
- **Mensaje de envío a mano** (copy literal del recurso):

  > "¡[Nombre], en marcha! 🚀 Primer paso: rellena este formulario (5-10 min). Con esto tengo todo lo necesario para empezar a construir sin hacerte perder tiempo. Idealmente antes de nuestra llamada del [día]. Cualquier duda, me escribes por aquí."

- **Prueba obligatoria antes de usarlo con nadie:** pago de prueba → redirección → formulario → te llega la respuesta. Si algo falla, que falle contigo, no con tu primer cliente.
- **Encadenado del proceso:** cobro (F4) → formulario el mismo día → respuesta recibida → llamada de arranque a 24-48h (guion de 7 pasos, criterios de aceptación, acuerdo firmado) → build de producción (L3). Sin acuerdo firmado no arranca el build.
- **Para grabar la lección:** el guion pide `[PANTALLA: el formulario de arranque campo a campo, montado en un formulario real]`. Móntalo antes de grabar L2 y usa esta guía para recorrerlo en pantalla.
- **KPI de la lección:** formulario enviado el mismo día del cobro + llamada de arranque hecha con criterios de aceptación pactados y acuerdo firmado.

---

*Notas internas (no van en el formulario ni las ve el cliente):* el .md de origen incluye tres piezas para ti que se han dejado fuera de la guía de campos y viven en el recurso original `modulos/F5-entrega/recursos/formulario-arranque-cliente.md` — el apartado **"Cómo montarlo (una vez, 30-45 min)"**, la **"Checklist de uso"** (formulario montado y conectado / enviado el mismo día / respuesta recibida antes de la llamada / recordatorio a las 24h), y la coletilla de la casa: esto es orientación práctica, no asesoría legal — valida tu proceso con un profesional.
