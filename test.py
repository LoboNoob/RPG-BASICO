import random

clas = ["Gojo","Sukuna","Zenin","Yuji","Nenhum"]
inatas = ["Ilimitado","Santuario","10 sombras","Restrição Celestial","Manipulação De espiritos"]


clan_sorteado = None
inata_sorteada = None

print('---------------RPG BASICO---------------')
print('Quer jogar?')
print('Sim ou Não?')

opcao = input().lower()

if opcao in ['não','nao','n']:
    print('ok até a próxima...')
    exit()

while True:

    print('\n======MENU======')
    print('1- Iniciar Jogo')
    print('2- Customizar Personagem')
    print('3- Sair')

    opcoes = int(input('Escolha uma opção: '))

    if opcoes == 1:
        print('Iniciando jogo...')
        player = {
            "cla": clan_sorteado,
            "inata": inata_sorteada,
            "hp": 100
            }
        print('Qual o seu nome?')
        nome = input('')
        print(f'Muito Prazer,{nome}!, Meu Nome é Geovane')
        print('e eu sou o desenvolvedor e vou narrar a historia para você.')
        print('Para começar saiba que o rpg é bem basico')
        print('e a tematica é do anime Jujutsu kaisen')
        print('Espero que goste :)')
        print('Agora vamos continuar')
        print('.')
        print('..')
        print('...')
        print('Você nasce em uma vila bem distante!')
        print('Sua vila é bem mediocre, não há muitas pessoas por lá.')
        print('Como você ainda tem dias de vida não há nada para fazer.')
        print('Timeskip...')
        input('Aperte qualquer tecla')
        print('Já passou 10 anos e nessa idade é despertado uma inata herdada')
        print('e como você não tinha noção ainda da sua propria familia')
        print('Descobrirá tanto seu clâ, quanto sua inata')
        print('Uma nevoa cobre seu corpo, enquanto seus pais te observam...')
        print('prosseguir?')
        input('')
        print('Entao você e seus pais conseguem ver')
        print('...')
        print('Portanto agora você definitivamente é')
        print(f'{nome}, seu clã é: {clan_sorteado}, Sua inata é: {inata_sorteada}')
        if inata_sorteada == "Restrição Celestial":
            print('Seus pais te olham com desprezo,nojo,raiva,tristeza,')
            print('Uma onda de emoções negativas veem deles, por conta da sua inata')
            print('Pelo que parece sua Inata é detestavel entre todos')
        elif inata_sorteada == "Ilimitado":
            print('Seus pais te olham com muito orgulho,felizes,empolgados com oq espera vc')
            print('Apenas com o seu despertar os chãos se tremem')
            print('Parece que sua inata não é comum...')
        elif inata_sorteada == "Ilimitado" and clan_sorteado == "Gojo":
            print('Seus pais te olham com muito orgulho,felizes,empolgados com oq espera vc')
            print('Apenas com o seu despertar os chãos se tremem')
            print('O mundo inteiro sente a sua chegada')
            print('O EQUILIBRIO DO MUNDO MUDOU')
            print('Você não é Uma pessoa qualquer...')
        else:
            print('Muito bem, Após o seu despertar')
            print('Seus pais te colocam em uma escola de treino')
            print('Para aprender sobre sua inata')






        break

    elif opcoes == 2:

        while True:

            print("\n-------MENU DE CUSTOMIZAÇÃO--------")
            print("1- Roletar Clã")
            print("2- Roletar Inata")
            print("3- Voltar pro Menu")

            opc = int(input("Escolha uma opção: "))

            # GIRAR CLÃ
            if opc == 1:
                spins = 3

                while spins > 0:

                    clan_sorteado = random.choice(clas)
                    print("Seu Clã é:", clan_sorteado)

                    spins -= 1

                    if spins == 0:
                        print("Você não tem mais giros!")
                        break

                    print(f'Você ainda tem {spins} giros')
                    girar = input('Deseja girar novamente? (s/n): ').lower()

                    if girar in ['n','2']:
                        print('Voltando ao menu de customização...')
                        break

            # GIRAR INATA
            elif opc == 2:
                spins = 3

                while spins > 0:

                    inata_sorteada = random.choice(inatas)
                    print("Sua Inata é:", inata_sorteada)

                    spins -= 1

                    if spins == 0:
                        print("Você não tem mais giros!")
                        break

                    print(f'Você ainda tem {spins} giros')
                    girar = input('Deseja girar novamente? (s/n): ').lower()

                    if girar in ['n','2']:
                        print('Voltando ao menu de customização...')
                        break

            # VOLTAR MENU
            elif opc == 3:
                print("Retornando ao menu principal...")
                break

            else:
                print("Opção inválida!")

    elif opcoes == 3:
        print("Saindo do jogo...")
        exit()

    else:
        print("Opção inválida!")
