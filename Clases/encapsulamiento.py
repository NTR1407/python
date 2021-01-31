class Persona:
    def __init__(self,n):
        self.__nombre = n #al ponerle __ a la variable nombre este queda como privado

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre


p1 = Persona("Nestor")
print(p1.get_nombre()) #de esta manera se accede al valor o cadena de la variable privada

p1.set_nombre("Fernando") #accede con este metodo para cambiar el valor de la variable privada
print(p1.get_nombre())