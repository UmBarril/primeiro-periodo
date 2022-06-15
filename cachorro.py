Animais = [["nome", "idade", "cachorro"], ["nome", "idade", "cachorro"]]

quantCachorros = 0
for animal in Animais:
    tipo = animal[2].lower()
    if tipo in ["cachorro", "cão"]:
        quantCachorros += 1
print("Quantidade de cachorros:", quantCachorros)
