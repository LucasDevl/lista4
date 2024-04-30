import random

print("a) Números inteiros do intervalo [0, 100]:")
for i in range(101):
    print(i, end=" ")
print("\n")

print("b) Números pares do intervalo [20, 50]:")
for i in range(20, 51, 2):
    print(i, end=" ")
print("\n")

print("c) Números inteiros do intervalo [25, 70] em ordem decrescente:")
for i in range(70, 24, -1):
    print(i, end=" ")
print("\n")

print("d) Números ímpares do intervalo [25, 95] em ordem decrescente:")
for i in range(95, 24, -1):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

print("e) Ler 15 números e escrever a soma e a média:")
soma = 0
for _ in range(15):
    numero = float(input("Digite um número: "))
    soma += numero

media = soma / 15
print("Soma dos números:", soma)
print("Média dos números:", media)
print("\n")

print("f) Ler 10 números inteiros e escrever a quantidade de números pares e ímpares:")
pares = 0
impares = 0
for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
print("\n")

print("g) Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem POSITIVO, NEGATIVO, ou NULO:")
positivos = 0
negativos = 0

for _ in range(20):
    numero = random.randint(-10, 10)
    if numero > 0:
        print(numero, "POSITIVO")
        positivos += 1
    elif numero < 0:
        print(numero, "NEGATIVO")
        negativos += 1
    else:
        print(numero, "NULO")

print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("\n")

print("h) Ler n números e imprimir no final a soma dos números lidos:")
n = int(input("Digite a quantidade de números a serem lidos: "))
soma = 0
for _ in range(n):
    numero = float(input("Digite um número: "))
    soma += numero

print("Soma dos números lidos:", soma)
