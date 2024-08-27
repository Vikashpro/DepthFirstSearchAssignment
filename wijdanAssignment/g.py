import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))
    
    
    visited = set()
    
    
    came_from = {}
    
    while open_list:
    
        _, current = heapq.heappop(open_list)
        
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        visited.add(current)
        
        
        for neighbor in graph[current]:
            if neighbor not in visited:
            
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))
                
                if neighbor not in came_from:
                    came_from[neighbor] = current

    
    return None


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}


heuristics = {
    1: 6,
    2: 5,
    3: 2,
    4: 1,
    5: 3,
    6: 0
}


start_node = 1
goal_node = 6
path = greedy_best_first_search(graph, heuristics, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found.")
