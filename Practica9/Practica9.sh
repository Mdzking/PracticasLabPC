#!/bin/bash

# Verificar si se proporcionó el archivo de registro
if [ -z "$1" ]; then
  echo "Usage: $0 <archivo_registro>"
  exit 1
fi

# Verificar si el archivo de registro existe
if [ ! -f "$1" ]; then
  echo "El archivo $1 no existe."
  exit 1
fi

# Directorio de RegRipper
regripper_dir="C:\Program Files (x86)\RegRipper"

# Ejecutar RegRipper en el archivo de registro
"$regripper_dir/rip.exe" -r "$1" > analysis.txt

echo "Análisis completado. Los resultados se guardaron en analysis.txt."
