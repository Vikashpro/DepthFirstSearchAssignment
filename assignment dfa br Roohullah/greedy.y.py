import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[start], start)]  # Priority queue with heuristic value

    while priority_queue:
        _, current = heapq.heappop(priority_queue)  # Dequeue the node with the lowest heuristic value

        if current in visited:
            continue

        print(current, end=' ')  # Print the current node
        visited.add(current)  # Mark it as visited

        if current == goal:
            print("\nGoal found!")
            return

        # Enqueue all unvisited neighbors with their heuristic values
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

heuristic = {
    'A': 6,  # Example heuristic values
    'B': 5,
    'C': 2,
    'D': 7,
    'E': 4,
    'F': 1
}
best_first_search(graph, 'A', 'F', heuristic) 