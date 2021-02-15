from utils.quicksort import quickSort
from app.Node import Node
from app.Graph import Graph
from utils.fileReader import readGraph

## TESTE QUICKSORT
# arr = []
# auxArr = [1, 0, 2]
# node1 = Node(1, 2)
# node3 = Node(1, 4)
# node2 = Node(1, 3)
# arr.append(node1)
# arr.append(node3)
# arr.append(node2)

# for x in arr:
#   print(x.degree)

# print('----------')
# quickSort(arr, auxArr, 0, len(arr)-1)
# for y in auxArr:
#   print(y)

# file = open('test.txt', 'r')
# print(file.readline().split(' '))
numNodes = 0
numEdges = 0
graph = Graph()
edges = readGraph('test')
for edge in edges:
  graph.addEdgeToGraph(edge[0], edge[1])
print('Cores: ', graph.greedyAlgorithm()) 
graph.printGraph()
