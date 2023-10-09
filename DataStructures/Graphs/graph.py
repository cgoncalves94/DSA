# Import the Vertex class
from vertex import Vertex

# Adapted Graph class definition
class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed
        
    # Method to add a vertex
    def add_vertex(self, vertex_value):
        new_vertex = Vertex(vertex_value)
        self.graph_dict[vertex_value] = new_vertex
        
    # Method to add an edge
    def add_edge(self, from_vertex_value, to_vertex_value, weight=0):
        from_vertex = self.graph_dict[from_vertex_value]
        to_vertex = self.graph_dict[to_vertex_value]
        from_vertex.add_edge(to_vertex_value, weight)
        if not self.directed:
            to_vertex.add_edge(from_vertex_value, weight)
            
    # Method to get vertices
    def get_vertices(self):
        return list(self.graph_dict.keys())
        
    # Method to get edges
    def get_edges(self):
        edges = []
        for vertex in self.graph_dict.values():
            for neighbour in vertex.get_edges():
                edges.append((vertex.value, neighbour))
        return edges
        
    # Modified find_path method
    def find_path(self, start_vertex_value, end_vertex_value):
        # Initialize a list to store the path from start to end vertex
        path = []
        # Initialize a list for BFS traversal
        start = [(start_vertex_value, path)]
        # Initialize a set to keep track of visited vertices
        seen = set()
        
        while len(start) > 0:
            # Dequeue a vertex from start and get its current path
            current_vertex_value, current_path = start.pop(0)
            # Mark the vertex as visited
            seen.add(current_vertex_value)
            
            # Update the current path
            current_path = current_path + [current_vertex_value]
            
            # Check if we reached the end vertex
            if current_vertex_value == end_vertex_value:
                return current_path  # Return the path taken to reach here
            
            # Enqueue unvisited neighbors to start list for further traversal
            vertices_to_visit = set(self.graph_dict[current_vertex_value].edges.keys())
            for vertex in vertices_to_visit:
                if vertex not in seen:
                    start.append((vertex, current_path))
                    
        return None  # Return None if no path exists from start to end vertex
