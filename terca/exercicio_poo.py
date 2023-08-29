class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        return f'Nome: {self.nome} Idade: {self.idade} Profissao: {self.profissao}'

class ContaBancaria:
    def __int__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

p1 = Pessoa('Ana', 23, 'Enfermeira')
p2 = Pessoa('Carlos', 27, 'Medico')
p3 = Pessoa('Sandra', 30, 'Programador')

print(p1.saudacao())
print(p2.saudacao())
print(p3.saudacao())

cb1 = ContaBancaria('Henrique', 3000)
cb1.depositar(350)
print(cb1.saldo)
cb1.sacar(250)
print(cb1.saldo)