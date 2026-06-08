try:
    with open("saldo.txt" , "r") as f:
        saldo = float(f.read())
except:
    saldo = 0.0
extrato = []
valord = 0
valors = 0

def ver_saldo(saldo):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
def depositar(saldo, extrato):
    valord = int(input("Digite o valor a ser depositado: "))
    extrato.append(f"Deposito: R$ {valord:.2f}")
    with open("extrato.txt" , "a") as f:
        f.write(f"deposito: R$ {valord:.2f}\n")
    return saldo + valord, extrato
def sacar(saldo, extrato, valors):
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
        with open("saldo.txt" , "w") as f:
            f.write(str(saldo))
        
        with open("extrato.txt" , "a") as f:
            f.write(f"Saque: R$ {valors:.2f}\n")

    return saldo, extrato
def ver_extrato(extrato, saldo):
    try:
        with open("extrato.txt" , "r") as f:
            print(f.read())
    except:
        print("Nheuma movimentação encotrda.")
    print(f"saldo atual: R$ {saldo:.2f}")
    print("Extrato:")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    

while True:
    print('1- ver saldo')
    print("2- Depositar")
    print("3- sacar")
    print("4- Extrato")

    opcao = int(input("Digite a opcao desejada:"))

    if opcao == 1:
        ver_saldo(saldo)
    elif opcao == 2:
        saldo, extrato = depositar(saldo, extrato)
        ver_saldo(saldo) 
    elif opcao == 3:
        saldo, extrato = sacar(saldo, extrato, valors)
    elif opcao == 4:
        ver_extrato(extrato, saldo)