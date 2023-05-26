from PIL import Image

# Función para decodificar una imagen
def decodificar_imagen(nombre_archivo):
    imagen = Image.open(nombre_archivo)
    pixeles = imagen.load()

    mensaje = ""
    for i in range(imagen.width):
        for j in range(imagen.height):
            r, g, b = pixeles[i, j]
            mensaje += chr(r)

    return mensaje

# Decodificar las dos imágenes
imagen1 = "imagen1.png"
imagen2 = "imagen2.png"

mensaje1 = decodificar_imagen(imagen1)
mensaje2 = decodificar_imagen(imagen2)

# Codificar el mensaje "Hola mundo" en C
codigo_c = """
#include <stdio.h>

int main() {
    printf("Hola mundo\\n");
    return 0;
}
"""

# Imprimir los mensajes decodificados
print("Mensaje decodificado de la imagen 1:")
print(mensaje1)
print()

print("Mensaje decodificado de la imagen 2:")
print(mensaje2)
print()

print("Código en C:")
print(codigo_c)
