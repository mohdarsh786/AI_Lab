from collections import deque
def bfs(graph,start,target):
    visited=set()
    queue=deque([start])
    while(queue):
        node=queue.popleft()
        print(node,end=" ")
        if node==target:
            print("Print node found:",target)
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)
    print("Target node not found:",target)
    return False

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
hello=bfs(graph,start='A',target='F')
print("Traget found:",hello)