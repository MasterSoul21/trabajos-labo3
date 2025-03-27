puntuacion = float(input("Introduzca puntuacion: "))

if 0.0 <= puntuacion and puntuacion <= 1.0:
    if puntuacion >= 0.9:
        print("Sobresaliente")
    elif puntuacion >= 0.8:
        print("Notable")
    elif puntuacion >= 0.7:
        print("Bien")
    elif puntuacion >= 0.6:
        print("Suficiente")
    elif puntuacion < 0.6:
        print("Insuficiente")
else:
    print("Puntuacion incorrecta")
    