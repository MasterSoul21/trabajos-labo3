x1,y1,x2,y2 = map(float,input("Ingrese x1, y1,x2,y2: ").split())
if x1 == x2 and y1 == y2:
    print("Los puntosson iguales,no se puede determinar una recta")
    exit()

if x1 == x2:
    print(f"x = {x1}")
else:
    m = (y2 - y1)/(x2 - x1)
    b = y1 - m*x1
    c = - m*x1 + y1
    print(f"y = {m:.2f}x + {b:.2f}\t{-m:.2f}x + y + {-b:.2f} = 0 ")