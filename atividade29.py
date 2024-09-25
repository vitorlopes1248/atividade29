# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.
presentes = []
alunos = []

while True:
    aluno = str(input("Digite os nomes dos alunos há(Digite sair parar acabar): "))
    if aluno == 'sair':
        break
    presentes.append(aluno)
    alunos.append(aluno)
    
    

print("Alunos presentes: {}".format(len(presentes)))
print(presentes)
if len(presentes)<5:
    print("Revise a lista de chamada")
else:
    print("Tudo certos")