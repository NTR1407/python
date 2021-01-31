class Caja:
    def __init__(self,largo,alto,ancho):
        self.largo = largo
        self.alto = alto
        self.ancho = ancho
    def perimetro(self):
        return self.largo * self.alto * self.ancho


print("Hola, a continuacion calcularemos el perimetro de una caja.")
largo = float(input("Ingrese el largo de la caja: "))
alto = float(input("Ingrese el alto de la caja: "))
ancho = float(input("Ingrese el ancho de la caja: "))

caja = Caja(largo,alto,ancho)

print("El perimetro de la caja es:",caja.perimetro())

