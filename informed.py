import json
import heapq
import math


def load_graph_and_coords(filename="map_data.json"):
    """Load map_data.json. Returns (adjacency_list, coords_dict)."""
    with open(filename) as f:
        data = json.load(f)

    adjacency = {node["name"]: [] for node in data["nodes"]}
    for edge in data["edges"]:
        adjacency[edge["from"]].append((edge["to"], edge["distance_km"]))
        adjacency[edge["to"]].append((edge["from"], edge["distance_km"]))

    coords = {node["name"]: (node["lat"], node["lon"]) for node in data["nodes"]}

    return adjacency, coords


def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Earth radius in km

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def heuristic(node, goal, coords):
    return haversine(coords[node], coords[goal])


def greedy(graph, coords, start, goal):
    if start == goal:
        return [start], 0, 0

    visited = set()
    priority_queue = [(heuristic(start, goal, coords), start, [start], 0)]
    nodes_expanded = 0

    while priority_queue:
        h, current, path, cost = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, cost, nodes_expanded

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (
                    heuristic(neighbor, goal, coords),
                    neighbor,
                    path + [neighbor],
                    cost + distance
                ))

    return None, None, nodes_expanded


def a_star(graph, coords, start, goal):
    if start == goal:
        return [start], 0, 0

    visited = set()
    priority_queue = [(heuristic(start, goal, coords), 0, start, [start])]
    nodes_expanded = 0

    while priority_queue:
        f, cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, cost, nodes_expanded

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                new_cost = cost + distance
                new_f = new_cost + heuristic(neighbor, goal, coords)
                heapq.heappush(priority_queue, (new_f, new_cost, neighbor, path + [neighbor]))

    return None, None, nodes_expanded