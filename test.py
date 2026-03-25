import random

clas = ["Gojo","Ryomen","Zenin","Itadori","Nenhum"]
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

    # INICIAR JOGO
    if opcoes == 1:

        if clan_sorteado is None or inata_sorteada is None:
            print("Você precisa roletar seu clã e inata primeiro!")
            continue

        player = {
            "cla": clan_sorteado,
            "inata": inata_sorteada,
            "hp": 100
        }

        print('Qual o seu nome?')
        nome = input()

        print(f'Muito Prazer, {nome}! Meu Nome é Geovane')
        print('E eu sou o desenvolvedor e vou narrar a história para você.')
        print('Para começar saiba que o rpg é bem basico')
        print('E a temática é do anime Jujutsu Kaisen')
        print("Só Lembrando quando for um personagem que fale eu usarei -- no começo da fala dele")
        print("Quando for eu narrando irei apenas escrever normalmente")
        print('Espero que goste :)')
        print('Agora vamos continuar')

        print('.')
        print('..')
        print('...')

        print('Você nasce em uma vila bem distante!')
        print('Sua vila é bem mediocre, não há muitas pessoas por lá.')
        print('Como você ainda tem dias de vida não há nada para fazer.')

        print('Timeskip...')
        input('Aperte ENTER para continuar')

        print('Já passou 10 anos e nessa idade é despertado uma inata herdada')
        print('E como você não tinha noção ainda da sua própria família')
        print('Descobrirá tanto seu clã quanto sua inata')

        print('Enquanto seus pais te observam, Uma névoa cobre seu corpo...')
        input('Prosseguir...')

        print('Então você e seus pais conseguem ver...')
        print('...')
        print('Portanto agora você definitivamente é')

        print(f'{nome}, seu clã é: {player["cla"]}, sua inata é: {player["inata"]}')

        # EVENTOS

        if player["inata"] == "Restrição Celestial":
            print('Seus pais te olham com desprezo, nojo, raiva e tristeza')
            print('Uma onda de emoções negativas vem deles')
            print('Pelo que parece sua inata é detestável entre todos')

        elif player["inata"] == "Ilimitado" and player["cla"] == "Gojo":
            print('Seus pais te olham com muito orgulho')
            print('O chão começa a tremer')
            print('O mundo inteiro sente sua chegada')
            print('O EQUILÍBRIO DO MUNDO MUDOU')
            print('Você não é uma pessoa qualquer...')

        elif player["inata"] == "Ilimitado":
            print('Seus pais te olham com orgulho')
            print('O chão começa a tremer')
            print('Parece que sua inata não é comum...')
        else:
            print('')
        input('Aperte qualquer tecla')
        print("Depois de alguns dias se passarem, Você é matriculado na escola Jujutsu")
        print("Aonde todos os feiticeiros despertados vão para treinar para ficar mais forte e obter mais conhecimento")
        print("Porém para ser aprovado oficialmente na escola, você precisa passar em um teste.")
        input("APERTE ENTER")
        print("Logo você vai até a sala que ocorerrá o teste")
        print("O examinador já estava te esperando, seu nome é Masamichi Yaga")
        print(f"-- Muito prazer {nome}! Estou aqui para realizar o seu teste, Vamos começar?")
        input("")
        print("Após o inicio do seu teste um Shinigami aparece")
        print("para resumir O que é um shinigami, são criaturas invocadas por feiticeiros")
        print("através de energia amaldiçoada para lutar ou realizar tarefas, agindo como familiares")
        print("--Seu teste é simples, Vença esse shinigami para ser admitido na escola Jujutsu")
        print("Vale lembrar que esse shinigami muitos tiveram dificuldade em lidar com ele assim que entraram na escola")
        print("Com exceção é claro de Satoru Gojo")


        


    # CUSTOMIZAÇÃO
    elif opcoes == 2:

        while True:

            print("\n-------MENU DE CUSTOMIZAÇÃO--------")
            print("1- Roletar Clã")
            print("2- Roletar Inata")
            print("3- Voltar pro Menu")

            opc = int(input("Escolha uma opção: "))

            # ROLETAR CLÃ
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

                    if girar == 'n':
                        print('Voltando ao menu de customização...')
                        break


            # ROLETAR INATA
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

                    if girar == 'n':
                        print('Voltando ao menu de customização...')
                        break


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
