#programa

#regra de Negócio
multaDiaria = 0.75

#entradas
atrasoDias = int(input("Quantos dias de atraso ? "))

print(atrasoDias)
#processamento
multaTotal = atrasoDias * multaDiaria

#saida
print(f"O valor a ser pago é : {multaTotal:.2f}")
