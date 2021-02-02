import numpy as np

print('Bienvenido al juego Ta Te Ti.\n')
print('Deberas llenar la siguiente matriz con O o con X. \nPuntos a tener en cuenta: \n ')
print('la matriz original se muestra asi: \n \n |_|_|_| \n |_|_|_| \n |_|_|_|\n')
print('Ejemplos de como se puede ganar:\n')
print(' |O|O|O| |_|_|_| |_|_|_| |O|_|_|\n |_|_|_| |X|X|X| |_|_|_| |_|O|_|\n |_|_|_| |_|_|_| |X|X|X| |_|_|O|\n')

print('NOTA: Las letras aceptadas son X y O ambas debe estar en mayusculas.\n')
print('NOTA1: Se aceptan números entre 1 y 3. Si digitas alguno diferente el juego se detendra.\n')
input('Para empezar presiona la tecla Enter.\n')

while True:
    
    matriz = np.array([['_','_','_'],['_','_','_'],['_','_','_']])
    
    a = range(9)
    
    for b in a:

        Fila = int(input('Elije la posición de la fila: '))-1
        if Fila < 0 or Fila > 2:
            print('El valor ingresado no es correcto, es necesario reiniciar el juego.\n')
            break
        Columna = int(input('Elije la posición de la columna: ')) -1
        if Columna < 0 or Fila > 2:
            print('El valor ingresado no es correcto, es necesario reiniciar el juego.\n')
            break
        Valor = input('Ingresa la letra X u O en mayuscula: ')
        if Valor != 'X' and Valor != 'O':
            print('Recuerda que las letras deben estar en mayuscula, es necesario reiniciar el juego.\n')
            break
        matriz [Fila,Columna] = Valor

        if matriz[0,0] != '_' and matriz[0,0] == matriz[0,1] and matriz[0,1] == matriz[0,2]: 

            print('\n ********* El jugador que ha elegido', matriz[0,0], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[1,0] != '_' and matriz[1,0] == matriz[1,1] and matriz[1,1] == matriz[1,2]:

            print('\n ********* El jugador que ha elegido', matriz[1,0], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[2,0]!= '_' and matriz[2,0] == matriz[2,1] and matriz[2,1] == matriz[2,2]:

            print('\n ********* El jugador que ha elegido', matriz[2,0], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[0,0] != '_'and matriz[0,0] == matriz[1,0] and matriz[1,0] == matriz[2,0]:

            print('\n ********* El jugador que ha elegido', matriz[0,0], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[0,1] != '_'and matriz[0,1] == matriz[1,1] and matriz[1,1] == matriz[2,1]:

            print('\n ********* El jugador que ha elegido', matriz[0,1], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[0,2] != '_'and matriz[0,2] == matriz[1,2] and matriz[1,2] == matriz[2,2]:

            print('\n ********* El jugador que ha elegido', matriz[0,2], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[0,0] != '_'and matriz[0,0] == matriz[1,1] and matriz[1,1] == matriz[2,2]:

            print('\n ********* El jugador que ha elegido', matriz[0,0], 'ha ganado la partida ********* \n')
            print(matriz)
            break

        elif matriz[0,2] != '_'and matriz[0,2] == matriz[1,1] and matriz[1,1] == matriz[2,0]:

            print('\n ********* El jugador que ha elegido', matriz[0,2], 'ha ganado la partida ********* \n')
            print(matriz)
            break
        else:
            print(matriz)
    
    c = input('El juego ha terminado. Presiona Enter si deseas jugar de nuevo, de lo contrado escribe No\n')
    
    if c == 'no' or c == 'No' or c == 'NO':
        print('Fin del Juego\n')
        break

print('Gracias por probar mi código!')