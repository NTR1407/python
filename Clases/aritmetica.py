class Aritmetica:
    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def sumar(self):
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
    def division(self):
        return self.operando1 / self.operando2
    def multiplicacion(self):
        return self.operando1 * self.operando2
#creamos un nuevo objeto

aritmetica = Aritmetica(10,20)

print(aritmetica.sumar())
print(aritmetica.resta())
print(aritmetica.division())
print(aritmetica.multiplicacion())
        