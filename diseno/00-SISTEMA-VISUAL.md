# Sistema visual AILINK Élite — léeme antes de diseñar nada

> Este documento se adjunta SIEMPRE, en todos los encargos. Es la constitución: marca, formatos, reglas y criterios de aceptación. Los briefs por módulo (`F*-pizarras.md`, `F*-entregables.md`) dicen QUÉ hay que hacer; este dice CÓMO tiene que verse y qué está prohibido.

## 1. Qué es esto

**AILINK Élite** es un programa de 90 días que enseña a montar una agencia que vende soluciones de IA a negocios. Español de España, tuteo. El alumno paga cifras altas y es dueño de un negocio, no un estudiante.

**Tono visual = tono del texto: directo, sobrio, caro por quietud.** Parece un contrato bien impreso, no un infoproducto de YouTube. Si una pieza podría llevar un cohete 🚀 o un degradado morado, está mal.

## 2. Los tres tipos de pieza (no se mezclan nunca)

| Tipo | Qué es | Formato | Dónde vive |
|---|---|---|---|
| **PIZARRA** | Lo que se ve **debajo/al lado de la cara de Agustín mientras graba**. Él habla; la slide ancla la idea. | PDF **16:9**, 1920×1080 | Se abre a pantalla completa en la grabación |
| **ENTREGABLE** | Lo que el **alumno descarga**, imprime y rellena. | PDF **A4** (vertical salvo indicación) | Adjunto de la lección en Skool |
| **TABLA** | Lo que el alumno **copia a una hoja de cálculo** (trackers, plantillas). | CSV o estructura de columnas (+ PDF de la cabecera de reglas si el brief lo pide) | Adjunto + enlace a copiar |

Un encargo nunca convierte una pizarra en entregable ni al revés. Si el brief del módulo dice "pizarra", es 16:9; si dice "entregable", es A4.

## 3. Marca

```
Fondo papel      #F5F5F2      (fondo de todo)
Tarjeta/papel    #FFFFFF      (bloques, cajas, filas)
Tinta            #101010      (texto)
Acento cobalto   #2743D0      (lo que importa: números, títulos clave, un solo elemento por pieza)
OK / verde       #1F7A4D      (estados correctos, "hecho")
Aviso / ámbar    #A35C0A      (advertencias, "no montar todavía")
```

- **Tipografía:** una grotesk seria (Inter, Geist o similar). Un solo tipo, dos o tres pesos. Cero script, cero serifas decorativas.
- **El acento se gana.** Cobalto solo en el elemento más importante de cada pieza. Si todo es cobalto, nada lo es.
- **Prohibido:** degradados, sombras blandas, iconos 3D, ilustraciones de gente feliz, stock, emojis decorativos, mockups de portátiles, "glassmorphism", cintas de "¡NUEVO!".
- **Permitido y bienvenido:** líneas finas, mucho blanco, tablas honestas, flechas simples, números enormes, tipografía como protagonista.
- **Pie de página:** `AILINK Élite` pequeño, en tinta al 40%. En manifiestos y certificados, también en cabecera.

## 4. Reglas de la PIZARRA (16:9)

Esto se graba: si no se lee en un recorte de vídeo comprimido, no sirve.

1. **Una idea = una diapositiva.** Pocas diapos. Si dudas entre partir o apretar, parte.
2. **Máximo ~12 palabras protagonistas por slide.** El guion lo dice Agustín en voz alta; la slide no lo recita.
3. **Tamaños mínimos** (lienzo 1920×1080): titular ≥ 90 px · texto protagonista ≥ 54 px · etiquetas de diagrama ≥ 36 px · pie/letra pequeña ≥ 28 px. Nada por debajo de 28 px, jamás.
4. **Zona segura:** margen de 120 px por lado. **Deja libre la esquina superior derecha (≈ 480×480 px)**: ahí se superpone la cara de Agustín en el montaje. No pongas ahí texto ni el elemento héroe.
5. **Un héroe por slide:** o un número gigante, o un diagrama, o una frase. Nunca los tres.
6. **Los diagramas se leen de izquierda a derecha o de arriba abajo**, con flechas simples. Máximo 5 nodos.
7. **Sin numeración de diapositivas, sin barra de progreso, sin logos grandes.** La slide es un fondo, no una presentación de consultoría.
8. **Nada de capturas de software** en las pizarras: eso Agustín lo graba en directo. Si el brief dice "pantalla real", esa diapo no existe.

## 5. Reglas del ENTREGABLE (A4)

1. **El copy se respeta literal.** No reescribes, no resumes, no "mejoras" el tono, no acortas. Si no cabe: reduce cuerpo o pasa a 2 páginas — nunca recortes contenido.
2. **Rellenable de verdad:** líneas de escritura con altura suficiente para bolígrafo (≥ 8 mm), checkboxes de ≥ 4 mm, campos de formulario en el PDF si tu herramienta lo permite.
3. **Imprimible en blanco y negro sin perder sentido**: el color refuerza, nunca es la única señal (un estado también se distingue por texto o forma).
4. **Márgenes ≥ 15 mm.** Cuerpo de texto ≥ 10 pt.
5. **Una pieza = un archivo.** Nada de PDFs monstruo de 40 páginas que junten varios recursos.

## 6. Reglas de copy (las dos que más se incumplen)

1. **No inventes frases.** El copy sale de los `.md` que te pasan. Si algo no cabe o no se entiende, lo señalas en la entrega — no lo reescribes tú.
2. **Español de España, tuteo.** Si se te cuela neutro o latinoamericano, corrígelo al original del `.md`.

## 7. Lista negra (no diseñar nunca)

- Guiones (`guiones/*.md`), `kpis.md`, `notas-fuente.md`, `00-plan-modulo.md` → son material interno de producción.
- Cualquier archivo marcado **interno** o **NO PUBLICAR**.
- Specs de formularios (Tally/Typeform) y prompts para copiar → se entregan como texto, no como PDF maquetado.
- Portadas de lección, thumbnails de YouTube, logos nuevos, landings.
- Cualquier mención a: dólares, mercados fuera de España, marcas de software que no aparezcan en el `.md`, o al origen del material.

## 8. Nombres de archivo

```
Pizarras:     F1-L3-pizarra.pdf
Entregables:  F1-worksheet-oferta.pdf
Tablas:       F3-tracker-captacion.csv   (+ F3-tracker-captacion.pdf si lleva cabecera de reglas)
```

Un archivo por pieza. Sin espacios, sin acentos, sin versiones tipo `_final_v2_BUENO`.

## 9. Entrega

Junto a los archivos, una tabla de dos columnas: **archivo de salida ↔ archivo `.md` de origen**, para saber sin dudas qué se sube a cada lección de Skool.

## 10. Checklist de aceptación (Agustín revisa con esto)

**Pizarra**
- [ ] Se lee en un móvil al 30% de tamaño (prueba real: mírala en el móvil a un palmo).
- [ ] La esquina superior derecha está libre.
- [ ] Ninguna slide pasa de ~12 palabras protagonistas.
- [ ] Ningún texto por debajo de 28 px.
- [ ] Cero capturas de software, cero elementos decorativos.
- [ ] El copy coincide con el `.md` de origen.

**Entregable**
- [ ] Impreso en A4 y en blanco y negro sigue funcionando.
- [ ] Se puede rellenar a bolígrafo sin apretar la letra.
- [ ] El texto está completo y literal.
- [ ] Nombre de archivo correcto y pie de marca puesto.
