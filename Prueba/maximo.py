def mayor(lista):
    a = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > a:
            a = lista[i]
    return a

print(mayor(lista = [10,20,600,30,60,200,120]))
