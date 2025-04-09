'''1.Despliegue la piramide. Escriba un programa que muestre los n´umeros de un 
patr´on piramidal (mediante ciclos anidados)
'''
n = int(input("Ingrese numero rango de 1 al 10: "))
for i in range (n):
    ascendente = [2**j for j in range (i+1)]
    descendente = ascendente[:-1][::-1]
    fila = " ".join(map(str, ascendente + descendente))
    print(fila.center(n * 4))
