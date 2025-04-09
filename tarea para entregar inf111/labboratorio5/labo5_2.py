'''2.n-´esimo Fibonacci. La serie de Fibonacci est´a definida como 
f0 = 0, f1 = 1 y fn = fn−1+fn−2 para n ≥ 2. Escriba un programa para imprimir 
la serie de fibonacci. Imprima
en la salida la serie correspondiente, por cada caso de entrada.'''
n = int(input("Ingrese n: ")) 
a = -1
b = 1
for i in range(1,n+1,1):
    c = a + b 
    print(c,end=" ")
    a = b
    b = c
    
    