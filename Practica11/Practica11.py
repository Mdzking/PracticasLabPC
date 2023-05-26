import socket
import datetime

# Obtener la dirección IP del sistema
def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip

# Obtener la hora actual
def obtener_hora_actual():
    hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return hora_actual

# Obtener la dirección IP y la hora actual
direccion_ip = obtener_direccion_ip()
hora_actual = obtener_hora_actual()

# Guardar la dirección IP y la hora actual en un archivo de texto
archivo_resultados = 'resultados.txt'
with open(archivo_resultados, 'w') as archivo:
    archivo.write(f"Dirección IP: {direccion_ip}\n")
    archivo.write(f"Hora actual: {hora_actual}\n")

print("Los resultados se han guardado en el archivo resultados.txt.")
