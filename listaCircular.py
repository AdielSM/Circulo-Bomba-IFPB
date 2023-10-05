class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga: any) -> None:
        self.__carga = carga
        self.__proximo = None

    @property
    def carga(self) -> any:
        return self.__carga

    @property
    def proximo(self) -> any:
        return self.__proximo

    @carga.setter
    def carga(self, carga: any) -> None:
        self.__carga = carga

    @proximo.setter
    def proximo(self, proximo: 'No') -> None:
        self.__proximo = proximo

    def __str__(self) -> str:
        return str(self.__carga)


class ListaCircular:
    def __init__(self) -> None:
        self.__inicio = None
        self.__final = None
        # Não é o tamanho da lista, é o tamanho do jogo, len(participantes)
        self.__tamanho = 0

    def __len__(self) -> int:
        return self.__tamanho

    def __str__(self) -> str:
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

    # Retorna true se a lista estiver vazia
    def estaVazia(self) -> bool:
        return self.__inicio == None

    # Recebe a carga de um elemento e retorna sua posição
    def busca(self, carga: any) -> int:
        try:
            assert not self.estaVazia(), "Lista vazia"
            aux = self.__inicio
            posicao = 1
            while aux.carga != carga:
                aux = aux.proximo
                posicao += 1
                if aux == self.__inicio:
                    raise ListaException("Elemento não encontrado na lista")
            
            return posicao
        
        except AssertionError as ae:
            raise ListaException(ae)

    # Recebe a posição de um elemento e retorna sua carga
    def elemento(self, posicao: int) -> any:
        assert not self.estaVazia(), "Lista vazia"
        assert posicao > 0 and posicao <= len(self), "Posição inválida"

        aux = self.__inicio

        for _ in range(posicao - 1):
            aux = aux.proximo

        return aux.carga

    # adiciona um elemento em alguma posição da lista
    def insert(self, carga: any, posicao: int) -> None:
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
            self.__tamanho += 1
        except AssertionError as ae:
            raise ListaException(ae)

    # Adiciona um novo elemento ao final da lista
    def append(self, carga: any) -> None:
        novo_no = No(carga)
        
        # Se a lista estiver vazia
        if not self.__inicio:
            self.__inicio = novo_no
            self.__final = novo_no
            self.__inicio.proximo = self.__inicio
        
        # Se a lista tiver apenas um elemento
        elif len(self) == 1:
            self.__inicio.proximo = novo_no
            novo_no.proximo = self.__inicio
            self.__final = novo_no

        # Se a lista tiver mais de um elemento
        else:
            self.__final.proximo = novo_no
            novo_no.proximo = self.__inicio
            self.__final = novo_no
        self.__tamanho += 1

    # Remove um elemento da lista pela posição e retorna sua carga
    def remove(self, posicao: int) -> any:
        try:
            assert self.__inicio, "Lista vazia"
            assert posicao > 0 and posicao <= len(self), "Posição inválida"

            carga = None
            
            # Se for o primeiro elemento da lista
            if posicao == 1:
                carga = self.__inicio.carga
                # Se for o único elemento da lista
                if self.__tamanho == 1:
                    self.__inicio = None
                    self.__final = None
                # Se não for o único elemento da lista
                else:
                    cursor = self.__final
                    # O último elemento aponta para o segundo elemento
                    cursor.proximo = self.__inicio.proximo
                    self.__inicio = self.__inicio.proximo

            # Se for o último elemento da lista
            elif posicao == len(self):
                carga = self.__final.carga
                cursor = self.__inicio
                # Percorre a lista até o elemento anterior ao que será removido
                for _ in range(posicao - 2):
                    cursor = cursor.proximo
                cursor.proximo = self.__inicio
                self.__final = cursor

            # Caso não seja um elemento extremo
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