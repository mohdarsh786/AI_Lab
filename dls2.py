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
node='A'
goal='E'
max_depth=2
result=dls(graph,node,goal,max_depth)
print("Goal found within limit:", result)