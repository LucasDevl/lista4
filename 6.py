import random

# Sortear 5 valores entre 0 e 100
valores = [random.randint(0, 100) for _ in range(5)]

# Encontrar o menor valor
menor_valor = min(valores)

# Encontrar o maior valor
maior_valor = max(valores)

# Calcular a média
media = sum(valores) / len(valores)

# Imprimir os resultados
print("Valores sorteados:", valores)
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Média dos valores:", media)
