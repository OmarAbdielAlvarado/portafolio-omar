import glob, os
from clickhouse_driver import Client
ch = Client(os.environ.get('CH_HOST','localhost'), database='qsoy',
            user=os.environ.get('CH_USER','default'), password=os.environ['CH_PASS'])
R = os.path.expanduser('~/proyectos/QSoy2')
py = [f for f in glob.glob(f'{R}/**/*.py', recursive=True)+glob.glob(f'{R}/**/*.sh', recursive=True) if 'venv' not in f and '9_basura' not in f]
loc = sum(len(open(f, errors='ignore').readlines()) for f in py)
tablas = ch.execute("SELECT name, total_rows FROM system.tables WHERE database='qsoy' ORDER BY total_rows DESC")
print(f"SCRIPTS: {len(py)} | LINEAS: {loc}")
print(f"TABLAS: {len(tablas)} | REGISTROS: {sum(t[1] or 0 for t in tablas):,}")
