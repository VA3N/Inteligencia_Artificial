import csv

archivos = [
    "datos/raw/vendas_2025_cuadrimestre1.csv",
    "datos/raw/vendas_2025_cuadrimestre2.csv",
    "datos/raw/vendas_2025_cuadrimestre3.csv"
]
total_ventas = 0
total_unidades = 0



for archivo in archivos:
    ventas = 0
    unidades = 0

    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=";")

        for venta in lector:
            ventas += 1
            unidades += int(venta["unidades"])
    total_ventas += ventas
    total_unidades += unidades
        

print("Número total de ventas:", total_ventas)
print("Total de unidades vendidas:", total_unidades)