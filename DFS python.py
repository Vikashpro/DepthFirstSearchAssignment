def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)
    print(start, end=" ")

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)

# Example usage:
# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform DFS starting from vertex 'A'
depth_first_search(graph, 'A')
