# To allow mathematical calculations
from flask import Flask, render_template
import math
import itertools  # provides Permutations() to help in generating all possible routes

app = Flask(__name__)
current_location = (-1.30000, 36.97995)

property_locations = [
    (-1.29238, 36.98497),
    (-1.29304, 36.97818),
    (-1.29255, 36.97772),
    (-1.29788, 36.98163),
    (-1.29506, 36.98250)
]  # property locations to be visited

# This function will take 2 parameters to calculate the distance between two points


def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    R = 6371.0  # earth's radius in km

    phi1 = math.radians(lat1)  # convert degrees to radians
    phi2 = math.radians(lat2)  # convert degrees to radians

    delta_phi = math.radians(lat2-lat1)  # difference between 2 latitudes
    delta_lambda = math.radians(lon2-lon1)  # difference between 2 longitudes

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(
        delta_lambda / 2)**2  # calculates the central angle between two coordinates

    # Calculate the actual angle
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c  # Earth's radius * central angle to bring distance in km between 2 points


@app.route('/')
def show_map():
    # Generates the permutations of possible paths
    all_routes = itertools.permutations(property_locations)
    shortest_route = None  # Stores the best path found so far
    # initialized to a very large number so the first calculated route will be better
    min_total_distance = float('inf')

    # Loop through all possible routes
    for route in all_routes:
        total_distance = 0  # keeps track of the total distance for the current route
    # adds distance from your starting point to first location
        total_distance += haversine_distance(current_location, route[0])
        for i in range(len(route) - 1):
            # while looping each route, it will add the distance from each location to the next in that route
            total_distance += haversine_distance(route[i], route[i+1])

        if total_distance < min_total_distance:  # Update the shortest route if this one is better
            min_total_distance = total_distance
            shortest_route = route

    path = [current_location] + list(shortest_route)
    if not path or not isinstance(path[0], (list, tuple)):
        return "Invalid path data", 500

    return render_template('map.html', route=path)


if __name__ == '__main__':
    app.run(debug=True)
