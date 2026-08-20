# BRIEF — Presupuestos automáticos (empresas de reformas)

> Brief completo relleno para el nicho típico de esta solución (formato de F2-R2). **Cómo se usa:** se lo das ENTERO a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …") y, a partir de la primera versión, iteras con las 3 reglas de dirección del final. Si tu nicho es otro, cambia negocio, servicios, tarifas y copy — el flujo es el mismo.

**Solución del catálogo:** Presupuestos automáticos · **Nicho:** empresas de reformas e instaladores

### 1. Contexto

- **Mi negocio cliente es:** una empresa de reformas familiar en España, 6 operarios, dirigida por su dueño, especializada en baños, cocinas, pintura y suelos. Hoy los presupuestos los hace el dueño por las noches con una hoja de cálculo y tarda 2-3 días en enviarlos — muchos se enfrían por el camino. Nombre inventado pero verosímil para la demo: **Reformas Velasco** (Zaragoza).
- **Su cliente final es:** particulares que quieren reformar su vivienda y piden presupuesto a 3-4 empresas a la vez; se quedan con la que responde antes y más claro.
- **El dolor que esta demo enseña resuelto:** presupuestos lentos = obras que se lleva el competidor que contestó primero. Un solo presupuesto ganado paga años del servicio.
- **Quién usará la pantalla en la demo:** el dueño de la empresa (el decisor). En mi llamada de venta hago yo de cliente final: relleno el configurador delante de él y ve salir el presupuesto al instante — el salto de "dos días" a "30 segundos" se explica solo.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve la portada de Reformas Velasco (nombre a modo de logo, claim "Reformas de baño, cocina, pintura y suelos en Zaragoza", teléfono y email ficticios) con un botón grande: "Calcula tu presupuesto al instante".
2. Paso 1 de 3: se elige el tipo de trabajo entre 4 tarjetas grandes con icono — Baño completo, Cocina completa, Pintura interior, Cambio de suelo. Solo se avanza pulsando una tarjeta: no hay ningún campo de texto libre en toda la demo. Un indicador muestra en qué paso estás (1 de 3, 2 de 3…).
3. Paso 2 de 3: se elige el tamaño entre 3 opciones con metros orientativos (p. ej. para baño: "Pequeño — hasta 4 m²", "Medio — 4 a 6 m²", "Grande — más de 6 m²"). Las opciones y sus metros cambian según el tipo de trabajo elegido.
4. Paso 3 de 3: se marcan extras opcionales (ninguno, uno o varios) como chips con el precio visible en cada uno, y se pulsa "Ver mi presupuesto".
5. El presupuesto aparece al instante en pantalla, como un documento presentable con el membrete de Reformas Velasco: trabajo y tamaño elegidos, desglose por partidas con importes alineados a la derecha, los extras elegidos como líneas propias, subtotal, IVA y el importe total destacado en grande. Las partidas suman exactamente el total.
6. Debajo del total, bien visible: **"Presupuesto orientativo. El importe definitivo se confirma con una visita técnica gratuita y sin compromiso."**
7. Botón "Solicitar visita técnica": se elige franja horaria pulsando botones (mañana / tarde) y aparece la confirmación "Visita solicitada — te llamamos hoy mismo para cerrar día y hora". No se piden datos personales.
8. Un botón "reiniciar demo", siempre accesible, devuelve a la portada con todo a cero, para repetir el flujo en cada llamada de venta.
9. Todo el flujo es usable desde el móvil (el cliente final pediría presupuesto desde el sofá; el dueño lo mirará desde la obra).

### 3. Qué NO entra

- Envío real del presupuesto por email o WhatsApp, ni PDF descargable: el presupuesto se ve en pantalla. El envío automático y la plantilla en PDF llegan en F5, con el piloto pagado.
- Formulario de datos personales (nombre, teléfono, dirección): la demo no recoge datos de nadie.
- Mediciones reales ni cálculo por m² exacto: las cifras son ilustrativas; las tarifas de verdad se cargan con el cliente en el piloto.
- Fotos de la vivienda, planos o subida de archivos.
- Usuarios, contraseñas y pagos.
- Más de una empresa (la demo es mono-negocio).

### 4. Datos de ejemplo

Tarifas base ilustrativas. IVA ilustrativo al 10% (reforma de vivienda), con nota en el documento: "tipo de IVA orientativo, se confirma en la visita".

| Tipo de trabajo | Tamaños (orientativos) | Precio base | Extras disponibles (precio) |
|---|---|---|---|
| Baño completo | Pequeño (hasta 4 m²) · Medio (4-6 m²) · Grande (más de 6 m²) | 3.900€ · 4.800€ · 5.900€ | Cambiar bañera por plato de ducha (+690€) · Mueble con espejo y luz (+430€) · Mampara de cristal (+380€) |
| Cocina completa | Pequeña (hasta 8 m²) · Media (8-12 m²) · Grande (más de 12 m²) | 6.400€ · 7.900€ · 9.600€ | Encimera de cuarzo (+1.100€) · Iluminación LED bajo mueble (+240€) · Toma para lavavajillas (+160€) |
| Pintura interior | Piso pequeño (hasta 60 m²) · Medio (60-90 m²) · Grande (más de 90 m²) | 1.150€ · 1.550€ · 2.100€ | Quitar gotelé (+520€) · Pintar techos (+280€) · Esmaltar puertas (+350€) |
| Cambio de suelo | Hasta 60 m² · 60-90 m² · Más de 90 m² | 2.300€ · 3.100€ · 4.200€ | Retirar suelo antiguo (+450€) · Rodapié nuevo (+320€) · Nivelado con pasta autonivelante (+380€) |

Desglose por partidas del precio base (reparto orientativo, para que el documento parezca un presupuesto de obra real): para baño y cocina — demolición y retirada de escombros 15% · fontanería y electricidad 20% · materiales y revestimientos 30% · sanitarios/mobiliario y acabados 20% · mano de obra y remates 15%. Para pintura y suelo, partidas propias: materiales · preparación de superficies · mano de obra.

Datos del membrete: **Reformas Velasco** · Zaragoza · Tel. 976 411 302 · presupuestos@reformasvelasco.es (todo ficticio).

### 5. Aspecto

- **Estilo general:** web de empresa de reformas seria y moderna — debe transmitir "esta empresa trabaja bien", no "proyecto de fin de semana". El presupuesto final debe parecer un documento de verdad, con membrete.
- **Referencias:** el configurador, como las calculadoras de presupuesto online modernas (una decisión por pantalla, tarjetas grandes con icono, indicador de pasos); el presupuesto, como un presupuesto de obra en papel (tabla de partidas con importes alineados, total grande al pie).
- **Colores / sensación:** blanco y gris antracita con un acento naranja obra; tipografía grande y legible — se verá muchas veces desde el móvil a pie de obra.

### 6. Cómo sabré que funciona

- [ ] El flujo completo (tipo → tamaño → extras → presupuesto en pantalla) se completa en menos de 1 minuto sin explicar nada.
- [ ] Dos combinaciones distintas dan totales distintos y coherentes (más tamaño y más extras = importe mayor), y el desglose suma exactamente el total en ambas.
- [ ] El aviso "orientativo, sujeto a visita técnica" se ve junto al total sin buscarlo.
- [ ] El botón "reiniciar demo" devuelve a la portada, listo para repetir el flujo.
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] Todos los datos parecen de una empresa real: nombres de partidas, precios y copy verosímiles.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
