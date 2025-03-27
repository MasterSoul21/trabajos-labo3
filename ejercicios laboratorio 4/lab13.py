import random

# Opciones del juego
opciones = ["Tijera", "Piedra", "Papel"]

# Generar elección aleatoria de la computadora
computadora = random.randint(0, 2)

# Solicitar entrada del usuario
usuario = int(input("Ingrese un número (0 = Tijera, 1 = Piedra, 2 = Papel): "))

# Validar entrada del usuario
if usuario not in [0, 1, 2]:
    print("Entrada no válida. Debe ingresar 0, 1 o 2.")
    exit()

print(f"La computadora eligió: {opciones[computadora]}")
print(f"Usted eligió: {opciones[usuario]}")

# Determinar el resultado
tabla_ganadora = {
    0: 2,  # Tijera gana contra Papel
    1: 0,  # Piedra gana contra Tijera
    2: 1   # Papel gana contra Piedra
}

if usuario == computadora:
    print("Es un empate!")
elif tabla_ganadora[usuario] == computadora:
    print("¡Usted gana!")
else:
    print("La computadora gana!")

