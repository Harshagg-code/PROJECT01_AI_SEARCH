import requests
import json
import time


LOCATIONS = [
    "Chicago Loop, Chicago, IL",
    "Wicker Park, Chicago, IL",
    "Hyde Park, Chicago, IL",
    "Lincoln Park, Chicago, IL",
    "Pilsen, Chicago, IL",
    "Evanston, IL",
    "Oak Park, IL",
    "Cicero, IL",
    "Skokie, IL",
    "Naperville, IL",
    "Aurora, IL",
    "Elgin, IL",
    "Schaumburg, IL",
    "Arlington Heights, IL",
    "Des Plaines, IL",
    "Berwyn, IL",
    "Downers Grove, IL",
    "Joliet, IL",
    "Waukegan, IL",
    "Elmhurst, IL",
    "Orland Park, IL",
    "Tinley Park, IL",
]

EDGES = [
    ("Chicago Loop, Chicago, IL", "Wicker Park, Chicago, IL"),
    ("Chicago Loop, Chicago, IL", "Hyde Park, Chicago, IL"),
    ("Chicago Loop, Chicago, IL", "Lincoln Park, Chicago, IL"),
    ("Chicago Loop, Chicago, IL", "Pilsen, Chicago, IL"),
    ("Lincoln Park, Chicago, IL", "Wicker Park, Chicago, IL"),
    ("Lincoln Park, Chicago, IL", "Evanston, IL"),
    ("Wicker Park, Chicago, IL", "Oak Park, IL"),
    ("Pilsen, Chicago, IL", "Cicero, IL"),
    ("Pilsen, Chicago, IL", "Berwyn, IL"),
    ("Hyde Park, Chicago, IL", "Orland Park, IL"),
    ("Oak Park, IL", "Cicero, IL"),
    ("Oak Park, IL", "Elmhurst, IL"),
    ("Cicero, IL", "Berwyn, IL"),
    ("Berwyn, IL", "Downers Grove, IL"),
    ("Evanston, IL", "Skokie, IL"),
    ("Skokie, IL", "Des Plaines, IL"),
    ("Des Plaines, IL", "Arlington Heights, IL"),
    ("Arlington Heights, IL", "Schaumburg, IL"),
    ("Schaumburg, IL", "Elgin, IL"),
    ("Elmhurst, IL", "Schaumburg, IL"),
    ("Elmhurst, IL", "Downers Grove, IL"),
    ("Downers Grove, IL", "Naperville, IL"),
    ("Naperville, IL", "Aurora, IL"),
    ("Aurora, IL", "Elgin, IL"),
    ("Downers Grove, IL", "Orland Park, IL"),
    ("Orland Park, IL", "Tinley Park, IL"),
    ("Tinley Park, IL", "Joliet, IL"),
    ("Naperville, IL", "Joliet, IL"),
    ("Skokie, IL", "Waukegan, IL"),
    ("Arlington Heights, IL", "Waukegan, IL"),
]


URL_NOMINATIM = "https://nominatim.openstreetmap.org/search"

OSRM_URL = "http://router.project-osrm.org/route/v1/driving"


def get_road_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    url = f"{OSRM_URL}/{lon1},{lat1};{lon2},{lat2}"

    params = {"overview": "false"}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if data.get("code") != "Ok":
        return None

    distance_meters = data["routes"][0]["distance"]

    return distance_meters/1000


def build_graph():

    print("Geocoding all locations")
    coordinates = geocode_all(LOCATIONS)

    print("Fetching road distance for edges")

    edges_with_distance = []

    for place1, place2 in EDGES:
        if place1 not in coordinates or place2 not in coordinates:
            print(f" SKIPPING edge ({place1}, {place2}) - missing coordinates")
            continue

        distance = get_road_distance(coordinates[place1], coordinates[place2])

        if distance is None:
            print(f" WARNING: no route found for ({place1}, {place2})")
            continue
        print(f"  {place1} <-> {place2}: {distance:.2f} km")

        edges_with_distance.append({
            "from" : place1,
            "to" : place2,
            "distance_km" : round(distance, 2)
        })

        time.sleep(1)


    graph = {
        "nodes": [
            {"name": name, "lat": lat, "lon": lon}
            for name, (lat, lon) in coordinates.items()
        ],
        "edges": edges_with_distance
    }
    return graph


def save_graph(graph, filename="map_data.json"):
    with open(filename, "w") as f:
        json.dump(graph, f, indent=2)
    print(f"Saved graph to {filename}")



def geocode(place_name):
    parameters = {
        "q": place_name,
        "format" : "json",
        "limit": 1,
    }


    headers ={
        "User-Agent" : "CS411-Search-Visualiser/1.0"
    }


    response = requests.get(URL_NOMINATIM, params=parameters, headers=headers)
    response.raise_for_status()
    results = response.json()


    if not results:
        return None

    latitude = float(results[0]["lat"])
    longitude= float(results[0]["lon"])

    return (latitude, longitude)


def geocode_all(locations):
  
    coordinates = {}
    for place in locations:
        print(f"Geocoding: {place}")
        coords = geocode(place)
        if coords is None:
            print(f"  WARNING: no result for {place}")
        else:
            coordinates[place] = coords
        time.sleep(1) 
    return coordinates




if __name__ == "__main__":
    graph = build_graph()
    save_graph(graph)