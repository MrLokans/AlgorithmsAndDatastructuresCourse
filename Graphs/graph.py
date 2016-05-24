"""This notebook provides dijkstra's short path algorithm implementation"""

class Graph(object):
    
    def __init__(self):
        self.vertices_dict = {}
    
    @property
    def num_vertices(self):
        return len(self.vertices_dict)
    
    @property
    def vertices(self):
        return list(self.vertices_dict)
    
    def __iter__(self):
        return iter(self.vertices_dict.values())
    
    def add_vertex(self, node):
        """Adds new vertext to graph"""
        new_vertex = Vertex(node)
        self.vertices_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, node):
        """Gets vertext from graph is vertext is present,
        otherwise returns None"""
        return self.vertices_dict.get(node, None)
    
    def add_edge(self, from_node, to_node, weight=0):
        """Adds edge from 'from_node' to 'to_node' with the given weight."""
        if from_node not in self.vertices_dict:
            self.add_vertex(from_node)
        if to_node not in self.vertices_dict:
            self.add_vertex(to_node)
            
        self.vertices_dict[from_node].add_neighbor(self.vertices_dict[to_node], weight)
        self.vertices_dict[to_node].add_neighbor(self.vertices_dict[from_node], weight)

class Vertex(object):
    
    def __init__(self, node):
        self._id = node
        self.adjacent = {}
    
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    @property
    def connections(self):
        return list(self.adjacent)
    
    @property
    def id(self):
        return self._id
    

if __name__ == "__main__":
    
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    
    g.add_edge('a', 'b', 40)
    g.add_edge('a', 'c', 30)
        
    for v in g:
        print(v)
