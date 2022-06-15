def MensagemENumeros(mensagem, loops, numeros):
    for _ in range(loops):
        print(mensagem)

        if numeros:
            return
        for i in range(10):
            print(i)

def Soma(numeroA, numeroB):
    return numeroA + numeroB

def SomaVariosNumeros(*numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

print("Olá")
print("Eu sou João")
print("eu estou usando funções")
print("haah")

# HelloWorldENumeros()
# MensagemENumeros("qualquer coisa", 1, False)

# resultado = Soma(10, 20)
resultado = SomaVariosNumeros(1,2)
print(resultado)

