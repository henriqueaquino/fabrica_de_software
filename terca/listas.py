def welcome_listas():
    print('Welcome listas')

def simula_fila():
    # simula uma fila de tarefas a ser executadas

    print('DIGITE O QUE FAZER: ')
    print('1. Adicionar tarefa')
    print('2. Executar fila de tarefas ')
    print('3. Sair')

    fila_tarefas = []

    while True:
        entrada = int(input("Escolha uma opcao: "))

        match entrada:
            case 1:
                descricao = str(input('Digite a descricao da tarefa: '))
                fila_tarefas.append(descricao)
            case 2:
                for i in range(len(fila_tarefas)):
                    print('Executando: ', fila_tarefas.pop(0))
            case 3:
                break

def simula_pilha():
    # simula uma pilha de tarefas a ser executadas

    print('DIGITE O QUE FAZER: ')
    print('1. Adicionar tarefa')
    print('2. Executar fila de tarefas ')
    print('3. Sair')

    fila_tarefas = []

    while True:
        entrada = int(input("Escolha uma opcao: "))

        match entrada:
            case 1:
                descricao = str(input('Digite a descricao da tarefa: '))
                fila_tarefas.append(descricao)
            case 2:
                for i in range(len(fila_tarefas)):
                    print('Executando: ', fila_tarefas.pop())
            case 3:
                break