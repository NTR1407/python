class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

#modificar los valores en los parametros de la clase
Persona.edad = 30
Persona.nombre = "Nestor"

#acceder a esos valores modificados

print("Su nombre es",Persona.nombre,"y su edad", Persona.edad)

#creacion de un nuevo objeto

persona = Persona("Fernando",50)

print(persona.nombre)
print(persona.edad)
