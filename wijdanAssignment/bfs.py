from collections import deque

def bfs(graph, start):
    
    queue = deque([start])
    
    visited = set()
    
    bfs_order = []

    while queue:
    
        node = queue.popleft()
        
    
        if node not in visited:
            
            visited.add(node)
            
            bfs_order.append(node)
            
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_order


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}


start_node = 1
bfs_result = bfs(graph, start_node)
print("BFS Traversal Order:", bfs_result)
