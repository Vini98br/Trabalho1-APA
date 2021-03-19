from utils.quicksort import quickSort
from app.Node import Node
from app.Graph import Graph
from utils.fileReader import readGraph
import sys
import time
import math

def main(args):
  if(len(args) > 1):
    print('------------')
    print('Round: ', args[1])
    print('------------')
  numNodes = 0  
  numEdges = 0
  graph = Graph()
  filename = 'school1'
  edges = readGraph("in/{filename}".format(filename=filename))
  for edge in edges:
    graph.addEdgeToGraph(edge[0], edge[1])
  
  startTimeGreedy = time.time()
  greedyColors = graph.greedyAlgorithm()
  print('Cores Guloso: ', greedyColors) 
  endTimeGreedy = time.time()
  execTimeGreedy = round((endTimeGreedy - startTimeGreedy)*1000, 3)
  print("--- %f milliseconds ---" % execTimeGreedy)

  startTimeSequential = time.time()
  sequentialColors = graph.sequential()
  print('Cores Força bruta: ', sequentialColors) 
  endTimeSequential = time.time()
  execTimeSequential = round((endTimeSequential - startTimeSequential)*1000, 3)
  print("--- %f milliseconds ---" % execTimeSequential)

  with open('out/{filename}-out.csv'.format(filename=filename), 'a') as outFile:
    outFile.write('{greedyColors};{execTimeGreedy};{sequentialColors};{execTimeSequential} \n'
      .format(
        greedyColors=greedyColors, 
        execTimeGreedy=str(execTimeGreedy).replace('.',','), 
        execTimeSequential=str(execTimeSequential).replace('.',','), 
        sequentialColors=sequentialColors)
    )

  # graph.printGraph() # Imprime o grafo

main(sys.argv)
