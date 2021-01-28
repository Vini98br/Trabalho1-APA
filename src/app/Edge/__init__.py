class Edge:
  def __init__(self, destinyNodeId, edgeId, destinyNodeIndex, sourceNodeIndex):
    self.destinyNodeId = destinyNodeId
    self.edgeId = edgeId
    self.destinyNodeIndex = destinyNodeIndex
    self.sourceNodeIndex = sourceNodeIndex

  def __init__(self):
    self.destinyNodeId = 0
    self.edgeId = 0
    self.destinyNodeIndex = 0
    self.sourceNodeIndex = 0