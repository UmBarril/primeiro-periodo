preco_un = float(input("Digite o preço do rodízio: "))
num_convidados = int(input("Digite o número de convidados: "))

quant_descontos = num_convidados // 10

preco_sem_disconto = num_convidados * preco_un

total = preco_sem_disconto - (quant_descontos * preco_un)

print("Total a pagar: ", total)
