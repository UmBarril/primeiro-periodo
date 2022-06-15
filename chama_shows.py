import Shows

QUANTIDADE_DE_SHOWS = 20

valor_total = 0 
bandas = []
for _ in range(QUANTIDADE_DE_SHOWS):
    banda = input("Digite o nome da banda: ")
    duracao = int(input("Digite a duração do show: "))
    cache = Shows.CalculaCacheBanda(banda, duracao)
    valor_total += cache
    if duracao > 6:
        bandas.append(banda)

print("Valor total: R$", valor_total)
for b in bandas:
    print(f"A banda {b} teve uma duração maior que 6h")