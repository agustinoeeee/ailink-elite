#!/usr/bin/env python3
"""Convierte los .dc.html de Claude Design a PDF con Chrome headless.

    python3 herramientas/convertir.py "~/Desktop/AILINK Élite. Formación visual"

Los .dc.html no sirven como adjunto: dependen de la carpeta _ds/ que los
acompaña y se rompen en cuanto se mueven. Este script los rasteriza a PDF
respetando el formato de cada uno (A4 vertical, A4 horizontal o 16:9).
Los PDF salen a pdf-convertidos/, que es de donde los lee componer.py.
"""
import os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.expanduser(sys.argv[1]) if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/AILINK Élite. Formación visual')
OUT = os.path.join(RAIZ, 'pdf-convertidos')
PROF = os.path.join(OUT, '.perfil')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
if not os.path.isdir(SRC):
    sys.exit(f'No existe la carpeta de entrada: {SRC}')
os.makedirs(OUT, exist_ok=True)

archivos = sorted(f for f in os.listdir(SRC) if f.endswith('.dc.html'))

def convertir(par):
    i, f = par
    base = f[:-len('.dc.html')]
    destino = os.path.join(OUT, base + '.pdf')
    if os.path.exists(destino) and os.path.getsize(destino) > 8000:
        return (base, 'ya estaba', os.path.getsize(destino))
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--no-sandbox',
           f'--user-data-dir={PROF}{i % 4}', '--allow-file-access-from-files',
           '--no-pdf-header-footer', '--virtual-time-budget=10000',
           f'--print-to-pdf={destino}', 'file://' + os.path.join(SRC, f)]
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):                      # espera a que aparezca el PDF
        time.sleep(1)
        if os.path.exists(destino) and os.path.getsize(destino) > 2000:
            time.sleep(2)
            break
    p.terminate()
    try: p.wait(timeout=5)
    except Exception: p.kill()
    if not os.path.exists(destino):
        return (base, 'FALLO', 0)
    d = open(destino, 'rb').read()
    pags = len(re.findall(rb'/Type\s*/Page[^s]', d))
    caja = re.search(rb'/MediaBox\s*\[([^\]]*)\]', d)
    return (base, f'{pags} pág · {caja.group(1).decode() if caja else "?"}', len(d))

with ThreadPoolExecutor(max_workers=4) as ex:
    for base, estado, size in ex.map(convertir, enumerate(archivos)):
        print(f'{base:42s} {estado:26s} {size//1024:5d} KB', flush=True)

subprocess.run(['pkill', '-f', 'headless=new'])
print('\nTERMINADO:', len(os.listdir(OUT)), 'PDF en', OUT)
