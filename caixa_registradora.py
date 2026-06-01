compras = []
total = 0
while True:
    Produto = str(input("Digite o nome do produto: "))
    if Produto == "fim":
        break
    Preco = float(input("Digite o preço do produto: "))
    compras.append((Produto, Preco))
    total += Preco

print("---Lista de Compras---")
for i, (produto, preco) in enumerate(compras):
    print(f"{i+1}. {produto}: R$ {preco:.2f}")

print(f"Total da compra: R$ {total:.2f}")

if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    print(f"Desconto 10%: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_final:.2f}")