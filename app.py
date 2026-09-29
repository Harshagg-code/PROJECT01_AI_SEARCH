from flask import Flask, render_template, request, jsonify
from uninformed import load_graph, bfs, dfs, ucs, ids
from informed import load_graph_and_coords, greedy, a_star

app = Flask(__name__)

# Load graph data once at startup, not on every request
GRAPH = load_graph()
GRAPH_WITH_COORDS, COORDS = load_graph_and_coords()

ALGORITHMS = {
    "bfs": lambda start, goal: bfs(GRAPH, start, goal),
    "dfs": lambda start, goal: dfs(GRAPH, start, goal),
    "ucs": lambda start, goal: ucs(GRAPH, start, goal),
    "ids": lambda start, goal: ids(GRAPH, start, goal),
    "greedy": lambda start, goal: greedy(GRAPH_WITH_COORDS, COORDS, start, goal),
    "astar": lambda start, goal: a_star(GRAPH_WITH_COORDS, COORDS, start, goal),
}

ALGORITHM_INFO = {
    "bfs": {
        "name": "Breadth First Search",
        "main_idea": "Explores the graph level by level, expanding all nodes at the current depth before moving deeper.",
        "node_selection": "Chooses the oldest node in the FIFO queue (first discovered, first expanded).",
        "information_used": "Only depth/order of discovery, no path cost or heuristic.",
    },
    "dfs": {
        "name": "Depth First Search",
        "main_idea": "Dives as deep as possible down one path before backtracking to try alternatives.",
        "node_selection": "Chooses the most recently discovered node in the LIFO stack.",
        "information_used": "Only order of discovery, no path cost or heuristic.",
    },
    "ucs": {
        "name": "Uniform Cost Search",
        "main_idea": "Always expands the path with the lowest total cost so far, guaranteeing the cheapest path is found.",
        "node_selection": "Chooses the node with the lowest cumulative path cost from a priority queue.",
        "information_used": "Path cost (cumulative distance) only, no heuristic.",
    },
    "ids": {
        "name": "Iterative Deepening Search",
        "main_idea": "Repeats depth limited DFS with increasing depth limits until the goal is found, combining DFS's low memory use with BFS's shortest path guarantee.",
        "node_selection": "Same as DFS within each bounded pass; the depth limit increases across passes.",
        "information_used": "Depth only, no path cost or heuristic.",
    },
    "greedy": {
        "name": "Greedy Best First Search",
        "main_idea": "Always expands the node that appears closest to the goal, ignoring cost already spent.",
        "node_selection": "Chooses the node with the lowest heuristic (straight line distance to goal) from a priority queue.",
        "information_used": "Heuristic estimate only, no path cost.",
    },
    "astar": {
        "name": "A* Search",
        "main_idea": "Combines path cost so far with a heuristic estimate to the goal, expanding the node with the lowest total estimated cost.",
        "node_selection": "Chooses the node with the lowest f(n) = g(n) + h(n) from a priority queue.",
        "information_used": "Both path cost (g) and heuristic estimate (h).",
    },
}


@app.route("/")
def index():
    locations = sorted(GRAPH.keys())
    return render_template("index.html", locations=locations)


@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json()
    start = data.get("start")
    goal = data.get("goal")
    algorithm = data.get("algorithm")

    if algorithm not in ALGORITHMS:
        return jsonify({"error": "Unknown algorithm"}), 400
    if start not in GRAPH or goal not in GRAPH:
        return jsonify({"error": "Unknown location"}), 400

    path, cost, nodes_expanded = ALGORITHMS[algorithm](start, goal)

    if path is None:
        return jsonify({"error": "No path found"}), 404

    path_coords = [{"name": name, "lat": COORDS[name][0], "lon": COORDS[name][1]} for name in path]

    return jsonify({
        "path": path,
        "path_coords": path_coords,
        "cost": round(cost, 2),
        "nodes_expanded": nodes_expanded,
        "algorithm_info": ALGORITHM_INFO[algorithm],
    })


@app.route("/api/graph")
def get_graph():
    nodes = [{"name": name, "lat": lat, "lon": lon} for name, (lat, lon) in COORDS.items()]
    edges = []
    seen = set()
    for name, neighbors in GRAPH.items():
        for neighbor, distance in neighbors:
            edge_key = tuple(sorted([name, neighbor]))
            if edge_key not in seen:
                seen.add(edge_key)
                edges.append({"from": name, "to": neighbor, "distance_km": distance})
    return jsonify({"nodes": nodes, "edges": edges})


if __name__ == "__main__":
    app.run(debug=True)