precio = int(input("Ingrese el precio por kilo(Bs): "))
cantidad = int(input("Ingrese la cantidad de kilos: "))

precio_inicial = precio * cantidad 
if 0<= cantidad and cantidad <= 2:
    total = precio_inicial * 0.0
else:
    if 2.01<= cantidad and cantidad <= 5:
        total = precio_inicial * 0.10
    else:
        if 5.01 <= cantidad and cantidad <= 10:
            total = precio_inicial * 0.20
        else:
            if cantidad > 10:
                total = precio_inicial * 0.30
precio_total = precio_inicial - total
print(f"Precio a cancelar Bs. {precio_total}")
