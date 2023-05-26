import requests
import socket
import base64
import nmap

# Obtener la IP pública
def obtener_ip_publica():
    try:
        # Realizar una solicitud HTTP a un servicio que devuelve la IP pública
        response = requests.get("https://api.ipify.org/?format=json")
        
        # Extraer la IP pública de la respuesta JSON
        ip_publica = response.json()["ip"]
        
        return ip_publica
    except requests.RequestException:
        return "No se pudo obtener la IP pública"

# Obtener la IP local
def obtener_ip_local():
    try:
        # Crear un socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Conectar el socket a un servidor de confianza
        s.connect(("8.8.8.8", 80))
        
        # Obtener la dirección IP local
        ip_local = s.getsockname()[0]
        
        # Cerrar el socket
        s.close()
        
        return ip_local
    except socket.error:
        return "No se pudo obtener la IP local"

# Obtener la IP pública y local
ip_publica = obtener_ip_publica()
ip_local = obtener_ip_local()

# Codificar los resultados en Base64
ip_publica_codificada = base64.b64encode(ip_publica.encode()).decode()
ip_local_codificada = base64.b64encode(ip_local.encode()).decode()

# Guardar los resultados codificados en Base64 en un archivo de texto
archivo_resultados = "ips.txt"

with open(archivo_resultados, "w") as archivo:
    archivo.write("IP Pública (Base64): " + ip_publica_codificada + "\n")
    archivo.write("IP Local (Base64): " + ip_local_codificada + "\n")

print("Los resultados codificados en Base64 se han guardado en el archivo ips.txt.")

# Obtener tu IP pública
def obtener_ip_publica():
    try:
        import requests
        response = requests.get("https://api.ipify.org/?format=json")
        ip_publica = response.json()["ip"]
        return ip_publica
    except requests.RequestException:
        return None


# Realizar un escaneo Nmap a la IP pública
def escanear_ip_publica(ip):
    nm = nmap.PortScanner()
    resultado = nm.scan(ip, arguments='-F')
    
    return resultado

# Obtener tu IP pública y realizar el escaneo
ip_publica = obtener_ip_publica()
if ip_publica:
    resultado_escaneo = escanear_ip_publica(ip_publica)
    print("Escaneo Nmap a la IP pública:", ip_publica)
    puertos_abiertos = resultado_escaneo['scan'][ip_publica]['tcp']
    if puertos_abiertos:
        print("Puertos abiertos:")
        for puerto, info in puertos_abiertos.items():
            if info['state'] == 'open':
                print("Puerto:", puerto, "Estado:", info['state'], "Servicio:", info['name'])
    else:
        print("No se encontraron puertos abiertos en la IP pública.")
else:
    print("No se pudo obtener la IP pública")