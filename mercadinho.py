import json
produto = 0
valor = 0
try:
    with open ("estoque.json", "r") as f:
        lista_produto = json.load(f)
except:
        lista_produto = []


def cadastra_produto():
    produto = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o valor do produto: "))
    q_estoque = int(input("Digite o quantidade em estoque: "))
    produto2 = {
        "produto": produto , 
        "preco": valor ,
        "quantidade":  q_estoque
    }
    lista_produto.append(produto2)
    with open("estoque.json" , "w") as f:
        json.dump(lista_produto , f, indent=4, ensure_ascii=False)
    return lista_produto

def ver_lista(lista_produto):
    for produto2 in lista_produto:
        print(f"Produto: {produto2["produto"]} | Preço: R${produto2["preco"]} | Estoque {produto2["quantidade"]}")

while True:
    print("1- Cadastra Produto")
    print("2- Listar Produto")
    print("3- Realizar Venda")
    print("4- Ver Relatório do Dia")
    print("5- Sair")

    opcao = int(input("Digite a Opção Desejada: "))

    if opcao == 1:
       lista_produto = cadastra_produto ()
    elif opcao == 2:
        ver_lista(lista_produto)
