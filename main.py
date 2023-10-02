from circuloBomba import CirculoBomba

def main():
    print('Bem vindo ao Circulo da Bomba!')
    print('='*30)
    try:
        print('Digite os participantes (separados por vírgula e espaço):')
        participantes = input()
        listaDeParticipantesUsuario = participantes.split(', ')
        if len(listaDeParticipantesUsuario) == 1:
            raise Exception('Você digitou incorretamente a lista de participantes, lembre de usar vírgula e espaço!')
        
        print('Digite o numero de vencedores:')
        numVencedores = int(input())

        print('Digite o numero de pulos iniciais:')
        pulosIniciais = int(input())

        print('='*30)

  
    
        jogo = CirculoBomba(listaDeParticipantesUsuario,numVencedores,pulosIniciais)
        jogo.jogar()

    except ValueError:
        print('Você não digitou um número válido como solicitado, tente novamente!')
        main()
    except Exception as e:
        print(e)
        main()


main()