#from code.import_data import stations
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys
#from code.station import Station
#from code.route import Route
from array import *
from baseline import Baseline_search
import math
import random



######### Instead of importing, include classes to file, and data downloads to file. ########

"""Class station."""

class Station():
    """Class station."""
    counter = 1
    def __init__(self, name, y, x):
        """Initalize class."""
        self.id = Station.counter
        self.name = name
        self.visited = False
        self.coordinates = (y, x)
        self.connections = []
        Station.counter += 1

    def add_connection(self, destination, time):
        """"""
        self.connections.append([destination, time, False])

    def ride_connection(self, destination):
        """Sets a connection to ridden"""
        for connection in self.connections:
            if connection[0] == destination:
                connection[2] == True

"""Route class."""
class Route():
    """Class route."""
    counter = 1
    def __init__(self, start):
        self.id = Route.counter
        self.route = [start]
        self.total_time = 0
        Route.counter += 1

    def add_route(self, destination, time):
        self.route.append(destination)
        self.total_time += time

    def delete_route(self, destination, time):
        self.route.remove(destination)
        self.total_time -= time

    def length(self):
        return len(self.route)


def Stations():
    # Creates list of all stations with coordinates
    stations = []
    with open(f"/Users/ali/Documents/Programming/AlgoHeur/data/StationsNationaal.csv", 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        if header != None:
            for row in reader:
                station = Station(row[0], float(row[1]), float(row[2]))
                stations.append(station)
    return stations


def Connections():
    connections = []
    stations = Stations()
    with open(f"data/ConnectiesNationaal.csv", 'r') as g:
        reader = csv.reader(g)
        header = next(reader)
        if header != None:
            for row in reader:

                for station_1 in stations:
                    if station_1.name == row[0]:

                        for station_2 in stations:
                            if station_2.name == row[1]:
                                station_1.add_connection(station_2, float(row[2]))

                for station_1 in stations:
                    if station_1.name == row[1]:

                        for station_2 in stations:
                            if station_2.name == row[0]:
                                station_1.add_connection(station_2, float(row[2]))
    return stations

stations = Connections()








####################################################################################

#### Convert to a class, and add visualize functions!









def SimulatedAnnealing(temperature, iterations):
    

    twofold_connectioncount = 0
    for station in stations:
        twofold_connectioncount += len(station.connections)

    runresults = Baseline_search(stations).run()
    ridden_connections = runresults[0]
    route_batch = runresults[1]
    K1 = runresults[2]

    T0 = temperature
    T = temperature

    for j in range(0, iterations):

        route1 = random.choice(route_batch)
        route1_length = len(route1.route)
        print(len(ridden_connections))

        for i in range(0, route1_length - 2):

            if (route1.route[i], route1.route[i+1]) in ridden_connections:
                ridden_connections.remove((route1.route[i], route1.route[i+1]))

            if (route1.route[i+1], route1.route[i]) in ridden_connections:
                ridden_connections.remove((route1.route[i+1], route1.route[i]))

        route_batch.remove(route1)

        start_station = random.choice(stations)
        route = Route(start_station)
        limit = 0

        while limit == 0:

            S = random.choice([0, 0, 0, 20, 0])
            connection = random.choice(start_station.connections)
            destination = connection[0]
            time = connection[1]
            route.add_route(destination, time)
            route.total_time += S
            if route.total_time > 120:
                route.delete_route(destination, time)
                limit = 1
                route_batch.append(route)
                break

            ridden_connections.append((start_station, destination))
            ridden_connections.append((destination, start_station))
            start_station = destination
            continue

        # Keep track of iterations and scores
        #print("Connections ridden:", len(set(ridden_connections))/2)
        Min = 0
        for route in route_batch:
            Min += route.total_time
        p = len(set(ridden_connections))/(twofold_connectioncount) 
        T = len(route_batch)
        K2 = 10000*p - (T*100 + Min)
        print("K2:", K2)

        # Perform simulated annealing
        old_value = K1
        new_value = K2
        delta = new_value - old_value

        # If the growth is too High, no growth at all occurs; annealing must happen gradually or by 'annealing' through profound shrinkage.
        probability = math.exp(-0.01*(delta)/T)
        #print("prob:", probability)
        #print("random", random.random())
        if random.random() < probability and K2 >= K1:
            K1 = K2
        else:
            route_batch.remove(route)
            route_batch.append(route1)
        print("K1:", K1)

        alpha = 0.99
        T = T * alpha



SimulatedAnnealing(1000, 100000)
