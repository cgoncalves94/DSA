import heapq

def dijkstras(graph, start):
    """
    Dijkstra's algorithm implementation to find the shortest path from a starting node to all other nodes in a weighted graph.

    :param graph: A dictionary representing the graph where each key is a node and its value is a dictionary of its neighbors and their edge weights.
    :param start: The starting node to find the shortest path from.
    :return: A dictionary representing the shortest distance from the starting node to all other nodes in the graph.
    """
    # Initialize the distances dictionary with the starting node having a distance of 0 and all other nodes having a distance of infinity.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize the priority queue with the starting node and its distance.
    pq = [(0, start)]

    while pq:
        # Pop the node with the smallest distance from the priority queue.
        current_distance, current_node = heapq.heappop(pq)

        # If the current node has already been visited, skip it.
        if current_distance > distances[current_node]:
            continue

        # Iterate through the current node's neighbors and update their distances if a shorter path is found.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def main():
    graph = {
        'A': {'B': 5, 'C': 1},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
        'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
        'E': {'C': 8, 'D': 3},
        'F': {'D': 6}
    }

    print("Original graph: ", graph)
    print("Shortest distances from node 'A': ", dijkstras(graph, 'A'))

if __name__ == "__main__":
    main()