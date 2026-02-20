import random
clas = ["Gojo","Sukuna","Zenin","Yuji","Nenhum"]
inatas = ["Ilimitado","Santuario","10 sombras","Restrição Celestial","Manipulação De espiritos"]
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
        print("-------MENU DE CUSTOMIZAÇÃO--------")
        print("1- Roletar Clã")
        print("2- Roletar Inata")
        print("3- Voltar pro Menu")
        opc = input("Escolha uma opção: ")
        if opc == 1:
            print("Seu Clã é: ",random.choice(clas))
        elif opc == 2:
            print("Sua inata é: ",random.choice(inatas))
        elif opc == 3:
            print("Retornando...")
        continue
    

    elif opcoes =='3':
        print('ok até a proxima...')

    else:
        print("Opção inválida.")
    break
