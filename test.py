print('---------------RPG BASICO---------------')
print('Quer jogar?')
print('Sim ou Não?')
opcao = str(input())

if opcao =='Não' or opcao == 'nao':
    print('ok até a proxima...')
    exit()

while True:
    print('======Menu======')
    print('1- Iniciar Jogo')
    print('2- Customizar Personagem')
    print('3- Sair')

    opcoes = input('Escolha uma opção: ')

    if opcoes == '1':
        print('Iniciando')
    elif opcoes =='2':
        print('Entrando na Customização...')
    elif opcoes =='3':
        print('ok até a proxima...')

    else:
        print("Opção inválida.")