a,b,c,d,e = map(int,input().split())

if a > b: 
    if a > c:
        if a > d:
            if a > e:
                mayor = a
            else:
                mayor = e
        else:
            if d > e: 
                mayor = d
            else:
                mayor = e
    else:
        if c > d: 
            if c > e: 
                mayor = c
            else: 
                mayor = e 
        else: 
            if d > e:
                mayor = d
            else:
                mayor = e
else:
    if b > c: 
        if b > d:
            if b > e:
                mayor = b 
            else:
                mayor = e
        else:
            if d > e: 
                mayor  = d 
            else: 
                mayor = e
    else: 
        if c > d: 
            if c > e:
                mayor = c 
            else:
                mayor = e 
        else: 
            if d > e: 
                mayor = d
            else: 
                mayor = e
                
if a < b: 
    if a < c:
        if a < d:
            if a < e:
                menor = a
            else:
                menor = e
        else:
            if d < e: 
                menor = d
            else:
                menor = e
    else:
        if c < d: 
            if c < e: 
                menor = c
            else: 
                menor = e 
        else: 
            if d < e:
                menor = d
            else:
                menor = e
else:
    if b < c: 
        if b < d:
            if b < e:
                menor = b 
            else:
                menor = e
        else:
            if d < e: 
                menor  = d 
            else: 
                menor = e
    else: 
        if c < d: 
            if c < e:
                menor = c 
            else:
                menor = e 
        else: 
            if d < e: 
                menor = d
            else: 
                menor = e
print (f"Maximo = {mayor}, Minimo = {menor}")            
        