import random as rd
import time

from listaCircular import ListaCircular
from pilhaParticipantes import Pilha

class CirculoBomba:
    def __init__(self,participantes:list,numVencedores:int,pulosIniciais:int):

        # Instancia a lista circular de participantes
        self.__listaParticipantes = ListaCircular()
        self.__adicionarParticipante(participantes)
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

    def __adicionarParticipante(self,arrayParticipantes):
        listaAux = []
        for participante in arrayParticipantes:
            if participante.title() in listaAux:
                raise Exception("Há participantes repetidos na lista!")
            else:
                self.__listaParticipantes.append(participante.title())
                listaAux.append(participante.title())

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
    def __escolherStartAleatorio(self):
        return rd.randint(1,len(self.listaParticipantes))
    
    def __escolherAvancoAleatorio(self):
        return rd.randint(4,15)

    def __mostrarPercurso(self, start:int, stop:int):
        for i in range(start, stop):
            if i > len(self.__listaParticipantes):
                i -= len(self.__listaParticipantes)

            print(f'A bomba está passando por {self.__listaParticipantes.elemento(i)}')
            time.sleep(0.5)
    
    # Iniciar jogo
    def jogar(self):
        # Escolhe o primeiro ponteiro aleatoriamente
        posicaoBomba = indicePonteiro = self.__escolherStartAleatorio()
        # Guarda o nome do primeiro ponteiro
        ponteiro = self.__listaParticipantes.elemento(posicaoBomba)
			
		# passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição    
        avanco = self.__pulosIniciais
        posicaoBomba = (indicePonteiro - 1 + avanco) % len(self.__listaParticipantes) + 1
        			
        # Jogando enquanto num vencedores != participantes
        while not self.verificarFimJogo():     
            print('='*30)
            print(f'Participantes: {self.__listaParticipantes}')
            print(f'Rodada {self.__rodada}')
            print(f'Ponteiro: {ponteiro} K: {avanco}')

            # Mostra os participantes que a bomba passou
            self.__mostrarPercurso(indicePonteiro + 1, (indicePonteiro + avanco + 1))

            # Exclui o eliminado e empilha nos perdedores
            participante_eliminado = self.__listaParticipantes.remove(posicaoBomba)
            self.__pilhaParticipantesPerdedores.empilha(participante_eliminado)
            print('A bomba explodiu! BOOM!💣💥💣💥💣')
            print('Item removido:', participante_eliminado)

            # Atualiza o ponteiro
            ponteiro = self.__listaParticipantes.elemento(posicaoBomba)
            indicePonteiro = posicaoBomba

            avanco = self.__escolherAvancoAleatorio()
            # passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição   
            posicaoBomba = ( indicePonteiro - 1 + avanco) % len(self.__listaParticipantes) + 1
            
            self.__rodada += 1


        # Caso o jogo tenha encerrado
        #Deixa a ordem correta dos participantes perdedores, mostrando a sequencia de eliminação da direita para a esquerda
        listaPerdedores = []
        for _ in range(len(self.__pilhaParticipantesPerdedores)):
            listaPerdedores.append(self.__pilhaParticipantesPerdedores.desempilha())
        
        # Lista os vencedores, adicionando-os numa lista a partir de uma repetição decrescente do número de vencedores
        listaVencedores = [] 
        for i in range(self.__numVencedores,0,-1):
            listaVencedores.append(self.__listaParticipantes.remove(i))
        
        #prints finais
        print("O jogo acabou!")
        print(f"O(s) vencedor(es) após {self.__rodada} rodadas, é(são): \033[1;32;40m<<< {', '.join(listaVencedores)} >>>>\033[0m") # cor verde para o(s) vencedor(es)
        print(f"Os perdedores são: {' < '.join(listaPerdedores)}")

    def verificarFimJogo(self):
        if self.__numVencedores == len(self.__listaParticipantes):
            return True
        else:
            return False
        

#salvar

'''
Lista
Pilha
NumVencedores
Rodada
Ponteiro

'''