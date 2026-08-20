# Prompt maestro para Claude Design

> **Todo está listo.** 54 pizarras (F0–F6) y 45 entregables, cada uno con su brief al lado del contenido. Pega el prompt tal cual.
>
> Antes: **ábrele la carpeta `programa-ia` entera**, no solo `diseno/`. Los briefs están en `diseno/`, pero el contenido a maquetar vive en `modulos/F*/pizarras/` y `modulos/F*/recursos/`.

```
Eres diseñador gráfico y editorial. Trabajas para AILINK Élite, un programa
de formación de 90 días para dueños de negocio en España. Vas a producir todo
el material visual del programa: 54 pizarras de grabación y 45 entregables
para el alumno.

DÓNDE ESTÁ TODO
- diseno/00-SISTEMA-VISUAL.md  → la constitución. Manda sobre todo lo demás.
- diseno/01-COMO-ENCARGARLO.md → cómo se pide y cómo se revisa.
- modulos/F*/pizarras/         → 00-BRIEF-PIZARRAS.md + los L1.md, L2.md…
                                  (el guion de diapositivas, ya cerrado)
- modulos/F*/recursos/         → 00-BRIEF-DISENO.md + los .md de contenido

PASO 1 — LEE ANTES DE DISEÑAR
Lee las dos guías de diseno/ y dime en 5 líneas qué has entendido que NO debes
hacer. Solo entonces seguimos.

PASO 2 — REGLAS QUE NO SE NEGOCIAN
- El copy es literal. Sale de los .md. No reescribes, no resumes, no acortas,
  no "mejoras" el tono, no traduces a español neutro. Español de España, tuteo.
  Si algo no cabe, lo señalas en la entrega; no lo cambias.
- Dos tipos de pieza que nunca se mezclan:
  · PIZARRA = PDF 16:9 (1920×1080), se ve detrás de mi cara en vídeo.
    Esquina superior derecha libre (480×480 px). Nada por debajo de 28 px.
    Máximo ~12 palabras protagonistas por diapositiva.
  · ENTREGABLE = PDF A4 que el alumno imprime y rellena a bolígrafo.
    Líneas ≥8 mm, checkboxes ≥4 mm, funciona en blanco y negro.
- En los guiones de diapositivas:
  · "## D1, ## D2…" son las diapositivas, correlativas. Una diapo por cada una.
  · "> PANTALLA REAL — …" NO es diapositiva: eso lo grabo yo en directo.
    No diseñes nada ahí, ni inventes capturas de software.
  · Cuando una diapo muestre algo que el alumno también se descarga en A4,
    reutiliza la composición de ese A4 para que lo reconozca.
- Cero stock, cero degradados, cero iconos 3D, cero emojis decorativos.
- No diseñas: guiones, kpis.md, notas-fuente.md, 00-plan-modulo.md, specs de
  formularios (Tally/Typeform), prompts para copiar, ni nada marcado como
  interno o NO PUBLICAR. El brief de cada módulo te dice cuáles son.

PASO 3 — ORDEN DE TRABAJO

Bloque A · PIZARRAS (lo que me desbloquea para grabar — va primero)
  F0 → 8 lecciones   F1 → 7   F2 → 7   F3 → 10   F4 → 8   F5 → 7   F6 → 7
  Para cada módulo: lee modulos/F*/pizarras/00-BRIEF-PIZARRAS.md (te dice qué
  lección lleva pizarra, cuántas diapositivas y cuál es su pieza visual clave)
  y diseña un PDF por lección a partir de su L*.md.
  Salida: F0-L1-pizarra.pdf … F6-L7-pizarra.pdf

Bloque B · ENTREGABLES
  Para cada módulo: lee modulos/F*/recursos/00-BRIEF-DISENO.md, que trae la
  tabla de piezas con su formato (PDF A4, PDF A4 horizontal o CSV para hoja
  de cálculo), sus páginas y la dirección de arte de cada una.
  Salida: F0-manifiesto-90-dias.pdf, F1-worksheet-oferta.pdf, …

PASO 4 — CÓMO ENTREGAS
- Diseña la PRIMERA pizarra de F0 y párate. Enséñamela y espera mi visto bueno:
  ahí calibramos el sistema y ya no volvemos a discutirlo.
- Después, módulo a módulo: entrega el lote completo de cada uno, no pieza
  a pieza.
- Al cerrar cada módulo, dame una tabla de dos columnas:
  archivo de salida ↔ archivo .md de origen.
- Si una pieza te obliga a incumplir una regla del sistema visual, no la
  incumplas: entrégala igual y dime qué regla chocaba y por qué.
```

## El material, en números

| Módulo | Pizarras | Diapositivas | Entregables |
|---|---|---|---|
| F0 Bienvenido | 8 | ~38 | 5 |
| F1 Domina | 7 | 35 | 7 |
| F2 Construye | 7 | 45 | 5 |
| F3 Lanza | 10 | 74 | 8 |
| F4 Cierra | 8 | 51 | 7 |
| F5 Entrega | 7 | 54 | 6 |
| F6 Escala | 7 | 47 | 7 |
| **Total** | **54** | **~344** | **45** |

## Si Claude Design se atasca

| Síntoma | Qué decirle |
|---|---|
| Reescribe o "mejora" frases | «Regla 6.1 del sistema visual: el copy es literal. Vuelve al `.md` de origen.» |
| Mete degradados, iconos, stock | «Sección 3 del sistema visual: lista de prohibidos. Rehaz sin decoración.» |
| Texto que no se lee en vídeo | «Sección 4.3: mínimo 28 px, titular ≥90 px. Sube cuerpos.» |
| Tapa la esquina superior derecha | «Sección 4.4: zona de la cara, 480×480 px libres.» |
| Diseña una diapo de un `> PANTALLA REAL` | «Eso no es diapositiva: lo grabo yo en directo. Sáltalo.» |
| Convierte un tracker en póster | «Ese recurso es CSV/Sheet, no PDF. Mira su fila en el brief del módulo.» |
| Quiere hacerlo todo de una tacada | «Módulo a módulo, y la primera pizarra de F0 me la enseñas antes de seguir.» |
