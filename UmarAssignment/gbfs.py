graph = {
    0: [1, 2, 3], 
    1: [0, 2], 
    2: [0, 1, 4], 
    3: [0], 
    4: [2]
}
heuristic = {
    0:7,
    1:6,
    2:2,
    3:9,
    4:0
}
def gbfs (graph, heuristic, start, goal):
    queue = [start]
    visited =set()
    while queue:
        queue.sort(key =lambda node: heuristic[node])
        current_node =queue.pop(0)
        print(current_node, end =" ")
        if current_node == goal:
            print("\nGoal is reached!")
            return
        for neighbour in graph[current_node]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
                
                print("\nGoal is not reached!")
                print("This the Greedy Best First Search Algorithm")
gbfs(graph,heuristic,0,4)
        