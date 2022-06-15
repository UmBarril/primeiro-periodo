PRECO_REFEICAO_KG = 20
PRECO_REFEICAO_GRAMA = PRECO_REFEICAO_KG / 1000
PESO_PRATO_VAZIO = 230

peso_total = int(input("Digite o peso do prato (em gramas): "))

peso_corrigido = peso_total - PESO_PRATO_VAZIO

preco_cobrar = peso_corrigido * PRECO_REFEICAO_GRAMA

print(f"O cliente deve pagar R${preco_cobrar:.2f}")
