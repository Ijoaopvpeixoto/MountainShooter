# Criando um programa de gerenciamento de tarefas

tarefas = []
NOME_ARQUIVO = "tarefas.txt" # Criamos uma constante para o nome do arquivo

def salvar_tarefas():
    with open(NOME_ARQUIVO, 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")
    print("Tarefas salvas com sucesso!")

def carregar_tarefas():
    try:
        with open(NOME_ARQUIVO, 'r') as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip()) # Adiciona cada linha como uma tarefa
        print("Tarefas carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado. Iniciando com lista vazia.")

carregar_tarefas() # chama a funcão para carregar as tarefas

while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa) # Adiciona a tarefa à lista
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif escolha == "2":
        if not tarefas: # Verifica se a lista de tarefas está vazia
            print("Não há tarefas na lista.")
        else:
            print("Suas tarefas: ")
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa}")

    elif escolha == "3":
        if not tarefas:
            print("Não há tarefas para remover.")
        else:
            print("Suas tarefas: ")
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa}")

            try:
                numero_para_remover = int(input("Digite o número da tarefa para remover: "))
                if 1 <= numero_para_remover <= len(tarefas):
                    tarefa_removida = tarefas.pop(numero_para_remover - 1)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif escolha == "4":
        salvar_tarefas() # Chama a funcão para salvar antes de sair
        print("Saindo do programa...")
        break #Saindo do programa

    else:
        print("Escolha inválida :( \n Tente novamente.")