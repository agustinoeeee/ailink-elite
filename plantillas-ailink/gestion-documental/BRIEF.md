# Brief relleno — Gestión documental · Gestorías y asesorías

> Brief completo en formato F2-R2, listo para usar. Se entrega ENTERO a Claude Code como primera instrucción ("construye esta demo web siguiendo este brief: …"). A partir de la primera versión, diriges con las 3 reglas del final.

**Solución del catálogo:** Gestión documental · **Nicho:** gestorías y asesorías

### 1. Contexto

- **Mi negocio cliente es:** una gestoría-asesoría independiente en España (fiscal, laboral y contable), 2 socios y 4 empleados, unos 180 clientes entre autónomos y pymes. Cada cierre de mes y de trimestre, el equipo pierde días enteros persiguiendo por teléfono y email los documentos que faltan. Nombre inventado pero verosímil para la demo: **Gestoría Ferrándiz**.
- **Su cliente final es:** autónomos y pequeñas empresas que deben entregar documentación cada mes o trimestre (facturas, extractos, nóminas, cuentas) y que casi siempre dejan algo sin enviar hasta que alguien les persigue.
- **El dolor que esta demo enseña resuelto:** los expedientes se quedan bloqueados por un documento que falta, y reclamarlo exige perseguir cliente a cliente; cada hora administrativa tiene un coste laboral directo y medible, y en campaña de impuestos el cuello de botella se come al equipo.
- **Quién usará la pantalla en la demo:** el socio o gerente de la gestoría (el decisor). La verá en mi llamada de venta, con mi pantalla compartida o abriendo la URL desde su móvil.

### 2. Qué debe hacer — comportamientos observables

1. Al abrir la web, se ve un panel de expedientes: cliente, trámite (IVA del trimestre, nóminas del mes, Impuesto de Sociedades…), la lista de documentos requeridos con su estado (recibido / pendiente) y el estado del expediente (completo / incompleto).
2. Sobre el panel, dos contadores bien visibles: "expedientes completos" (p. ej. 2 de 5) y "horas de persecución ahorradas este mes" (calculadas con los minutos por documento reclamado, configurables; cifra ilustrativa).
3. Cada documento "pendiente" tiene un botón "Reclamar"; al pulsarlo se abre al lado un simulador visual de conversación tipo WhatsApp — dentro de la web, no WhatsApp real — con ese cliente.
4. La conversación simulada sigue este flujo: mensaje amable recordando exactamente qué documento falta y para qué trámite → el cliente responde pulsando una respuesta sugerida ("Te lo envío ahora mismo" — botones dentro del simulador: conversación guiada, sin texto libre) → burbuja del cliente con el documento adjunto simulado (icono y nombre de archivo verosímil) → confirmación de recepción con agradecimiento.
5. Al confirmarse, el documento pasa a "recibido" en el panel y — el momento "wow" — sus datos aparecen extraídos y clasificados en una fila de la tabla del expediente (proveedor, importe, fecha; valores de ejemplo GUIONIZADOS, sin IA real: la lectura de verdad llega en F5). Si era el último que faltaba, el expediente entero cambia a "completo" con un distintivo visual claro, y los dos contadores suben.
6. Un botón "reiniciar demo" devuelve todos los datos a su estado inicial, para repetir el flujo en cada llamada de venta.
7. Todo el flujo es usable desde el móvil.

### 3. Qué NO entra

- WhatsApp ni email de verdad: la conversación es una simulación visual dentro de la web. La integración real llega en F5, con el piloto pagado.
- Lectura y extracción de datos de los documentos (que la IA lea la factura y saque importes y fechas): es el corazón del piloto real y llega en F5. En la demo, la "extracción" del comportamiento 5 es una simulación guionizada con valores de ejemplo — enseña el resultado sin procesar nada de verdad.
- Subida real de archivos: el adjunto de la conversación es visual.
- Conexión con el software de la gestoría (A3, Sage, Holded…): los datos de la demo son de ejemplo.
- Usuarios, contraseñas y pagos.
- Más de una gestoría (la demo es mono-gestoría).

### 4. Datos de ejemplo

Minutos ahorrados por documento reclamado, para el contador: 20 minutos (cifra ilustrativa, configurable).

| Cliente | Trámite | Documentos requeridos (estado inicial) | Expediente |
|---|---|---|---|
| Talleres Yagüe SL | IVA 2º trimestre | Facturas emitidas ✓ · Facturas recibidas ✗ · Extracto bancario ✓ | Incompleto |
| Clara Montesinos (autónoma) | IRPF trimestral | Facturas emitidas ✓ · Gastos deducibles ✓ | Completo |
| Panadería San Roque SL | Nóminas de julio | Parte de horas ✗ · Altas y bajas del mes ✓ | Incompleto |
| Instalaciones Beltrán SL | Impuesto de Sociedades | Cuentas anuales ✓ · Libro mayor ✗ · Certificado bancario ✗ | Incompleto |
| Floristería Petunia | IVA 2º trimestre | Facturas emitidas ✓ · Facturas recibidas ✓ · Extracto bancario ✓ | Completo |

(✓ = recibido · ✗ = pendiente. Nombres de archivo verosímiles para los adjuntos simulados: `facturas-recibidas-jun.pdf`, `parte-horas-julio.pdf`, `libro-mayor-2025.xlsx`…)

### 5. Aspecto

- **Estilo general:** sobrio y profesional; debe transmitir "software serio de gestoría", no "proyecto de fin de semana". Es una pantalla de trabajo, no de marketing.
- **Referencias:** el panel, como un gestor de tareas moderno (filas o tarjetas por expediente, estados con color: verde = recibido/completo, ámbar = pendiente/incompleto); el simulador, reconocible al instante como una conversación de WhatsApp (burbujas verdes y blancas), sin usar logos oficiales.
- **Colores / sensación:** blanco, gris y azul marino; tipografía clara y compacta — el gerente lo verá a veces desde el móvil.

### 6. Cómo sabré que funciona

- [ ] El flujo completo (Reclamar → conversación → documento recibido → expediente completo → contadores suben) se reproduce en menos de 1 minuto sin explicar nada.
- [ ] Funciona igual en el móvil que en el ordenador.
- [ ] El botón "reiniciar demo" deja todo listo para repetir el flujo.
- [ ] Todos los datos parecen de una gestoría real: clientes, trámites y documentos con nombre y apellidos.
- [ ] La URL carga rápido a la primera.

---

## Las 3 reglas de dirección

1. **Una petición = un cambio.** El brief inicial se entrega entero; a partir de la primera versión, cada mensaje pide UNA sola cosa.
2. **Probar entre pasos.** Antes de pedir lo siguiente, prueba tú lo construido como lo usaría tu cliente. Lo que no has probado, no existe.
3. **Los errores se pegan, no se pelean.** ¿Mensaje de error? Cópialo entero, pégaselo a Claude Code y pídele que lo arregle. Es información, no un examen.
