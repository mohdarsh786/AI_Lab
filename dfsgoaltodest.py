from collections import deque

def dfs_search(graph, start, target):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == target:
            print(f"\nFound target node: {target}")
            return True

        if node not in visited:
            visited.add(node)
            # Add neighbors in reverse order for similar output to recursive DFS
            stack.extend(neighbor for neighbor in reversed(graph[node]) if neighbor not in visited)

    print(f"Target node {target} not found in the graph.")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

hello = dfs_search(graph, start='A', target='F')
print("Search completed:", hello)