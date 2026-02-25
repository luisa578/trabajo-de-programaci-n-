# Pedir datos
nom = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

edad_mayor = int(input("Edad del hermano mayor: "))
edad_menor = int(input("Edad del hermano menor: "))

# Calcular diferencia
diferencia = edad_mayor - edad_menor

# Mostrar resultado (interpolacion)
print(f"Nombre completo: {nombre} {apellido}")
print(f"La diferencia de edad entre los hermanos es: {diferencia} años")

