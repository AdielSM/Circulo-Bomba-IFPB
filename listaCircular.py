class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga):
        self.__carga = carga
        self.__proximo = None

    @property
    def carga(self) -> any:
        return self.__carga

    @property
    def proximo(self) -> any:
        return self.__proximo

    @carga.setter
    def carga(self, carga: any):
        self.__carga = carga

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo

    def __str__(self):
        return str(self.__carga)
    


class ListaCircular:
    def __init__(self,tamanho:int) -> None:
        self.__inicio = None
        self.__tamanho = tamanho # Não é o tamanho da lista, é o tamanho do jogo, len(participantes

    def __len__(self) -> int:
        return self.__tamanho

    def __str__(self):
        if not self.__inicio:
            return '[  ]'

        aux = self.__inicio
        retorno = ''
        while True:
            retorno += aux.carga
            aux = aux.proximo
            if aux == self.__inicio:
                return "inicio -> [ " + retorno + "]"
            else:
                retorno += " -> "

    def estaVazia(self) ->  bool:
        return self.__inicio == None
        
    def busca(self, carga:any)->int:
        try:
            assert not self.estaVazia(), "Lista vazia"
            aux = self.__inicio
            indice = 1
            while aux.carga != carga:
                aux = aux.proximo
                indice += 1
            return indice
        except AssertionError as ae:
            raise ListaException(ae)

    def elemento(self, posicao:int) ->  int:
        aux = self.__inicio

        for _ in range(posicao - 1):
            aux = aux.proximo
        
        return aux.carga

    #adiciona um elemento em alguma posição da lista
    def insert(self, carga:any, posicao:int):
        try:
            assert posicao > 0 and posicao <= len(self), "Posição inválida"
            novo_no = No(carga)
            contador = 1

            aux = self.__inicio
            while contador != posicao:
                aux = aux.proximo
                contador += 1
                if contador == posicao - 1:
                    aux.proximo = novo_no

            novo_no.proximo = aux
        except AssertionError as ae:
            raise ListaException(ae)

    # Adiciona um novo elemento ao final da lista
    def append(self, carga): 
        novo_no = No(carga)
        if not self.__inicio:
            self.__inicio = novo_no
            self.__inicio.proximo = self.__inicio
        else:
            aux = self.__inicio
            while aux.proximo != self.__inicio:
                aux = aux.proximo
            aux.proximo = novo_no
            novo_no.proximo = self.__inicio
            
    # Remove um elemento da lista pela posição
    def remove(self, posicao: int)  ->  any:
        try:
            assert self.__inicio, "Lista vazia"
            assert posicao > 0 and posicao <= len(self), "Posição inválida"
            
            carga = None

            if posicao == 1:
                carga = self.__inicio.carga
                # Se for o único elemento da lista
                if self.__tamanho == 1:
                    self.__inicio = None
                else:
                    cursor = self.__inicio
                    # Percorre a lista até o último elemento
                    while cursor.proximo != self.__inicio:
                        cursor = cursor.proximo
                    # O último elemento aponta para o segundo elemento
                    cursor.proximo = self.__inicio.proximo
                    self.__inicio = self.__inicio.proximo

            else:
                cursor = self.__inicio
                # Percorre a lista até o elemento anterior ao que será removido
                for _ in range(posicao - 2):
                    cursor = cursor.proximo
                carga = cursor.proximo.carga
                cursor.proximo = cursor.proximo.proximo

            self.__tamanho -= 1
            return carga

        except AssertionError as ae:
            raise ListaException(ae)