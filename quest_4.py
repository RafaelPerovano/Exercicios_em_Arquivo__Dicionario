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

procurar = str(input('Digite o nome de quem deseja verificar os dados: '))
if procurar in dados:
    print(dados[procurar])
else:
    print('Esse nome nao existe no banco de dados')
