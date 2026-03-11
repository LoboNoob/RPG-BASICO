import random

clas = ["Gojo","Sukuna","Zenin","Yuji","Nenhum"]
inatas = ["Ilimitado","Santuario","10 sombras","Restrição Celestial","Manipulação De espiritos"]

print('---------------RPG BASICO---------------')
print('Quer jogar?')
print('Sim ou Não?')
opcao = input()

if opcao.lower() in ['não', 'nao']:
    print('ok até a proxima...')
    exit()
    
while True:
    print('\n======Menu======')
    print('1- Iniciar Jogo')
    print('2- Customizar Personagem')
    print('3- Sair')

    opcoes = int(input('Escolha uma opção: '))

    if opcoes == 1:
        print('Iniciando...')
        #DAQ PARA BAIXO É O MENU DE CUSTOMIZAÇÃO
    elif opcoes == 2:
        print('Entrando na Customização...')

        while True:
            print("\n-------MENU DE CUSTOMIZAÇÃO--------")
            print("1- Roletar Clã")
            print("2- Roletar Inata")
            print("3- Voltar pro Menu")

            opc = int(input("Escolha uma opção: "))

            if opc == 1:
                print("Seu Clã é:", random.choice(clas))

            elif opc == 2:
                print("Sua inata é:", random.choice(inatas))

            elif opc == 3:
                print("Retornando ao menu principal...")
                break 

            else:
                print("Opção inválida!")
        #TERMINA AQUI O MENU
    elif opcoes == 3:
        print("Saindo do jogo...")  
        exit()
    else:
        print("Opção inválida!")
