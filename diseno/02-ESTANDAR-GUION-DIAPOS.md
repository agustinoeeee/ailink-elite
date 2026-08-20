# Estándar del guion de diapositivas (los `L*.md` de `pizarras/`)

> El paso 0 del flujo. Un archivo por lección que dice, diapo a diapo, qué se ve en pantalla mientras Agustín habla. Es el **input** del diseñador: sin él, Claude Design inventa copy.
>
> El estándar sale de los 8 guiones de F0, que son la referencia. Este documento lo formaliza para poder producir F1–F6 igual.

## Qué es y qué no es

- **Es** un extracto del guion de la lección: solo lo que necesita apoyo visual.
- **No es** el guion. Si una frase se entiende oyéndola, no va a la pizarra.
- **No inventa** contenido: cada frase de una diapo existe ya en el guion de la lección o en su recurso.

## Cómo se decide qué va en una diapo

Cinco cosas justifican una diapositiva. El resto, no:

1. **Un número o una cifra** que el alumno debe retener (promesa, benchmark, precio, plazo).
2. **Un diagrama o flujo** (el mapa de fases, el árbol de decisión, la tubería, un antes/después).
3. **Una lista corta y cerrada** que se va recorriendo (los 7 errores, los 6 componentes, los 3 niveles).
4. **Una frase-ancla** que el alumno debe recordar literal ("Ejecuta rápido. Falla rápido.").
5. **Una tabla** que se lee mientras se explica (benchmarks, síntoma→palanca).

**No justifican diapositiva:** una transición, un saludo, una anécdota, una acotación `[PANTALLA: …]` que en realidad es una captura de software real (eso se graba en directo), ni el cierre con la acción del alumno (se dice a cámara).

## Formato del archivo

```markdown
# LX — Pizarra de explicación (Título corto)

16:9 · N diapos · entregable detrás: [nombre del recurso · o "no hay"]

## D1 — [Etiqueta de la diapo]
[El copy exacto que se ve, tal cual, en las líneas que debe ocupar]

Letra pequeña: *[el matiz, si lo hay]*

## D2 — [Etiqueta]
[Si es diagrama, se describe la estructura y luego el copy de cada nodo]

Diagrama horizontal, 4 cajas:
CAJA 1 → CAJA 2 → CAJA 3 → CAJA 4

Pie: *[una línea]*
```

## Las 9 reglas de escritura

1. **Máximo ~12 palabras protagonistas por diapo.** Lo demás va en "letra pequeña" o no va.
2. **Entre 4 y 8 diapos por lección** — hasta **10 en lecciones prácticas o demo** (las de 10 minutos o más). Menos de 4: la lección probablemente no necesita pizarra. Más del tope: estás transcribiendo el guion.
3. **Cada diapo lleva etiqueta** (`## D3 — La promesa`) para poder citarla al revisar. **La numeración es correlativa y solo cuenta diapositivas: D1, D2, D3… sin saltos.** El número de `## D` del archivo debe coincidir exactamente con el que declara la cabecera.
   *La cabecera tiene que decir siempre dos cosas: cuántas diapositivas hay y qué hay detrás (entregable del alumno o pantalla real). Puede hacerlo en formato corto (`16:9 · 5 diapos · entregable detrás: roadmap-90-dias`) o en prosa, como los archivos de F0 (`16:9 · 4 diapos. El A4 es el mismo mapa para clavar en la pared; aquí es timeline de vídeo.`). Las dos valen: la segunda además le da contexto al diseñador.*
4. **Toda estructura que se anuncia, se entrega completa.** Si escribes "tabla de dos columnas y cuatro filas", van las ocho celdas. Si escribes "matriz con las 8 soluciones", van las 8 posiciones. El diseñador no puede inventar el contenido que falta: dejaría la diapo a medias o se lo inventaría él.
5. **Ningún marcador editorial llega a diseño.** Nada de `[BORRADOR]`, `[PENDIENTE]` ni notas internas dentro del copy. Si un dato está sin validar, se escribe la versión cualitativa que sí está cerrada ("la parte restante" en vez de "el 50% restante") y el aviso va fuera del bloque de copy.
6. **El copy se copia del guion, no se reescribe.** Se puede acortar quitando palabras; no cambiando las que quedan.
7. **Los diagramas se describen en texto**, con la estructura primero ("Línea de 7 puntos", "4 cajas horizontales") y los nodos después. El diseñador dibuja; tú decides qué dice.
8. **Marca lo que es pantalla real** con `> PANTALLA REAL — qué se enseña (p. ej. Stripe creando el enlace de pago)`, colocado en su posición del flujo y **sin número de diapo**. Así el diseñador sabe que ahí no diseña nada y la numeración D no se rompe.
9. **Indica si hay entregable detrás** en la cabecera. Si la diapo enseña el mismo árbol que el alumno se descarga en A4, el diseñador debe reutilizar la composición para que el alumno reconozca la pieza.

## Ejemplo (real, de F0-L1)

```markdown
## D5 — El mapa (el más importante de L1)
Línea de 7 puntos, F0 como salida:

**F0 Bienvenido** → F1 Domina → F2 Construye → F3 Lanza → F4 Cierra → F5 Entrega → F6 Escala

Bajo cada uno, 3–4 palabras máx.:
- F0 kick-off + setup
- F1 nicho + oferta
- ...

Pie: *90 días. El contenido se abre en orden. A partir de Lanza, el trabajo se solapa.*
```

Fíjate: dice **qué estructura** (línea de 7 puntos), **qué copy** (los nombres y las 3-4 palabras) y **qué matiz** (el pie). No dice colores ni tipografía — eso es del sistema visual.

## Control de calidad antes de mandarlo a diseño

- [ ] ¿Alguna diapo pasa de 12 palabras protagonistas?
- [ ] ¿Alguna frase no existe en el guion de la lección?
- [ ] ¿Se pasa del tope de diapos (8, o 10 si es práctica)? Si sí: ¿cuáles son transiciones disfrazadas?
- [ ] ¿La numeración D es correlativa y coincide con el número declarado en la cabecera?
- [ ] ¿Toda tabla, matriz o comparativa anunciada entrega TODAS sus celdas?
- [ ] ¿Queda algún `[BORRADOR]` u otra nota interna dentro del copy?
- [ ] ¿Las capturas de software van como `> PANTALLA REAL —`, sin número?
- [ ] ¿La cabecera dice si hay entregable detrás, y es el correcto?
