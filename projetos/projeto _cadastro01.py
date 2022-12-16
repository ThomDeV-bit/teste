def linha():
    print('=' * 20)



from datetime import date


homem = 0
mulher = 0
nao_bin = 0
maioridade = []
menoridade = []
continuar = ' '
cont = 0
nmulher = []
nhomem = []
nbinario = []

while True:


# Verificando nome:

    print('=' * 20)
    nome = str(input('Digite seu nome: ')).split()

# Verificando sexo:

    print('''Sexo:
    [M] Masculino
    [F] Feminino
    [N] Nao binário ''')

    sexo = str(input('Digite seu sexo: ')).upper().strip()[0]

    while sexo not in 'MFN':
        sexo = str(input('Digite seu sexo: ')).upper().strip()[0]

    if sexo == 'M':
        homem += 1
        nhomem += nome

    elif sexo == 'F':
        mulher += 1
        nmulher += nome

    elif sexo == 'N':
        nao_bin += 1
        nbinario += nome

# Verificando idade:

    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maioridade += nome
    else:
        menoridade += nome
    cont += 1

# Opção continuar;
    continuar = str(input('Deseja continuar? [s/n]: ')).upper().strip()[0]
    if continuar == 'N':
        break

linha()
print(f'Foram Realizados \033[1;32m{cont}\033[m Cadatros no dia \033[1;32m{(date.today())}\033[m')

linha()
print(f'''\033[1;34m{homem}\033[m Homem
nome: ''')
for c in range(0,len(nhomem)):
    print(f'\033[1;34m{nhomem[c].title()}\033[m')

linha()
print(f'''\033[1;34m{mulher}\033[m Mulher
nome: ''')
for c in range(0,len(nmulher)):
    print(f'\033[1;34m{nmulher[c].title()}\033[m')

linha()
print(f'''\033[1;34m{nao_bin}\033[m Não binário
nome: ''')
for c in range(0,len(nbinario)):
    print(f'\033[1;34m{nbinario[c].title()}\033[m')

linha()
print('Os Maiores de idade são: ')
for c in range (0,len(maioridade)):
    print(f'\033[1;35m{maioridade[c].title()}\033[m')

linha()
print('Os Menores de idades são')
for c in range(0,len(menoridade)):
    print(f'\033[1;35m{menoridade[c].title()}\033[m') int(