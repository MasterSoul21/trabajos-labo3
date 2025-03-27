import math
base = float(input("base: "))
x = float(input("x: "))

if x > 0 and x != 1:
    resul = math.log(x , base)
    print(f"{resul:.4f}")

