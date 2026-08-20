# Plantilla AILINK — Automatización de reseñas Google (restaurantes)

> **Kit de brief.** Esta plantilla trae el brief COMPLETO relleno para su nicho típico (restaurantes) y las reglas de proyecto para Claude Code. La demo la construyes TÚ dirigiendo a Claude Code — esa es exactamente la habilidad de F2 — usando la plantilla insignia (`../recuperacion-citas-dental/`) como referencia estructural de cómo debe quedar.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `BRIEF.md` | El brief completo relleno (formato de F2-R2) para un restaurante inventado pero verosímil — listo para dárselo entero a Claude Code como primera instrucción |
| `CLAUDE.md` | Las instrucciones de proyecto para Claude Code: qué es, qué reglas tiene, qué no se puede romper |
| `README.md` | Este archivo |

El objetivo del kit es que acabes con **un `index.html` en esta carpeta**: un solo archivo, sin dependencias, con el panel de reseñas + el simulador de conversación guiada + los marcadores subiendo + el botón reiniciar.

## Qué enseña esta demo (el momento "quiero eso")

El flujo completo de la solución **Automatización de reseñas Google** simulado de punta a punta: un cliente termina de comer → le llega un mensaje pidiendo valoración → si puntúa 4-5 estrellas, se le lleva a dejar la reseña pública y el dueño ve su nota media SUBIR en pantalla; si puntúa 1-3, la queja se desvía en privado al dueño antes de hacerse pública. Dos caminos, dos "wow": la nota que sube y la queja que nunca llega a Google.

## Cómo se usa (alumno)

1. **Mira primero la insignia**: abre `../recuperacion-citas-dental/index.html` y reprodúcela entera. Ese es el listón de calidad y la estructura de referencia (panel + simulador + contadores + reiniciar).
2. **Lee el `BRIEF.md` de esta carpeta** completo antes de tocar nada. Fíjate en los dos caminos (contento / descontento): son el corazón de la demo.
3. **Construye con Claude Code**: abre esta carpeta con Claude Code y entrégale el brief entero como primera instrucción ("construye esta demo web siguiendo este brief: …").
4. **Itera con las 3 reglas de dirección** del final del brief: una petición = un cambio; probar entre pasos; los errores se pegan, no se pelean.
5. **Despliega** (F2-L2) y tendrás tu URL compartible.
6. **No la enseñes a nadie** sin pasar la checklist pre-demo de F2-L6.

## Qué NO es

- No es el piloto real: no se conecta al perfil de Google del negocio ni a WhatsApp de verdad. La conversación es un simulador visual guiado (botones, sin texto libre — decisión del programa) y la pantalla de reseña es genérica, sin logos oficiales de Google. La integración real y los borradores de respuesta con IA de verdad llegan en F5, con el piloto pagado.
- No guarda datos: todo vive en la página y se reinicia con el botón (a propósito: cada llamada de venta empieza limpia).

## Adaptación rápida a otros nichos (mismo esqueleto)

Talleres mecánicos (coche entregado → valoración), peluquerías y estética (servicio terminado), alojamientos turísticos (check-out del huésped), clínicas de fisioterapia (fin de tratamiento): cambia comensales→clientes, mesas→servicios y el copy de los mensajes y reseñas. Los dos caminos (4-5 estrellas → público, 1-3 → privado) son idénticos en todos.
