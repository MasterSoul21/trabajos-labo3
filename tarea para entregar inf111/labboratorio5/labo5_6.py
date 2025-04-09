'''6.Calcular: sin(x), cos(x) y e^x'''
import math
x = float(input())
n_terminos = 10 
#calculando el seno de x usando la serie de taylor 
resultado = 0
resultado2 = 0
resultado3 = 0
print("n\tsin(0.5)\tcos(0.5)\te^0.5")
print("---\t-----------\t----------\t----------") 
for n in range(n_terminos):
    termino = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    resultado += termino
    
    termino2 = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    resultado2 += termino2
    
    termino3 = (x ** n) / math.factorial(n)
    resultado3 += termino3
    print(f"x={n}\t{resultado:.11f}\t{resultado2:.11f}\t{resultado3:.11f}")




