class Animal:
    def __init__(self):
        pass

    def emitir_som(self):
        pass

    def mostrar_informacoes(self):
        pass

class Cachorro(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        print("Latindo !!!")

class Gato(Animal):
    def __init__(self):
        pass

    def emitir_som(self):
        print("Miando !!!")

c = Cachorro()
m = Gato()
c.emitir_som()
m.emitir_som()