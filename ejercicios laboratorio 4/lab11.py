n = int(input("Ingrese n [1..99]: "))

b = n % 10
a = n // 10
if 11 <= n and n <= 19:
    if n == 11:
        print("once")
    if n == 12:
        print("doce")
    if n == 13:
        print("trece")
    if n == 14:
        print("catorce")
    if n == 15: 
        print("quince")
    if n == 16:
        print("deieciseis")
    if n == 17:
        print("diecisiete")
    if n == 18:
        print("dieciocho")
    if n == 19:
        print("diecinueve")
if a == 1:
    decimal = "diez"
if a == 2:
    decimal = "veinte"
if a == 3:
    decimal = "treinta"
if a == 4:
    decimal = "cuarenta" 
if a == 5:
    decimal = "cincuenta"
if a == 6:
    decimal = "sesenta"
if a == 7:
    decimal = "setenta"
if a == 8:
    decimal = "ochenta"
if a == 9:
    decimal = "noventa"

if b == 1:
    unidad = "uno"   
if b == 2:
    unidad = "dos"
if b == 3:
    unidad = "tres"
if b == 4:
    unidad = "cuatro"
if b == 5: 
    unidad = "cinco"
if b == 6:
    unidad = "seis"
if b == 7:
    unidad = "siete"
if b == 8: 
    unidad = "ocho"
if b == 9:
    unidad = "nueve"

print(f"{decimal} y {unidad}")


