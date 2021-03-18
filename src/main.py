from utils.quicksort import quickSort
from app.Node import Node
from app.Graph import Graph
from utils.fileReader import readGraphWithWeight
import sys
import time
import math

def main(args):
  # if(len(args) > 1):
  #   print('------------')
  #   print('Round: ', args[1])
  #   print('------------')
  # numNodes = 0
  # numEdges = 0
  # graph = Graph()
  # filename = 'grafo_125'
  # edges = readGraphWithWeight("in/{filename}".format(filename=filename))
  # print(edges)
  # for edge in edges:
  #   graph.addEdgeToGraphWithWeight(edge[0], edge[1], edge[2])
  # graph.printGraphWithWeight()  # Imprime o grafo

  # startTimeFloyd = time.time()
  # # greedyColors = graph.greedyAlgorithm()
  # # print('Cores Guloso: ', greedyColors)
  # endTimeFloyd = time.time()
  # execTimeFloyd = round((endTimeFloyd - startTimeFloyd)*1000, 3)
  # print("--- %f milliseconds ---" % execTimeFloyd)

  # with open('out/{filename}-out.csv'.format(filename=filename), 'a') as outFile:
  #   outFile.write('{execTimeFloyd}; \n'.format(execTimeFloyd=str(execTimeFloyd).replace('.', ','))

  # #graph.printGraphWithWeight() # Imprime o grafo

  graph = Graph()
  graph.addEdgeToGraphWithWeight(1,2,5)
  graph.addEdgeToGraphWithWeight(1,3,10)
  graph.addEdgeToGraphWithWeight(2,3,15)
  
  graph.printGraphWithWeight() # Imprime o grafo

main(sys.argv)
