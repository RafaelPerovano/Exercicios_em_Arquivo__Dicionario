def exclui(dados):
    nome_cha = str(input('Digite qual nome deseja excluir dos dados: '))
    if nome_cha in dados:
        del dados[nome_cha]
        nomes.remove(nome_cha)
    else:
        print('Esse nome nao esta nos dados')
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

excluir = str(input('Digite "excluir" se quiser alterar algum registro: '))

if excluir == 'excluir':
    dados = exclui(dados)

with open ('arquivos(estudantes).txt', 'w') as arquivos:
    for nome in nomes:
        arquivos.write('nome: {}, idade: {}, curso: {}\n'.format(nome, dados[nome]['idade'], dados[nome]['curso']))