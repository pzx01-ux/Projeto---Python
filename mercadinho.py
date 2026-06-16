import json
try:
    with open ("estoque.json", "r") as f:
        lista_produto = json.load(f)
except:
        lista_produto = []

try:
    with open ("vendas.json", "r") as f:
        lista_vendas = json.load(f)
except:
        lista_vendas = []

try:
    with open ("reposicao.json", "r") as f:
        lista_reposicao = json.load(f)
except:
        lista_reposicao = []



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
        print(f"Produto: {produto2['produto']} | Preço: R${produto2['preco']} | Estoque {produto2['uantidade']}")

def vendas(lista_produto):
    venda_produto = input("Digite o nome do produto: ")
    produto_encontrado = None
    for produto2 in lista_produto:
        if produto2["produto"] == venda_produto:
            produto_encontrado = produto2
            break
    if produto_encontrado is None:
        print("Produto não encontrado.")
        return
    venda_quantidade = int(input("Digite a quantidade: "))
    if produto_encontrado["quantidade"] < venda_quantidade:
        print("Quantidade não disponível em estoque")
        return
    produto_encontrado["quantidade"] -= venda_quantidade
    with open("estoque.json", "w") as f:
        json.dump(lista_produto, f, indent=4, ensure_ascii=False)
    vendas2={
        "produto": produto_encontrado["produto"],
        "quantidade": venda_quantidade,
        "total": produto_encontrado["preco"] * venda_quantidade
    }
    lista_vendas.append(vendas2)
    with open("vendas.json" , "w") as f:
        json.dump(lista_vendas , f, indent=4, ensure_ascii=False)
    return venda_produto, lista_produto

def reposicao(lista_produto):
    reposicao_produto = input("Digite qual nome de produto: ")
    produto_encontrado = None
    for produto2 in lista_produto:
        if produto2["produto"] == reposicao_produto:
            produto_encontrado = produto2
            break
    if produto_encontrado is None:
        print("produto não encontrado.")
        return
    quantidade_reposicao = int(input("Digite a quantidade de reposição: "))
    produto_encontrado["quantidade"] += quantidade_reposicao
    with open("estoque.json", "w") as f:
        json.dump(lista_produto, f, indent=4, ensure_ascii=False)
    reposicao2={
        "produto": produto_encontrado["produto"],
        "quantidade": quantidade_reposicao
    }
    lista_reposicao.append(reposicao2)
    with open("reposicao.json", "w") as f:
        json.dump(lista_reposicao, f, indent=4,
                  ensure_ascii=False)
    return reposicao_produto, lista_produto

def relatorio_do_dia(lista_vendas, lista_reposicao):
    for vendas2 in lista_vendas:
        print(f"vendas \nProduto: {vendas2["produto"]}  \nquantidade: {vendas2["quantidade"]}  \nvalor total: R${vendas2["total"]}")
    for reposicao2 in lista_reposicao:
        print(f"reposição\nProduto: {reposicao2["produto"]}  \nquantidade: {reposicao2["quantidade"]}")

while True:
    print("1- Cadastra Produto")
    print("2- Listar Produto")
    print("3- Realizar Venda")
    print("4- Reposição")
    print("5- Ver Relatório do Dia")
    print("6- Sair")

    opcao = int(input("Digite a Opção Desejada: "))

    if opcao == 1:
       lista_produto = cadastra_produto ()
    elif opcao == 2:
        ver_lista(lista_produto)
    elif opcao == 3:
        vendas(lista_produto)
    elif opcao == 4:
        reposicao(lista_produto)
    elif opcao == 5:
        relatorio_do_dia(lista_vendas, lista_reposicao)
    elif opcao == 6:
        break