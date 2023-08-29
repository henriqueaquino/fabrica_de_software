def welcome_operadores():
    print('Welcome operadores')

def mostra_suc_ant():
    #Recebe um numero e mostra seu sucessor e antecessor

    num = int(input('Digite um numero: '))
    print('Sucessor: ', num+1, ' Antecessor: ', num-1)

def faz_operacoes():
    # Ler dois numeros, exibe a soma, subtracao, multiplicacao e divisao dos dois numeros

    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    print('Soma: ', num1+num2,
          ' Subtracao: ', num1-num2,
          ' Multiplicacao: ', num1*num2,
          ' Divisao: ', num1/num2)

def le_dois():
    # ler dois numeros, exibe True se o primeiro eh maior que o segundo e False
    # se o primeiro numero for menor ou igual ao segundo numero

    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))

    if num1 > num2:
        print(True)
    else:
        print(False)

def celsius_fahren():
    # ler temperatura em celsius e converte para fahrenheit

    temp_celsius = float(input('Digite temperatura em celsius: '))
    temp_fahren = (1.8 * temp_celsius) + 32
    print("Temperatura em fahrenheit: ", temp_fahren)