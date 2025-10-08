def dfs(graph,start,goal):
    visited=set()
    stack=[stack]
    while stack:
        node=stack.pop()
        print(node,end=' ')
        if node==goal:
            print(f"\nFound target node: {goal}")
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(reversed(graph[node]))
    print(f"\nTarget node: {goal} not found in the graph.")
        