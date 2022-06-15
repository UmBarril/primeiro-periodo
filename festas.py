mulheres_que_gostam_de_sao_joao = 0

festa = None
sexo = None
while festa != "" or sexo != "":
    festa = input("Festa preferida: ").lower()
    sexo = input("Sexo: ").lower()
    if festa == "carnaval":
        print("Fevereiro")
    elif festa == "são joão":
        if sexo == "feminino":
            mulheres_que_gostam_de_sao_joao += 1
        print("Junho")
    else:
        print("Dezembro")
print(f"Mulheres que preferem São João: {mulheres_que_gostam_de_sao_joao}")