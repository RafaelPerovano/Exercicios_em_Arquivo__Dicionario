tam = int(input('Digite quantos alunos deseja inserir: '))
dadas ={}
nomes = []
c = 0
while c <= tam-1:
    nome = str(input('Digite o nome da aluno: '))
    idade = int(input('Digite a idade da aluno: '))
    curso = str(input('Digite o curso que o aluno está cursanda: '))

    nomes.append(nome)
    novos_dadas = {nome:{'idade':idade,'curso':curso}}
    dadas.update(novos_dadas)
    c += 1
c = 0
with open ('arquivos(estudantes).txt', 'w') as arquivos:
    while c <= tam-1:
        arquivos.write('nome: {}, idade: {}, curso: {}\n'.format(nomes[c], dadas[nomes[c]]['idade'], dadas[nomes[c]]['curso']))
        c += 1