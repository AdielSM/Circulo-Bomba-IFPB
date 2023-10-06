from circuloBomba import CirculoBomba
import time

def main() -> None:
    # Cabeçalho de início do jogo
    print('')
    print(f'💣💥 \033[1mBem vindo ao Círculo da Bomba!\033[0m 💣💥')
    print('='*45)

    try:
        # Para "n" partidas que o jogador quiser repetir (caso ele não repita, apenas 1 partida acontecerá)
        while True:
            print(f'Deseja carregar os participantes por meio de um arquivo? \033[4m(S/N)\033[0m')
            print(f'\033[2mEm caso afirmativo, os dados deverão estar em "carregamento.txt", cada nome deve estar separado por vírgula e espaço.\033[0m\n')
            opcao = input().upper()

            # Verifica se o jogador deseja carregar os participantes de um arquivo
            if opcao == 'S':
                listaDeParticipantesUsuario = carregar().split(', ')

            # Verifica se o jogador deseja digitar os participantes
            elif opcao == 'N':
                print('Digite os participantes (separados por vírgula e espaço):')
                participantes = input()
                listaDeParticipantesUsuario = participantes.split(', ')
                # Caso tenha sido informado apenas um participante (ou usado o separador incorreto)
                if len(listaDeParticipantesUsuario) == 1:
                    raise Exception(
                        'Você digitou incorretamente a lista de participantes, lembre de usar vírgula e espaço!')

            # Caso o jogador não tenha digitado uma opção válida
            else:
                raise Exception('Você não digitou uma opção válida, tente novamente!')

            print('Digite o numero de vencedores:')
            numVencedores = int(input())

            print('Digite o numero de pulos iniciais:')
            pulosIniciais = int(input())

            print('='*45)

            # instancia o jogo em uma variável e o inicia
            jogo = CirculoBomba(listaDeParticipantesUsuario,
                                numVencedores, pulosIniciais)
            jogo.jogar()

            # verifica se o jogador deseja repetir o jogo
            if not jogarNovamente():
                print('Fim do Programa! Obrigado por jogar!')
                break

    except KeyboardInterrupt:
        print('Ok, encerrando o jogo... ✔')
    except ValueError:
        print(f'\033[91m ⚠ Você não digitou um número válido como solicitado, tente novamente!\n\033[0m')
        time.sleep(1)
        main()
    except Exception as e:
        print(f'\033[91m ⚠ {e}\033[0m')
        print('')
        time.sleep(1)
        main()


# Verifica se o jogador deseja repetir o jogo
def jogarNovamente() -> bool:
    repetir_jogo = input(
        'Deseja jogar novamente?\n (S) - Sim\n (N) - Não\n').upper()
    match repetir_jogo:
        case 'S':
            return True
        case 'N':
            return False
        case _:
            raise Exception(
                'Você não digitou uma opção válida, tente novamente!')


# Carrega os participantes de um arquivo de texto
def carregar() -> str:
    with open('carregamento.txt', 'r') as f:
        return f.read()


# Programa Principal
main()