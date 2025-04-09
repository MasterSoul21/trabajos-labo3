'''9.Aplicaci´on financiera: compare pr´estamos con varias tasas de inter´es. 
Escriba un programa que le permita al usuario ingresar el monto del pr´estamo y el per´ıodo de pr´estamo en
cantidad de a˜nos y muestra los pagos mensuales y totales de cada tasa de inter´es comenzando entre 
5 % y 8 %, con un incremento de 1/8'''
monto = int(input("Monto del prestamo: "))
edad = int(input("Cantidad de años: "))
tasa_anual = 5.0

cantidad_meses = edad * 12
print("Tasa de interes\tPago Mensual\tPago Total")
print("------------------------------------------------------")
while tasa_anual <= 8.0:  # Hasta el 8%
    tasa_interes_mensual = tasa_anual / 12 / 100  # Convertir a tasa mensual
    cantidad_meses = edad * 12

    pago_mensual = (monto * tasa_interes_mensual) / \
                    (1 - (1 + tasa_interes_mensual) ** -cantidad_meses)
    pago_total = pago_mensual * cantidad_meses

    print(f"{tasa_anual:.2f}\t\t{pago_mensual:.2f}\t\t{pago_total:.2f}")
    tasa_anual += 0.125