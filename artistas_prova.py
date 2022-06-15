# Nome: João Victor Lima Barros

NUM_ARTISTAS = 300 
ORCAMENTO = 5000.00
VALOR_CARO = 10000.00

Artistas = []
for _ in range(NUM_ARTISTAS):
    nome = input("Digite o nome do artista: ")
    tipo_de_artista = input("Digite o tipo de artista: ")
    dinheiro_cobrado = float(input("Digite o cachê cobrado: "))
    cidade_de_origem = input("Digite a cidade de origem: ")

    artista = [nome, tipo_de_artista, dinheiro_cobrado, cidade_de_origem]
    Artistas.append(artista)

bandas_da_regiao_escolhidas = []
quantidade_de_cantoras = 0
valor_cobrado_pelas_cantoras = 0
cidades_de_cantores_caros = []
for artista in Artistas:
# o código acima também pode ser escrito assim:
# for i in range(len(Artistas)):
#     artista = Artistas[i]
    nome, tipo_de_artista, dinheiro_cobrado, cidade_de_origem = artista 
    # o codigo acima também pode ser escrito assim:
    # nome = artista[0]
    # tipo_de_artista = artista[1]
    # dinheiro_cobrado = artista[2]
    # cidade_de_origem = artista[3]

    eh_banda = tipo_de_artista.lower() == "banda"
    eh_da_regiao = (cidade_de_origem.lower() in 
                        ["mamanguape", "rio tinto", "mataraca"])
    esta_dentro_do_orcamento = dinheiro_cobrado < ORCAMENTO
    if eh_banda and eh_da_regiao and esta_dentro_do_orcamento:
        bandas_da_regiao_escolhidas.append(nome)

    eh_cantora = tipo_de_artista.lower() == "cantora"
    if eh_cantora:
       quantidade_de_cantoras += 1
       valor_cobrado_pelas_cantoras += dinheiro_cobrado 

    eh_cantor = tipo_de_artista.lower() == "cantor"
    eh_cantor_caro = dinheiro_cobrado > VALOR_CARO
    cidade_nao_esta_na_lista = (cidade_de_origem.lower() not in
                                    cidades_de_cantores_caros)
    if eh_cantor and eh_cantor_caro and cidade_nao_esta_na_lista:
        cidades_de_cantores_caros.append(cidade_de_origem.lower())
    
media_cache_cantoras = 0.00
if quantidade_de_cantoras > 0.00:
    media_cache_cantoras = valor_cobrado_pelas_cantoras / quantidade_de_cantoras

print()
print(f"Bandas da região que cobram menos que R${ORCAMENTO:.2f}:", 
                    bandas_da_regiao_escolhidas)
print(f"Cachê médio cobrado pelas cantoras: R${media_cache_cantoras:.2f}")

cidades_de_cantores_caros_formatada = [cidade.capitalize() 
                                        for cidade in cidades_de_cantores_caros]

print(f"Cidades que têm um (ou mais) cantores cobram mais de R${VALOR_CARO:.2f} por show:",
    cidades_de_cantores_caros_formatada)
