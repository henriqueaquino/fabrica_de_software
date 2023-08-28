# imprime numeros de 0 a 10

for i in range(11):
    print(i)

# imprime numeros de 10 a 0

for i in range(10, -1, -1):
    print(i)

# imprime numeros pares de 0 a 10

for i in range(0, 11, 2):
    print(i)

# tabuada de adição de 0 a 10

num = int(input('Digite um numero: '))
print('Tabuada da adicao: ')

for i in range(10):
    print(f'{num} + {i} = {num + i}')

# pede varios nomes e só para quando eh digitado "parar"

while True:
    nome = str(input('Digite um nome: '))
    if nome == 'parar':
        break

# faz a soma de todos os numeros digitados, para quando 0 eh digitado
soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 0:
        break
    soma += numero
    print('Soma: ', soma)

# ler o sexo como 'F' 'M', termina quando eh digitado 'sair', mostra a quantidade de F e M

count_m = 0
count_f = 0
while True:
    entrada = str(input("Digite o sexo: "))

    if entrada == 'F':
        count_f += 1
    elif entrada == 'M':
        count_m += 1
    elif entrada == 'sair':
        print('Numero homens: ', count_m, ' Numero mulheres: ', count_f)