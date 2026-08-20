# Plantilla AILINK — Recepcionista IA (clínicas veterinarias)

> **Kit de brief.** Esta plantilla trae todo lo necesario para que construyas TU demo de Recepcionista IA con Claude Code: el brief completo relleno, las reglas de proyecto y este manual. No trae la demo construida — por diseño: construirla a partir del brief ES la habilidad que entrenas en F2. Tu referencia estructural es la plantilla insignia (`../recuperacion-citas-dental/`), que sí está completa y funcionando.

## Qué contiene

| Archivo | Qué es |
|---|---|
| `BRIEF.md` | El brief COMPLETO relleno para el nicho típico (clínica veterinaria — teléfono saturado), en el formato de F2-R2. Listo para dárselo entero a Claude Code como primera instrucción. |
| `CLAUDE.md` | Las instrucciones de proyecto para Claude Code: qué es esta demo, sus reglas innegociables y qué no tocar mientras la construyes y la personalizas. |
| `README.md` | Este manual. |

## La solución (ficha del catálogo: Recepcionista IA — WhatsApp/llamadas)

Una conversación que atiende como lo haría la persona de recepción: saluda, responde las dudas de siempre (horarios, ubicación, precios orientativos), propone huecos libres y apunta la cita en la agenda. La demo lo enseña con el gancho más doloroso del nicho: las **llamadas perdidas** que la recepcionista IA convierte en citas — incluida la urgencia que se detecta y se deriva en vez de darle cita.

Dificultad 1, potencia de demo 3: la esquina de oro del catálogo, junto a la insignia.

## Cómo se usa (alumno)

1. **Lee `BRIEF.md` entero** antes de abrir Claude Code. Es tu herramienta de dirección: describe QUÉ debe pasar, nunca cómo programarlo.
2. **Abre y prueba la insignia** (`../recuperacion-citas-dental/index.html`): panel + simulador + contadores + reiniciar. Esa estructura es la misma que vas a construir aquí, con otro flujo dentro.
3. **Abre ESTA carpeta con Claude Code** y dale el brief entero como primera instrucción: "construye esta demo web siguiendo este brief" + el contenido de `BRIEF.md`. Objetivo: UN solo archivo `index.html`, sin dependencias.
4. **Itera con las 3 reglas de dirección** (al final del brief): una petición = un cambio; probar entre pasos; los errores se pegan, no se pelean.
5. **Pasa los checks** de la sección 6 del brief. Lo que no has probado, no existe.
6. **Despliégala** en tu hosting (F2-L2) y tendrás tu URL compartible.
7. **No la enseñes a nadie** sin pasar la checklist pre-demo de F2-L6.

## Qué NO es

- No es el piloto real: la conversación es un simulador visual guiado (botones, sin texto libre, sin APIs de IA — decisión del programa). La integración real con el WhatsApp y el teléfono del negocio, y el cerebro de IA de verdad, llegan en F5 con el piloto pagado.
- No guarda datos: todo vive en la página y se reinicia con el botón (a propósito: cada llamada de venta empieza limpia).
- No es una demo genérica: está rellena para clínica veterinaria. Si tu oferta V1 es otro nicho, adapta el brief ANTES de construir (abajo).

## Adaptación rápida a otros nichos (mismo esqueleto)

Talleres mecánicos (nadie coge el teléfono con las manos en el motor), clínicas dentales y de fisioterapia (recepción saturada), restaurantes con volumen (reservas): cambia mascotas→vehículos/pacientes/mesas, los motivos de llamada, los precios orientativos y el caso de urgencia (avería en carretera, dolor agudo…). El flujo llamada perdida → conversación → cita en agenda es idéntico.
