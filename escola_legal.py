horas = int(input("Horas de aula: "))
projetos = int(input("Projetos: "))

valor_hora = 35
valor_projetos = 80

salario = (valor_hora * horas) + (valor_projetos * projetos)
print(f"O salario desse professor é R${salario:.2f}")

