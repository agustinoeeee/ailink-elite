# Prompt para Claude Design — la tanda de correcciones

> **Antes de pegarlo, dos cosas:**
>
> 1. **Ábrele las dos carpetas:** `programa-ia` (de donde sale el copy, ya actualizada con los cambios del 20/08) y `AILINK Élite. Formación visual` (donde están sus `.dc.html`).
> 2. **El renombrado del paso 0 YA ESTÁ HECHO.** Los 12 archivos se renumeraron el 20/08 y quedan libres `F0-L3`, `F1-L2` y `F1-L9`. Hay copia de seguridad en `~/Desktop/formacion-visual-ANTES-de-renumerar.tgz`. No le pidas que renombre nada.
>
> Son **30 piezas**: 7 nuevas y 23 a rehacer (4 de ellas, de una sola línea).

```
Seguimos con AILINK Élite. Ya me entregaste 71 piezas y están bien: NO
empezamos de cero y NO se toca nada que no esté en esta lista.

El programa ha cambiado y hay material que ha quedado caducado. Todo lo que
hay que hacer está detallado, pieza a pieza y con el motivo del cambio, en:

    diseno/03-REENCARGOS-PENDIENTES.md

Léelo entero antes de tocar nada. Es la lista de trabajo; esto es el encargo.

LO PRIMERO, PARA QUE NO LA LIEMOS
- Los archivos YA están renumerados. F0 va de L1 a L9 y F1 de L1 a L9, con
  F0-L3, F1-L2 y F1-L9 libres para las lecciones nuevas. No renombres nada,
  no muevas nada, no reordenes nada.
- El copy sale SIEMPRE del .md de origen que indica cada fila, leyéndolo
  ahora: esos .md han cambiado. No lo saques de tu versión anterior de la
  pieza ni de memoria.
- Cuando una fila diga "cambio mínimo", es literal: cambias esa frase y no
  tocas una coma más. Cuatro piezas están así.
- Lo que no está en la lista, no se toca. El propio documento tiene una
  sección "Lo que NO hay que rehacer": respétala.

LOS CUATRO CAMBIOS DE FONDO (para que entiendas por qué caduca cada cosa)
1. La promesa: +10.000€ pasa a +5.000€ acumulados en 90 días, y de 2-4
   clientes a 1-3.
2. La anatomía de la oferta pasa de 6 a 7 componentes: "red de seguridad"
   se llama ahora GARANTÍA y entra URGENCIA.
3. Los hitos y el setup de F0 se mueven; el paso 4 deja de ser "Stripe" y
   pasa a ser "método de pago".
4. Tres lecciones nuevas: F0-L3 "Tu norte", F1-L2 "Tu inventario de
   ventajas" y F1-L9 "De la oferta al resto del negocio".
Y una regla nueva que afecta a varias piezas: los recursos del alumno citan
las lecciones POR NOMBRE, nunca por número.

ORDEN DE TRABAJO — módulo a módulo, no pieza a pieza

  Bloque 1 · F0
    Nuevas:    F0-L3-pizarra · F0-norte-personal (A4)
    A rehacer: F0-L1, F0-L6, F0-L8, F0-L9 (pizarras)
               F0-roadmap-90-dias · F0-checklist-setup-negocio (A4)
               F0-manifiesto-90-dias · F0-plantilla-base-de-tests
               (estas dos, cambio mínimo: una frase de cabecera)

  Bloque 2 · F1
    Nuevas:    F1-L2-pizarra · F1-L9-pizarra
               F1-inventario-ventajas · F1-catalogo-oportunidades ·
               F1-revision-oferta (A4)
    A rehacer: F1-L1, F1-L3, F1-L4, F1-L5, F1-L6, F1-L7, F1-L8 (pizarras)
               F1-avatar-cliente-ideal · F1-calculadora-pricing ·
               F1-worksheet-oferta · F1-ejemplos-ofertas ·
               F1-checklist-validacion-nicho (A4)
               F1-lista-micro-nichos-espana · F1-cuaderno-f1
               (estas dos, cambio mínimo)

  Bloque 3 · F3
    A rehacer: F3-L1-pizarra (solo D3: la cadena de números nueva)

EMPIEZA POR AQUÍ Y PÁRATE
Haz primero DOS piezas y enséñamelas antes de seguir:
  1. F0-L3-pizarra (una pizarra nueva desde cero)
  2. F1-calculadora-pricing (un A4 que gana un paso entero)
Con esas dos calibramos y ya no volvemos a discutirlo.

REGLAS DE SIEMPRE
- Español de España, tuteo. El copy es literal: no reescribes, no resumes,
  no acortas, no "mejoras" el tono.
- Pizarra = 16:9 con la esquina superior derecha libre (480×480 px).
  Entregable = A4 que se imprime y se rellena a bolígrafo: líneas ≥8 mm,
  casillas ≥4 mm, legible en blanco y negro.
- "## D1, D2…" son diapositivas correlativas. "> PANTALLA REAL" no es
  diapositiva: no diseñes nada ahí.
- Cero stock, cero degradados, cero iconos 3D, cero emojis decorativos.
- Si algo no cabe, lo señalas en la entrega. NO recortas el copy.
- El documento trae cuatro avisos de encaje concretos (F1-L3 D2, F1-L5,
  F1-inventario-ventajas y F1-revision-oferta). Léelos: son los sitios
  donde el texto nuevo revienta la composición vieja.

AL CERRAR CADA BLOQUE
Tabla de dos columnas: archivo de salida ↔ .md de origen, marcando cuáles
son nuevos y cuáles sustituyen a una versión anterior.
```

## Cuando te lo entregue

Los `.dc.html` nuevos se convierten y se reparten con el circuito de siempre:

```bash
python3 herramientas/convertir.py "~/Desktop/AILINK Élite. Formación visual"
python3 herramientas/componer.py
cd skool && python3 build.py
```

Después, **borra de `diseno/03-REENCARGOS-PENDIENTES.md` la fila de cada pieza entregada**. Ese documento se vacía solo: mientras una pieza siga listada, su PDF está caducado y no se graba ni se sube con él.
