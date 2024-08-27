graph = {
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}
visited =set()
def dfs(visited, graph, node):
    if node not in graph:
        print(f"node {node} not found in the graph!")
        return
    if node not in visited:
        print(node, end= " ")
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("This is the Depth First Search")
dfs(visited, graph, 0)