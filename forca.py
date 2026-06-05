from random import choice

palavras = ["python", "javascript", "televisão", "júepiter", "satélite", "nova zelândia", "macaxeira"]
palavra = choice(palavras)
letras_corretas = []
letras_erradas = []
tentativas = 6

print(f"Bem-vindo ao jogo da forca! A palavra tem {len(palavra)} letras.")

while tentativas > 0:
    for letras in palavra:
        if letras in letras_corretas:
            print(letras, end=" ")
        else:
            print("_", end=" ")
    letra = input("Digite uma letra: ")
    if letra in palavra:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        if tentativas == 0:
            print(f"acabaram as tentativas! A palavra era {palavra}")
            break
    if letras_erradas:
        print(f"\nLetras erradas: {', '.join(letras_erradas)}")
    if all(letra in letras_corretas for letra in palavra):
        print(f"\nParabéns! Você ganhou! A palavra era {palavra}")
        break