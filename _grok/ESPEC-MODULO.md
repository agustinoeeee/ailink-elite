# Contrato de módulo — AILINK Élite

Todo módulo (F0…F6) se mide contra esto. Si un documento no encaja, se corrige el documento, no el contrato — salvo que Agustín cambie la Biblia.

## Estructura de carpeta

```
modulos/FX-nombre/
  README.md              índice: lecciones, orden, semana, entregable del alumno
  lecciones/
    01-slug/
      guion.md           esqueleto de vídeo (no teleprompter palabra por palabra)
    02-slug/
      guion.md
  recursos/              worksheets, SOPs, plantillas del ALUMNO
  kpis.md                solo métricas de ESTE módulo (apuntan a la tabla maestra de la Biblia)
  notas-fuente.md        chunk(s) de origen + qué se copió / adaptó / eliminó y por qué
```

Material de Agustín (posicionamiento, afiliación, cómo vender el programa) **no** va en `recursos/`. Va en `notas-fuente.md` o en un `para-agustin.md` claramente marcado.

## Qué es un guion.md

- Duración objetivo, gancho, orden de beats, demos a grabar, CTA de la lección (qué hace el alumno al terminar).
- Frases-ancla de frameworks (las que el alumno debe poder repetir).
- Lo que NO es: traducción del ASR, ni ensayo de “Owen en español”.

## Adaptación (la Biblia manda)

| Tipo de segmento | Qué sale |
|---|---|
| `framework` | Casi verbatim. Se cita origen de terceros (Hormozi, etc.). |
| `mentalidad` | Guion. Recurso ligero o ninguno. |
| `script-plantilla` | Plantilla ya adaptada (€, España, entregables). |
| `matematica-kpi` | Re-derivada al modelo piloto/proyecto/retainer. Prohibido copiar $147/cita. |
| `tutorial-herramienta` | SOP del stack de AILINK. Se reescribe, no se traduce GHL/Meta-USA. |
| `demo-en-vivo` | Guion de demo equivalente con un caso de Agustín. |
| `venta-del-programa` | Solo `para-agustin.md`. Cero en materiales del alumno. |

## Prohibido en cualquier entregable de alumno

- Dólares, Angi, HomeAdvisor, GoHighLevel como stack prescrito, cold SMS masivo, contractors USA, “este curso es gratis en YouTube”, “pagué 7.000 $”.
- Números de la Biblia que Agustín no haya validado, presentados como ley (rangos de precio, +10K€/mes vs +10K€ en 90 días).
- Inventar KPIs “porque quedan bien”. Si no está en la transcripción ni en la Biblia, se marca `PENDIENTE-AGUSTIN`.
- Residuo de ASR: “Alexi”, “Onland”, “paper shown”, “door knockocking”.

## El alumno tiene que HACER algo

Cada lección termina con una acción de esta semana. Ver un vídeo no cuenta como entregable. F0 no es excepción: onboarding = setup + reglas de juego + primera acción hacia F1.
