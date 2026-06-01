agenda = {}
while True:
    print("1- Adicinar contato")
    print("2- Buscar contato")
    print("3- Listar contatos")
    print("4- Remover contato")
    print("5- Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do contato:")
        telefone = input("Digite o telefone do contato:")
        tamanho = len(telefone)
        if tamanho != 9:
            print("Telefone inválido, tente novamente.")
            continue
        email = input("Digite o mail do contato:")
        agenda[nome] = {"telefone": telefone, "email": email}
        
        print("Contato adicionado com sucesso!")
    
    elif opcao == 2:
        nome = input("Digite o nome do contato que deseja buscar:")
        if nome in agenda:
            print(f"nome: {nome}")
            print(f"telefone: {agenda[nome]['telefone']}")
            print(f"email: {agenda[nome]['email']}")
        else:
            print("Contato não encontrado.")
    
    elif opcao == 3:
        print("Lista de contatos:")
        for nome, info in agenda.items():
            print(f"nome: {nome}")
            print(f"telefone: {info['telefone']}")
            print(f"email: {info['email']}")
            print("-" * 20)

    elif opcao == 4:
        nome = input("Digite o nome do contato que deseja remover:")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")
    
    elif opcao == 5:
        break