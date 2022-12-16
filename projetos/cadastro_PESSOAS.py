def menu():
    print('''        \033[32m[{:^10}]\033[m

    [1] Cadastrar Pessoas
    [2] Listar pessoas cadastradas
    [3] Remover cadastro 
    [4] Finalizar'''.format('MENU'))


def linha():
    print('='*30)


# VARIAVEIS

lista = []
dados = dict()
opçao = 0
continuar = 'S'


# CADASTRANDO NOMES

while True:
    linha()
    menu()
    opçao = int(input('Escolha uma Opção do MENU: '))
    if opçao == 1:
        while True:
            dados.clear()
            dados['nome'] = str(input('Nome: '))
            dados['idade'] = int(input('Idade: '))
            dados['cpf'] = str(input('Cpf: '))
            lista.append(dados.copy())

            continuar = ''
            continuar = str(input('Quer continuar cadastrando? [S/N]: '))
            if continuar == 'N':
                break

# LISTANDO NOMES


    if opçao == 2:
        print('No.{:<12} {:^50} {:50}\n'.format('Nome','Idade','Cpf'))
        for i,p in enumerate(lista):
            print(f'\033[32m{i}\033[m  {p["nome"].title():<16} {p["idade"]:^40} {p["cpf"]}')


# EXCLUINDO CADASTRO


    if  opçao == 3:
        if len(lista) == 0:
             print('Lista de Cadastros Vazia')
        else:
            print('No.{:<12} {:^50} {:50}\n'.format('Nome', 'Idade', 'Cpf'))
            for i, p in enumerate(lista):
                print(f'\033[32m{i}\033[m  {p["nome"].title():<16} {p["idade"]:^40} {p["cpf"]}')
            excluir = int(input('Digite o numero do cadastro que deseja excluir:'))
            del lista[excluir]
    linha()



    # ENCERRANDO PROGRAMA
    if opçao == 4:
        break
        













