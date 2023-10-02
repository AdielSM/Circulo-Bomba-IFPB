import random as rd
import time

from listaCircular import ListaCircular
from pilhaParticipantes import Pilha

class CirculoBomba:
    def __init__(self,participantes:list,numVencedores:int,pulosIniciais:int):

        # Instancia a lista circular de participantes
        self.__listaParticipantes = ListaCircular(len(participantes))
        for participante in participantes:
            self.__listaParticipantes.append(participante)

        self.__numVencedores = self.__verificadorNumeroVencedores(numVencedores)
        self.__pulosIniciais = self.__verificadorPulosIniciais(pulosIniciais)
        self.__rodada = 1
        self.__pilhaParticipantesPerdedores = Pilha()

    @property
    def listaParticipantes(self):
        return self.__listaParticipantes
    
    @property
    def numVencedores(self):
        return self.__numVencedores
    
    @property
    def pulosIniciais(self):
        return self.__pulosIniciais
    
    def __verificadorNumeroVencedores(self, valor):
        if valor > 0 and valor <= len(self.__listaParticipantes) - 1:
            return valor
        else:
            raise ValueError("O numero de vencedores deve ser maior que 0 e menor que o número de participantes!")
    
    def __verificadorPulosIniciais(self,valor):
        if valor >= 4 and valor <= 15:
            return valor
        else:
            raise ValueError("O numero de pulos iniciais deve ser maior que 3 e menor que 16!")


    # Só na primeira rodada
    def escolherStartAleatorio(self):
        return rd.randint(1,len(self.listaParticipantes))
    
    def escolherAvancoAleatorio(self):
        return rd.randint(4,15)
    
    # Iniciar jogo
    def jogar(self):
        # Usado para não alterar a lista original e para a legibilidade do código
        # ? Precisa? Não achei necessário e vantajoso
        auxLista = self.__listaParticipantes
        auxPilha = self.__pilhaParticipantesPerdedores

        # Variável onde será armazenado o ponteiro atual
        # Avanço que só vai ser usado na primeira rodada para encontrar o elemento que será o start que é gerado aleatoriamente
        start = self.escolherStartAleatorio()
        ponteiro = auxLista.elemento(start)
        avanco = self.__pulosIniciais
			
			# Se avançou sem dar uma volta completa
        if (start + avanco) <= len(self.__listaParticipantes):
            posicaoBomba = start + avanco
            # Se deu a volta até o último elemento e partindo dele
        elif (start + avanco) > len(self.__listaParticipantes) and (start + avanco) % len(self.__listaParticipantes) == 0:
            posicaoBomba = start
            # Se deu a volta em qualquer outro elemento
        else:
            posicaoBomba = (start + avanco) % len(self.__listaParticipantes)
        
        # posicaoBomba = (start + avanco) % len(self.__listaParticipantes) if ((start + avanco) % len(self.__listaParticipantes) > 0) else start
			
        # Jogando enquanto num vencedores != participantes
        while not self.verificarFimJogo():     
                print('='*30)
                print(f'Participantes: {self.__listaParticipantes}')
                print(f'Rodada {self.__rodada}')
                # ! Corrigir print para mostrar o posicaoBomba anterior (não o que vai ser eliminado)
                print(f'Ponteiro: {ponteiro} K: {avanco}')

                # Exclui o eliminado e empilha nos perdedores
                participante_eliminado = auxLista.remove(posicaoBomba)
                auxPilha.empilha(participante_eliminado)

                if posicaoBomba > len(self.__listaParticipantes):
                    posicaoBomba = 1
                    ponteiro = auxLista.elemento(posicaoBomba)
                else:
                    ponteiro = auxLista.elemento(posicaoBomba)

                print('Item removido:', participante_eliminado)
            
                avanco = self.escolherAvancoAleatorio()
					
                # Se avançou sem dar uma volta completa
                if (posicaoBomba + avanco) <= len(self.__listaParticipantes):
                    posicaoBomba = posicaoBomba + avanco
                # Se deu a volta até o último elemento e partindo dele
                elif (posicaoBomba + avanco) > len(self.__listaParticipantes) and (posicaoBomba + avanco) % len(self.__listaParticipantes) == 0:
                    posicaoBomba = posicaoBomba
                # Se deu a volta em qualquer outro elemento
                else:
                    posicaoBomba = (posicaoBomba + avanco) % len(self.__listaParticipantes)
									
                # posicaoBomba = (posicaoBomba + avanco) % len(self.__listaParticipantes) if ((posicaoBomba + avanco) % len(self.__listaParticipantes) > 0) else posicaoBomba
                if posicaoBomba > len(self.__listaParticipantes):
                    posicaoBomba -= len(self.__listaParticipantes)
                self.__rodada += 1

        # Caso o jogo tenha encerrado
        print("O jogo acabou!")

        # ! Temos que ajeitar pro output do documento ainda
        print(f"Os vencedores são: {self.__listaParticipantes}")
        print(f"Os perdedores são: {self.__pilhaParticipantesPerdedores}")

    def verificarFimJogo(self):
        if self.__numVencedores == len(self.__listaParticipantes):
            return True
        else:
            return False