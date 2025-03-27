import math
a = float(input("a(cm): "))
b = float(input("b(cm): "))
ang_c = float(input("C(grados): "))

C_rad = math.radians(ang_c)
c = math.sqrt(a ** 2 + b ** 2 - 2*a*b* math.cos(C_rad))




temp_A = (b ** 2 + c ** 2 - a **2)/(2*b*c)
ang_A = math.degrees(math.acos(temp_A)) 
temp_B = (c ** 2 + a ** 2 - b ** 2)/(2*c*a)
ang_B = math.degrees(math.acos(temp_B))
Total = ang_A + ang_B + ang_c


print(f"c = {c:.2f}\nA = {ang_A:.2f}\nB = {ang_B:.2f}\nTotal = {Total:.2f}")
