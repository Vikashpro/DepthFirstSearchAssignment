graph = {
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}
visited = []
queue =[]
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end =" ")
        
        for neighbour in graph [m]:
            if neighbour not in visited:
                visited.append (neighbour)
                queue.append(neighbour)
print("This is the breadth Frist Search")
bfs(visited, graph, 1)