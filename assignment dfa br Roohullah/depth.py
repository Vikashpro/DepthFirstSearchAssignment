def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the set of visited nodes
    visited.add(start)  # Mark the current node as visited
    print(start, end=' ')  # Print the current node

    # Recur for all the neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')  # Output: A B D E F C