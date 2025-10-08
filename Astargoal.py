import heapq
def heuristic(node,goal):
    return 0
def astar(graph,start,goal):
    queue=[]
    heapq.heappush(queue,(0+heuristic(start,goal),0,start,[start]))
    visited=set()
    while queue:
        est_cost,cur_cost,current,path=heapq.heappop(queue)
        if current==goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor,weight in graph.get(current,{}).items():
            if neighbor not in visited:
                new_cost=cur_cost+weight
                est=new_cost+heuristic(neighbor,goal)
                heapq.heappush(queue,(est,new_cost,neighbor,path+[neighbor]))
    return None
