curso_total = {}

with open('arquivos(estudantes).txt', 'r') as arquivo:
    for linha in arquivo:
        curso = linha.split('curso: ')[1].split(', ')[0].strip()

        if curso in curso_total:
            curso_total[curso] = curso_total[curso] + 1
        else:
            curso_total[curso] = 1
print(curso_total)
