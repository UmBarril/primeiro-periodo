estados = [["Santa Catarina", "Sul", 10, 100000], ["São Paulo", "Sudeste", 10000, 10000]]

# questão A
print("Estados do sul:", end=" ")
for estado in estados:
    nome, regiao, municipios, habitantes = estado
    if regiao.lower() == "sul":
        print(f"'{nome}'", end=' ')
print()
    
# questão B
print("Estados com mais de 100 municipios:", end=" ")
for estado in estados:
    nome, regiao, municipios, habitantes = estado
    if municipios > 100:
        print(f"'{nome}'", end=' ')
print()
    
# questão C
num_municipios_norte = 0
for estado in estados:
    nome, regiao, municipios, habitantes = estado
    if regiao.lower() == "norte":
        num_municipios_norte += municipios
print("Quantidade de cidades dos estados da região Norte:", num_municipios_norte)

# questão D
estados_centrooeste_menos_500hab = 0
for estado in estados:
    nome, regiao, municipios, habitantes = estado
    if regiao.lower() == "centro-oeste" and habitantes > 500000:
        estados_centrooeste_menos_500hab += 1
print("Quantidade de estados da região Centro-Oeste com mais de 500 mil habitantes:", 
            estados_centrooeste_menos_500hab)

# questão E
num_hab_sudeste = 0
num_estados_sudeste = 0
for estado in estados:
    nome, regiao, municipios, habitantes = estado
    if regiao.lower() == "sudeste":
        num_hab_sudeste += habitantes
        num_estados_sudeste += 1

# evitar divisão por zero
media_hab_sudeste = 0
if num_estados_sudeste > 0:
    media_hab_sudeste = num_hab_sudeste / num_estados_sudeste

print("Quantidade média de habitantes dos estados da região Sudeste:", media_hab_sudeste)

