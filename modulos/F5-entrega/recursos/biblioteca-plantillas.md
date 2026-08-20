# Biblioteca de plantillas

> Recurso de L7 (F5 Entrega). La estructura de tu plantilla personal (los 4 activos por proyecto), el ritual post-entrega de 30 minutos que la alimenta y el inventario de tu biblioteca. Las `[PLANTILLAS AILINK]` del programa te dan el arranque; esta biblioteca, alimentada entrega a entrega, te da el negocio. Crea hoy la carpeta `mi-biblioteca/`.

---

## 1 | Estructura de una plantilla propia

Una carpeta por combinación nicho + solución. Ejemplo (ilustrativo):

```
mi-biblioteca/
└── chatbot-citas-clinicas/
    ├── repo-plantilla/              ← el repo LIMPIO del proyecto
    ├── brief-tipo.md                ← el brief final, con huecos
    ├── checklist-entrega.md         ← la checklist de L5 + casos límite del nicho
    ├── atascos-y-soluciones.md
    └── mensajes-que-funcionan.md
```

### repo-plantilla/
Copia del repo del proyecto **sin rastro del cliente**: fuera datos reales, credenciales, accesos y nombres; en su lugar, marcadores tipo `[DATOS_CLIENTE]`, `[API_KEY]`, `[NOMBRE_NEGOCIO]`. Con el CLAUDE.md actualizado (qué es la solución, cómo se despliega, qué integraciones lleva). Regla fija: **lo que es del cliente se queda con el cliente** — su solución entregada es suya al pago completo (acuerdo de L2) y sus datos no salen de su proyecto; tu plantilla guarda el CÓMO, nunca lo suyo.

### brief-tipo.md
El brief final del proyecto (plantilla de F2-L3 con las secciones de producción de L3) con los campos del cliente vaciados. El siguiente cliente del nicho no parte de un folio en blanco: rellena huecos en la llamada de arranque.

### checklist-entrega.md
Tu copia de la checklist de entrega de L5, ampliada con los casos límite ESPECÍFICOS del nicho que descubriste en el QA (qué pregunta rara hacen los pacientes, qué formato de factura rompe el flujo…). Es la parte de la plantilla que más valor gana con cada entrega.

### atascos-y-soluciones.md

| Atasco | Cuánto costó | Solución | Nota para la próxima vez |
|---|---|---|---|
| (ej. ilustrativo) el proveedor de WhatsApp rechazaba el webhook | media tarde | validar la URL con el paso a paso que me dio Claude Code | hacerlo ANTES de conectar datos reales |

### mensajes-que-funcionan.md
Los toques diarios de L4 que mejor respuesta generaron (el mensaje de arranque, el Loom que provocó el "qué pasada", el aviso de atasco que calmó al cliente), copiados literales y listos para adaptar en el siguiente build.

---

## 2 | El ritual post-entrega: 30 minutos

Se hace en los 3 días siguientes a la entrega — ideal, el día siguiente, con todo fresco. **Lo que no entra en la biblioteca en esos 3 días, no entra nunca.**

| Minutos | Paso | Cómo |
|---|---|---|
| 0-10 | Repo limpio | Pídele a Claude Code: "crea una copia plantilla de este repo: elimina datos, credenciales y referencias al cliente, sustitúyelos por marcadores y actualiza el CLAUDE.md". Después **revisa tú a mano** que no queda nada del cliente — la máquina ayuda; la responsabilidad es tuya |
| 10-15 | Brief tipo | Duplica el brief final y vacía los campos del cliente dejando los huecos con nombre |
| 15-20 | Checklist del nicho | Añade a tu copia de la checklist de L5 los casos límite nuevos que aparecieron en el QA |
| 20-25 | Atascos | Anota los 1-3 atascos del build con su solución en la tabla |
| 25-30 | Mensajes + inventario | Copia los 2-3 mensajes con mejor respuesta y actualiza la fila del inventario |

---

## 3 | Inventario de mi biblioteca

Mantenlo al principio de `mi-biblioteca/` (un `INVENTARIO.md` o una hoja de cálculo). Una fila por plantilla:

| Nicho | Solución | Veces reutilizada | Tiempo del último build | Última actualización |
|---|---|---|---|---|
| (ej. ilustrativo) clínicas dentales | chatbot de citas por WhatsApp | 2 | 3 días | — |
|  |  |  |  |  |

La columna que tiene que bajar es **tiempo del último build**; la que tiene que subir, **veces reutilizada**. Si una plantilla lleva meses sin reutilizarse, no es un fracaso: es información para F1 (qué ofertas repites y cuáles no).

---

## 4 | Cómo se usa con el siguiente cliente

1. **En la llamada de arranque (L2):** el brief tipo del nicho se rellena en vivo — transmite oficio y ahorra media llamada.
2. **En el build (L3):** no empiezas de cero: empiezas de `repo-plantilla/` y le pides a Claude Code que lo adapte con los datos del nuevo cliente. Los atascos conocidos ya no son atascos.
3. **En la entrega (L5):** el QA usa la checklist del nicho, que ya conoce sus casos límite.
4. **Después de entregar:** ritual de 30 minutos otra vez. La plantilla es un ser vivo: cada reutilización la mejora y el build siguiente baja de días.
