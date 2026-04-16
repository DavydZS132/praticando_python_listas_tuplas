# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

# Exemplo de Entrada:

# Digite o nome incorreto: Carlos
# Digite o nome correto: João

# Saída esperada:

# O nome Carlos foi substituído por João.
# Lista atualizada: ['Ana', 'João', 'Pedro']

# lista = ['Ana', 'Carlos', 'Pedro']
# print(lista)

# nome_errado = input('Digite o nome incorreto:')
# nome_correto = input('Digite o nome correto:')

# if nome_errado in lista:
#     indice = lista.index(nome_errado)
#     lista[indice] = nome_correto
#     print(f'O nome Carlos foi substituído por {nome_correto}.')
#     print(lista)

resultados = ["Ana", "Carlos", "Pedro"]
print("Lista original:", resultados)

erro = input("Digite o nome incorreto: ")
if erro in resultados:
    correto = input("Digite o nome correto: ")
    posicao = resultados.index(erro)
    resultados.remove(erro)
    resultados.insert(posicao, correto)
    print(f"O nome {erro} foi substituído por {correto}.")
    print("Lista atualizada:", resultados)
else:
    print("Nome não encontrado.")
