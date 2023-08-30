class FormaGeometrica:
    def __init__(self):
        pass

    def calcularArea(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio ** 2)

ret = Retangulo(10, 5)
print(ret.calcularArea())

cir = Circulo(7)
print(cir.calcularArea())