import json
from collections import deque
import heapq

def load_graph(filename="map_data.json"):
    with open(filename) as f:
        data = json.load(f)

    adjacency = {node["name"]: [] for node in data["nodes"]}
    for edge in data["edges"]:
        adjacency[edge["from"]].append((edge["to"], edge["distance_km"]))
        adjacency[edge["to"]].append((edge["from"], edge["distance_km"]))

    return adjacency




def bfs (graph, start, goal):

    if start == goal:
        return [start], 0, 0


    visited = {start}

    queue = deque([(start, [start], 0)])

    nodes_expanded = 0


    while queue:

        current, path, cost = queue.popleft()
        nodes_expanded+=1


        for neighbour, distance in graph[current]:
            if neighbour == goal:
                return path + [neighbour], cost + distance, nodes_expanded

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour], cost + distance))


    return None, None, nodes_expanded    




def dfs (graph, start, goal):
    if start == goal:
        return [start], 0, 0

    visited = {start}

    stack = [(start, [start], 0)]

    nodes_expanded = 0

    while stack:

        current, path, cost = stack.pop()

        nodes_expanded+=1

        if current == goal:
            return path, cost, nodes_expanded

        for neighbour, distance in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, path + [neighbour], cost+distance))
   
   
    return None, None, nodes_expanded    




def ucs(graph, start, goal):
    if start == goal:
        return [start], 0,0

    visited = set()

    priority_queue = [(0, start, [start])]
    nodes_expanded = 0


    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)


        if current in visited:
            continue

        visited.add(current)
        nodes_expanded +=1



        if current == goal:
            return path, cost, nodes_expanded


        for neighbour, distance in graph[current]:
            if neighbour not in visited:
                heapq.heappush(priority_queue, (cost+distance, neighbour, path + [neighbour]))

    return None, None, nodes_expanded



#helper for ids
def depth_limited_dfs(graph, current, goal, limit, path, cost, visited, nodes_expanded):
    nodes_expanded[0] += 1

    if current == goal:
        return path, cost

    if limit <= 0:
        return None, None

    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            result_path, result_cost = depth_limited_dfs(
                graph, neighbor, goal, limit - 1,
                path + [neighbor], cost + distance, visited, nodes_expanded
            )
            if result_path is not None:
                return result_path, result_cost
            visited.remove(neighbor) 

    return None, None


def ids(graph, start, goal, max_depth=50):
    if start == goal:
        return [start], 0, 0

    total_expanded = 0
    for limit in range(max_depth + 1):
        visited = {start}
        nodes_expanded = [0]  
        result_path, result_cost = depth_limited_dfs(
            graph, start, goal, limit, [start], 0, visited, nodes_expanded
        )
        total_expanded += nodes_expanded[0]
        if result_path is not None:
            return result_path, result_cost, total_expanded

    return None, None, total_expanded    