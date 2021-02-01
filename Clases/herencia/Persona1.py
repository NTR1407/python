class Persona1: #clase padre
    def __init__(self, n,e):
        self.nombre = n
        self.edad = e
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)

class Empleado(Persona1): #clase hija hereda metodos de clase Persona1
    def __init__(self,n,e,s):
        super().__init__(n,e)#con super se traen llamamos el metodo __init__ de la clase padre
        self.sueldo = s
    
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)

persona1 = Persona1("Nestor", 31)
empleado = Empleado("Beatriz",30, 3500000)
print(persona1)
print(empleado)

