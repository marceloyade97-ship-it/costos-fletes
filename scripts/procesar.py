import csv
with open('data/fletes.csv', encoding='utf-8') as f:
    filas = [r for r in csv.DictReader(f) if r['km'] and r['costo_km']]
total = 0
with open('reporte_costos.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['fecha', 'ruta', 'unidad', 'km', 'costo_km', 'costo_total'])
    for r in filas:
        costo = float(r['km']) * float(r['costo_km'])
        total += costo
        w.writerow([r['fecha'], r['ruta'], r['unidad'], r['km'], r['costo_km'], round(costo, 2)])
print('Viajes procesados:', len(filas))
print('Costo total de fletes (S/):', round(total, 2))