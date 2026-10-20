import csv

archivos = [
    "vendas_2025_cuadrimestre1.csv",
    "vendas_2025_cuadrimestre2.csv",
    "vendas_2025_cuadrimestre3.csv"
]

total_ventas = 0
total_unidades = 0

for archivo in archivos:
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=";")

        for venta in lector:
            total_ventas += 1
            total_unidades += int(venta["unidades"])

print("Número total de ventas:", total_ventas)
print("Total de unidades vendidas:", total_unidades)