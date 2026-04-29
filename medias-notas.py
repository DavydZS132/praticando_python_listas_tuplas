# A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.

# Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

# Exemplo de Entrada:

# Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

# Saída esperada:

# Média final da turma: 7.88

entrada = input('Digite as notas dos alunos separadas por vírgula:')

lista_notas = [float(n.strip()) for n in entrada.split(',')]
soma = 0
quantidade = 0

for nota in lista_notas:
    soma += nota
    quantidade += 1

media = soma / quantidade

print(f'Media: {media}')