from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge to the graph (u -> v)."""
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        """Breadth-First Search (BFS)"""
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))

# Example usage for BFS
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('C', 'G')

print("BFS starting from node A:")
g.bfs('A')
