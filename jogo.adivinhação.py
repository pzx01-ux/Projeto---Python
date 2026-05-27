from  random import randint

resposta = randint(1, 100)

Tentativas = 0

print('Bem-vindo ao jogo de adivinhação!')

print('O computador escolheu um número entre 1 e 100. Tente adivinhar qual é!')
palpite = int(input('Digite um número entre 1 e 100: '))



while palpite != resposta:
    Tentativas += 1

    if palpite < resposta:
        print('O número é maior do que o seu palpite.')
    elif palpite > resposta:
        print('O número é menor do que o seu palpite.')

    palpite = int(input('Digite outro número: '))
    
print(f'Parabéns! Você acertou o número! o computador escolheu {resposta} e você digitou {palpite}.')

if Tentativas <= 5:
    print(f'Você fez {Tentativas} tentativas execelentes!')
elif Tentativas >= 6 and Tentativas <= 10:
    print(f'Você fez {Tentativas} tentativas muito bom!')
elif Tentativas >= 10:
    print(f'Você fez {Tentativas} tentativas, tente melhorar na próxima vez!') 
