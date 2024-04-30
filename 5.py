def calcular_media_unisinos(nota_a, nota_b):
    return (nota_a + nota_b) / 2

def verificar_aprovacao_unisinos(media):
    if media >= 6.0:
        return True
    else:
        return False

def substituir_nota(nota_a, nota_b, escolha, nota_c):
    if escolha == 'A':
        nota_a = nota_c
    elif escolha == 'B':
        nota_b = nota_c
    return calcular_media_unisinos(nota_a, nota_b)

num_alunos = int(input("Digite o número de alunos: "))

soma_notas = 0

for aluno in range(1, num_alunos + 1):
    nota_a = float(input("Digite a nota do Grau A do aluno {}: ".format(aluno)))
    nota_b = float(input("Digite a nota do Grau B do aluno {}: ".format(aluno)))

    media = calcular_media_unisinos(nota_a, nota_b)

    if verificar_aprovacao_unisinos(media):
        print("Aluno {} APROVADO".format(aluno))
    else:
        nota_c = float(input("Digite a nota do Grau C do aluno {}: ".format(aluno)))
        escolha = input("Qual nota deseja substituir (A ou B)? ").upper()

        nova_media = substituir_nota(nota_a, nota_b, escolha, nota_c)

        if verificar_aprovacao_unisinos(nova_media):
            print("Aluno {} APROVADO".format(aluno))
        else:
            print("Aluno {} REPROVADO".format(aluno))

    soma_notas += media

media_geral = soma_notas / num_alunos
print("Média geral dos alunos:", media_geral)
