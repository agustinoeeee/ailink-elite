# KPIs y benchmarks de captación

> Recurso de L6-L7 (F3 Lanza). La tabla de benchmarks del programa, las reglas kill/keep/scale, las reglas de cambios, el prompt de análisis de cuellos de botella con Claude y la checklist pre-lanzamiento de L6. Tenlo a mano: se consulta UNA vez al día, con el tracker de captación (recurso de L1) delante — no diez veces.

## Cómo usar este recurso

- Los benchmarks del programa marcan el **suelo**: son la referencia para diagnosticar, no una promesa de resultados. Tus datos mandan.
- Ninguna decisión sin **muestra mínima** (ver reglas de validez). La única excepción es la muerte anticipada.
- Toda cifra que no esté en esta tabla y veas en ejemplos del módulo es **ilustrativa**.

## Tabla de benchmarks del programa (ads B2B)

| Métrica | Benchmark del programa | Si está fuera, ¿qué señala? |
|---|---|---|
| Presupuesto por adset | 30-50€/día recomendado · 20€/día mínimo absoluto | Con menos, la fase de aprendizaje se alarga y la campaña no demuestra nada |
| Presupuesto de testeo por creativo | 10-20€/día por creativo | Con 30-50€/día caben 2-4 creativos a la vez; más creativos = todos muertos de hambre |
| CPM (coste por mil impresiones) | Sano: 40-100€ | Por encima: creativo débil o página fría — Meta no quiere empujar tu anuncio |
| CTR link (clics únicos al enlace) | ≥1,5% | Por debajo: hook o mensaje — te ven pero no hacen clic |
| Conversión de landing (visitante → lead) | 5-10% | Por debajo: congruencia anuncio↔titular o fricción del formulario |
| Show rate | 60-70% (B2B templado) | Por debajo: recordatorios y pre-llamada — se trabaja en F4 |
| Coste por reunión agendada B2B | 50-150€ (rango orientativo) | Por encima de forma sostenida: análisis de cuellos de botella |
| Speed to lead | <5 minutos | El primero en responder se lleva la mayoría de las ventas |
| Campaña de engagement (L4) | 5€/día por adset | Calentamiento de página: seguidores y señales para bajar CPMs |

## Reglas de validez (antes de decidir NADA)

- **Muestra mínima: 50 eventos o 5-7 días, lo que llegue antes.** Hasta entonces, los números son ruido.
- Los leads llegan en olas: un día flojo no es una señal, es un día flojo.
- Única excepción: la **muerte anticipada** (tabla siguiente).

## Kill / Keep / Scale

| Situación (con muestra mínima) | Decisión |
|---|---|
| Coste por resultado ≥2x tu objetivo | **MATAR.** Apaga el creativo; antes de tirarlo, apunta en qué métrica falló para no repetirlo |
| Ha gastado 3x tu coste objetivo sin UNA sola conversión | **MATAR YA** (muerte anticipada: no espera la muestra mínima — un anuncio así no es mala suerte, está roto) |
| Coste por resultado en o por debajo del objetivo | **MANTENER.** No lo toques; déjalo trabajar |
| Entre 1x y 2x del objetivo | **ZONA INTERMEDIA:** ni matar ni escalar — más datos o diagnóstico con la jerarquía de L7 |
| En objetivo de forma sostenida y las reuniones se REALIZAN | **ESCALAR: +20-30% cada 2-3 días.** Subirlo de golpe rompe el aprendizaje |

## Reglas de cambios

1. **NUNCA edites un anuncio o adset activo.** Ni el copy, ni el enlace, ni "solo una palabra": editar reinicia el aprendizaje y funde lo pagado. Para cambiar algo: **duplica** y cambia en la copia.
2. **Una variable por cambio.** Si cambias hook, audiencia y presupuesto a la vez y mejora, no sabes por qué: no estás testeando, estás adivinando.
3. **Escalado: +20-30% cada 2-3 días**, solo si es rentable de forma sostenida.
4. **Revisión: una vez al día**, apuntando el día completo de ayer en el tracker. Lo roto del funnel (enlace, calendario) se arregla al momento — eso no es editar un anuncio.

## Jerarquía de diagnóstico (chuleta)

| Síntoma | Sospechoso | Dónde se arregla |
|---|---|---|
| CPM > 100€ | Creativo débil / página fría | L5 (creativo) · L4 (calentamiento) |
| CTR link < 1,5% | Hook o mensaje | L5 — el hook es el 80% del creativo |
| Conversión de landing < 5% | Congruencia o fricción | L2 (funnel) |
| Show rate < 60% | Proceso pre-reunión | F4 (recordatorios, pre-llamada) |

Se diagnostica en este orden, de arriba abajo: arreglar la landing cuando el problema es el hook es pintar las puertas de una casa sin cimientos.

## Prompt de análisis de cuellos de botella con Claude

Copia, rellena los corchetes con datos REALES de tu tracker y pégalo en Claude:

```
Actúa como analista de campañas de Meta ads B2B.

Contexto: capto reuniones con dueños de negocio de [NICHO] en [ZONA]
mediante un funnel con VSL, demo y calendario. Mi coste objetivo por
reunión agendada es [X]€.

Benchmarks de referencia de mi programa:
- CPM sano: 40-100€ · CTR link: ≥1,5% · Conversión de landing: 5-10%
- Show rate: 60-70% · Coste por reunión agendada: 50-150€ (orientativo)
- Reglas: muestra mínima 50 eventos o 5-7 días · matar a ≥2x del objetivo ·
  muerte anticipada a 3x gastado sin conversión · nunca editar un activo
  (duplicar y cambiar UNA variable) · escalar +20-30% cada 2-3 días

Mis métricas de los últimos [7/14] días (del tracker):
- Gasto: [—]€ · CPM: [—]€ · CTR link: [—]%
- Conversión de landing: [—]% · Leads: [—]
- Reuniones agendadas: [—] (coste: [—]€) · Reuniones realizadas: [—]

Tarea:
1. Compara mis métricas con los benchmarks y dime cuál es el cuello de
   botella principal (UNA sola métrica).
2. Dime qué regla se aplica a cada creativo: matar, mantener, zona
   intermedia o escalar — y si tengo muestra mínima para decidir.
3. Propón la ÚNICA variable que cambiarías primero y por qué, recordándome
   que el cambio se hace duplicando, nunca editando el activo.
```

## Tabla equivalente para outreach (email frío / llamada)

Mismas reglas de juego, otras columnas. Aquí el programa no fija tasas: **tus porcentajes salen de tu tracker** (y en llamada, de tu calculadora inversa de L1). Lo que sí fija es el volumen y la validez.

| Concepto | Ads | Email frío B2B | Llamada B2B |
|---|---|---|---|
| Volumen | Gasto (30-50€/día) | Envíos (200-400/semana sostenibles con personalización real) | Llamadas (bloque diario) |
| Interés | CTR link | Tasa de respuesta (tuya, del tracker) | Conversaciones reales (tuyas, del tracker) |
| Conversión | Conversión de landing | Respuestas → reuniones agendadas | Conversaciones → reuniones agendadas |
| Resultado | Coste por reunión agendada (50-150€ orientativo) | Reuniones por cada 100 envíos (tu dato) | Reuniones por cada 100 llamadas (tu dato) |
| Validez mínima | 50 eventos o 5-7 días | **300 toques** antes de juzgar | **300 toques** antes de juzgar (cada llamada ES un toque) |
| Regla de cambios | Duplicar, una variable | Una variable por test (asunto O primera línea) | Una variable por test (apertura O pregunta) |

- El speed to lead también rige aquí: al que responde a un email se le llama **ese mismo día**; <5 minutos si el aviso te pilla disponible.
- Lo que funciona se escala con MÁS volumen antes de montar un canal nuevo (Más/Mejor/Nuevo, de F0).
- No confundas validez de canal con validez de cierre: las **30 llamadas DE VENTA realizadas** validan tu tasa de cierre — eso es materia de F4; aquí solo queda apuntado como puente.
- Las reglas de captación conforme a la normativa viven en `recursos/rgpd-captacion.md` — pásalo antes de tu primer envío.

## Checklist pre-lanzamiento (de L6)

Márcala entera antes de programar la campaña — y publícala marcada en la comunidad.

- [ ] **Congruencia anuncio↔titular:** lo que promete el ad es lo primero que se lee en la landing (L2)
- [ ] **Links probados:** del anuncio a la landing, de la landing a la demo, del formulario al calendario
- [ ] **Pixel probado con consentimiento:** aceptas el aviso de cookies en el test y los eventos de lead y reserva disparan
- [ ] **Calendario funcionando:** reserva de prueba completada
- [ ] **Avisos de speed to lead activos:** entra un lead, tu móvil suena, respondes en <5 minutos
- [ ] **Revisión desde el móvil:** funnel completo recorrido en tu teléfono, creativos y textos legibles, cero faltas
