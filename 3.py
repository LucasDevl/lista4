def tabuada_multiplicacao(numero):
    print("Tabuada de multiplicação do número", numero)
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

continuar = 's'

while continuar.lower() == 's':
    numero = int(input("Entre com um número de 1 a 9: "))
    
    if 1 <= numero <= 9:
        tabuada_multiplicacao(numero)
    else:
        print("Número inválido. O número deve estar entre 1 e 9.")
    
    continuar = input("Calcular outro número (s/n)? ")

print("Fim do programa.")
