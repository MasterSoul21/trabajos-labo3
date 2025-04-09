'''8.Sucesi´on de Cantor. Una de las pruebas famosas de las matem´aticas modernas es la
demostraci´on de Georg Cantor el cual indica que el conjunto de los n´umeros racionales es
enumerable'''
#sucesion de cantor 
n = int(input())
diagonal, count = 1, 0
while count + diagonal < n:
    count += diagonal
    diagonal += 1

r = n - count - 1
if diagonal % 2 == 0:
    numerator = 1 + r
    denominator = diagonal - r
else:
    numerator = diagonal - r
    denominator = 1 + r

print(f"{numerator}/{denominator}")
