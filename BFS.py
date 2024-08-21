graph ={'A' : ['B','C'],
        'B' : ['D','E'],
        'C' : ['F','G'] 
}

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=' ')

    for item in graph:
        if item not in visited:
            dfs(graph , item , visited)

dfs(graph, 'A')
