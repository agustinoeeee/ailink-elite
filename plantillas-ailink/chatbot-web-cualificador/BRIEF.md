# Brief de solución — Chatbot web cualificador (inmobiliaria)

> Formato de F2-R2, RELLENO para el nicho típico de esta solución. Se entrega entero a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …") y a partir de la primera versión se itera con las 3 reglas de dirección del final. Si tu nicho es otro, adapta los datos ANTES de construir.

**Solución del catálogo:** Chatbot web cualificador · **Nicho:** inmobiliarias

### 1. Contexto

- **Mi negocio cliente es:** una inmobiliaria de barrio en Sevilla, un gerente y 2 comerciales, con una cartera de unas 30 viviendas. Reciben interesados por los portales y por su propia web, pero nadie filtra: cada llamada y cada formulario cae en los comerciales tal cual, curiosos incluidos. Nombre inventado pero verosímil para la demo: **Inmobiliaria Alameda**.
- **Su cliente final es:** interesados en comprar vivienda que visitan la web a cualquier hora, también de noche y en fin de semana. La mayoría son curiosos; unos pocos son compradores reales con la financiación encaminada — y esos no esperan.
- **El dolor que esta demo enseña resuelto:** leads sin respuesta rápida y sin filtrar; los comerciales pierden horas con curiosos mientras el comprador real espera, y responder tarde regala la operación a la agencia de enfrente.
- **Quién usará la pantalla en la demo:** el gerente (el decisor). En mi llamada de venta hará él mismo de visitante: recorrerá el chat pulsando botones y verá su lead entrar cualificado en el panel.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web se ve una página de inmobiliaria verosímil: marca "Inmobiliaria Alameda", un titular y 4 fichas de vivienda (imagen ilustrativa o bloque de color, zona, precio, habitaciones, m²). Abajo a la derecha, la burbuja flotante del chat.
2. A los 2-3 segundos la burbuja saluda sola ("¿Buscas piso en Sevilla? Te ayudo en 1 minuto"); al pulsarla se abre la ventana de chat con el saludo y 3 opciones: "Busco comprar" / "Quiero vender mi piso" / "Solo estoy mirando". Todas las respuestas del visitante, siempre, son botones (conversación guiada, sin texto libre).
3. Camino "Busco comprar": el chat cualifica con 4 preguntas, cada una con sus botones — zona (Triana / Nervión / Macarena / Aljarafe), presupuesto (hasta 200.000€ / 200.000–300.000€ / más de 300.000€), financiación (necesito hipoteca / hipoteca pre-aprobada / al contado) y plazo (cuanto antes / en 3-6 meses / solo estoy mirando).
4. Con las respuestas, el chat muestra dentro de la conversación la vivienda de la cartera que encaja (o las dos que encajan) como mini-ficha, y ofrece agendar visita con 2 huecos por botón (jueves 18:00 / sábado 11:30).
5. Para cerrar, el visitante pulsa "Enviar mis datos" y el chat los rellena con el interesado de ejemplo (Carlos Navarro · 655 210 448) — no hay formularios reales que teclear. El lead aparece al instante en el mini-panel "Leads del chat" con todo lo recogido (nombre, teléfono, zona, presupuesto, financiación, plazo, vivienda y visita) y su etiqueta de temperatura calculada con las respuestas: **caliente** (plazo "cuanto antes" + financiación resuelta), **frío** ("solo estoy mirando") y **templado** (cualquier otra combinación — incluida "cuanto antes" con hipoteca por resolver).
6. Los leads calientes aparecen destacados con el aviso "avisar al comercial ya". El panel arranca con 2 leads de ejemplo anteriores para que no se vea vacío.
7. Los otros dos caminos también terminan bien: "Quiero vender mi piso" pregunta zona y cuándo, y entra en el panel como lead de "valoración"; "Solo estoy mirando" responde amable e invita a ver las viviendas o dejar una alerta de novedades.
8. Un botón "reiniciar demo" devuelve todo al estado inicial (chat cerrado, panel con solo los 2 leads de ejemplo), para repetir el flujo en cada llamada de venta. Todo el flujo es usable desde el móvil.

### 3. Qué NO entra

- Cerebro de IA real (API): la conversación es guiada y guionizada. El cerebro de verdad llega en F5, con el piloto pagado (esta solución, incluso en real, sigue siendo 100% web).
- Texto libre en el chat, en ningún punto.
- Instalación en la web real del cliente: la demo trae su propia página inventada (en el piloto sí se instala en la web real de la agencia).
- Conexión con portales inmobiliarios ni con el CRM de la agencia: la cartera y los leads son de ejemplo.
- Envío real de emails o mensajes con los leads.
- Fotos ni datos de inmuebles reales.
- Usuarios, contraseñas y pagos.

### 4. Datos de ejemplo

**Cartera de viviendas (las 4 fichas de la página):**

| Vivienda | Zona | Precio | Detalles |
|---|---|---|---|
| Piso 3 hab · 92 m² | Triana | 249.000€ | 2 baños, balcón, 4ª planta con ascensor |
| Ático 2 hab · 78 m² | Nervión | 310.000€ | Terraza de 20 m², plaza de garaje |
| Adosado 4 hab · 150 m² | Mairena del Aljarafe | 265.000€ | Patio, 2 plazas de garaje |
| Piso 2 hab · 68 m² | Macarena | 189.000€ | Reformado, 2ª planta sin ascensor |

**Leads de ejemplo ya en el panel al abrir:**

| Lead | Lo recogido | Temperatura |
|---|---|---|
| Lucía Márquez · 611 348 902 | Comprar · Macarena · hasta 200.000€ · necesita hipoteca · 3-6 meses | Templado |
| Fran Cordero · 622 570 133 | Solo mirando · dejó alerta de novedades | Frío |

Interesado de ejemplo para "Enviar mis datos": **Carlos Navarro · 655 210 448**. Huecos de visita: jueves 18:00 · sábado 11:30. Todas las cifras son ilustrativas.

### 5. Aspecto

- **Estilo general:** web inmobiliaria moderna y sobria; debe parecer la web real de una agencia de barrio bien llevada, no una maqueta.
- **Referencias:** las fichas, como las de un portal inmobiliario (imagen grande, precio destacado, zona y m² a la vista); el chat, como los widgets profesionales de chat web (burbuja flotante redonda, ventana con esquinas redondeadas, avatar de la agencia).
- **Colores / sensación:** blanco con azul marino y un acento cálido (ámbar) para precios y botones; el rojo/naranja reservado para "avisar al comercial ya"; tipografía grande y legible — el gerente lo verá a veces desde el móvil.

### 6. Cómo sabré que funciona

- [ ] El flujo comprador completo (burbuja → 4 preguntas → vivienda propuesta → visita → lead caliente en el panel) se reproduce en menos de 90 segundos sin explicar nada.
- [ ] La etiqueta de temperatura cambia si cambio las respuestas (probar: "solo estoy mirando" debe salir frío).
- [ ] Funciona igual en el móvil que en el ordenador, y la burbuja no tapa el contenido.
- [ ] El botón "reiniciar demo" deja el chat cerrado y el panel con solo los 2 leads de ejemplo.
- [ ] Viviendas, precios, zonas y nombres parecen de una agencia real de Sevilla.
- [ ] La URL carga rápido a la primera.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
