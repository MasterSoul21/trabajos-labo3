'''4.Muestre los n´umeros primos entre el 2 y el 1,000.Mostrar todos los n´umeros primos entre
2 y 1,000. Muestre diez n´umeros primos por cada l´ınea. Los n´umeros est´an separados por exactamente un espacio'''
x = 1
for j in range(2,1000,1):
    c = 0
    for i in range(1,j+1,1):
        if j % i == 0:
            c +=1
        
    if c == 2:
        print(j,end=" ")
        if(x==10):
            x=0
            print()
        x=x+1      
