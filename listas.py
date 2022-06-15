numero = []
tamLista = 10

for _ in range(tamLista):
    n = int(input("Número: "))
    while (n in numero):
       n = int(input("Já temos esse número. Escolha outro: ")) 
    numero.append(n)

# print("Essa foi a lista informada: ")
# print(numero)
# somaPares = sum(n for n in numeros if n % 2 == 0)
#
# OU
#
# somaPares = 0
# for i in range(len(numero)):
#     if numero[i] % 2 == 0:
#         somaPares += numero[i]
# OU
#
somaPares = 0
for n in numero:
    if n % 2 == 0:
        somaPares += n

# quantPositivos = sum(n >= 0 for n in numero)
#
# OU
#
# quantPositivos = 0
# for i in range(len(numero)):
#     if numero[i] >= 0:
#         quantPositivos += 1
#
# OU
#
quantPositivos = 0
for n in numero:
    if n >= 0:
        quantPositivos += 1

print("Soma dos pares:", somaPares)
print("Quantidade de números positivos:", quantPositivos)
