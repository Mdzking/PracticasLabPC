#!/bin/bash

# Definir una variable
nombre="Juan"

# Ejemplo de un if
if [ "$nombre" = "Juan" ]; then
    echo "Hola, Juan. ¡Bienvenido!"
else
    echo "Hola, desconocido. ¿Quién eres?"
fi

# Ejemplo de un ciclo (for)
for ((i=1; i<=5; i++)); do
    echo "Iteración $i"
done

# Ejemplo de una función con parámetro
saludar() {
    echo "¡Hola, $1!"
}

# Llamar a la función con el parámetro
saludar "María"
