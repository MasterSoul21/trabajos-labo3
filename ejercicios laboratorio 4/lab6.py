horas = int(input("Ingrese el n umero de horas trabajadas: "))
salario = int(input("Ingrese el salario por hora en Bs: "))

total = salario * horas
horas_mas = horas - 40
if horas > 40: 
    horas_extras = (horas_mas)*salario * 0.50

salario_total = total + horas_extras

print(salario_total)