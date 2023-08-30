class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor

cb1 = ContaBancaria('Henrique', 3000)
cb1.depositar(350)
print(cb1.saldo)
cb1.sacar(250)
print(cb1.saldo)