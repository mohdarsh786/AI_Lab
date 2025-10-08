def iddfs(graph,node,goal,max_depth):
    for depth in range(max_depth+1):
        print(f"Searching at the depth limit:{depth}")
        if dls(graph,node,goal,depth):
            return True
    return False

def dls(graph,node,goal,depth):
    if node==goal:
        return True
    if depth<=0:
        return False
    for child in graph.get(node,[]):
        if dls(graph,child,goal,depth-1):
            return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': []
}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
max_depth = int(input("Enter the maximum depth limit: "))

found = iddfs(graph, start, goal, max_depth)
print("Goal found within limit:", found)