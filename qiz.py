qiz = {
    "A capital do Brasil?": "Brasília",
    "Quantos continentes existem?": "7",
    "Qual é o nome do satélite natural da Terra?": "Lua",
    "Qual é o maior planeta do sistema solar?": "Júpiter",
    "Qual é  o maior oceano do mundo?": "Oceano Pacífico",
}

pontuação = 0

for pergunta, resposta in qiz.items():
    resposta_usuario = input(pergunta + "").strip().lower()
    if resposta_usuario == resposta.lower():
        print("Resposta correta!")
        pontuação += 1
    else:
        print(f"Resposta incorreta! A resposta correta é: {resposta}")

if pontuação == 5:
    print("Parabéns! Você acertou todas as perguntas!")

elif pontuação >= 3 and pontuação <= 4:
    print("muito bom!")

elif pontuação >= 1 and pontuação <= 2:
    print("Você precisa estudar mais.")

elif pontuação == 0:
    print("Que pena! Você não acertou nenhuma pergunta. Tente novamente!")

poncentagem = (pontuação / 5) * 100
    
print(f"Sua pontuação final é: {pontuação} de 5 ({poncentagem:.0f}%)")
