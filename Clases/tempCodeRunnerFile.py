class Rectangulo:
    def __init__(self,base,altura):
        self.base = base 
        self.altura = altura
    def calculo(self):
        return self.base*self.altura
print("Hola")
base = input("Ingresa la base del Rectangulo:")
altura = input("Ingresa la altura del Rectangulo:")

rectangulo = Rectangulo(base,altura)

print("El area del rectangulo es:",rectangulo.calculo(),"Gracias")
          