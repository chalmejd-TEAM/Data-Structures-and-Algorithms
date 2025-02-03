#       2 --- 0
#     /  \
#    1 -- 3
# 

# Edge List
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
graph = [[2], [2,3], [0,1,3], [1,3]]

# Adjacent Matrix
graph = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0]
}

# -------------------------------------------------------------------

# Undirected, unweighted, using adjacenct list
class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1
        return
    
    def addEdge(self, node1, node2):
        # Undirected
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return
    
    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ''
            for vertex in nodeConnections:
                connections = connections + vertex + ' '
            print(node + '-->' + connections)

myGraph = Graph()

myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()

# Answer:
#  0-->1 2 
#  1-->3 2 0 
#  2-->4 1 0 
#  3-->1 4 
#  4-->3 2 5 
#  5-->4 6 
#  6-->5