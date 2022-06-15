BONUS_POR_CENTO = 4

nome_vendedor1 = input("Insira o nome do vendedor 1: ")
vendas_vendedor1 = float(input("Insira o valor das vendas do vendedor 1: "))

nome_vendedor2 = input("Insira o nome do funcionário 2: ")
vendas_vendedor2 = float(input("Insira o valor das vendas do vendedor 2: "))

if vendas_vendedor1 == vendas_vendedor2:
    vencedor = "Empate"
elif vendas_vendedor1 > vendas_vendedor2:
    vencedor = nome_vendedor1
else:
    vencedor = nome_vendedor2

total_vendas = vendas_vendedor1 + vendas_vendedor2
premio = total_vendas * (BONUS_POR_CENTO / 100)

print(vencedor)
print(f"R$ {premio:.2f}")