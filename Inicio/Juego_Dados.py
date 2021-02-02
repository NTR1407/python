
import random

print("""Hola!
         El siguiente programa simula el lanzamiento de dos dados de 6 caras, 
         su resultado se sumara y se consultara si desea realizar un nuevo lanzamiento.
         Muchas Gracias.\n""")

x = input("¿Desea simular el lanzamiento de dados? Si / No \n")

a = random.randint(1,6)
b = random.randint(1,6)

while True:
    if x == "Si" or x == "SI" or x == "si":
        
        print("\nEl dado 1 ha caido en: ", a, ".")
        print("\nEl dado 2 ha caido en: ", b, ".")
        print("\nLa suma entre ", a, " y ", b, " es: ", a + b)
        
        x = input("\n¿Desea continuar lanzando los dados? Si / No \n")
        
    elif x == "No" or x == "NO" or x == "no":
        
        print("\n¡Muchas gracias! \n")
        
        break
        
    else:
        
        print("No se reconoce la opción marcada, corra de nuevo la simulación. \n")
        
        break             

print("Fin programa.")





