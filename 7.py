nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nomes_ordenados = sorted(nomes)

print("O primeiro nome em ordem alfabética é:", nomes_ordenados[0])
