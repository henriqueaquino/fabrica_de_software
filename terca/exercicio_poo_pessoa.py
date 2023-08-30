class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        return f'Nome: {self.nome} Idade: {self.idade} Profissao: {self.profissao}'

p1 = Pessoa('Ana', 23, 'Enfermeira')
p2 = Pessoa('Carlos', 27, 'Medico')
p3 = Pessoa('Sandra', 30, 'Programador')

print(p1.saudacao())
print(p2.saudacao())
print(p3.saudacao())

