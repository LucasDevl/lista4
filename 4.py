divisor = int(input("Entre com o valor do divisor: "))
inicio_intervalo = int(input("Início do intervalo: "))
final_intervalo = int(input("Final do intervalo: "))

print("Números divisíveis por", divisor, "no intervalo de", inicio_intervalo, "a", final_intervalo, ":")

for numero in range(inicio_intervalo, final_intervalo + 1):
    if numero % divisor == 0:
        print(numero, end=" ")
