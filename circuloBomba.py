import random as rd
import time
from listaCircular import ListaCircular
from pilhaParticipantes import Pilha


class CirculoBomba:
    def __init__(self, participantes: list, numVencedores: int, pulosIniciais: int) -> None:
        # Instancia a lista circular de participantes e adiciona os participantes
        self.__listaParticipantes = ListaCircular()
        self.__adicionarParticipante(participantes)

        # Instancia a pilha de participantes perdedores com o tamanho máximo como a quantidade de jogadores
        self.__pilhaParticipantesPerdedores = Pilha(len(participantes))
        
        self.__quantidadeDeVencedores = self.__verificarQuantidadeDeVencedores(numVencedores)
        self.__pulosIniciais = self.__verificarPulosIniciais(pulosIniciais)
        self.__numeroRodadaAtual = 1

    @property
    def listaParticipantes(self) -> 'ListaCircular':
        return self.__listaParticipantes

    @property
    def numVencedores(self) -> int:
        return self.__quantidadeDeVencedores

    @property
    def pulosIniciais(self) -> int:
        return self.__pulosIniciais

    @property
    def pilhaParticipantesPerdedores(self) -> 'Pilha':
        return self.__pilhaParticipantesPerdedores

    @property
    def rodada(self) -> int:
        return self.__numeroRodadaAtual

    # Adiciona cada participante à lista circular, verificando se há repetição de nomes
    def __adicionarParticipante(self, arrayParticipantes: list) -> None:
        listaAux = []
        for participante in arrayParticipantes:
            if participante.title() in listaAux:
                raise Exception("Há participantes repetidos na lista!")
            else:
                self.__listaParticipantes.append(participante.title())
                listaAux.append(participante.title())

    def __verificarQuantidadeDeVencedores(self, valor: any) -> int:
        if valor > 0 and valor <= len(self.__listaParticipantes) - 1:
            return valor
        else:
            raise ValueError(
                "O numero de vencedores deve ser maior que 0 e menor que o número de participantes!")

    def __verificarPulosIniciais(self, valor: int) -> int:
        if valor >= 4 and valor <= 15:
            return valor
        else:
            raise ValueError(
                "O numero de pulos iniciais deve ser maior que 3 e menor que 16!")

    # Só na primeira rodada
    def __escolherPrimeiroJogador(self) -> int:
        return rd.randint(1, len(self.listaParticipantes))

    def __escolherAvancoAleatorio(self) -> int:
        return rd.randint(4, 15)

    # Mostra o percurso da bomba do ponteiro ao avanço, passando por cada jogador
    def __mostrarPercursoDaBomba(self, start: int, stop: int) -> None:
        for i in range(start, stop):
            if i > len(self.__listaParticipantes):
                i = (i - 1) % len(self.__listaParticipantes) + 1

            print(
                f'A bomba está passando por {self.__listaParticipantes.elemento(i)}')
            time.sleep(0.5)

    # Iniciar jogo
    def jogar(self) -> None:
        # Escolhe o primeiro ponteiro aleatoriamente
        posicaoBomba = indicePonteiro = self.__escolherPrimeiroJogador()
        # Guarda o nome do primeiro ponteiro
        ponteiro = self.__listaParticipantes.elemento(posicaoBomba)

        # passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição
        avanco = self.__pulosIniciais
        posicaoBomba = (indicePonteiro - 1 + avanco) % len(self.__listaParticipantes) + 1

        # Jogando enquanto num vencedores != participantes
        while not self.__verificarFimJogo():
            print('='*30)
            print(f'Participantes: {self.__listaParticipantes}')
            print(f'Rodada {self.__numeroRodadaAtual}')
            print(f'Ponteiro: {ponteiro} K: {avanco}')

            # Mostra os participantes que a bomba passou
            self.__mostrarPercursoDaBomba(
                indicePonteiro + 1, (indicePonteiro + avanco + 1))

            # Exclui o eliminado e empilha nos perdedores
            participante_eliminado = self.__listaParticipantes.remove(
                posicaoBomba)
            self.__pilhaParticipantesPerdedores.empilha(participante_eliminado)
            print('A bomba explodiu! BOOM!💣💥💣💥💣')
            print('Item removido:', participante_eliminado)

            # Caso o jogador removido tenha sido o último, o seu sucessor será o primeiro jogador
            if (posicaoBomba == len(self.__listaParticipantes) + 1): 
                posicaoBomba = 1

            # Atualiza o ponteiro
            ponteiro = self.__listaParticipantes.elemento(posicaoBomba)
            indicePonteiro = posicaoBomba

            # passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição
            avanco = self.__escolherAvancoAleatorio()
            posicaoBomba = (indicePonteiro - 1 + avanco) % len(self.__listaParticipantes) + 1

            self.__numeroRodadaAtual += 1

        # Caso o jogo tenha encerrado
        # Deixa a ordem correta dos participantes perdedores, mostrando a sequencia de eliminação da direita para a esquerda
        listaPerdedores = []
        for _ in range(len(self.__pilhaParticipantesPerdedores)):
            listaPerdedores.append(self.__pilhaParticipantesPerdedores.desempilha())

        # Lista os vencedores, adicionando-os numa lista a partir de uma repetição decrescente do número de vencedores
        listaVencedores = []
        for i in range(self.__quantidadeDeVencedores, 0, -1):
            listaVencedores.append(self.__listaParticipantes.remove(i))
        
        # prints finais
        print("O jogo acabou!")
        
        # cor verde para o(s) vencedor(es)
        print(f"O(s) vencedor(es) após {self.__numeroRodadaAtual} rodadas, é(são): \033[1;32;40m<<< {', '.join(listaVencedores)} >>>>\033[0m")
        print(f"Os perdedores são: {' < '.join(listaPerdedores)}")

    # Verifica se o jogo acabou
    def __verificarFimJogo(self) -> bool:
        if self.__quantidadeDeVencedores == len(self.__listaParticipantes):
            return True
        else:
            return False