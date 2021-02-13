from utils.quicksort import quickSort
from app.Node import Node
from app.Graph import Graph

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
with open('./src/test.txt', 'r') as reader:
  # Read and print the entire file line by line
  lines = reader.readlines()
  numNodes = lines[0].split(' ')[2]
  numEdges = lines[0].split(' ')[3].rsplit('\n')[0]
  for index in range(1, len(lines)):
    node1 = lines[index].split(' ')[1]
    node2 = lines[index].split(' ')[2].rsplit('\n')[0]
    graph.addEdgeToGraph(node1, node2)

print('Cores: ', graph.greedyAlgorithm())
