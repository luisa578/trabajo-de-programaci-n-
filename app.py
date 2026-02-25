# Solicitar datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad_mayor = int(input("Ingrese la edad del hermano mayor: "))
edad_menor = int(input("Ingrese la edad del hermano menor: "))

# Calcular diferencia de edades
diferencia = edad_mayor - edad_menor

# Mostrar resultado (concatenación e interpolación)
print("\nNombre completo:", nombre + " " + apellido)
print(f"Diferencia de edad entre hermanos: {diferencia} años")