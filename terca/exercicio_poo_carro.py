class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print('Acelerando...')

c1 = Carro('FIAT', 'uno', 2015)
c1.acelerar()