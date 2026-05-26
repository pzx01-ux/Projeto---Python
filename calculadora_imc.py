NOME = input("Digite seu nome: ")
PESO = float(input("Digite seu peso (kg): "))
ALTURA = float(input("Digite sua altura (m): "))

IMC = PESO / (ALTURA ** 2)

if IMC < 18.5:
    print(f"{NOME}, seu IMC é: {IMC:.2f} abaixo de peso")
elif 18.5 <= IMC < 25:
    print(f"{NOME}, seu IMC é: {IMC:.2f} peso normal")
elif 25 <= IMC < 30:
    print(f"{NOME}, seu IMC é: {IMC:.2f} sobrepeso")
elif 30 <= IMC < 39.9:
    print(f"{NOME}, seu IMC é: {IMC:.2f} obesidade")
else:
    print(f"{NOME}, seu IMC é: {IMC:.2f} obesidade grave")