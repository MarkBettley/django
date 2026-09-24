from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    count,
    desc,
    round,
    sum,
)


def analizar_ventas():
    spark = (
        SparkSession.builder
        .appName("AnalisisVentasEcommerce")
        .master("local[*]")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    ventas = spark.read.csv(
        "ventas_ecommerce.csv",
        header=True,
        inferSchema=True,
    )

    print("\n=== ANÁLISIS DE VENTAS DEL E-COMMERCE ===")

    print("\n1. Total de ventas registradas:")
    print(ventas.count())

    resumen = ventas.agg(
        round(sum("ingresos"), 2).alias(
            "ingresos_totales"
        ),
        round(sum("costo"), 2).alias(
            "costos_totales"
        ),
        round(sum("utilidad"), 2).alias(
            "utilidad_total"
        ),
        round(avg("ingresos"), 2).alias(
            "venta_promedio"
        ),
    )

    print("\n2. Resumen financiero:")
    resumen.show()

    por_categoria = (
        ventas.groupBy("categoria")
        .agg(
            count("*").alias("ventas"),
            sum("unidades").alias(
                "unidades_vendidas"
            ),
            round(
                sum("ingresos"), 2
            ).alias("ingresos"),
            round(
                sum("utilidad"), 2
            ).alias("utilidad"),
        )
        .orderBy(desc("ingresos"))
    )

    print("\n3. Ventas por categoría:")
    por_categoria.show()

    productos = (
        ventas.groupBy("producto")
        .agg(
            sum("unidades").alias(
                "unidades_vendidas"
            ),
            round(
                sum("ingresos"), 2
            ).alias("ingresos"),
        )
        .orderBy(desc("ingresos"))
    )

    print("\n4. Productos con mayores ingresos:")
    productos.show(10, truncate=False)

    print("\n5. Esquema de los datos:")
    ventas.printSchema()

    spark.stop()


if __name__ == "__main__":
    analizar_ventas()
