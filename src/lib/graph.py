class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.graph = {}

    """ For directed graphs, the edge is
    from node1 to node2"""
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def nodeExists(self, node):
        return node in self.graph

    def add_node(self, node):
        if not self.nodeExists(node):
            self.graph[node] = []

    #returns the number of connected components.  This should be used for undirected graphs
    def countConnectedComponents(self):
        count = 0
        visitedDict = {}
        for key in self.graph:
            visitedDict[key] = False
        
        for vertex, visited in visitedDict.items():
            if not visited:
                self.visitComponentNodes(vertex, visitedDict)
                count += 1
        
        return count
    
    #Recursively mark all nodes in the same component as startNode using DFS
    def visitComponentNodes(self, startNode, visitedDict):
        visitedDict[startNode] = True
        for node in self.graph[startNode]:
            if not visitedDict[node]:
                self.visitComponentNodes(node,visitedDict)