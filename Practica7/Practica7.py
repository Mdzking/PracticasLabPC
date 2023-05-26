import os
from ftplib import FTP

# Función para descargar archivos de texto del servidor FTP
def descargar_archivos_ftp(ftp, carpeta_actual, carpeta_destino):
    # Cambiar al directorio de la carpeta actual en el servidor FTP
    ftp.cwd(carpeta_actual)

    # Obtener una lista de todos los archivos y carpetas en la carpeta actual
    archivos = ftp.nlst()

    # Iterar sobre los archivos y carpetas
    for archivo in archivos:
        # Obtener el nombre y la extensión del archivo
        nombre, extension = os.path.splitext(archivo)

        # Comprobar si es un archivo de texto
        if extension.lower() in ['.txt', '.msg', '.readme']:
            # Crear la carpeta de destino si no existe
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            # Descargar el archivo de texto
            archivo_destino = os.path.join(carpeta_destino, archivo)
            with open(archivo_destino, 'wb') as file:
                ftp.retrbinary('RETR ' + archivo, file.write)
                print("Descargado:", archivo)

        # Comprobar si es una carpeta y llamar recursivamente a la función
        elif '.' not in archivo:
            descargar_archivos_ftp(ftp, os.path.join(carpeta_actual, archivo), carpeta_destino)

# Datos de conexión al servidor FTP
servidor_ftp = '192.168.0.15'
usuario_ftp = 'johnny'
contraseña_ftp = '1996528'

# Carpeta actual en el servidor FTP a explorar
carpeta_actual_ftp = '/carpeta_principal'

# Carpeta de destino local para los archivos de texto descargados
carpeta_destino_local = 'TXT'

# Conexión al servidor FTP
ftp = FTP(servidor_ftp)
ftp.login(usuario_ftp, contraseña_ftp)

# Descargar archivos de texto del servidor FTP y guardarlos en la carpeta de destino local
descargar_archivos_ftp(ftp, carpeta_actual_ftp, carpeta_destino_local)

# Cerrar la conexión FTP
ftp.quit()
