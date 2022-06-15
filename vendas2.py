BONUS_POR_CENTO = 4

# é um exagero fazer uma classe para essa questão... mas por que não?
class Vendedor:
    def perguntar(self):
        self.nome = input("Insira o nome do vendedor: ") 
        self.vendas = float(input("Insira o valor das vendas do vendedor: "))

print("--Dados do vendedor 1--")
vendedor1 = Vendedor()
vendedor1.perguntar()

print("--Dados do vendedor 2--")
vendedor2 = Vendedor()
vendedor2.perguntar()

if vendedor1.vendas == vendedor2.vendas:
    vencedor = "Empate"

elif vendedor1.vendas > vendedor2.vendas:
    vencedor = vendedor1.nome

else:
    vencedor = vendedor2.nome

total_vendas = vendedor1.vendas + vendedor2.vendas
premio = total_vendas * (BONUS_POR_CENTO / 100)

print("--Resultado--")
print(vencedor)
print(f"R$ {premio:.2f}")
