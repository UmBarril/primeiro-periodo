# Nome: João Victor Lima Barros

QUANTIDADE_DE_LOJAS = 80

Lojas = []
for _ in range(QUANTIDADE_DE_LOJAS):
    nome = input("Digite o nome da loja: ")
    tipo_de_produto = input("Digite o tipo de produto vendido: ")
    funcionarios = int(input("Digite a quantidade de funcionários: "))

    loja = [nome, tipo_de_produto, funcionarios]
    Lojas.append(loja)

lj_de_roupa_menos_de_20_funcionarios  = []
funcionarios_em_lojas_de_sapato = 0
for loja in Lojas:
# o código acima também pode ser escrito assim:
# for i in range(len(Lojas)):
#     loja = Lojas[i]
    nome, tipo_de_produto, funcionarios = loja
    # o codigo acima também pode ser escrito assim:
    # nome = loja[0]
    # tipo_prrduto = loja[1]
    # funcionarios = loja[2]

    eh_loja_de_roupa = (tipo_de_produto.lower() in 
                ["roupa", "roupas", "vestuário", "vestimenta", "vestimentas"])
    if eh_loja_de_roupa and funcionarios < 20:
        lj_de_roupa_menos_de_20_funcionarios.append(nome)

    eh_loja_de_sapato = (tipo_de_produto.lower() in 
                ["sapato", "sapatos", "calçado", "calçados"])
    if eh_loja_de_sapato:
        funcionarios_em_lojas_de_sapato += funcionarios

print("\nLojas de roupa com menos de 20 funcionarios:", 
            lj_de_roupa_menos_de_20_funcionarios)
print("Quantidade de funcionarios que trabalham em lojas de sapato:", 
            funcionarios_em_lojas_de_sapato)