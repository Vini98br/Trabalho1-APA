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

  startTimeBruteForce = time.time()
  bruteForceColors = graph.bruteForce()
  print('Cores Força bruta: ', bruteForceColors) 
  endTimeBruteForce = time.time()
  execTimeBruteForce = round((endTimeBruteForce - startTimeBruteForce)*1000, 3)
  print("--- %f milliseconds ---" % execTimeBruteForce)

  with open('out/{filename}-out.csv'.format(filename=filename), 'a') as outFile:
    outFile.write('{greedyColors};{execTimeGreedy};{bruteForceColors};{execTimeBruteForce} \n'
      .format(
        greedyColors=greedyColors, 
        execTimeGreedy=str(execTimeGreedy).replace('.',','), 
        execTimeBruteForce=str(execTimeBruteForce).replace('.',','), 
        bruteForceColors=bruteForceColors)
    )

  # graph.printGraph()

main(sys.argv)
