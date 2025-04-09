'''5.Primo y Fibonacci. Los n´umeros Fibonacci tienen la siguiente secuencia 0, 1, 1, 2, 3, 5, 8,
13 y as´ı sucesivamente. Realizar un programa que permita imprimir el n-´esimo t´ermino
primo de la serie de Fibonacci. Imprima en la salida un n´umero por cada caso de entrada.'''
cantidad = int(input("Ingrese la cantidad de casos: "))
for _ in range(cantidad):
    n = int(input())
    a, b = 0, 1
    contador = 0
    for _ in range(100000): 
        fib = a + b
        a, b = b, fib

        if fib >= 2:
            for i in range(2, int(fib ** 0.5) + 1):
                if fib % i == 0:
                    break
            else:
                contador += 1
                if contador == n:
                    print(fib)
                    break

    
    







#for i in range(1,n+1,1):
#    c = a + b 
#    print(c)
#    a = b
#    b = c
