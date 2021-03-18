def readGraphWithWeight(filename):
  with open('{filename}.txt'.format(filename=filename), 'r') as reader:
    lines = reader.readlines()
    edgeArr = []
    numNodes = lines[0].rsplit('\n')[0]
    for index in range(1, len(lines)):
      node1 = lines[index].split(' ')[0]
      node2 = lines[index].split(' ')[1]
      weight = lines[index].split(' ')[2].rsplit('\n')[0]
      edgeArr.append([node1, node2, weight])
    return edgeArr
