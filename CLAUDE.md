# Instrucciones para Claude en este repositorio

Esto es **AILINK Élite**, un programa high ticket de 90 días que enseña a vender soluciones de IA hechas con Claude Code a negocios españoles. Lee `README.md` para el mapa; aquí están las reglas que hay que respetar al tocar cualquier cosa.

## La jerarquía de autoridad

1. **`01-BIBLIA.md`** manda sobre todo lo demás. Promesa, modelo de negocio, precios, glosario, reglas de España y RGPD.
2. **`02-INDICE-MAESTRO.md`** dice qué existe y qué está pendiente.
3. El `00-plan-modulo.md` de cada módulo es el contrato de esa pieza.

Si encuentras una contradicción entre un documento y la Biblia, gana la Biblia y se corrige el documento — no al revés. Si la Biblia no cubre el caso, se añade allí primero y luego se propaga a todos los módulos afectados.

## Idioma

**Español de España, tuteo.** Nada de español neutro ni giros latinoamericanos.

Se quedan en inglés: hook, funnel, retainer, close rate, show rate, pipeline, onboarding, kick-off, lead, no-show, MRR, save/reset/exit call, proof-of-work.

**Prohibidos** (el glosario completo está en la Biblia):

| No se dice | Se dice |
|---|---|
| prospect / prospecto | lead · el dueño |
| follow-up | seguimiento |
| handoff | traspaso |
| fulfillment | entrega |
| wording | palabras |
| info-bomb | bomba de información |
| tie-down | amarre |
| mock call | llamada de práctica |
| reps | repeticiones |

Tampoco: «aplicar» en intransitivo («aplicar al programa»), «andando», «no ser tema», «marcaciones».

## Reglas de contenido

- **Los rangos de precio solo se enseñan en F1.** Ningún otro módulo los cita.
- **Nada marcado `⛔ NO PUBLICAR` llega al alumno**: guiones, `kpis.md`, `notas-fuente.md`, `00-plan-modulo.md`, los briefs de `diseno/` y `modulos/F0-bienvenido/guia-interna-operador.md`.
- **`[BORRADOR]` significa sin validar.** Son cifras que solo puede cerrar Agustín. No se dan por buenas, no se maquetan y nunca aparecen dentro del copy de una pizarra: ahí va la versión cualitativa («la parte restante», no «el 50% restante»).
- **La promesa es una y literal:** +5.000€ de facturación acumulada al final de los 90 días (total, no mensual), y para cumplirla bastan 1-3 clientes.

## Estándares de cada pieza

| Pieza | Dónde está su estándar |
|---|---|
| Guion de vídeo (`modulos/F*/guiones/L*.md`) | `01-BIBLIA.md` — gancho, secciones, cierre con acción y KPI, `[PANTALLA]`, 600-1.200 palabras |
| Guion de diapositivas (`modulos/F*/pizarras/L*.md`) | `diseno/02-ESTANDAR-GUION-DIAPOS.md` — `## D1, D2…` correlativas, `> PANTALLA REAL` sin numerar, 4-8 diapos |
| Recurso del alumno (`modulos/F*/recursos/*.md`) | `diseno/00-SISTEMA-VISUAL.md` para su versión en PDF |
| Descripción de lección en Skool | `skool/contenido-skool.json` — no se edita el HTML, se edita el JSON y se regenera |

## Lo que se genera, no se edita a mano

- `skool/aula-ailink.html` y `aula-ailink-web.html` → `cd skool && python3 build.py`
- `adjuntos-skool/`, `pizarras-grabacion/`, los `_LEEME.md` y `skool/estado-adjuntos.json` → `python3 herramientas/componer.py`

Si editas uno de esos archivos a mano, el siguiente `build` o `componer` se lo lleva por delante. Toca la fuente: el JSON o el script.

## Al terminar un cambio transversal

Si cambias una cifra, un término o una decisión que aparece en varios sitios, **búscala en todo el repo antes de dar el trabajo por hecho** y actualiza también la Biblia y el índice maestro. Los módulos se escribieron en paralelo: la coherencia no se mantiene sola.
