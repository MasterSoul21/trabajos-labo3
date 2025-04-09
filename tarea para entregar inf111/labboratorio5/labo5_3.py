'''3.Cantidad de Fibonacci. Dados dos n´umeros a, b donde a < b < 2
64. Contar cu´antos
n´umeros de Fibonacci fi existen entre este par de n´umeros enteros 
(a ≤ fi ≤ b). Imprima en la salida un n´umero por cada caso de entrada.'''
a,b = map(int,input("Introduce el rango: ").split())
x = -1
y = 1
u = 0
for i in range(a,b,1):
    c = x + y 
    if a <= c and c <= b:
        u += 1
    
    x = y
    y = c
print(u)
    

    