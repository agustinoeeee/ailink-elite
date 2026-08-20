# CLAUDE.md — Demo: Informes automáticos (Arrieta & Soler Abogados)

## Qué es este proyecto
Demo comercial web de informes automáticos para despachos de abogados. UN solo archivo (`index.html`), sin dependencias externas, desplegable tal cual. Es una herramienta de VENTA: se enseña en llamadas comerciales, no es el producto final.

## Reglas del proyecto
- **Un solo archivo**: todo (HTML, CSS, JS) vive en `index.html`. No crees archivos nuevos ni añadas librerías/CDNs.
- **Informe GUIONIZADO**: el resumen redactado está escrito para los datos de ejemplo y las cifras se calculan desde la tabla de datos de la página. JAMÁS añadas entrada de texto libre ni conexión a APIs de IA — es una decisión de diseño del programa (la redacción real con IA llega en el piloto, en F5).
- **Las cifras SIEMPRE cuadran**: cualquier número del informe (totales, comparativas, gráficas) debe calcularse desde la tabla de datos, nunca escribirse duplicado a mano. Si un dato de la tabla cambia, el informe debe reflejarlo. Un informe que descuadra mata la demo.
- **Gráficas sin librerías**: dibujadas con CSS o SVG inline. Ni CDNs ni dependencias.
- **Datos ficticios y verosímiles**: asuntos, clientes, abogados y plazos creíbles en español de España. Nada de "Cliente 1" ni lorem ipsum. Toda la facturación es ilustrativa (tarifa por hora configurable).
- **El botón "Reiniciar demo" debe dejar SIEMPRE el estado inicial exacto** (panel de datos visible, sin informe generado) — cada llamada de venta empieza limpia. Si añades estado nuevo, inclúyelo en la función de reinicio.
- **Móvil primero**: cualquier cambio se comprueba también en viewport de 375px.
- **Español de España** en todo el copy (tuteo, cero latinoamericanismos).

## Los 8 comportamientos que NO se pueden romper (del BRIEF.md)
1. Panel de datos del mes: tabla de asuntos (cliente, materia, abogado, estado, horas, facturación ilustrativa) + lista corta de plazos próximos.
2. Botón grande y bien visible: "Generar informe del mes".
3. Al pulsarlo, breve animación de "preparando informe…" y aparece el informe en la misma página: cifras clave con comparativa contra el mes anterior.
4. El informe incluye 2-3 gráficas simples (facturación por semana, horas por abogado, asuntos por materia).
5. El informe incluye un resumen redactado en lenguaje claro con un bloque de avisos: plazos que vencen en 15 días y asuntos sin actividad en 30 días.
6. Todas las cifras del informe cuadran con la tabla de datos del panel.
7. "Reiniciar demo" vuelve al panel sin informe generado.
8. Usable desde el móvil.

## Al personalizar para otro nicho
Cambiar SOLO: nombre del negocio, asuntos→tu unidad de trabajo (trámites, pacientes, reparaciones, matrículas), materias→tus categorías, datos de la tabla, texto guionizado del resumen y colores. La estructura panel → botón → informe no se toca.
