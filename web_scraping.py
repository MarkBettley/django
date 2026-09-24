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

        url_completa = urljoin(
            LIST_URL,
            link,
        )

        links.append(url_completa)

    return links


def obtener_detalle_producto(url):
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

    precio = soup.select_one(
        "p.price_color"
    ).get_text(strip=True)

    # El sitio puede devolver un carácter extra
    # antes del símbolo de libra.
    precio = precio.replace("Â", "")

    disponibilidad = soup.select_one(
        "p.instock.availability"
    ).get_text(
        " ",
        strip=True,
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

    filas = soup.select(
        "table.table.table-striped tr"
    )

    upc = ""

    for fila in filas:
        encabezado = fila.select_one("th")
        valor = fila.select_one("td")

        if (
            encabezado
            and valor
            and encabezado.get_text(strip=True)
            == "UPC"
        ):
            upc = valor.get_text(strip=True)
            break

    return {
        "titulo": titulo,
        "precio": precio,
        "disponibilidad": disponibilidad,
        "categoria": categoria,
        "rating": rating,
        "upc": upc,
    }


def main():
    print(
        "Obteniendo links de productos..."
    )

    links = obtener_links_productos()

    print(
        f"Productos encontrados: {len(links)}"
    )

    print(
        "\nExtrayendo primeros 5 productos...\n"
    )

    for numero, link in enumerate(
        links[:5],
        start=1,
    ):
        producto = obtener_detalle_producto(
            link
        )

        print(f"Producto {numero}")
        print(
            f"Título: {producto['titulo']}"
        )
        print(
            f"Precio: {producto['precio']}"
        )
        print(
            "Disponibilidad: "
            f"{producto['disponibilidad']}"
        )
        print(
            f"Categoría: "
            f"{producto['categoria']}"
        )
        print(
            f"Rating: {producto['rating']}"
        )
        print(
            f"UPC: {producto['upc']}"
        )
        print(f"URL: {link}")
        print("-" * 50)


if __name__ == "__main__":
    main()
