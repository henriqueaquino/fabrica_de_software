def welcome_condicionais():
    print('Welcome condicionais')

def determina_CNH():
    # recebe idade e determina se pode obter CNH

    idade = int(input('Digite a idade: '))

    if idade >= 18:
        print("Pode obter CNH")
    else:
        print("Nao pode obter CNH")

def determina_multa():
    #ler velocidade e multa se passar de 80 km/h

    velocidade = int(input('Digite a velocidade: '))

    if velocidade > 80:
        resto = velocidade % 80
        print('Foi multado por passar de 80 km/h, a multa eh de: ', resto * 7, ' reais')
    else:
        print('Nao foi multado')

def determina_tres():
    # ler 3 numeros e mostra qual eh o maior e menor

    num1 = int(input('Digite numero 1: '))
    num2 = int(input('Digite numero 2: '))
    num3 = int(input('Digite numero 3: '))

    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print("Maior: ", num1, "Menor: ", num3)
        else:
            print("Maior: ", num1, "Menor: ", num2)
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print("Maior: ", num2, "Menor: ", num3)
        else:
            print("Maior: ", num2, "Menor: ", num1)
    else:
        if num1 > num2:
            print("Maior: ", num3, "Menor: ", num2)
        else:
            print("Maior: ", num3, "Menor: ", num1)

def calcula_canetas():
    # recebe uma quantidade de canetas pretas e azuis, mostra a quantidade final a ser paga

    can_pretas = int(input('Digite quantidade de canetas pretas: '))
    can_azuis = int(input('Digite quantidade de canetas azuis: '))

    print('Total a ser pago: ', (can_pretas * 2.5) + (can_azuis * 2), ' reais')

def le_tres():
    # ler o nome de tres pessoas

    nome1 = str(input('Digite o primeiro nome: '))
    nome2 = str(input('Digite o segundo nome: '))
    nome3 = str(input('Digite o terceiro nome: '))

    print('Oi, eu sou ', nome1)
    print('Oi, eu sou ', nome2)
    print('Oi, eu sou ', nome3)