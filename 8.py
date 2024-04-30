def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

continuar = 's'

while continuar.lower() == 's':
    numero = int(input("Entre com um número: "))
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
    continuar = input("Calcular outro número (s/n)? ")

print("Fim do programa.")
