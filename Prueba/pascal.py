def nivel_posicion(n,j):
    x =[1]
    cero = [0]
    for i in range(n):
        z = x
        print(x) 
        x = [ i + d for i,d in zip(x + cero, cero + x)]   
    try:           
        print(z.index(j))
    except:
        print("El numero no se encuentra en la lista")
nivel_posicion(5,6)
nivel_posicion(5,9)



