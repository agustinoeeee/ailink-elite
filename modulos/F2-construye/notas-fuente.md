# F2 | Construye — Notas de fuente

> Solo para uso interno de Agustín.

## Qué es este módulo respecto al curso fuente

**F2 es el módulo REEMPLAZAR de la Biblia**: el equivalente estructural de "Meta Ads Mastery" (el flagship de Owen, "vale más que el curso entero"), pero con OTRA habilidad core: construir con Claude Code en vez de comprar tráfico. Del curso fuente solo se hereda:

| Herencia estructural | De dónde viene | Cómo se aplica aquí |
|---|---|---|
| Esqueleto de módulo flagship: filosofía → flujo → componentes → build en directo → disciplina de testeo → benchmarks | Bloque 5 (estructura de Meta Ads Mastery) | L1 filosofía · L2-L3 fundamentos · L4 componentes/catálogo · L5 build en directo · L6 testeo · L7 activo final |
| "El creativo es el 80%" → aquí "el brief es el 80%" | Bloque 5.3 | L3: la calidad del output = calidad del brief |
| Builds en directo como formato didáctico | Bloques 12.4 (live buildouts) | L5 con bloques [DEMO:] |
| Disciplina de testeo / no enseñar nada roto | Bloque 4 (pitfall 6: fallos técnicos) | L6 + checklist pre-demo |
| "Snapshots" copy-paste | Bloque 7 (snapshots GHL) | Plantillas AILINK (repos base) — **pendientes de construir** |

**Todo el contenido técnico (Claude Code, stack, catálogo por dentro, briefs) es creación original de este proyecto**, no de la transcripción.

## Decisiones de diseño tomadas (validar en tu auditoría)

1. **"Todo web en F2"**: la demo vive en una URL; las integraciones reales (WhatsApp Business API, telefonía) se posponen a F5 con el primer piloto pagado. Motivo: la verificación de Meta Business en la semana 4 ahogaría a alumnos no técnicos, y la demo web simula el flujo y vende igual.
2. **Stack propuesto (BORRADOR)**: Claude Code + GitHub + Vercel + Supabase. Elegido por: capa gratuita suficiente para demos, deploy en un paso, y es el stack que Claude Code maneja con más soltura. **Si usas otro en AILINK VIP, dilo y se cambia en L2/L4/R1.**
3. **Primera demo recomendada**: recepcionista/recuperación de citas o chatbot web cualificador (máximo efecto visual, mínima complejidad) — coherente con la demo dental de F1-L7.
4. **El vídeo-demo de respaldo** (L7): red de seguridad para llamadas de venta. Idea propia, no de la fuente.
5. **Demos conversacionales = conversación GUIADA en F2** (decidido en la ronda de corrección, 20/08): las demos de recepcionista IA y chatbot cualificador usan botones/respuestas sugeridas — sin backend de API de Anthropic, sin coste extra, y no se rompen con entradas libres. El **chat libre real** (API de Anthropic, coste por uso) llega en F5 con el piloto pagado, repercutido al cliente como coste operativo. Motivo: mantener la promesa de coste de F2 ("una suscripción y cuentas gratuitas") y no meter gestión de claves de API a un no-técnico en la semana 4. **Validar si prefieres otra línea.**

## Pendientes que SOLO tú puedes resolver

1. **Las plantillas AILINK (repos base por solución)**: los guiones las referencian como `[PLANTILLAS AILINK: pendientes]`. Hay que construirlas de verdad — **puedo generarlas yo** (repo por solución del catálogo con CLAUDE.md, estructura y datos de ejemplo) como fase aparte del proyecto si me das el OK.
2. **`[PRUEBA SOCIAL]` de L5**: tu experiencia real ("mi tercera demo fue la primera decente" — pon tu anécdota real).
3. **Validar stack y costes orientativos** (mencionados como ~20€/mes con "consulta precios actuales").
4. **La demo dental de L5**: al grabarla, harás el build de verdad en cámara — el guion te da la estructura, el resultado real saldrá de tu build.
