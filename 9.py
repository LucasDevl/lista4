n = int(input("Entre com um número: "))
caracter = input("Entre com um caracter: ")

for i in range(1, n + 1):
    linha = ""
    for j in range(i):
        linha += caracter + " "
    print(linha)
