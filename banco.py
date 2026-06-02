saldo = 0.0
extrato = []

while True:
    print("1- Ver saldo")
    print("2- Depositar")
    print("3- Sacar")
    print("4- Extrato")
    print("5- Sair")

    opcao = int(input("Digite a opcao desejada:"))

    if opcao == 1:
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == 2:
        valord = int(input("Digite o valor a ser depositodo: "))
        extrato.append(f"Deposito: R$ {valord:.2f}")
        if valord <= 0:
            print("Valor de deposito deve ser maior que zero.")
        else:
            saldo += valord
            print(f"Deposito realizado com sucesso! seu novo saldo é: R$ {saldo:.2f}")

    elif opcao == 3:
        print("Notas depinivel para saque: R$ 20,50,100,200")
        valors = int(input("Digite o valor a ser sacado:"))

        restante = valors

        t200 = restante // 200
        restante -= t200 * 200

        t100 = restante // 100
        restante -= t100 * 100

        t50 = restante // 50
        restante -= t50 * 50

        t20 = restante // 20

        print(f"Notas de R$ 200: {t200}")
        print(f"Notas de R$ 100: {t100}")
        print(f"Notas de R$ 50: {t50}")
        print(f"Notas de R$ 20: {t20}")
                
        if valors <= 0:
            print("Valor de saque deve ser maior que zero.")
        elif valors > saldo:
            print("saldo insuficiente para realizar o saque.")
        else:
            saldo -= valors
            extrato.append(f"Saque: R$ {valors:.2f}")
            print(f"Saque realizado com sucesso! seu novo saldo é: R$ {saldo:.2f}")
    
    elif opcao == 4:
        print("Extrato:")
        for item in extrato:
            print(item)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao ==5:
        break