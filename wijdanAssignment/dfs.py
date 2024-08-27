def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    
    visited.add(start)
    
    print(start, end=' ')
    
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}


print("DFS Traversal Order:")
dfs(graph, 1)
