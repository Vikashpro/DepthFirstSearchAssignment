class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge to the graph (u -> v)."""
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        """Depth-First Search (DFS)"""
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, node, visited):
        """Helper function for DFS using recursion."""
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                self._dfs_recursive(neighbor, visited)

# Example usage for DFS
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('C', 'G')

print("DFS starting from node A:")
g.dfs('A')
