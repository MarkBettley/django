import pandas as pd
import plotly.express as px

from dash import (
    Dash,
    Input,
    Output,
    dcc,
    html,
)


# Cargar datos
df = pd.read_csv(
    "ventas_ecommerce.csv",
    parse_dates=["fecha"],
)


# Crear aplicación Dash
app = Dash(__name__)

app.title = "Dashboard Financiero eCommerce"


# Opciones del filtro de categorías
categorias = sorted(
    df["categoria"].unique()
)


# Diseño del dashboard
app.layout = html.Div(
    [
        html.H1(
            "Dashboard Financiero eCommerce",
            style={
                "textAlign": "center",
            },
        ),

        html.P(
            "Análisis de ventas, costos y utilidad",
            style={
                "textAlign": "center",
            },
        ),

        html.Hr(),

        # Filtros
        html.Div(
            [
                html.Div(
                    [
                        html.Label(
                            "Rango de fechas"
                        ),

                        dcc.DatePickerRange(
                            id="filtro-fecha",
                            min_date_allowed=(
                                df["fecha"].min()
                            ),
                            max_date_allowed=(
                                df["fecha"].max()
                            ),
                            start_date=(
                                df["fecha"].min()
                            ),
                            end_date=(
                                df["fecha"].max()
                            ),
                            display_format=(
                                "YYYY-MM-DD"
                            ),
                        ),
                    ],
                    style={
                        "width": "48%",
                        "display": "inline-block",
                    },
                ),

                html.Div(
                    [
                        html.Label(
                            "Categoría"
                        ),

                        dcc.Dropdown(
                            id="filtro-categoria",
                            options=[
                                {
                                    "label": categoria,
                                    "value": categoria,
                                }
                                for categoria
                                in categorias
                            ],
                            value=categorias,
                            multi=True,
                            placeholder=(
                                "Selecciona categorías"
                            ),
                        ),
                    ],
                    style={
                        "width": "48%",
                        "display": "inline-block",
                    },
                ),
            ],
            style={
                "padding": "20px",
            },
        ),

        # Indicadores financieros
        html.Div(
            [
                html.Div(
                    [
                        html.H4(
                            "Ingresos"
                        ),
                        html.H2(
                            id="kpi-ingresos"
                        ),
                    ],
                    style={
                        "width": "23%",
                        "display": "inline-block",
                        "textAlign": "center",
                        "border": (
                            "1px solid #ccc"
                        ),
                        "padding": "10px",
                        "margin": "5px",
                    },
                ),

                html.Div(
                    [
                        html.H4(
                            "Costos"
                        ),
                        html.H2(
                            id="kpi-costos"
                        ),
                    ],
                    style={
                        "width": "23%",
                        "display": "inline-block",
                        "textAlign": "center",
                        "border": (
                            "1px solid #ccc"
                        ),
                        "padding": "10px",
                        "margin": "5px",
                    },
                ),

                html.Div(
                    [
                        html.H4(
                            "Utilidad"
                        ),
                        html.H2(
                            id="kpi-utilidad"
                        ),
                    ],
                    style={
                        "width": "23%",
                        "display": "inline-block",
                        "textAlign": "center",
                        "border": (
                            "1px solid #ccc"
                        ),
                        "padding": "10px",
                        "margin": "5px",
                    },
                ),

                html.Div(
                    [
                        html.H4(
                            "Margen"
                        ),
                        html.H2(
                            id="kpi-margen"
                        ),
                    ],
                    style={
                        "width": "23%",
                        "display": "inline-block",
                        "textAlign": "center",
                        "border": (
                            "1px solid #ccc"
                        ),
                        "padding": "10px",
                        "margin": "5px",
                    },
                ),
            ],
            style={
                "textAlign": "center",
            },
        ),

        # Gráficas
        html.Div(
            [
                dcc.Graph(
                    id="grafica-ventas-tiempo"
                ),

                dcc.Graph(
                    id="grafica-categorias"
                ),

                dcc.Graph(
                    id="grafica-productos"
                ),

                dcc.Graph(
                    id="grafica-ingresos-utilidad"
                ),
            ]
        ),
    ],
    style={
        "fontFamily": "Arial",
        "margin": "30px",
    },
)


# Callback interactivo
@app.callback(
    [
        Output(
            "kpi-ingresos",
            "children",
        ),
        Output(
            "kpi-costos",
            "children",
        ),
        Output(
            "kpi-utilidad",
            "children",
        ),
        Output(
            "kpi-margen",
            "children",
        ),
        Output(
            "grafica-ventas-tiempo",
            "figure",
        ),
        Output(
            "grafica-categorias",
            "figure",
        ),
        Output(
            "grafica-productos",
            "figure",
        ),
        Output(
            "grafica-ingresos-utilidad",
            "figure",
        ),
    ],
    [
        Input(
            "filtro-fecha",
            "start_date",
        ),
        Input(
            "filtro-fecha",
            "end_date",
        ),
        Input(
            "filtro-categoria",
            "value",
        ),
    ],
)
def actualizar_dashboard(
    fecha_inicio,
    fecha_fin,
    categorias_seleccionadas,
):
    datos = df.copy()

    datos = datos[
        (
            datos["fecha"]
            >= pd.to_datetime(fecha_inicio)
        )
        & (
            datos["fecha"]
            <= pd.to_datetime(fecha_fin)
        )
    ]

    if categorias_seleccionadas:
        datos = datos[
            datos["categoria"].isin(
                categorias_seleccionadas
            )
        ]
    else:
        datos = datos.iloc[0:0]

    ingresos = datos["ingresos"].sum()
    costos = datos["costo"].sum()
    utilidad = datos["utilidad"].sum()

    if ingresos > 0:
        margen = (
            utilidad
            / ingresos
            * 100
        )
    else:
        margen = 0

    # Ventas por fecha
    ventas_tiempo = (
        datos.groupby(
            "fecha",
            as_index=False,
        )
        .agg(
            ingresos=(
                "ingresos",
                "sum",
            ),
            utilidad=(
                "utilidad",
                "sum",
            ),
        )
    )

    figura_tiempo = px.line(
        ventas_tiempo,
        x="fecha",
        y=[
            "ingresos",
            "utilidad",
        ],
        title=(
            "Evolución de ingresos "
            "y utilidad"
        ),
        labels={
            "value": "Monto ($)",
            "fecha": "Fecha",
            "variable": "Indicador",
        },
    )

    # Ventas por categoría
    ventas_categoria = (
        datos.groupby(
            "categoria",
            as_index=False,
        )["ingresos"]
        .sum()
        .sort_values(
            "ingresos",
            ascending=False,
        )
    )

    figura_categorias = px.bar(
        ventas_categoria,
        x="categoria",
        y="ingresos",
        title="Ingresos por categoría",
        labels={
            "categoria": "Categoría",
            "ingresos": "Ingresos ($)",
        },
    )

    # Productos más vendidos
    productos = (
        datos.groupby(
            "producto",
            as_index=False,
        )["unidades"]
        .sum()
        .sort_values(
            "unidades",
            ascending=False,
        )
        .head(10)
    )

    figura_productos = px.bar(
        productos,
        x="unidades",
        y="producto",
        orientation="h",
        title=(
            "Top 10 productos "
            "por unidades vendidas"
        ),
        labels={
            "producto": "Producto",
            "unidades": "Unidades",
        },
    )

    figura_productos.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    # Ingresos vs utilidad
    comparacion = (
        datos.groupby(
            "categoria",
            as_index=False,
        )
        .agg(
            ingresos=(
                "ingresos",
                "sum",
            ),
            utilidad=(
                "utilidad",
                "sum",
            ),
        )
    )

    figura_comparacion = px.scatter(
        comparacion,
        x="ingresos",
        y="utilidad",
        size="ingresos",
        text="categoria",
        title=(
            "Ingresos vs utilidad "
            "por categoría"
        ),
        labels={
            "ingresos": "Ingresos ($)",
            "utilidad": "Utilidad ($)",
        },
    )

    figura_comparacion.update_traces(
        textposition="top center"
    )

    return (
        f"${ingresos:,.2f}",
        f"${costos:,.2f}",
        f"${utilidad:,.2f}",
        f"{margen:.2f}%",
        figura_tiempo,
        figura_categorias,
        figura_productos,
        figura_comparacion,
    )


if __name__ == "__main__":
    app.run(debug=True)
