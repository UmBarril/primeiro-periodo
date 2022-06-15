META_CADERNOS = 90
META_MOCHILAS = 60

cadernos = 0
mochilas = 0
continuar = True
while continuar:
    tipo_material = input("Digite o tipo de material: ").lower()
    if tipo_material not in ["mochila", "caderno"]:
        print("Entrada inválida. Digite \"mochila\" ou \"caderno\" para doar.")
        continue

    quantidade_str = input("Digite a quantidade: ")
    if not quantidade_str.isdigit():
        print("Entrada inváliada. Digite uma quantidade por favor.")
        continue

    quantidade = int(quantidade_str)
    if tipo_material == "mochila":
        mochilas += quantidade
    else:
        cadernos += quantidade

    continuar = input("Deseja continuar doando?: ").lower() == "sim"  

sucesso_cadernos = cadernos >= META_CADERNOS
sucesso_mochilas = mochilas >= META_MOCHILAS
sucesso_total = sucesso_cadernos and sucesso_mochilas

if sucesso_total:
    print("Sucesso Total")
elif sucesso_cadernos or sucesso_mochilas:
    print("Sucesso parcial")
else:
    print("Fracasso")