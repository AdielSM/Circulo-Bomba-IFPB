from circuloBomba import CirculoBomba


def main() -> None:
    # Cabeçalho de início do jogo
    print('Bem vindo ao Circulo da Bomba!')
    print('='*30)
    try:
        # Para "n" partidas que o jogador quiser repetir (caso ele não repita, apenas 1 partida acontecerá)
        while True:
            print('Digite os participantes (separados por vírgula e espaço):')
            participantes = input()
            listaDeParticipantesUsuario = participantes.split(', ')
            # Caso tenha sido informado apenas um participante (ou usado o separador incorreto)
            if len(listaDeParticipantesUsuario) == 1:
                raise Exception(
                    'Você digitou incorretamente a lista de participantes, lembre de usar vírgula e espaço!')

            print('Digite o numero de vencedores:')
            numVencedores = int(input())

            print('Digite o numero de pulos iniciais:')
            pulosIniciais = int(input())

            print('='*30)

            # instancia o jogo em uma variável e o iniciai
            jogo = CirculoBomba(listaDeParticipantesUsuario,
                                numVencedores, pulosIniciais)
            jogo.jogar()

            # verifica se o jogador deseja repetir o jogo
            if not jogarNovamente():
                print('Fim do Programa! Obrigado por jogar!')
                break

    except KeyboardInterrupt:
        print('Ok, encerrando o jogo...')
    except ValueError:
        print('Você não digitou um número válido como solicitado, tente novamente!')
        main()
    except Exception as e:
        print(e)
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


# começa o jogo
main()
