from random import randint
from time import sleep

def regras():
    print("\033[m")
    print("\033[36mRegras:")
    print("\033[m")
    print("\033[36m-\033[m Jogadores: 1 ou 2")
    print("\033[36m-\033[m Rodadas: 2")
    print("\033[36m-\033[m O Jogador 1 escolhe um número secreto de 1 a 100")
    print("\033[36m-\033[m O jogador 2 tenta advinhar o número secreto escolhido pelo Jogador 1")
    print("\033[36m-\033[m A cada tentativa errada, é mostrado na tela se o número secreto é menor ou maior")
    print("\033[36m-\033[m O jogador 2 tem chances ilimitadas para advinhar, mas não pode repetir escolhas")
    print("\033[36m-\033[m Todas tentativas são computadas até o Jogador 2 advinhar o número secreto")
    print("\033[36m-\033[m Quando o Jogador 2 advinhar o número secreto, muda para a segunda rodada")
    print("\033[36m-\033[m Na segunda rodada, o Jogador 1 advinha um número secreto do Jogador 2")
    print("\033[36m-\033[m Vence a partida o jogador que advinhar o número secreto com menos tentativas que seu adversário")

parar = False
modo = 3

while parar == False:
    cont1 = 0
    cont2 = 0
    rodada = 1
    valido = False
    robot = 'Computador'
    valido1 = False
    valido2 = False

    if modo == 0:
        break

    print("")
    print("\033[34m=" * 60)
    print("ADVINHE O MEU NÚMERO".center(57))
    print("=" * 60)
    print("\033[m")

    while True:
        try:
            print("")
            print("""[ 1 ] = Jogador 1 vs Jogador 2
[ 2 ] = Jogador vs Computador""")
            print("")
            modo = int(input("Escolha o modo de jogo: "))
            if modo != 1 and modo != 2:
                print("\n" * 130)
                print("\n\033[33mERRO! Por favor, digite uma opção vál.\033[m")
                continue
        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
            print("\n" * 130)
            print("\n\033[33mERRO! Por favor, digite uma opção válida.\033[m")
            continue
        else:
            rodada = 1
            break

    while modo == 1:
        print("\n" * 130)
        print("\033[34m=" * 60)
        print("Jogador 1 vs Jogador 2".center(57))
        print("=" * 60)
        print("\033[m")
        while rodada == 1:
            print("\033[36m=" * 60)
            print("PRIMEIRA RODADA".center(57))
            print("=" * 60)
            print("\033[m")
            while True:
                try:
                    regra = str(input("Deseja ver as regras? (S/N) ")).strip() [0]
                    if not regra.isalpha() or not regra in 'SsNn':
                        print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                    continue
                else:
                    if regra in 'Ss':
                        regras()
                        try:
                            apagar = str(input("\nDeseja apagar as regras? (S/N) ")).strip() [0]
                            if not apagar.isalpha() or not apagar in 'SsNn':
                                print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                                continue
                        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                            print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                            continue
                        else:
                            if apagar in 'Ss':
                                print("\n" * 130)
                                break
                            else:
                                break
                    else:
                        break

            while valido1 == False:
                try:
                    Jogador1 = str(input("\nJogador 1, digite seu nome: ")).strip().capitalize()
                    if not Jogador1.isalpha():
                        print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                        valido1 = False
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                    valido1 = False
                    continue
                else:
                    print("\n" * 130)
                    valido1 = True
                    break

            while valido2 == False:
                try:
                    Jogador2 = input("\nJogador 2, digite seu nome: ").strip().capitalize()
                    if not Jogador2.isalpha():
                        print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                        valido2 = False
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                    valido2 = False
                    continue
                else:
                    print("\n" * 130)
                    valido2 = True
                    break

            while True:
                try:
                    secreto = int(input(f"\n{Jogador1}, escolha um \033[32mnúmero secreto\033[m de 1 a 100: "))
                    if not secreto > 0 or not secreto < 101:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                    continue
                else:
                    print("\n" * 130)
                    print(f"{Jogador1} já escolheu o \033[32mnúmero secreto\033[m!")
                    print("")
                    break

            while True:
                try:
                    tentativa = int(input(f"\n{Jogador2}, tente advinhar o número secreto: "))
                    if not tentativa > 0 or not tentativa < 101:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100: \033[m")
                    continue
                else:
                    cont2 += 1

                if tentativa != secreto:
                    if tentativa > secreto:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MENOR que \033[31m{tentativa}\033[m")
                        if cont2 == 1:
                            print(f"Você já tentou \033[36m{cont2}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont2}\033[m vezes")
                    else:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MAIOR que \033[31m{tentativa}\033[m")
                        if cont2 == 1:
                            print(f"Você já tentou \033[36m{cont2}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont2}\033[m vezes")
                else:
                    print("\n" * 130)
                    print(f"\n\033[32mVocê acertou!\033[m O número secreto era \033[32m{secreto}\033[m")
                    if cont2 == 1:
                        print(f"{Jogador2} advinhou o número secreto com \033[36m{cont2}\033[m tentativa")
                    else:
                        print(f"{Jogador2} advinhou o número secreto com \033[36m{cont2}\033[m tentativas")
                    rodada = 2
                    break

        while rodada == 2:
            print("")
            print("\033[36m=" * 60)
            print("SEGUNDA RODADA".center(57))
            print("=" * 60)
            print("\033[m")
            while True:
                try:
                    secreto = int(input(f"\n{Jogador2}, escolha um \033[32mnúmero secreto\033[m de 1 a 100: "))
                    if not secreto > 0 or not secreto < 101:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                    continue
                else:
                    print("\n" * 130)
                    print(f"{Jogador2} já escolheu o \033[32mnúmero secreto\033[m!")
                    print("")
                    break

            while True:
                try:
                    tentativa = int(input(f"\n{Jogador1}, tente advinhar o número secreto: "))
                    if not tentativa > 0 or not tentativa < 101:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100: \033[m")
                    continue
                else:
                    cont1 += 1

                if tentativa != secreto:
                    if tentativa > secreto:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MENOR que \033[31m{tentativa}\033[m")
                        if cont1 == 1:
                            print(f"Você já tentou \033[36m{cont1}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont1}\033[m vezes")
                    else:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MAIOR que \033[31m{tentativa}\033[m")
                        if cont1 == 1:
                            print(f"Você já tentou \033[36m{cont1}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont1}\033[m vezes")
                else:
                    print("\n" * 130)
                    print(f"\n\033[32mVocê acertou!\033[m O número secreto era \033[32m{secreto}\033[m")
                    if cont1 == 1:
                        print(f"{Jogador1} advinhou o número secreto com \033[36m{cont1}\033[m tentativa")
                    else:
                        print(f"{Jogador1} advinhou o número secreto com \033[36m{cont1}\033[m tentativas")
                    rodada = 3
                    break

            if cont2 < cont1:
                print(f"\n{Jogador2} \033[32mVENCEU!\033[m")
                rodada = 0
            elif cont2 > cont1:
                print(f"\n{Jogador1} \033[32mVENCEU!\033[m")
                rodada = 0
            else:
                print(f"\n\033[36mEMPATE!\033[m")
                rodada = 3

            print(f"\n\033[36mNúmero de tentativas de {Jogador2}: {cont2}\033[m")
            cont2 = 0
            print(f"\033[36mNúmero de tentativas de {Jogador1}: {cont1}\033[m")
            cont1 = 0

            while rodada == 3:
                print("")
                print("\033[34m=" * 60)
                print("PARTIDA DE DESEMPATE".center(57))
                print("=" * 60)
                print("\033[m")
                cont1 = 0
                cont2 = 0
                valido1 = True
                valido2 = True
                modo = 1
                rodada = 1

            while rodada == 0:
                cont1 = 0
                cont2 = 0
                valido1 = False
                valido2 = False
                try:
                    again = str(input("\nDeseja jogar outra partida? (S/N) ")).strip() [0]
                    if not again.isalpha() or not again in 'SsNn':
                        print("\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                    continue
                else:
                    print("\n" * 130)
                    if again in 'Ss':
                        rodada = 1
                        modo = 3
                        break
                    else:
                        rodada = 1
                        modo = 0
                        parar = True
                        break





    while modo == 2:
        print("\n" * 130)
        print("\033[34m=" * 60)
        print("Jogador vs Computador".center(57))
        print("=" * 60)
        print("\033[m")
        while rodada == 1:
            print("\033[36m=" * 60)
            print("PRIMEIRA RODADA".center(57))
            print("=" * 60)
            print("\033[m")
            while True:
                try:
                    regra = str(input("Deseja ver as regras? (S/N) ")).strip() [0]
                    if not regra.isalpha() or not regra in 'SsNn':
                        print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                    continue
                else:
                    if regra in 'Ss':
                        regras()
                        try:
                            apagar = str(input("\nDeseja apagar as regras? (S/N) ")).strip() [0]
                            if not apagar.isalpha() or not apagar in 'SsNn':
                                print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                                continue
                        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                            print("\n\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                            continue
                        else:
                            if apagar in 'Ss':
                                print("\n" * 130)
                                break
                            else:
                                break
                break

            while valido == False:
                try:
                    Jogador1 = str(input("\nJogador 1, digite seu nome: ")).strip().capitalize()
                    if not Jogador1.isalpha():
                        print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                    continue
                else:
                    valido = True

            secreto = randint(1, 100)
            print("\n" * 130)
            print(f"O Computador já escolheu o \033[32mnúmero secreto\033[m!")
            print("")

            while True:
                try:
                    tentativa = int(input(f"\n{Jogador1}, tente advinhar o número secreto: "))
                    if tentativa < 1 or tentativa > 100:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100: \033[m")
                    continue
                else:
                    cont1 += 1

                if tentativa != secreto:
                    if tentativa > secreto:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MENOR que \033[31m{tentativa}\033[m")
                        if cont1 == 1:
                            print(f"Você já tentou \033[36m{cont1}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont1}\033[m vezes")
                    else:
                        print(f"\n\033[31mVocê errou!\033[m O número secreto é MAIOR que \033[31m{tentativa}\033[m")
                        if cont1 == 1:
                            print(f"Você já tentou \033[36m{cont1}\033[m vez")
                        else:
                            print(f"Você já tentou \033[36m{cont1}\033[m vezes")
                else:
                    print("\n" * 130)
                    print(f"\n\033[32mVocê acertou!\033[m O número secreto era \033[32m{secreto}\033[m")
                    if cont1 == 1:
                        print(f"{Jogador1} advinhou o número secreto com \033[36m{cont1}\033[m tentativa")
                    else:
                        print(f"{Jogador1} advinhou o número secreto com \033[36m{cont1}\033[m tentativas")
                    rodada = 2
                    break

        while rodada == 2:
            print("")
            print("\033[36m=" * 60)
            print("SEGUNDA RODADA".center(57))
            print("=" * 60)
            print("\033[m")

            while True:
                try:
                    secreto = int(input(f"{Jogador1}, escolha um número secreto de 1 a 100: "))
                    if secreto < 1 or secreto > 100:
                        print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                    continue
                else:
                    print("\n" * 130)
                    break
            while tentativa != secreto:
                if cont2 == 0:
                    tentativa = randint(45, 55)
                    cont2 += 1
                    num_segurança1 = tentativa
                    num_segurança2 = tentativa
                    print(f"O Computador está pensando em um número...")
                    sleep(4)
                    print(f"O Computador pensou no número {tentativa:.0f}")
                else:
                    num_segurança2 = num_segurança1
                    num_segurança1 = tentativa
                if cont2 == 1:
                    print("")
                    print(f"O {robot} já tentou \033[36m{cont2}\033[m vez")
                    print("")
                else:
                    print("")
                    print(f"O {robot} já tentou \033[36m{cont2}\033[m vezes")
                    print("")

                while True:
                    if num_segurança1 > secreto and num_segurança2 > secreto:
                        if num_segurança1 % 2 != 0:
                            num_segurança1 += 1
                        if num_segurança2 % 2 != 0:
                            num_segurança2 += 1
                        tentativa = num_segurança1 / 2
                        cont2 += 1
                        print(f"O Computador está pensando em um número...")
                        sleep(4)
                        print(f"O Computador pensou no número {tentativa:.0f}")
                        break

                    elif num_segurança1 > secreto and num_segurança2 < secreto:
                        if num_segurança1 - num_segurança2 == 4:
                            tentativa = num_segurança1 - 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break
                        elif num_segurança1 - num_segurança2 == 3:
                            tentativa = num_segurança1 - 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break
                        else:
                            if num_segurança1 % 2 != 0:
                                num_segurança1 += 1
                            if num_segurança2 % 2 != 0:
                                num_segurança2 -= 1
                            tentativa = num_segurança1 + (num_segurança2 - num_segurança1) / 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break

                    elif num_segurança1 < secreto and num_segurança2 > secreto:
                        if num_segurança2 - num_segurança1 == 4:
                            tentativa = num_segurança1 + 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break
                        elif num_segurança2 - num_segurança1 == 3:
                            tentativa = num_segurança1 + 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break
                        else:
                            if num_segurança1 % 2 != 0:
                                num_segurança1 -= 1
                            if num_segurança2 % 2 != 0:
                                num_segurança2 += 1
                            tentativa = num_segurança1 + (num_segurança2 - num_segurança1) / 2
                            cont2 += 1
                            print(f"O Computador está pensando em um número...")
                            sleep(4)
                            print(f"O Computador pensou no número {tentativa:.0f}")
                            break

                    elif num_segurança1 < secreto and num_segurança2 < secreto:
                        if num_segurança1 % 2 != 0:
                            num_segurança1 -= 1
                        if num_segurança2 % 2 != 0:
                            num_segurança2 -= 1
                        tentativa = num_segurança1 + (100 - num_segurança1) / 2
                        cont2 += 1
                        print(f"O Computador está pensando em um número...")
                        sleep(4)
                        print(f"O Computador pensou no número {tentativa:.0f}")
                        break

            sleep(4)
            print("\n" * 130)
            print(f"\n\033[32mO {robot} acertou!\033[m O número secreto era \033[32m{secreto}\033[m")
            if cont2 == 1:
                print(f"O {robot} advinhou o número secreto com \033[36m{cont2}\033[m tentativa")
            else:
                print(f"O {robot} advinhou o número secreto com \033[36m{cont2}\033[m tentativas")

            if cont2 < cont1:
                print(f"\nO {robot} \033[32mVENCEU!\033[m")
                rodada = 0
            elif cont2 > cont1:
                print(f"\n{Jogador1} \033[32mVENCEU!\033[m")
                rodada = 0
            else:
                print(f"\n\033[36mEMPATE!\033[m")
                rodada = 3

            print(f"\n\033[36mNúmero de tentativas de {Jogador1}: {cont1}\033[m")
            cont1 = 0
            print(f"\033[36mNúmero de tentativas do {robot}: {cont2}\033[m")
            cont2 = 0

            while rodada == 3:
                print("")
                print("\033[34m=" * 60)
                print("PARTIDA DE DESEMPATE".center(57))
                print("=" * 60)
                print("\033[m")
                cont1 = 0
                cont2 = 0
                valido = True
                rodada = 1

            while rodada == 0:
                cont1 = 0
                cont2 = 0
                valido = False
                try:
                    again = str(input("\nDeseja jogar outra partida? (S/N) ")).strip() [0]
                    if not again.isalpha() or not again in 'SsNn':
                        print("\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                        continue
                except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                    print("\033[33mERRO! Por favor, digite 'S' para 'Sim' ou 'N' para 'Não'\033[m")
                    continue
                else:
                    print("\n" * 130)
                    if again in 'Ss':
                        rodada = 1
                        modo = 3
                        break
                    else:
                        rodada = 1
                        modo = 0
                        parar = True
                        break
