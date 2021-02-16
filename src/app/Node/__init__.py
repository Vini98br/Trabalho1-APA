from app.Edge import Edge
class Node:
  def __init__(self, id, exitDegree):
    self.edgeList = []
    self.adjacentColors = []
    self.id = id
    self.degree = exitDegree
    self.visited = False
    self.color = -1

  def addEdge(self, destinyNodeId, sourceNodeId, destinyNodeIndex, sourceNodeIndex):
    edge = Edge(destinyNodeId, sourceNodeId, destinyNodeIndex, sourceNodeIndex)
    if destinyNodeId == self.id:
      self.degree += 2
    else:
      self.degree += 1
    self.edgeList.append(edge)

  def addAdjacentColor(self, color):
    flag = False
    for item in self.adjacentColors:
      if item == color:
        flag = True
        break
    
    if flag == False:
      self.adjacentColors.append(color)

  def verifyIfNodeIsAdjacent(self, id):
    for edge in self.edgeList:
      if(edge.destinyNodeId == id):
        return True
    return False
       
