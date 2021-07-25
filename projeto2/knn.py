class Run:
    """
    Esta classe define o perfil de investidor de acordo com a carteira de investimentos utilizando KNN.
    
    Atributos:
    data(lista) : Uma lista de investidores com perfil ja definido.
    k(int) : O valor de k, ou seja, o número de vizinhos que deseja comparar.  
    """
    def __init__(self, data, k):
        self.data = data
        self.k = k
        
    # Recebe a tupla da carteira do investidor e retorna uma lista com a distância em relação a todos os ja valiados.
    def calc_distan(self, ponto):
        """
        Calcula a distância do ponto em relação a todos da tabela treinada(data).
        
        Parâmetros:
        ponto(lista) : Recebe a lista de um investidor contendo [cpf, <espaço para alocar o perfil>, [carteira de investimentos]].
        
        Retorno:
        Lista : Contendo a distância de todos os elementos da lista treinada em relação ao ponto  definido.
        """
        distancias = []
        for i in self.data:
            soma = 0
            for j in range(len(i[2])):
                soma += (i[2][j] - ponto[j]) ** 2
            dist = soma ** .5
            distancias.append(dist)

        return distancias
                           
    # Recebe a lista de distâncias e retorna as 5 menores.
    def achar_vizinhos(self, lista):
        """
        Pega os k vizinhos mais próximos.
        
        Parâmetros:
        lista[lista] : Contém as distâncias em relação a todos da lista 'treinada' (retorno do método 'calc_distan').
        
        Retorno:
        Lista : Contendo os k vizinhos mais próximos.
        """
        lista_enumerada = list(enumerate(lista))
        lista_organizada = sorted(lista_enumerada, key=lambda enumerada: enumerada[1])
        lista_pronta = []

        for indice in range(len(lista)):
            lista_pronta.append(sorted(lista_organizada[indice]))

        return lista_pronta[0:self.k]
    
    # Recebe a lista com as menores distâncias e retorna a moda delas.
    def calc_moda(self, vizinhos):
        """
        Calcula a moda de perfil dos vizinhos.
        
        Parâmetros:
        vizinhos(lista) : Contém os k vizinhos mais próximos (retorno do método 'achar_vizinhos').
        
        Retorno:
        Lista : Contendo o perfil mais frequente entre os vizinhos e, quantas vezes ele se repete.
        """
        repeticoes = []
        vizinhos_class = []
        vizinhos_indice = []

        for i in vizinhos:
            vizinhos_indice.append(i[0])

        for i in vizinhos_indice:
            vizinhos_class.append(self.data[i][1])

        for element in vizinhos_class:
            soma = 0
            for i in vizinhos_class:
                if i == element:
                    soma += 1

            repeticoes.append([element, soma])

        return max(repeticoes, key=lambda rep: rep[1])