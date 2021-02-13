from utils.quicksort import quickSort
from app.Node import Node

class Graph:
  def __init__(self):
    self.adjacentNodeList = []
    self.orderedIndexList = []  # Manda a posicao de todos os nós na listaAdj para o vetor ordenado
    self.auxSort = []

  def addNode(self, id):
    node = Node(id, 0)
    self.adjacentNodeList.append(node)

  def isOnGraph(self, id):
    if(len(self.adjacentNodeList) > 0):
      for node in self.adjacentNodeList:
        if node.id == id:
          return True
      return False
    else:
      return False

  def addEdgeToGraph(self, id1, id2):
    # containInGraph = [False, False]
    flag1 = False
    flag2 = False
    if self.isOnGraph(id1):
      flag1 = True
    else:
      self.addNode(id1) # Se não está no Grafo adicionar
      flag1 = True

    if self.isOnGraph(id2):
      flag2 = True
    else:
      self.addNode(id2) # Se não está no Grafo adicionar
      flag2 = True

    # print(containInGraph)
    # Se os dois ids estão no Grafo
    if flag1 != False and flag2 != False:
      indexNode1 = -1
      indexNode2 = -1
      for index in range(0, len(self.adjacentNodeList) - 1):
        if id1 != id2:
          if self.adjacentNodeList[index].id == id1:
            indexNode1 = index
          elif self.adjacentNodeList[index].id == id2:
            indexNode2 = index
          
          # print(indexNode1)
          # print(indexNode2)
        if indexNode1 != -1 and indexNode2 != -1:
          print(self.adjacentNodeList[indexNode1])
          self.adjacentNodeList[indexNode1].addEdge(id2, id1, indexNode2, indexNode1)
          self.adjacentNodeList[indexNode2].addEdge(id1, id2, indexNode1, indexNode2)
          break

  def greedyAlgorithm(self):
    # Limpando vetores auxiliares
    self.orderedIndexList = []
    self.auxSort = []

    cont = 0 # Contador auxiliar para o FOR
    for node in self.adjacentNodeList:
      node.color = -1 # Coloca as cores de todos os nos como -1
      self.orderedIndexList.append(cont) # Manda a posicao de todos os nós na listaAdj para o vetor ordenado
      cont += 1

    # for x in self.adjacentNodeList: 
    #   print(x.degree)

    self.auxSort = self.adjacentNodeList.copy()

    quickSort(self.auxSort, self.orderedIndexList, 0, len(self.auxSort) - 1) # Ordena o vetor em ordem decrescente em relação ao grau.

    maxColors = 0 # O maximo de cor no momento.
    
    firstNode = self.adjacentNodeList[self.orderedIndexList[0]]
    firstNode.color = maxColors # Pega o primeiro vertice com maior No (grau, não?) e adiciona a primeira cor a ele.

    for edge in firstNode.edgeList:
      self.adjacentNodeList[edge.destinyNodeIndex].addAdjacentColor(maxColors) # Adiciona a "cor" 0 no vetor de cores adjacentes de todos os nós adjacentes ao primeiro no.

    maxColors += 1 # Atualiza a cor

    for orderedIndex in self.orderedIndexList: # Pega os próximos nós de acordo com a ordem decrescente em relação ao grau.
      position = orderedIndex # Variável que guarda qual o indice da listaAdj fica o nó.

      for colorNumber in range(0, maxColors): # Loop que roda todas as cores que existem até o momento
        flag = False

        if colorNumber < maxColors: # Se colorNumber é igual a cor atual, então nenhum nó adjacente a ele tem cor maxColors, assim a cor dele sera maxColors e nao é preciso checar suas cores adjacentes.
          for adjacentColor in self.adjacentNodeList[position].adjacentColors: # Loop que percorre todas as cores que são adjacentes ao nó, pelo vetor adjacentColors que pertence ao nó.
            if adjacentColor == colorNumber:
              flag = True # Flag recebe true se existe a cor 'colorNumber" no vetor adjacentColors do nó, e assim passa para a próxima cor
              break
        
        # Se a Var flag for falsa, então temos que aquele indice de cor nao está sendo
        # utilizada por nenhum nó adjacente, portanto pode ser dada a esse nó, e para
        # isso, é necessário verificar se a cor i é uma cor que ja foi utilizada antes
        # ou é uma cor nova (o que implica que o nó é adjacente a todas as cores já
        # utilizadas), sendo assim necessário atualizar a variavel k, com uma cor nova.
        if flag == False and colorNumber < maxColors: # Cor "colorNumber" já existe
          self.adjacentNodeList[position].color = colorNumber
          for edge in self.adjacentNodeList[position].edgeList:
            self.adjacentNodeList[edge.destinyNodeIndex].addAdjacentColor(colorNumber) # Adiciona "maxColors" no vetor de cores adjacentes de todos os nós adjacentes ao no.
          break
        elif flag == False and colorNumber == maxColors:
          self.adjacentNodeList[position].color = colorNumber
          for edge in self.adjacentNodeList[position].edgeList:
            self.adjacentNodeList[edge.destinyNodeIndex].addAdjacentColor(colorNumber) # Adiciona "maxColors" no vetor de cores adjacentes de todos os nós adjacentes ao no
          maxColors += 1 # Atualiza com a nova cor   
          break

    return maxColors