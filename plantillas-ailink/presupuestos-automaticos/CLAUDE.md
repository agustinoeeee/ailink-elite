# CLAUDE.md — Demo: Presupuestos automáticos (Reformas Velasco)

## Qué es este proyecto
Demo comercial web de presupuestos automáticos para empresas de reformas. UN solo archivo (`index.html`, construido a partir de `BRIEF.md`), sin dependencias externas, desplegable tal cual. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Flujo GUIADO**: el cliente final solo avanza pulsando tarjetas, chips y botones. JAMÁS añadas entrada de texto libre, campos de formulario abiertos ni conexión a APIs de IA — es una decisión de diseño del programa (el cerebro real y el envío en PDF llegan en el piloto, no en la demo).
- **Datos ficticios y verosímiles**: nombre de empresa, tipos de trabajo, partidas y precios creíbles en español de España. Nada de "Trabajo 1" ni lorem ipsum. Todas las cifras (tarifas, IVA, extras) son ilustrativas.
- **El desglose siempre cuadra**: las partidas más los extras suman exactamente el total mostrado. Un presupuesto que no suma mata la demo.
- **El aviso "Presupuesto orientativo, sujeto a visita técnica" es innegociable**: visible junto al total, en todas las pantallas de resultado.
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** (portada, sin selecciones) — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en `reiniciar()`.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).
- No uses marcas ni logos reales: la empresa, el teléfono y el email son inventados.

## Los 9 comportamientos que NO se pueden romper (del BRIEF.md)
1. Portada del negocio con botón "Calcula tu presupuesto al instante".
2. Paso 1 de 3: tipo de trabajo elegido entre 4 tarjetas con icono.
3. Paso 2 de 3: tamaño entre 3 opciones con metros orientativos, que cambian según el tipo elegido.
4. Paso 3 de 3: extras opcionales como chips marcables con precio visible.
5. Presupuesto instantáneo con membrete, desglose por partidas, extras, subtotal, IVA y total destacado.
6. Aviso "orientativo, sujeto a visita técnica gratuita" bien visible bajo el total.
7. "Solicitar visita técnica": franja mañana/tarde por botones → confirmación. Sin datos personales.
8. "Reiniciar demo" restaura todo.
9. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio y membrete, tipos de trabajo → servicios del nicho, tarifas y extras, partidas del desglose, copy y colores. El flujo de 3 pasos y la estructura no se tocan.
