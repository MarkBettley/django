from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("SistemaRecomendacionProductos")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")


productos = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("productos.csv")
)


def getRelatedProducts(producto):
    producto_actual = (
        productos
        .filter(F.col("id") == producto)
        .first()
    )

    if producto_actual is None:
        print(
            f"No existe un producto con ID {producto}"
        )
        return None

    id_actual = producto_actual["id"]
    titulo_actual = producto_actual["titulo"]
    categoria_actual = producto_actual["categoria"]
    precio_actual = producto_actual["precio"]

    palabras_titulo = [
        palabra.lower()
        for palabra in titulo_actual.split()
        if len(palabra) > 3
    ]

    relacionados = productos.filter(
        F.col("id") != id_actual
    )

    relacionados = relacionados.withColumn(
        "puntos_categoria",
        F.when(
            F.col("categoria") == categoria_actual,
            5,
        ).otherwise(0),
    )

    condicion_palabras = F.lit(False)

    for palabra in palabras_titulo:
        condicion_palabras = (
            condicion_palabras
            | F.lower(
                F.col("titulo")
            ).contains(palabra)
        )

    relacionados = relacionados.withColumn(
        "puntos_titulo",
        F.when(
            condicion_palabras,
            3,
        ).otherwise(0),
    )

    diferencia_precio = F.abs(
        F.col("precio") - F.lit(precio_actual)
    )

    relacionados = relacionados.withColumn(
        "puntos_precio",
        F.when(
            diferencia_precio <= 5,
            2,
        ).when(
            diferencia_precio <= 10,
            1,
        ).otherwise(0),
    )

    relacionados = relacionados.withColumn(
        "puntuacion",
        F.col("puntos_categoria")
        + F.col("puntos_titulo")
        + F.col("puntos_precio"),
    )

    relacionados = (
        relacionados
        .filter(
            F.col("puntuacion") > 0
        )
        .orderBy(
            F.desc("puntuacion"),
            F.asc(diferencia_precio),
        )
        .limit(5)
    )

    print("\nProducto seleccionado:")
    print(
        f"ID: {id_actual}"
    )
    print(
        f"Título: {titulo_actual}"
    )
    print(
        f"Categoría: {categoria_actual}"
    )
    print(
        f"Precio: £{precio_actual}"
    )

    print(
        "\nProductos relacionados:"
    )

    relacionados.select(
        "id",
        "titulo",
        "categoria",
        "precio",
        "puntuacion",
    ).show(
        truncate=False
    )

    return relacionados


if __name__ == "__main__":
    print("Productos disponibles:\n")

    productos.select(
        "id",
        "titulo",
        "categoria",
        "precio",
    ).show(
        20,
        truncate=False,
    )

    getRelatedProducts(1)

    spark.stop()
