tarefas=[]
while True:
    print("1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- remover tarefas")
    print("4- Sair")
    
    opcao=int(input("Digite a opção desejada: "))

    if opcao==1:
        tarefa=input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    
    elif opcao==2:
        print('lista de tarefas:')
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
        input("\n\Pressione enter para continuar...")

    elif opcao==3:
        indece=int(input("Digite o numero de tarefa a ser removida:  "))
        if 0<indece<=len(tarefas):
            tarefas.pop(indece-1)
            print("tarefas removida com sucesso!")
    elif opcao==4:
        print("saindo do programa...")
        break



