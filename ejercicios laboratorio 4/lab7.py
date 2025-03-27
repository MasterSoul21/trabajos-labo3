sexo = int(input("Ingrese el sexo 1 = mujer, 2 = hombre: "))
edad = int(input("Ingrese su edad: "))

if sexo == 1:
    pulsaciones = (220 - edad) / 10
elif sexo == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("Opción no válida. Debe ingresar 1 para mujer o 2 para hombre.")
    exit()

print(f"Usted debería tener {pulsaciones:.1f} pulsaciones por cada 10 segundos de ejercicio.")
