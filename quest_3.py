def mudar(dados):
    nome_cha = str(input('Digite qual nome deseja alterar os dados: '))
    if nome_cha in dados:
        idade_cha = int(input('Digite qual a nova idade de {} que deseja alterar: '.format(nome_cha)))
        curso_cha = str(input('Digite qual o novo curso de {} que deseja alterar: '.format(nome_cha)))
        dados[nome_cha]['idade'] = idade_cha
        dados[nome_cha]['curso'] = curso_cha
    return dados

c = 0
nomes = []
dados = {}

with open('arquivos(estudantes).txt', 'r') as arquivo:
    for linha in arquivo:
        nome = linha.split('nome: ')[1].split(', ')[0].strip()
        idade = linha.split('idade: ')[1].split(', ')[0].strip()
        curso = linha.split('curso: ')[1].split(', ')[0].strip()

        nomes.append(nome)
        novos_dados = {nome: {'idade': idade, 'curso': curso}}
        dados.update(novos_dados)
        c += 1

for n in nomes:
        print('nome: {} | idade: {} | curso: {}\n'.format(n, dados[n]['idade'], dados[n]['curso']))

alterar = str(input('Digite "alterar" se quiser alterar algum registro: '))

if alterar == 'alterar':
    dados = mudar(dados)

with open ('arquivos(estudantes).txt', 'w') as arquivos:
    for nome in nomes:
        arquivos.write('nome: {}, idade: {}, curso: {}\n'.format(nome, dados[nome]['idade'], dados[nome]['curso']))