import os

def verifica_arquivo(nome_arquivo):
    return os.path.isfile(nome_arquivo)

def adicionar(contatos):
    print('Se deseja parar digite "parar".')
    while True:
        nome = input('Digite o nome do contato: ')
        if nome == 'parar':
            break
        telefone = input('Digite o número de telefone do contato: ')
        if telefone == 'parar':
            break

        contatos[nome] = telefone

    with open('arquivos(agenda).txt', 'a') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))
    return contatos

def visualizar():
    with open('arquivos(agenda).txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def excluir(contatos):
    parar = True
    print('Se deseja parar digite "parar".')
    while parar:
        nome = input('Digite o nome do contato que deseja excluir da agenda: ')
        if nome == 'parar':
            break
        elif nome in contatos:
            del contatos[nome]
        else:
            print('Esse contato não está na agenda.')

    with open('arquivos(agenda).txt', 'w') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))

    return contatos

def atualizar(contatos):
    parar = True
    print('Se deseja parar digite "parar": ')
    while parar:    
        nome = str(input('Digite qual o nome que deseja alterar da agenda: '))
        if nome == 'parar':
            break
        if nome in contatos:
            nome_cha = str(input('Digite qual o novo nome de {} que deseja alterar: '.format(nome)))
            if nome_cha == 'parar':
                break
            telefone_cha = input('Digite qual o novo valor de {} que deseja alterar: '.format(nome))
            if telefone_cha == 'parar':
                break

            contatos[nome] = telefone_cha
            contatos[nome_cha] = contatos.pop(nome)
        else:
            print('O contato nao esta na agenda.')

    with open('arquivos(agenda).txt', 'w') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))

    return contatos

if __name__ == '__main__':
    sair = True
    contatos = {}
    nome_arquivo = 'arquivos(agenda).txt'
    while sair:
        arquivo_existe = verifica_arquivo(nome_arquivo)
        if arquivo_existe:
            print('[0] Adicionar contato\n[1] Visualizar a agenda telefônica\n[2] Excluir contato da agenda\n[3] Atualizar contato na agenda\n[4] Sair da interface da agenda telefônica')
            decisao = int(input('Digite o que deseja fazer na agenda telefônica: '))
            if decisao == 0:
                contatos = adicionar(contatos)
            elif decisao == 1:
                visualizar()
            elif decisao == 2:
                contatos = excluir(contatos)
            elif decisao == 3:
                contatos = atualizar(contatos)
            else:
                break
        else:
            print('A agenda telefônica ainda não foi criada. Vamos começar adicionando contatos: ')
            contatos = adicionar(contatos)
