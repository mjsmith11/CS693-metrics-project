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