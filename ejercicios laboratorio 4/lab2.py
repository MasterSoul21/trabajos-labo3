a,b,c,d,e = map(int,input().split())


if a != b and a != c and a != d and a != e:
    if b != c and b != d and b != e:
        if c != d and c != e:
            if d != e:
                print("Todos unicos")
            else:
                print("Duplicados")
        else:
            print("Duplicados")
    else:
        print("Duplicados")
else:
    print("Duplicados")
