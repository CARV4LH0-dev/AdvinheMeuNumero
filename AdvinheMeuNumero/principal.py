def regras():
    print("\033[m")
    print("\033[36mRegras:")
    print("\033[m")
    print("\033[36m-\033[m Jogadores: 2")
    print("\033[36m-\033[m Rodadas: 2 (3 em caso de empate)")
    print("\033[36m-\033[m O Jogador 1 escolhe um número secreto de 1 a 100")
    print("\033[36m-\033[m O jogador 2 tenta advinhar o número secreto escolhido pelo Jogador 1")
    print("\033[36m-\033[m A cada tentativa errada, é mostrado na tela se o número secreto é menor ou maior")
    print("\033[36m-\033[m O jogador 2 tem chances ilimitadas para advinhar, mas não pode repetir escolhas")
    print("\033[36m-\033[m Todas tentativas são computadas até o Jogador 2 advinhar o número secreto")
    print("\033[36m-\033[m Quando o Jogador 2 advinhar o número secreto, muda para a segunda rodada")
    print("\033[36m-\033[m Na segunda rodada, o Jogador 1 advinha um número secreto do Jogador 2")
    print("\033[36m-\033[m Vence a partida o jogador que advinhar o número secreto com menos chances que seu adversário")

cont1 = 0
cont2 = 0
rodada = 1
Jogador1 = ''
Jogador2 = ''

print("")
print("\033[34m=" * 60)
print("ADVINHE O MEU NÚMERO".center(57))
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
                while True:
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

    while True:
        if Jogador1 != '':
            break
        try:
            Jogador1 = str(input("\nJogador 1, digite seu nome: ")).strip()
            if not Jogador1.isalpha():
                print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                continue
        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
            print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
            continue
        else:
            print("\n" * 130)
            break

    while True:
        if Jogador2 != '':
            break
        try:
            Jogador2 = input("\nJogador 2, digite seu nome: ").strip()
            if not Jogador2.isalpha():
                print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
                continue
        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
            print("\n\033[33mERRO! Por favor, digite um nome válido.\033[m")
            continue
        else:
            print("\n" * 130)
            break

    while True:
        try:
            secreto = int(input(f"\n{Jogador1}, escolha um número secreto de 1 a 100: "))
            if secreto < 1 or secreto > 100:
                print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                continue
        except (ValueError, TypeError, KeyboardInterrupt, IndexError):
            print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
            continue
        else:
            print("\n" * 130)
            break

    while True:
        try:
            tentativa = int(input(f"\n{Jogador2}, tente advinhar o número secreto: "))
            if tentativa < 1 or tentativa > 100:
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
                secreto = int(input(f"{Jogador2}, escolha um número secreto de 1 a 100: "))
                if secreto < 1 or secreto > 100:
                    print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                    continue
            except (ValueError, TypeError, KeyboardInterrupt, IndexError):
                print("\n\033[33mERRO! Por favor, escolha um número inteiro de 1 a 100.\033[m")
                continue
            else:
                print("\n" * 130)
                break

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
            rodada = 1

        while rodada == 0:
            cont1 = 0
            cont2 = 0
            Jogador1 = ''
            Jogador2 = ''
            while True:
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
                        break
                    else:
                        rodada = 4
                        break
