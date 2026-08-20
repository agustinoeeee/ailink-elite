# Checklist de setup del stack

> Recurso de L2 (F2 Construye). Complétala en orden, de arriba abajo, sin saltarte casillas: cada paso asume el anterior. Tiempo total estimado: **una tarde (2-3 horas)**, la mayoría de espera tranquila mientras las cosas se instalan o construyen. No memorices nada — para eso existe esta hoja. No la cierres hasta marcar la última casilla.

## Checklist secuencial

- [ ] **1. Cuenta de Claude** *(~10 min)* — Regístrate en la web oficial de Claude con el email de tu negocio y activa la suscripción. Coste orientativo: en torno a 20€/mes — consulta precios actuales antes de contratar.
- [ ] **2. Instalar Claude Code** *(~15-30 min)* — Desde la página oficial de Claude Code, sigue el instalador para tu sistema:
  - **macOS:** abre el terminal (búscalo con Spotlight: "Terminal") y sigue los pasos de instalación de la página oficial para macOS.
  - **Windows:** abre el terminal (búscalo en Inicio: "Terminal" o "PowerShell") y sigue los pasos de la página oficial para Windows.
  - Usa SOLO la fuente oficial: los tutoriales de terceros caducan; el instalador oficial no.
- [ ] **3. Verificar que responde** *(~5 min)* — Arranca Claude Code: escribe `claude` en el terminal y pulsa Enter — es la orden que el instalador oficial te indica al terminar; si allí figura otra, usa esa. Inicia sesión con tu cuenta de Claude y escríbele en español: preséntate y pregúntale qué puede hacer por ti. Si te responde con sentido, está vivo. ✅
- [ ] **4. Cuenta de GitHub** *(~10 min)* — Regístrate en GitHub con el email de tu negocio. GitHub es donde vive tu código: tu repositorio, tu copia de seguridad y el historial de cambios de cada proyecto. Capa gratuita: suficiente para todo F2.
- [ ] **5. Cuenta de Vercel** *(~10 min)* — Regístrate en Vercel eligiendo la opción de entrar **con tu cuenta de GitHub**: quedan conectadas desde el primer día. Vercel es donde harás el deploy: publicar tu web en una URL pública. Capa gratuita: suficiente para tus demos.
- [ ] **6. "Hola mundo" desplegado** *(~30-60 min)* — Abre Claude Code y pégale esta orden, sustituyendo los corchetes por lo tuyo:

  > Crea una página web sencilla de una sola pantalla con el nombre de mi agencia, "[NOMBRE DE TU AGENCIA]", y el texto "Soluciones de IA para [TU NICHO]". Diseño limpio y profesional. Cuando esté lista, súbela a GitHub y despliégala en Vercel para que tenga una URL pública. Si necesitas que yo haga algo (iniciar sesión, dar un permiso), guíame paso a paso.

  Claude Code te pedirá permisos y algún inicio de sesión por el camino: léelos y confirma. Al terminar te dará una URL — ábrela en el ordenador **y en tu móvil**.
- [ ] **7. URL publicada en la comunidad** *(~5 min)* — Comparte tu URL en el hilo de la comunidad indicado en la lección. Es el KPI de L2 y tu primer "míralo funcionar" público.

## Si algo falla

**Instrucción universal, válida para el 90% de los casos:** copia el mensaje de error COMPLETO (entero, aunque no entiendas nada — precisamente porque no necesitas entenderlo) y pégaselo a Claude Code con: *"Esto ha fallado. Explícame qué pasa en lenguaje sencillo y arréglalo."* Pelearte tú con el error es el camino largo; pegárselo es la habilidad.

Los 5 atascos típicos:

1. **"Acabo de instalar y el terminal no reconoce Claude Code."** Cierra el terminal del todo, ábrelo de nuevo y vuelve a intentarlo — tras una instalación, el terminal necesita reiniciarse para enterarse. Si persiste, repasa la página oficial de instalación por si quedó un paso a medias.
2. **"El sistema bloquea el instalador o pide permisos."** macOS y Windows desconfían por defecto de software recién descargado. Si lo has bajado de la página oficial, autoriza desde el propio aviso del sistema (o desde los ajustes de seguridad si el aviso ya se cerró) y continúa.
3. **"El inicio de sesión no funciona."** Normalmente es una de dos: el navegador abrió una cuenta distinta de la que tiene la suscripción (cierra sesión en el navegador y entra con la buena) o el proceso se quedó a medias (ciérralo y vuelve a intentar el inicio de sesión desde Claude Code).
4. **"Claude Code dice que has alcanzado el límite de uso."** No es un fallo: los planes tienen límites por franjas. Espera a que se restablezca — el propio mensaje te dice cuándo — y continúa donde estabas.
5. **"Falta una herramienta (git u otra) o el login de GitHub/Vercel se queda colgado."** Si falta algo, acepta la instalación que proponga el sistema o pídele a Claude Code que te guíe. Si un login se atasca, ciérralo y repítelo desde el principio.

¿Y si el atasco es tan temprano que Claude Code ni arranca? Misma jugada en otra ventanilla: pega el error en el chat de Claude del navegador (tu cuenta del paso 1 ya te da acceso) y pide diagnóstico y solución paso a paso.

## Costes orientativos del stack

| Pieza | Papel | Coste orientativo |
|---|---|---|
| Claude (suscripción) | Claude Code, tu constructor | ~20€/mes |
| GitHub | Guarda tu código (repositorios) | Capa gratuita suficiente |
| Vercel | Publica tus webs (deploy a URL) | Capa gratuita solo para uso no comercial; para enseñar demos a clientes es probable que toque su plan de pago — consulta condiciones actuales |
| Supabase | Datos, cuando una solución lo necesite — normalmente en el piloto real (F5) | Capa gratuita suficiente |

> Cifras **orientativas** a fecha de producción del programa: **consulta precios actuales** en las webs oficiales antes de contratar. Las capas gratuitas cubren de sobra la fase de demos — con la salvedad de Vercel (ver su fila); los demás límites solo importarán con clientes reales, y eso se resuelve en F5.

---

**Setup completado el (fecha):** ______________________ · **Mi URL:** ______________________
