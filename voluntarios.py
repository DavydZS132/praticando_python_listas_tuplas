# Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

# Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

# Exemplo de Entrada:

# Digite o nome do voluntário (ou 'sair' para encerrar): Ana
# Digite o nome do voluntário (ou 'sair' para encerrar): João
# Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
# Digite o nome do voluntário (ou 'sair' para encerrar): sair

# Saída esperada:

# Voluntários registrados: ['Ana', 'João', 'Mariana']

voluntarios = []
while True:
    digitar_voluntarios = input('Digite o nome do voluntário (ou sair para encerrar):').strip()

    if digitar_voluntarios.lower():
        print('Programa Finalizado')
        break
    else:
        voluntarios.append(digitar_voluntarios)
        print(f'Voluntario {digitar_voluntarios} adicionado com sucesso.')

for i in voluntarios:
    print(i)