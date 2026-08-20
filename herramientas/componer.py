#!/usr/bin/env python3
"""Reparte los adjuntos por módulo y lección, listos para subir a Skool.

    python3 herramientas/componer.py

Lee el mapa de skool/contenido-skool.json (qué adjunto va en qué lección),
coge los PDF de pdf-convertidos/ y los CSV de entregables-listos/csv/, y
escribe adjuntos-skool/ (material del alumno) y pizarras-grabacion/ (material
de grabación). De paso genera el _LEEME.md de cada carpeta y el
skool/estado-adjuntos.json que la maqueta usa para sus sellos.

Regla clave: un adjunto se copia UNA sola vez en todo el programa, a la
lección donde aparece por primera vez, aunque lo reutilicen otros módulos.
"""
import json, os, re, shutil

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF  = os.path.join(RAIZ, 'pdf-convertidos')
CSV  = f'{RAIZ}/entregables-listos/csv'
DEST = f'{RAIZ}/adjuntos-skool'
PIZ  = f'{RAIZ}/pizarras-grabacion'

# Un nombre de CSV del mapa puede corresponder a varios ficheros reales.
CSVS = {
    'F0-plantilla-base-de-tests.csv': ['F0-plantilla-tests.csv'],
    'F3-tracker-captacion.csv': ['F3-matematica-actividad.csv', 'F3-tracker-email.csv',
        'F3-tracker-llamadas.csv', 'F3-tracker-linkedin.csv', 'F3-tracker-ads.csv',
        'F3-tracker-creativos.csv', 'F3-tracker-resumen-semanal.csv'],
    'F4-tracker-ventas.csv': ['F4-tracker-ventas.csv', 'F4-tracker-ventas-totales-semanales.csv'],
    'F6-dashboard-agencia.csv': ['F6-dashboard-agencia.csv', 'F6-decisiones-mes.csv'],
}
CARPETA = {'F0':'1-bienvenido','F1':'2-domina','F2':'3-construye','F3':'4-lanza',
           'F4':'5-cierra','F5':'6-entrega','F6':'7-escala'}

D = json.load(open(f'{RAIZ}/skool/contenido-skool.json', encoding='utf-8'))
# Se rehacen las subcarpetas, pero NO se toca el 00-LEEME.md de la raíz.
for d in (DEST, PIZ):
    os.makedirs(d, exist_ok=True)
    for sub in os.listdir(d):
        if os.path.isdir(f'{d}/{sub}'):
            shutil.rmtree(f'{d}/{sub}')

resumen, faltan, estado = [], [], {}
primera = {}   # nombre de adjunto -> (módulo, lección) donde se sube por primera vez, en TODO el programa

for m in D:
    cod, carp = m['codigo'], CARPETA[m['codigo']]
    dest = f'{DEST}/{carp}'; os.makedirs(dest, exist_ok=True)
    filas = []

    for i, l in enumerate(m['lecciones'], 1):
        for a in l['adjuntos']:
            nom, tipo = a['nombre'], a['tipo']
            if nom in primera:
                mod0, l0 = primera[nom]
                donde = f'L{l0}' if mod0 == cod else f'{mod0} · L{l0}'
                filas.append((i, l['titulo'], nom, tipo, f'ya subido en {donde}', ''))
                continue
            primera[nom] = (cod, i)
            pref = f'L{i:02d}'
            if tipo in ('Enlace', 'Formulario'):
                filas.append((i, l['titulo'], nom, tipo, 'enlace en la descripción, no es un archivo', ''))
                continue
            if tipo == 'CSV':
                reales = CSVS.get(nom, [nom])
                puestos = []
                for r in reales:
                    o = f'{CSV}/{r}'
                    if os.path.exists(o):
                        # el CSV mantiene su nombre real, con prefijo de lección
                        shutil.copy2(o, f'{dest}/{pref}-{r}'); puestos.append(f'{pref}-{r}')
                if puestos:
                    filas.append((i, l['titulo'], nom, tipo, 'listo', ' · '.join(puestos)))
                else:
                    filas.append((i, l['titulo'], nom, tipo, 'FALTA', ''))
                    faltan.append((cod, i, nom))
                continue
            # PDF
            base = nom[:-4]
            origen = f'{PDF}/{base}.pdf'
            if os.path.exists(origen):
                shutil.copy2(origen, f'{dest}/{pref}-{nom}')
                filas.append((i, l['titulo'], nom, tipo, 'listo', f'{pref}-{nom}'))
            else:
                filas.append((i, l['titulo'], nom, tipo, 'FALTA — sin diseñar', ''))
                faltan.append((cod, i, nom))

    # README del módulo
    hechos = sum(1 for f in filas if f[4] == 'listo')
    pend   = sum(1 for f in filas if f[4].startswith('FALTA'))
    plural = 'archivo listo' if hechos == 1 else 'archivos listos'
    out = [f'# {m["nombreCurso"]} — adjuntos por lección', '',
           f'> {m["semanas"]} · {len(m["lecciones"])} lecciones · {hechos} {plural}'
           + (f' · **{pend} pendientes de diseño**' if pend else ' · **completo**'), '',
           '| Lección | Adjunto | Archivo en esta carpeta | Estado |', '|---|---|---|---|']
    for i, tit, nom, tipo, est, arch in filas:
        estado[f'{cod}|{i}|{nom}'] = {'est': est, 'arch': arch, 'carp': carp}
        marca = {'listo': '✅', 'FALTA': '⛔', 'FALTA — sin diseñar': '⛔'}.get(est, '↩︎' if est.startswith('ya subido') else '🔗')
        out.append(f'| L{i} {tit} | {nom} | {arch or "—"} | {marca} {est} |')
    out += ['', '**Cómo se lee:** ✅ el archivo está aquí y se sube a esa lección · ↩︎ ya se subió antes, '
            'en la descripción se menciona con «(ya lo tienes en LX)» · 🔗 va como enlace en la descripción, '
            'no como adjunto · ⛔ falta por producir.']
    open(f'{dest}/_LEEME.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    resumen.append((cod, m['palabraTarjeta'], hechos, pend, len(os.listdir(dest)) - 1))

# Pizarras: material de grabación, carpeta aparte
npiz = 0
for f in sorted(os.listdir(PDF)):
    mo = re.match(r'(F\d)-L(\d+)-pizarra\.pdf$', f)
    if mo:
        sub = f'{PIZ}/{CARPETA[mo.group(1)]}'; os.makedirs(sub, exist_ok=True)
        shutil.copy2(f'{PDF}/{f}', f'{sub}/{mo.group(1)}-L{int(mo.group(2)):02d}-pizarra.pdf'); npiz += 1

json.dump(estado, open(f'{RAIZ}/skool/estado-adjuntos.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)

print(f'{"MÓD":4s} {"CURSO":12s} {"LISTOS":>7s} {"PEND":>5s} {"ARCHIVOS":>9s}')
for c, p, h, pe, n in resumen:
    print(f'{c:4s} {p:12s} {h:7d} {pe:5d} {n:9d}')
print(f'\nPizarras copiadas: {npiz}')
print(f'Faltan {len(faltan)} adjuntos:')
for c, i, n in faltan:
    print(f'  {c} L{i} — {n}')
