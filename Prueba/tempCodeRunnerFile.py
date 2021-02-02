def nivel_posicion(n,j):
    x =[1]
    cero = [0]
    for i in range(n):
        print(x) 
        x = [ i + d for i,d in zip(x + cero, cero + x)]
        if x.index(j) is True:
            z = x 
    print(z)
    print(z.index(j)) 
nivel_posicion(5,6)