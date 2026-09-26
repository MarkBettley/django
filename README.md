# Python, Django y Data - Portfolio

Repositorio de proyectos y ejercicios desarrollados durante mi formacion en Backend Python, Django y analisis de datos.

El repositorio integra desarrollo backend, APIs REST, procesamiento de datos, visualizacion, web scraping y procesamiento distribuido con PySpark.

## Proyectos principales

### Django y Django REST Framework

Aplicacion Django con gestion de productos y ventas.

Incluye:

- Modelos relacionales con Django ORM.
- CRUD de productos mediante Class Based Views.
- Registro e inicio de sesion de usuarios.
- Vistas protegidas mediante LoginRequiredMixin.
- API REST CRUD.
- Django REST Framework.
- ModelSerializer y ModelViewSet.
- Paginacion de resultados.
- Autenticacion mediante tokens.
- Endpoint de perfil para usuarios autenticados.
- SQLite para persistencia local.

### Dashboard financiero de e-commerce

Dashboard interactivo para analizar ventas, costos, utilidad y margen de un conjunto de datos de comercio electronico.

Tecnologias:

- Python
- Pandas
- Dash
- Plotly

El dashboard permite filtrar informacion por rango de fechas y categorias y visualizar indicadores financieros y graficas.

### Analisis de ventas con PySpark

Procesamiento de datos de ventas utilizando Apache Spark mediante PySpark.

El analisis incluye:

- Total de ventas.
- Ingresos y costos.
- Utilidad.
- Venta promedio.
- Agrupacion por categoria.
- Productos con mayores ingresos.

### Sistema de recomendacion con PySpark

Sistema de recomendacion de productos basado en similitud de categoria, palabras del titulo y proximidad de precio.

Los productos reciben una puntuacion y se ordenan para obtener las recomendaciones mas relacionadas.

### Web Scraping

Extraccion automatizada de informacion de productos utilizando Requests y BeautifulSoup.

Se obtienen datos como:

- Titulo.
- Precio.
- Disponibilidad.
- Categoria.
- Rating.
- UPC.

Los datos tambien pueden exportarse a CSV para su posterior procesamiento.

### Blockchain con Python

Implementacion educativa de una blockchain utilizando programacion orientada a objetos.

Incluye wallets, transacciones, bloques, hashes SHA-256, encadenamiento de bloques y validacion de integridad.

## Jupyter Notebooks

El repositorio tambien contiene notebooks sobre:

- Fundamentos de Django.
- Views y Class Based Views.
- Templates y Forms.
- Models y Django Admin.
- Introduccion a REST.
- Django REST Framework.
- Autenticacion en Django REST Framework.
- Paginacion.
- Web Scraping.
- PySpark.
- Visualizacion de datos.
- Blockchain con Python.

## Tecnologias

- Python
- Django
- Django REST Framework
- SQLite
- Pandas
- PySpark
- Dash
- Plotly
- Requests
- BeautifulSoup
- Jupyter Notebook
- Git y GitHub

## Instalacion

Clonar el repositorio e instalar las dependencias:

    git clone https://github.com/MarkBettley/django.git
    cd django
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Ejecutar Django

Aplicar las migraciones:

    python manage.py migrate

Iniciar el servidor:

    python manage.py runserver

La aplicacion estara disponible en:

    http://127.0.0.1:8000/

## API

Entre los endpoints implementados se encuentran:

- `/api/products/` - API CRUD de productos.
- `/api/viewset/products/` - API mediante Django REST Framework ViewSet.
- `/api/token/` - obtencion de token de autenticacion.
- `/api/profile/` - perfil del usuario autenticado.

## Ejecutar proyectos de Data

Dashboard financiero:

    python dashboard_financiero.py

Analisis de ventas con PySpark:

    python pyspark_ventas.py

Sistema de recomendacion:

    python pyspark_recomendador.py

Web scraping:

    python web_scraping.py

Blockchain:

    python blockchain_python.py

## Autor

Marco Antonio Hernandez Banos

Psicologia y Neuropsicologia | Software Development | Data & AI
