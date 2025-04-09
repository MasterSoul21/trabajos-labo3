'''10.Matem´aticas: combinaciones. Escriba un programa que muestre, todas las combinaciones
de los n´umeros enteros del 1 al 7. Tambi´en muestre el n´umero total de todas ´estas combinaciones.'''
c=0
for j in range(1,7,1):
    for i in range(2,8,1):
        if (i!=j and i>j) :
            c+=1
        print(j, i, sep=' ')  
print (f"El total es: {c}")