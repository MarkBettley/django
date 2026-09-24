import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)


productos = [
    {
        "producto": "Laptop Pro",
        "categoria": "Tecnología",
        "precio": 18500,
        "costo": 14000,
    },
    {
        "producto": "Smartphone X",
        "categoria": "Tecnología",
        "precio": 12500,
        "costo": 9000,
    },
    {
        "producto": "Audífonos Bluetooth",
        "categoria": "Tecnología",
        "precio": 1800,
        "costo": 950,
    },
    {
        "producto": "Monitor 24 pulgadas",
        "categoria": "Tecnología",
        "precio": 4200,
        "costo": 3000,
    },
    {
        "producto": "Silla Ergonómica",
        "categoria": "Hogar",
        "precio": 4800,
        "costo": 3100,
    },
    {
        "producto": "Escritorio",
        "categoria": "Hogar",
        "precio": 3500,
        "costo": 2200,
    },
    {
        "producto": "Lámpara LED",
        "categoria": "Hogar",
        "precio": 650,
        "costo": 300,
    },
    {
        "producto": "Mochila",
        "categoria": "Accesorios",
        "precio": 1200,
        "costo": 600,
    },
    {
        "producto": "Reloj",
        "categoria": "Accesorios",
        "precio": 2300,
        "costo": 1200,
    },
    {
        "producto": "Tenis Deportivos",
        "categoria": "Ropa",
        "precio": 1900,
        "costo": 1000,
    },
    {
        "producto": "Playera",
        "categoria": "Ropa",
        "precio": 550,
        "costo": 220,
    },
    {
        "producto": "Sudadera",
        "categoria": "Ropa",
        "precio": 1100,
        "costo": 500,
    },
]


fecha_inicio = datetime(2026, 1, 1)
fecha_fin = datetime(2026, 9, 23)

dias = (fecha_fin - fecha_inicio).days

ventas = []


for numero in range(1, 301):
    producto = random.choice(productos)

    fecha = (
        fecha_inicio
        + timedelta(
            days=random.randint(0, dias)
        )
    )

    unidades = random.randint(1, 5)

    ingresos = (
        producto["precio"]
        * unidades
    )

    costo_total = (
        producto["costo"]
        * unidades
    )

    utilidad = (
        ingresos
        - costo_total
    )

    ventas.append(
        {
            "pedido_id": f"PED-{numero:04d}",
            "fecha": fecha.strftime("%Y-%m-%d"),
            "producto": producto["producto"],
            "categoria": producto["categoria"],
            "unidades": unidades,
            "precio_unitario": producto["precio"],
            "ingresos": ingresos,
            "costo": costo_total,
            "utilidad": utilidad,
        }
    )


df = pd.DataFrame(ventas)

df = df.sort_values(
    "fecha"
).reset_index(drop=True)

df.to_csv(
    "ventas_ecommerce.csv",
    index=False,
    encoding="utf-8",
)


print(
    "CSV creado: ventas_ecommerce.csv"
)

print(
    "Registros:",
    len(df),
)

print(
    "Desde:",
    df["fecha"].min(),
)

print(
    "Hasta:",
    df["fecha"].max(),
)

print(
    "Ingresos totales: $",
    f"{df['ingresos'].sum():,.2f}",
)

print(
    "Utilidad total: $",
    f"{df['utilidad'].sum():,.2f}",
)
