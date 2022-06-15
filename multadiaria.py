# Pergunta na tela "Quantos dias foram de atraso?" e volta com a resposta do usuario
dias_atraso_string = input("Quantos dias foram de atraso? ")

# Transforma a resposta do usuario em int
dias_atraso_int = int(dias_atraso_string)

# Valor da multa por dia
multa = 0.75

# Gera o valor final
valor_final = dias_atraso_int * multa

# Mostra na tela o valor_final com duas casas decimais
print(f"{valor_final:.2f}")
