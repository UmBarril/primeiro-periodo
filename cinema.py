entradas_gratuitas = 0
continuar = ""
while continuar != "não":
	idade = int(input("Digite a idade do cliente: "))
	continuar = input("deseja continuar? ").lower()
	if idade <= 10 or idade > 60:
		entradas_gratuitas += 1

print("Total de entradas gratuitas: ", entradas_gratuitas)

