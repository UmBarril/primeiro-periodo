quantidadeFaltaEstoque = 0
itemMaisCaro = ""
precoItemMaisCaro = 0
vendaTotalMedicamentos = 0
for _ in range(2):
    nome = input("Digite o nome do produto: ").lower()
    tipo = input("Digite o tipo do produto: ").lower()
    while tipo not in ["higiene", "medicamento"]:
        print("Tipo inválido. Digite \"higiene\" ou \"medicamento\" para definir um tipo")
        tipo = input("Digite o tipo do produto: ").lower()
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite o quantidade do produto: "))

    if quantidade < 5:
        quantidadeFaltaEstoque += 1

    if tipo == "higiene" and preco > precoItemMaisCaro:
        itemMaisCaro = nome
        precoItemMaisCaro = preco

    if tipo == "medicamento":
        vendaTotalMedicamentos += preco * quantidade

print(quantidadeFaltaEstoque, "produtos faltam estoque")
print(itemMaisCaro, "é o produto mais caro")
print("A fármacia irá receber", vendaTotalMedicamentos, "pelos medicamentos")
