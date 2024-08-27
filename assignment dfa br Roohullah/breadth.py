from collections import deque

def bfs(graph, start):
    visited = set()      # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        if vertex not in visited:
            print(vertex, end=' ')  # Print the current vertex
            visited.add(vertex)  # Mark the vertex as visited

            # Enqueue all unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # Output: A B C D E F