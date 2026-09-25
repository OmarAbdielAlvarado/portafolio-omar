import csv, glob, os
RAIZ = os.path.expanduser('~/proyectos/QSoy2/revisar')
import pathlib
files = [str(x) for x in pathlib.Path(RAIZ).rglob('*.csv')]
def es_real(p):
    head = open(p,'rb').read(400).lower()
    return b'<html' not in head and b'<!doctype' not in head
def col(hs, pats):
    for i,h in enumerate(hs):
        hl = h.strip().lower()
        if any(p in hl for p in pats): return i
    return -1
for f in sorted(files):
    if not es_real(f) or os.path.getsize(f) < 1024: continue
    try:
        with open(f, encoding='utf-8', errors='replace') as fh:
            r = csv.reader(fh); hs = next(r); n = sum(1 for _ in r)
        print(f"{n:>7} {os.path.relpath(f,RAIZ)}  N={col(hs,['nombre'])} P={col(hs,['paterno','primer apellido'])} M={col(hs,['materno','segundo apellido'])} RFC={col(hs,['rfc'])}")
    except Exception as e:
        print(f"ERROR {os.path.basename(f)}: {e}")
