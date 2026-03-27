import random

# ================= DADOS =================
clas = ["Gojo","Ryomen","Zenin","Itadori","Nenhum"] #proximo okkutsu
inatas = ["Ilimitado","Santuario","10 sombras","Restrição Celestial","Manipulação De espiritos"] # proximo RIKA

clan_sorteado = None
inata_sorteada = None

# ================= Combate sem poderes ainda =================
def combate(player, inimigo):

    print(f"\n⚔️ Combate contra {inimigo['nome']} iniciado!")

    esquiva_ativa = False

    while player["hp"] > 0 and inimigo["hp"] > 0:

        print("\n====== SEU TURNO ======")
        print(f"Seu HP: {player['hp']} | Energia: {player['energia']}")
        print(f"{inimigo['nome']} HP: {inimigo['hp']}")

        print("\n1- Atacar⚔️")
        print("2- Juntar energia⚡")
        print("3- Esquivar💨")

        acao = input("Escolha: ")

        # ATAQUE
        if acao == "1":
            dano = random.randint(8, 15)
            inimigo["hp"] -= dano
            print(f"Você atacou e causou {dano} de dano!")

        # JUNTAR ENERGIA
        elif acao == "2":
            ganho = random.randint(5, 10)
            player["energia"] += ganho
            print(f"Você concentrou energia e recuperou {ganho}!")

        # ESQUIVA
        elif acao == "3":
            esquiva_ativa = True
            print("Você se preparou para esquivar do próximo ataque!")

        else:
            print("Ação inválida!")
            continue

        # VERIFICA SE INIMIGO MORREU
        if inimigo["hp"] <= 0:
            break

        # TURNO DO INIMIGO
        print(f"\n👹 Turno de {inimigo['nome']}!")

        dano_inimigo = random.randint(6, 12)

        if esquiva_ativa:
            chance = random.randint(1, 100)
            if chance <= 50:
                print("Você esquivou do ataque!")
                esquiva_ativa = False
                continue
            else:
                print("Você tentou esquivar, mas falhou!")
                esquiva_ativa = False

        player["hp"] -= dano_inimigo
        print(f"{inimigo['nome']} te atacou e causou {dano_inimigo} de dano!")

    # FIM DO COMBATE
    print("\n====== FIM DO COMBATE ======")

    if player["hp"] <= 0:
        print("💀 Você foi derrotado...")
    else:
        print("🏆 Você venceu o combate!")


# Preciso criar a mesma função mais pra frente porém com poderes já
#elif acao == "4":  # ataque especial
    #inata_jogador = player["inata"]
    #if inata_jogador in poderes:
        #poderes[inata_jogador](player, inimigo)  # chama a função correta automaticamente
    #else:
        #print("Você ainda não tem poderes especiais.")

# ================= INÍCIO =================
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

    try:
        opcoes = int(input('Escolha uma opção: '))
    except:
        print("Digite um número válido!")
        continue

    # ================= INICIAR JOGO =================
    if opcoes == 1:

        if clan_sorteado is None or inata_sorteada is None:
            print("Você precisa roletar seu clã e inata primeiro!")
            continue

        player = {
            "cla": clan_sorteado,
            "inata": inata_sorteada,
            "hp": 100,
            "energia": 50
        }

        print('Qual o seu nome?')
        nome = input()

        # ===== INTRODUÇÃO E NARRATIVA =====
        print(f'Muito Prazer, {nome}! Meu Nome é Geovane')
        print('E eu sou o desenvolvedor e vou narrar a história para você.')
        print('Para começar saiba que o RPG é bem básico')
        print('E a temática é do anime Jujutsu Kaisen')
        print("Só lembrando: quando for um personagem que fale eu usarei '--' no começo da fala dele")
        print("Quando for eu narrando, escreverei normalmente")
        print('Espero que goste :)')
        print('Agora vamos continuar...')

        print('.')
        print('..')
        print('...')

        print('Você nasce em uma vila bem distante!')
        print('Sua vila é bem medíocre, não há muitas pessoas por lá.')
        print('Como você ainda é criança, não há nada para fazer.')

        print('Timeskip...')
        input('Aperte ENTER para continuar')
        print("...")
        print('Já passaram 10 anos e nessa idade você desperta uma inata herdada!')
        print('Como você não tinha noção ainda da sua própria família,')
        print('Descobrirá tanto seu clã quanto sua inata.')

        print('Enquanto seus pais te observam, uma névoa cobre seu corpo...')
        input('Prosseguir...')

        print('Então você e seus pais conseguem ver...')
        print('...')
        print('Portanto agora você definitivamente é:')
        print(f'{nome}, seu clã é: {player["cla"]}, sua inata é: {player["inata"]}')

        # ================= EVENTOS =================
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

        input('Aperte ENTER para continuar')

        # ================= ESCOLA E EXPLICAÇÃO =================
        print("")
        print("Depois de alguns dias, você é matriculado na escola Jujutsu")
        print("Aonde todos os feiticeiros despertados vão para treinar e obter mais conhecimento")
        print("Porém, para ser aprovado oficialmente, você precisa passar em um teste.")
        input("APERTE ENTER")

        print("Logo você vai até a sala onde ocorrerá o teste")
        print("O examinador já estava te esperando, seu nome é Masamichi Yaga")
        print(f"-- Muito prazer {nome}! Estou aqui para realizar o seu teste. Vamos começar?")

        input("")  # Inicio do teste
        print("Após o início do seu teste, um Shinigami aparece")
        print("Para resumir, um Shinigami é uma criatura invocada por feiticeiros")
        print("através de energia amaldiçoada para lutar ou realizar tarefas, agindo como familiar")
        print("--Seu teste é simples: vença esse Shinigami para ser admitido na escola")
        print("Vale lembrar que muitos tiveram dificuldade com ele, Com execeção é claro de Satoru Gojo")
        print("")
        input("Aperte ENTER")  # Explicação do sistema de luta
        print("")
        print("Uma breve pausa para ensinar sobre como você lutará no game:")
        print("Quando um oponente for avistado, normalmente virá 3 opções de ações")
        print("1- Atacar (Quando aprender mais sobre suas técnicas terá outro menu para escolher o ataque)")
        print("2- Juntar energia (Para usar em ataques ou outras ações)")
        print("3- Esquivar (Auto explicativo né?)")
        print("As ações não são reversíveis, então tome cuidado.")
        input("Aperte ENTER se já entendeu tudo")

        # ================= INICIO DO COMBATE =================
        shinigami_masa = { #preciso configurar cada um que for inimigo**
            "nome": "Shinigami de Masamichi",
            "hp": 60,
            "energia": 0
        }

        print("O shinigami de Masamichi está vindo em sua direção")
        print("Combate iniciando...")
        combate(player, shinigami_masa) # função para chamar o combate

        #continuação da historia
        print(f"-- Até que você não foi ruim {nome}, Parabens Você está oficialmente na escola Jujutsu!")
        print("...")
        input("APERTE ENTER")
        print("")
        print("Você foi levado até os outros calouros para se apresentar")        
        exit()
    # ================= CUSTOMIZAÇÃO =================
    elif opcoes == 2:

        while True:

            print("\n-------MENU DE CUSTOMIZAÇÃO--------")
            print("1- Roletar Clã")
            print("2- Roletar Inata")
            print("3- Voltar pro Menu")

            try:
                opc = int(input("Escolha uma opção: "))
            except:
                print("Digite um número válido!")
                continue

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
                    if input('Deseja girar novamente? (s/n): ').lower() == 'n':
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
                    if input('Deseja girar novamente? (s/n): ').lower() == 'n':
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
