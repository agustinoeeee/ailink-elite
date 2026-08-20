# L3 | Cómo dirigir a Claude Code

| Fase | Duración objetivo | Recurso vinculado |
|---|---|---|
| F2 Construye | 10-14 min | recursos/plantilla-brief-solucion.md |

**Objetivo:** al terminar, el alumno sabe escribir un brief que produce lo que quiere, iterar en pasos pequeños y no romper lo que ya funciona.

## Gancho (0:00-0:20)

"En L2 publicaste tu primera web. Hoy aprendes la habilidad de la que vive todo este negocio: dirigir. Porque Claude Code construye exactamente lo que le pides — y ahí está la trampa: casi nadie sabe pedir. Al final de esta lección, tú sí."

[PANTALLA: pantalla partida con dos resultados — la misma idea pedida mal ("hazme una web para mi clínica") y pedida con brief completo; la diferencia salta a la vista]

## Sección 1 — La regla de oro: el brief manda

- "La calidad de lo que Claude Code construye es un espejo exacto de la calidad de tu brief." Glosario: un **prompt** es cualquier instrucción que le escribes a la IA; un **brief** es el documento donde describes de forma ordenada lo que quieres construir. Un prompt suelto produce cosas sueltas; un brief produce soluciones.
- La regla, subrayada tres veces: describe **QUÉ debe pasar y PARA QUIÉN. Nunca CÓMO programarlo.** "Al fontanero no le dices qué llave inglesa usar. Le dices que la ducha pierde agua y compruebas que deja de perder."
- Ejemplo mal → bien: "hazme un chatbot con IA" → "cuando la recepcionista marca una cita como cancelada, la web ofrece al paciente dos huecos libres y, si acepta uno, la cita vuelve al panel como recuperada".
- Frase ancla del módulo: **"si sabes explicárselo a un becario brillante, sabes construir software."** El becario brillante teclea rapidísimo y no se queja — pero no conoce tu negocio ni lee tu mente. Todo lo que no le cuentes, se lo inventará.

## Sección 2 — La plantilla de brief del programa

[PANTALLA: recursos/plantilla-brief-solucion.md abierta; se recorren las 6 secciones con el cursor]

- Seis secciones, siempre las mismas:
  1. **Contexto**: quién es tu negocio cliente, quién es su cliente final y quién usará la pantalla.
  2. **Qué debe hacer**: lista numerada de comportamientos observables.
  3. **Qué NO entra**: el alcance del piloto que ya acotaste en F1 — tan importante como lo que entra.
  4. **Datos de ejemplo**: una tabla con nombres y casos verosímiles de tu nicho.
  5. **Aspecto**: 2-3 referencias visuales, sin tratados de diseño.
  6. **Cómo sabré que funciona**: los checks que convertirán tu demo en enseñable.
- La sección 2 es el corazón. "Comportamiento observable" significa algo que se puede VER pasar en pantalla y comprobar con un sí o un no. "Que sea intuitivo" no es observable; "al abrir la web, la recepcionista ve las citas de hoy sin tocar nada" sí lo es.
- En la plantilla tienes el ejemplo COMPLETO relleno con la demo dental que construiré en L5. Léelo entero antes de escribir el tuyo: es tu patrón de calidad.

## Sección 3 — Iterar en pasos pequeños

- Las dos reglas gemelas: **una petición = un cambio**, y **probar antes de pedir el siguiente**. Es el método científico de F0-L6 que ya conectamos en L1, con otra bata.
- Por qué funciona: si pides cinco cambios a la vez y algo se rompe, no sabes cuál de los cinco fue. Si pides uno, lo sabes siempre. Estás aislando variables, como un profesional.
- Así también proteges lo que ya funciona: tras cada cambio, comprueba que lo anterior sigue vivo. Y cuando algo te guste, díselo explícitamente: "esto está bien, no lo toques; ahora quiero…".

## Sección 4 — CLAUDE.md: las reglas fijas de tu proyecto

- Dentro de tu proyecto (la carpeta donde vive tu código — tu repositorio de L2) hay un archivo especial: **CLAUDE.md**. Es un texto que Claude Code lee SIEMPRE antes de ponerse a trabajar.
- Qué se escribe ahí: qué es el proyecto y para quién ("demo de recuperación de citas para clínicas dentales"), reglas fijas ("todo en español de España", "diseño limpio, azul y blanco") y qué no debe tocar ("los datos de ejemplo no se cambian sin pedirlo").
- La metáfora: "es el manual de bienvenida del becario. Se lo das el primer día y no se lo repites cada mañana."
- Cómo se crea: pídeselo en lenguaje natural, por ejemplo: "crea el CLAUDE.md de este proyecto con estas reglas: …" — y revisa que diga lo que tú querías decir.

[PANTALLA: un CLAUDE.md real de la demo dental en pantalla, 6-8 líneas de reglas legibles en voz alta]

## Sección 5 — Los 5 errores del no-técnico

[PANTALLA: los 5 errores en lista, se tachan uno a uno al explicarlos]

1. **Pedirlo todo de golpe.** El brief inicial va entero, sí — pero desde la primera versión, cada mensaje pide UNA cosa. "Cámbiame el color, añade un buscador, quita esa columna y de paso…" es la receta del caos.
2. **No probar entre cambios.** Acumulas fallos sin saber de dónde vino cada uno. Probar no es opcional: es la mitad de tu trabajo como director.
3. **Aceptar sin revisar.** Claude Code te dirá "hecho". Tu trabajo empieza ahí: pruébalo como lo usaría tu cliente. Lo que no has probado, no existe.
4. **Pelearse con el error en vez de pegárselo a Claude.** Un mensaje de error no es un examen que suspendes: es información. Cópialo entero, pégaselo y pide que lo arregle. Esa ES la habilidad — ya la usaste en L2.
5. **Cambiar de idea a mitad sin actualizar el brief.** Si cambia el destino, cambia el mapa: actualiza el brief (y el CLAUDE.md si toca) y díselo. Claude Code no lee tu mente; lee tu brief.

## Cierre + CTA

- Recap en 2 frases: "Diriges describiendo QUÉ y PARA QUIÉN, nunca CÓMO; el brief de 6 secciones es tu herramienta, CLAUDE.md tus reglas fijas, y se avanza de un cambio en un cambio, probando siempre. Los 5 errores ya los conoces antes de cometerlos — esa es tu ventaja sobre el 90% de la gente que abre esta herramienta."
- **Acción del alumno AHORA:** abre `recursos/plantilla-brief-solucion.md`, lee el ejemplo dental completo y rellena tu brief V1 con TU solución — la que promete tu oferta V1 de F1. En L4 lo contrastarás con la ficha técnica de tu solución, y en L5 se lo darás a Claude Code.
- **KPI de esta lección:** brief V1 de tu solución escrito con las 6 secciones completas — ninguna en blanco, y la lista de comportamientos observables numerada.
- Puente: "Ya sabes dirigir. En la próxima lección abrimos el catálogo por dentro: qué es técnicamente cada solución, cuál luce más en una demo web y la confirmación final de la tuya."
