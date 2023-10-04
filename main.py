from circuloBomba import CirculoBomba


def main():
    print('Bem vindo ao Circulo da Bomba!')
    print('='*30)
    try:
        while True:
            print('Digite os participantes (separados por vírgula e espaço):')
            participantes = input()
            listaDeParticipantesUsuario = participantes.split(', ')
            if len(listaDeParticipantesUsuario) == 1:
                raise Exception(
                    'Você digitou incorretamente a lista de participantes, lembre de usar vírgula e espaço!')

            print('Digite o numero de vencedores:')
            numVencedores = int(input())

            print('Digite o numero de pulos iniciais:')
            pulosIniciais = int(input())

            print('='*30)

            jogo = CirculoBomba(listaDeParticipantesUsuario,
                                numVencedores, pulosIniciais)
            jogo.jogar()

            if not jogarNovamente():
                print('Fim do Programa! Obrigado por jogar!')
                break

    except ValueError:
        print('Você não digitou um número válido como solicitado, tente novamente!')
        main()
    except Exception as e:
        print(e)
        main()


def jogarNovamente():
    repetir_jogo = input('Deseja jogar novamente?\n (S) - Sim\n (N) - Não\n').upper()
    match repetir_jogo:
        case 'S':
            return True 
        case 'N':
            return False
        case _:
            raise Exception('Você não digitou uma opção válida, tente novamente!')


main()