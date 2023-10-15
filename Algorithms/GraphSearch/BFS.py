from collections import deque

def bfs(graph, start):
    """
    Perform a breadth-first search on a graph, starting from a given node.

    Args:
        graph (dict): A dictionary representing the graph, where each key is a node and its value is a list of adjacent nodes.
        start (any): The starting node for the search.

    Returns:
        A list of nodes in the order they were visited during the search.
    """
    # Create a queue to keep track of nodes to visit
    queue = deque([start])
    # Create a set to keep track of visited nodes
    visited = set([start])
    # Create a list to keep track of the order in which nodes are visited
    order_visited = [start]

    # While there are still nodes to visit
    while queue:
        # Get the next node to visit
        current_node = queue.popleft()

        # For each adjacent node
        for neighbor in graph[current_node]:
            # If the node hasn't been visited yet
            if neighbor not in visited:
                # Add it to the queue and mark it as visited
                queue.append(neighbor)
                visited.add(neighbor)
                # Add it to the list of visited nodes
                order_visited.append(neighbor)

    # Return the list of visited nodes
    return order_visited

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Original graph: ", graph)
    print("BFS traversal: ", bfs(graph, 'A'))
    
if __name__ == "__main__":
    main()