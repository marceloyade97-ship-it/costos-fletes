import csv, sys
with open('data/fletes.csv', encoding='utf-8') as f:
    filas = list(csv.DictReader(f))
incompletos = [r for r in filas if not r['km'] or not r['costo_km']]
print('Viajes leidos:', len(filas))
print('Viajes con datos incompletos:', len(incompletos))
for r in incompletos:
    print('  Observado:', r['fecha'], r['ruta'], r['unidad'])
if len(filas) == 0:
    sys.exit(1)
print('Validacion OK')