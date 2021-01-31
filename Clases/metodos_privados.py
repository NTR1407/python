class Personas:
    def __init__(self,nombre,apellido_paterno,apellido_materno):
        self.nombre = nombre 
        self._apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
    
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)

    def metodo_publico(self):
        self.__metodo_privado()
        
    def get_apellido_materno (self):
        return self.__apellido_materno
    
    def set_apellido_materno (self,apellido_materno):
         self.__apellido_materno = apellido_materno    
    

p1 = Personas("Nestor","Cuellar","Serrato")

p1.metodo_publico()

