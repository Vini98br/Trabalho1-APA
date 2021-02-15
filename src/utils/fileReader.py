def readGraph(filename):
  with open('./src/{filename}.txt'.format(filename=filename), 'r') as reader:
    lines = reader.readlines()
    edgeArr = []
    numNodes = lines[0].split(' ')[2]
    numEdges = lines[0].split(' ')[3].rsplit('\n')[0]
    for index in range(1, len(lines)):
      node1 = lines[index].split(' ')[1]
      node2 = lines[index].split(' ')[2].rsplit('\n')[0]
      edgeArr.append([node1, node2])
    return edgeArr
