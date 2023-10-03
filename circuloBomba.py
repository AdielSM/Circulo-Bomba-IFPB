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
            if participante in listaAux:
                raise Exception("Há participantes repetidos na lista!")
            else:
                self.__listaParticipantes.append(participante)
                listaAux.append(participante)

    
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
        # Variável onde será armazenado o ponteiro atual
        # Avanço que só vai ser usado na primeira rodada para encontrar o elemento que será o start que é gerado aleatoriamente
        start = self.escolherStartAleatorio()
        ponteiro = self.__listaParticipantes.elemento(start)
        avanco = self.__pulosIniciais
			
		# passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição    
        posicaoBomba = (start - 1 + avanco) % len(self.__listaParticipantes) + 1
        
        # posicaoBomba = (start + avanco) % len(self.__listaParticipantes) if ((start + avanco) % len(self.__listaParticipantes) > 0) else start
			
        # Jogando enquanto num vencedores != participantes
        while not self.verificarFimJogo():     
            print('='*30)
            print(f'Participantes: {self.__listaParticipantes}')
            print(f'Rodada {self.__rodada}')
            print(f'Ponteiro: {ponteiro} K: {avanco}')

            # Mostra os participantes que a bomba passou
            aux = self.__listaParticipantes.busca(ponteiro)
            for i in range(aux + 1, aux + avanco + 1):
                if i > len(self.__listaParticipantes):
                    i -= len(self.__listaParticipantes)
                    print(f'A bomba está passando por {self.__listaParticipantes.elemento(i)}')
                    time.sleep(0.5)
                else:
                    print(f'A bomba está passando por {self.__listaParticipantes.elemento(i)}')
                    time.sleep(0.5)

            # Exclui o eliminado e empilha nos perdedores
            participante_eliminado = self.__listaParticipantes.remove(posicaoBomba)
            self.__pilhaParticipantesPerdedores.empilha(participante_eliminado)
            print('Item removido:', participante_eliminado)

            if posicaoBomba > len(self.__listaParticipantes):
                posicaoBomba = 1
                ponteiro = self.__listaParticipantes.elemento(posicaoBomba)
            else:
                ponteiro = self.__listaParticipantes.elemento(posicaoBomba)


            avanco = self.escolherAvancoAleatorio()
            auxPonteiro = self.__listaParticipantes.busca(ponteiro)            
            # passa a posição da bomba para o jogador a ser excluído, transformando em índice depois em posição   
            posicaoBomba = ( auxPonteiro - 1 + avanco) % len(self.__listaParticipantes) + 1
            
            if posicaoBomba > len(self.__listaParticipantes):
                posicaoBomba -= len(self.__listaParticipantes)
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
        print(f"O(s) vencedor(es) após {self.__rodada} rodadas, é(são): <<< {', '.join(listaVencedores)} >>>>")
        print(f"Os perdedores são: {' < '.join(listaPerdedores)}")

    def verificarFimJogo(self):
        if self.__numVencedores == len(self.__listaParticipantes):
            return True
        else:
            return False