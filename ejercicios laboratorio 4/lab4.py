import math
x1,y1,x2,y2,x3,y3 = map(float,input("Ingrese los tres vertices v1, v2 y v3: ").split())

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
c = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

if a > b: 
    if a > c: 
        may = a
    else:
        if c > b:
            may = c
else:
    if b > c: 
        may = b
    else:
        may = c

tetha = math.degrees(math.acos((a ** 2 + b **2 - c**2)/(2*a*b)))
beta = math.degrees(math.acos((a ** 2 + c **2 - b**2)/(2*a*c)))
sigma = math.degrees(math.acos((b ** 2 + c **2 - a**2)/(2*b*c)))

p = a + b + c
area = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Longitud de los lados = {a:.4f} {b:.4f} {c:.4f}\nAngulos de las esquinas = {tetha:.4f} {beta:.4f} {sigma:.4f}\nPerimetro = {p:.4f}\nArea = {area:.4f}")

