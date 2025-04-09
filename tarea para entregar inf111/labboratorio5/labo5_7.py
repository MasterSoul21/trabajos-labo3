'''7.Estad´ısticas: calcular la media y la desviaci´on est´andar. En las aplicaciones empresariales,
a menudo se le solicita que calcule la media y la desviaci´on est´andar de los datos. La media
es simplemente el promedio de los n´umeros. La desviaci´on est´andar es una estad´ıstica que
le indica qu´e tan estrechamente se agrupan los diferentes datos alrededor de la media en
un conjunto de datos. Por ejemplo, ¿cu´al es la edad promedio de los estudiantes en una
clase? ¿Qu´e tan cerca est´an las edades? Si todos los estudiantes tienen la misma edad, la
desviaci´on es 0.'''
import math
a,b,c,d,e,f,g,h,i,j = map(float,input("Ingrese 10 valores..: ").split())
datos = [a,b,c,d,e,f,g,h,i,j]
n = 10 
media = (a+b+c+d+e+f+g+h+i+j)/n
suma_cuadrados = sum(x**2 for x in datos)
suma = sum(datos)
cuadrado_suma = (suma**2)/n
varianza = (suma_cuadrados - cuadrado_suma) / (n-1)
desviacion = math.sqrt(varianza)
print(f"{media}\n{desviacion}")