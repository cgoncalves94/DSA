def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start] - visited:
        dfs_recursive(graph, neighbor, visited)
    return visited

def main():
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    print("Original graph: ", graph)
    print("DFS traversal: ", dfs_recursive(graph, 'A'))
    
if __name__ == "__main__":
    main()