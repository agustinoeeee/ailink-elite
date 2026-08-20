# Criterios de auditoría — F0 Bienvenido / Onboarding

Se corre cuando exista algo en `modulos/` para F0. Hoy la carpeta está vacía.

Fuente: `fuente/chunks/00-intro-mentalidad.txt` + este mapa + `01-BIBLIA.md` §F0.

F0 en la Biblia: kick-off call, mentalidad (señal/ruido, More/Better/New, pitfalls), expectativas de 90 días, setup básico. Semana 1.

## Pase 1 — Cobertura (¿está lo que tiene que estar?)

- [ ] Kick-off call: guion para Agustín (agenda, expectativas, reglas) + qué ve el alumno
- [ ] Mapa de los 90 días y desbloqueo evergreen (F0→F6, qué se abre cuándo)
- [ ] Lección “tienes todo lo que necesitas”
- [ ] Lección Señal vs ruido (90 días, no 12 semanas)
- [ ] Lección More / Better / New, citando a Hormozi
- [ ] Lección pitfalls, con ejemplos de AILINK (no roofing / Ads Manager como centro)
- [ ] Setup básico de semana 1 (mínimo: Claude Code + lo que la Biblia tenga cerrado)
- [ ] `notas-fuente.md` que separe B0 (para Agustín) de B1–B4 (alumno)
- [ ] Cada lección acaba en una ACCIÓN, no en “pasa al siguiente vídeo”
- [ ] Entregable de la semana 1 explícito en el README del módulo

## Pase 2 — Residuo Owen (si aparece, corte)

- [ ] Cero “curso gratis / YouTube / no hay link abajo”
- [ ] Cero 7.000 $ / pay-per-shown / $147 / GHL como stack del alumno
- [ ] Cero contractors, roofing, Angi, homeowners como ICP del alumno
- [ ] Cero “12 semanas” (son 90 días)
- [ ] Cero ASR sucio (“Alexi”, “Onland”, “paper shown”)
- [ ] El vídeo de intro de Owen NO está calcado como bienvenida del alumno

## Pase 3 — Alcance (lo que F0 NO debe hacer)

F0 se come el programa si se pone ambicioso. Fuera de F0:

- Matemática de pricing y rangos € del alumno → F1 (y la Biblia aún no está validada)
- Lista larga de nichos + worksheet de ICP → F1
- Tutorial de Claude Code / repos plantilla → F2
- Meta ads, VSL, warmup de página → F3
- Scripts de cierre / objeciones → F4
- Two tracks, onboarding de CLIENTE → F5
- Retención, referidos, CEO dashboard → F6
- Fundamental Flow completo (26 k palabras en chunk 08). Biblia: **versión ligera** en F0 (como mucho: “una variable por test” + validez 300/30, una tarjeta). El resto es F6.

## Pase 4 — Coherencia con preguntas abiertas

Hasta que Agustín cierre Checkpoint 1:

- Promesa +10K€: si se menciona, debe quedar **tal cual está en la Biblia hoy**, o marcada `PENDIENTE-AGUSTIN`. No convertirla en “+10K€/mes” ni en “10K€ totales” por libre.
- Rangos piloto/proyecto/retainer: **no en materiales de alumno de F0**. Se diseñan en F1.
- Stack: F0 solo pide lo mínimo para semana 1. No prescribir Vercel/Supabase/WhatsApp API como si estuviera cerrado.
- Comunidad semanal: si Claude la asume, tiene que ser condicional. Si no está decidida, F0 no puede prometer “llamada cada martes”.

## Cómo entrego yo la auditoría

Archivo: `_grok/auditorias/F0.md`

Formato:

```
VEREDICTO: OK / OK CON CORTES / REHACER
Cortes (archivo + línea de ataque)
Contradicciones con Biblia
Residuo Owen
Lo que falta
Lo que sobra (alcance)
```

No reescribo `guion.md`. Claude aplica o discute.
