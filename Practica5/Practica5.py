import requests
from bs4 import BeautifulSoup

# URL del sitio web a scrapear
url = "https://swapi.dev/"

# Realizar la solicitud HTTP GET al sitio web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear el objeto BeautifulSoup con el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar los elementos deseados en el HTML utilizando selectores CSS
    # Aquí se muestra un ejemplo de encontrar todos los elementos <a> con la clase "enlace"
    enlaces = soup.select("a.enlace")

    # Crear un archivo para guardar la información extraída
    archivo_salida = open("resultado.txt", "w")

    # Recorrer los elementos encontrados y guardar la información en el archivo
    for enlace in enlaces:
        texto_enlace = enlace.text.strip()  # Obtener el texto del enlace sin espacios al inicio y al final
        archivo_salida.write(texto_enlace + "\n")

    # Cerrar el archivo de salida
    archivo_salida.close()

    print("Web scraping completado. La información ha sido guardada en el archivo resultado.txt.")
else:
    print("Error al hacer la solicitud HTTP al sitio web.")
