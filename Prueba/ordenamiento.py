def ordenamiento(lista):
    z = []
    for i in lista:
        z.append(''.join(sorted(i,key=str.upper)))
    return z
print(ordenamiento(lista = ["Hola","soy","el","candidato","al","cargo","Data Expert"]))
        