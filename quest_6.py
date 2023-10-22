c = 0
idade_total = 0

with open('arquivos(estudantes).txt', 'r') as arquivo:
    for linha in arquivo:
        idade = int(linha.split('idade: ')[1].split(', ')[0].strip())
        idade_total += idade
        c += 1

media = idade_total/c
print(f"A media das idades é: {media:.1f}")