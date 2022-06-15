valor_original = int(input("Escreva o peso do prato (em gramas): "))
valor_corrigido = valor_original - 230
preco_final = (valor_corrigido / 1000) * 20

print(f"Resultado: ${preco_final:.2f}")
