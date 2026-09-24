import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
LIST_URL = urljoin(
    BASE_URL,
    "catalogue/page-1.html",
)


def obtener_links_productos():
    response = requests.get(
        LIST_URL,
        timeout=10,
    )
    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )

    productos = soup.select(
        "article.product_pod h3 a"
    )

    links = []

    for producto in productos:
        link = producto.get("href")

        links.append(
            urljoin(LIST_URL, link)
        )

    return links


def obtener_producto(url):
    response = requests.get(
        url,
        timeout=10,
    )
    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )

    titulo = soup.select_one(
        "div.product_main h1"
    ).get_text(strip=True)

    precio_texto = soup.select_one(
        "p.price_color"
    ).get_text(strip=True)

    precio_texto = precio_texto.replace(
        "Â",
        "",
    )

    precio = float(
        precio_texto.replace("£", "")
    )

    categoria = soup.select(
        "ul.breadcrumb li a"
    )[-1].get_text(strip=True)

    rating_element = soup.select_one(
        "p.star-rating"
    )

    rating = rating_element.get(
        "class"
    )[-1]

    return {
        "titulo": titulo,
        "categoria": categoria,
        "precio": precio,
        "rating": rating,
        "url": url,
    }


def crear_csv():
    links = obtener_links_productos()

    productos = []

    print(
        f"Productos encontrados: {len(links)}"
    )

    for numero, link in enumerate(
        links,
        start=1,
    ):
        producto = obtener_producto(link)

        producto["id"] = numero

        productos.append(producto)

        print(
            f"{numero}. "
            f"{producto['titulo']}"
        )

    with open(
        "productos.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as archivo:
        campos = [
            "id",
            "titulo",
            "categoria",
            "precio",
            "rating",
            "url",
        ]

        writer = csv.DictWriter(
            archivo,
            fieldnames=campos,
        )

        writer.writeheader()
        writer.writerows(productos)

    print(
        "\nCSV productos.csv "
        "creado correctamente."
    )


if __name__ == "__main__":
    crear_csv()
