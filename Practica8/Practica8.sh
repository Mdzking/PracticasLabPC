#!/bin/bash

# Verificar si se proporcionó el archivo de direcciones
if [ -z "$1" ]; then
  echo "Usage: $0 <archivo_direcciones>"
  exit 1
fi

# Verificar si el archivo de direcciones existe
if [ ! -f "$1" ]; then
  echo "El archivo $1 no existe."
  exit 1
fi

# Leer el archivo de direcciones línea por línea y enviar correos
while IFS= read -r direccion; do
  echo "Enviando correo a: $direccion"
  echo "Cuerpo del correo" | mail -s "Asunto del correo" "$direccion"
done < "$1"
