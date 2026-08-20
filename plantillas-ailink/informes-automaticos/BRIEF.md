# Brief relleno — Informes automáticos · Despachos de abogados

> Brief completo en formato F2-R2, listo para usar. Se entrega ENTERO a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …"). A partir de la primera versión, diriges con las 3 reglas del final.

**Solución del catálogo:** Informes automáticos · **Nicho:** despachos de abogados

### 1. Contexto

- **Mi negocio cliente es:** un despacho de abogados pequeño en España, 3 abogados y una oficial administrativa, generalista con peso en mercantil y laboral. El socio director quiere saber cómo va el mes (asuntos, horas, plazos, facturación), pero montarlo exige cruzar a mano el Excel de horas, la agenda y la facturación: lo hace tarde, a medias o directamente no lo hace. Nombre inventado pero verosímil para la demo: **Arrieta & Soler Abogados**.
- **Su cliente final es:** pymes y particulares cuyos asuntos generan los datos del informe: encargos, horas trabajadas, plazos procesales y facturación.
- **El dolor que esta demo enseña resuelto:** el socio dirige a ciegas — se entera tarde de los plazos que se echan encima, de los asuntos parados sin facturar y de los meses flojos — y el informe que lo evitaría cuesta horas de trabajo administrativo que nadie factura.
- **Quién usará la pantalla en la demo:** el socio director (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve el panel de datos del despacho con el mes en curso: una tabla de asuntos (cliente, materia, abogado responsable, estado, horas del mes y facturación ilustrativa) y una lista corta de plazos próximos.
2. Sobre el panel, un botón grande y bien visible: "Generar informe del mes".
3. Al pulsarlo, tras una breve animación de "preparando informe…" (1-2 segundos), aparece el informe del mes en la misma página, encabezado por las cifras clave: asuntos abiertos y cerrados, horas trabajadas y facturación ilustrativa del mes, cada una con su comparación contra el mes anterior (datos del mes anterior precargados).
4. El informe incluye 2-3 gráficas simples y limpias: facturación por semana, horas por abogado y asuntos por materia — dibujadas en la propia página, sin librerías externas.
5. El informe incluye un resumen redactado en lenguaje claro — qué ha pasado, qué destaca, dónde conviene mirar — con un bloque de avisos: plazos que vencen en los próximos 15 días y asuntos sin actividad en los últimos 30 días. (El texto está guionizado para los datos de ejemplo: la redacción real con IA llega en el piloto.)
6. Todas las cifras del informe cuadran con la tabla de datos del panel — el socio puede comprobar las sumas delante de mí.
7. Un botón "reiniciar demo" vuelve al panel de datos sin informe generado, para repetir el flujo en cada llamada de venta.
8. Todo el flujo es usable desde el móvil.

### 3. Qué NO entra

- Conexión con el software real del despacho (gestión de expedientes, contabilidad, facturación): los datos de la demo son de ejemplo. El volcado o la conexión ligera a los datos del cliente llegan en F5.
- Redacción con IA de verdad: el texto del informe de la demo está guionizado. El cerebro real llega en F5, con el piloto pagado.
- Envío automático programado (el informe que llega solo cada mes por email): en la demo se genera con el botón; el envío se cuenta de palabra.
- Exportar a PDF, usuarios, contraseñas y pagos.
- Cifras reales: toda la facturación es ilustrativa (tarifa por hora configurable).
- Más de un despacho (la demo es mono-despacho).

### 4. Datos de ejemplo

Tarifa por hora ilustrativa: 120 €/hora (configurable). Mes en curso de la demo: julio; comparativa de junio precargada: 41 horas · 4.920 € · 1 asunto cerrado.

| Asunto / cliente | Materia | Abogado | Estado | Horas julio | Facturado julio (ilustrativo) |
|---|---|---|---|---|---|
| Construcciones Landeta SL — reclamación de impago | Mercantil | Beatriz Arrieta | Abierto | 14 h | 1.680 € |
| Miguel Cano — despido improcedente | Laboral | Sergio Soler | Cerrado en julio | 9 h | 1.080 € |
| Herencia familia Peñalver | Civil | Beatriz Arrieta | Abierto | 6 h | 720 € |
| Restaurante La Bardena SL — revisión de contratos | Mercantil | Nuria Gaspar | Abierto (sin actividad desde el 18 de junio) | 0 h | 0 € |
| Elvira Sanchís — divorcio contencioso | Familia | Sergio Soler | Abierto | 11 h | 1.320 € |
| Transportes Iriarte SL — sanción administrativa | Administrativo | Nuria Gaspar | Abierto | 7 h | 840 € |

Plazos próximos: contestación a la demanda (Construcciones Landeta) — 4 de agosto · recurso contra la sanción (Transportes Iriarte) — 11 de agosto.

(Comprobación para el informe: julio suma 47 horas y 5.640 € — las cifras de los titulares deben salir de esta tabla, no escribirse a mano.)

### 5. Aspecto

- **Estilo general:** sobrio y elegante, de despacho; el informe debe parecer un informe de dirección que da gusto enseñar, casi listo para imprimir — no un panel técnico.
- **Referencias:** las cifras clave como tarjetas de un panel de métricas moderno; las gráficas limpias y sin adornos; el resumen redactado como una nota de dirección, no como un listado de datos.
- **Colores / sensación:** blanco, gris antracita y un acento azul oscuro; tipografía serena y legible; nada estridente — el lector es un abogado, y a veces lo verá desde el móvil.

### 6. Cómo sabré que funciona

- [ ] El flujo completo (abrir → "Generar informe del mes" → informe entero visible) se reproduce en menos de 1 minuto sin explicar nada.
- [ ] Todas las cifras del informe cuadran con la tabla de datos (las sumas se pueden comprobar delante del cliente).
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] El botón "reiniciar demo" vuelve al panel sin informe, listo para repetir el flujo.
- [ ] Todos los datos parecen de un despacho real: asuntos, materias, nombres y plazos verosímiles.
- [ ] La URL carga rápido a la primera.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
