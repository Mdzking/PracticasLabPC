# Definir una variable
$nombre = "Juan"

# Ejemplo de un if
if ($nombre -eq "Juan") {
    Write-Host "Hola, Juan. ¡Bienvenido!"
} else {
    Write-Host "Hola, desconocido. ¿Quién eres?"
}

# Ejemplo de un ciclo (for)
for ($i = 1; $i -le 5; $i++) {
    Write-Host "Iteración $i"
}

# Ejemplo de una función con parámetro
function Saludar($nombre) {
    Write-Host "¡Hola, $nombre!"
}

# Llamar a la función con el parámetro
Saludar "María"
