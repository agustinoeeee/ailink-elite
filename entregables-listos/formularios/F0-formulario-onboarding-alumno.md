# Guía de montaje — Formulario de onboarding del alumno (pre-kick-off)

> Fuente: `modulos/F0-bienvenido/recursos/formulario-onboarding-alumno.md`
> Montaje estimado: 15 minutos en Tally o Typeform.

## Para qué sirve

Es el formulario que el alumno completa **antes** de su kick-off call. Con estas respuestas se traza su plan en la llamada — en especial su **ruta de captación en F3**, que la define el presupuesto. Sin él, la kick-off se convierte en una recogida de datos en vez de una sesión de decisión.

**Quién lo rellena:** el alumno recién entrado al programa, él mismo.

**Cuándo se envía:** en F0 Bienvenido, dentro de la lección L2 "Tu kick-off call". El alumno lo ve enlazado en la propia lección y lo completa del tirón justo después de reservar su kick-off — siempre **antes** de la llamada.

---

## Ajustes generales

- **Título del formulario:** Formulario de onboarding del alumno
- **Una pregunta por pantalla:** sí. Lo pide el recurso y encaja con el objetivo de <10 minutos de respuesta.
- **Número de preguntas:** 9 (8 obligatorias + 1 opcional).
- **Mensaje de bienvenida** (pantalla 1, copy literal):

  > **Tu plan empieza aquí.**
  > 9 preguntas, menos de 10 minutos. Con esto preparamos tu kick-off para dedicarla a decidir tu plan, no a recoger datos.
  > Responde con números reales, no aspiracionales. Nada de esto se puntúa: se usa para ayudarte.

- **Bloques:** el recurso agrupa las preguntas en 4 bloques (Tu situación · Tus recursos · Tu punto de partida comercial · Tu porqué). Si tu herramienta permite títulos de sección, úsalos; si no, no pasa nada: el orden de las preguntas ya es el correcto.

---

## Bloque 1 — Tu situación

### P1

- **Enunciado:** ¿Cuál es tu situación actual?
- **Tipo de campo:** opción única
- **Opciones:**
  - Trabajo por cuenta ajena (jornada completa)
  - Trabajo por cuenta ajena (jornada parcial)
  - Estudio
  - Tengo un negocio en marcha
  - Sin ocupación actualmente / disponibilidad total
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna dentro del formulario. Define el ritmo real que se calibra en la kick-off.

### P2

- **Enunciado:** Ingresos actuales y objetivo a 90 días
- **Tipo de campo:** número — **dos campos** dentro de la misma pregunta:
  1. Ingresos mensuales actuales (aprox., €)
  2. Objetivo de facturación ACUMULADA de tu agencia al final de los 90 días (€ totales de los 90 días, no mensuales)
- **Obligatoria:** sí (los dos campos)
- **Texto de ayuda:** —
- **Lógica:** ninguna.

> Montaje: si tu herramienta no permite dos campos en una pantalla, ponlos como dos preguntas numéricas seguidas con esos mismos enunciados. No toques el paréntesis del segundo: es el que evita que confundan acumulado con mensual.

### P3

- **Enunciado:** ¿Cuántas horas a la semana puedes dedicar DE VERDAD al programa?
- **Tipo de campo:** opción única
- **Opciones:**
  - Menos de 5 h/semana
  - 5-10 h/semana
  - 10-20 h/semana
  - Más de 20 h/semana
- **Obligatoria:** sí
- **Texto de ayuda:** "Las de verdad, quitando trabajo, familia y vida. El roadmap se calibra con este número: si lo inflas, te calibras mal a ti mismo."
- **Lógica:** ninguna dentro del formulario. El roadmap se calibra con este número en la kick-off.

---

## Bloque 2 — Tus recursos

### P4 ⭐ pregunta clave

- **Enunciado:** ¿Qué presupuesto tienes para captación de clientes durante el programa?
- **Tipo de campo:** opción única
- **Opciones:**
  - Menos de 500€
  - Entre 500€ y 2.000€
  - Más de 2.000€
- **Obligatoria:** sí
- **Texto de ayuda:** "El que puedas gastar sin sufrir. No lo infles: hay una ruta del programa para cada presupuesto, incluida la de menos de 500€."
- **Lógica:** no salta ni ramifica dentro del formulario, pero es la respuesta que **asigna la ruta de captación en F3 Lanza** (tres rutas: menos de 500€ / entre 500 y 2.000€ / más de 2.000€). Si tu herramienta permite etiquetar respuestas, etiquétala para poder filtrar alumnos por ruta.

### P5

- **Enunciado:** ¿Cuál es tu experiencia técnica?
- **Tipo de campo:** opción única
- **Opciones:**
  - Ninguna (0 — nunca he tocado nada técnico)
  - Uso herramientas de IA (ChatGPT, Claude…) a nivel usuario
  - He programado o he construido algo técnico alguna vez
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

### P6

- **Enunciado:** ¿Cuál es tu experiencia en ventas?
- **Tipo de campo:** opción única
- **Opciones:**
  - Ninguna (0 — nunca he vendido nada)
  - Alguna (he vendido en algún trabajo o proyecto)
  - Mucha (la venta ha sido parte central de mi trabajo)
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:** ninguna.

---

## Bloque 3 — Tu punto de partida comercial

### P7

- **Enunciado:** ¿Tienes ya un nicho en mente o clientes potenciales a los que podrías vender?
- **Tipo de campo:** opción única + texto corto condicional
- **Opciones:**
  - No, empiezo de cero (perfecto: el nicho se elige en F1)
  - Tengo un nicho en mente
  - Conozco negocios concretos que podrían comprarme
- **Obligatoria:** sí
- **Texto de ayuda:** —
- **Lógica:**
  - Si elige **"Tengo un nicho en mente"** → aparece un campo de texto corto: **¿Cuál?**
  - Si elige **"Conozco negocios concretos que podrían comprarme"** → aparece un campo de texto corto: **¿Cuáles/de qué sector?**
  - Si elige **"No, empiezo de cero"** → no aparece nada y pasa a P8.

---

## Bloque 4 — Tu porqué

### P8

- **Enunciado:** ¿Qué tendría que pasar para que consideres estos 90 días un éxito?
- **Tipo de campo:** texto largo
- **Obligatoria:** sí
- **Texto de ayuda:** "Sé concreto: una cifra, una situación, algo que puedas señalar el día 90 y decir «esto era»."
- **Lógica:** ninguna.

### P9

- **Enunciado:** ¿Algo que debamos saber antes de la kick-off?
- **Tipo de campo:** texto largo
- **Obligatoria:** no
- **Texto de ayuda:** "Miedos, limitaciones de tiempo o dinero, malas experiencias con otros programas, salud, lo que sea. Esta es la pregunta más útil del formulario. No se puntúa: se usa para ayudarte."
- **Lógica:** ninguna.

---

## Pantalla final

Copy literal:

> **Hecho.** Revisaremos tus respuestas antes de la llamada.
> Si aún no has reservado tu kick-off: `[LINK CALENDARIO]`.
> Nos vemos en la llamada — en firme.

**Qué pasa después:**

- Sustituye `[LINK CALENDARIO]` por la URL real de tu calendario de reservas y déjalo como enlace clicable en la pantalla final. Es la red de seguridad para quien rellena el formulario sin haber agendado todavía.
- No hay redirección automática: la pantalla final es el último paso. Si prefieres redirigir, que sea al calendario de reservas — nunca a otra lección.
- La respuesta llega a tu bandeja de respuestas y se lee **antes** de la kick-off.

---

## Conexiones

- **Dónde se pega el enlace:** en `modulos/F0-bienvenido/guiones/L2-tu-kickoff-call.md`, Sección 3 "Qué preparar" — sustituye el marcador `[LINK FORMULARIO]`. Ese mismo enlace va también enlazado en la descripción / recursos de la lección L2 dentro de la plataforma, porque el guion dice "lo tienes enlazado en esta lección".
- **Segundo punto de contacto:** en el Cierre + CTA de esa misma lección, la acción del alumno es (1) abrir `[LINK CALENDARIO]` y reservar, (2) completar el formulario antes de cerrar la pestaña. El enlace del formulario tiene que estar visible ahí también.
- **Antes:** el alumno reserva su kick-off en el calendario (KPI: agendada en <72h desde su fecha de acceso).
- **Después:** la pantalla final devuelve al `[LINK CALENDARIO]` a quien no haya agendado aún. Las respuestas se leen antes de la llamada y alimentan la kick-off: situación, horas y presupuesto → ruta de captación de F3.
- **KPI asociado a la lección:** kick-off agendada en <72h + formulario completado antes de la llamada. Si mides el segundo, hazlo cruzando respuestas del formulario con citas agendadas.

---

*Nota interna (no va en el formulario):* el .md de origen no incluye guía de lectura de respuestas ni banderas — así que aquí no se ha omitido nada de eso. La interpretación de las respuestas vive en el guion `modulos/F0-bienvenido/guiones/L2-tu-kickoff-call.md` (Sección 1: situación + horas + presupuesto → ruta) y se aplica en la propia kick-off call.
