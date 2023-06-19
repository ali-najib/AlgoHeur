#from code.import_data import stations
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys
#from code.station import Station
#from code.route import Route
from array import *
import time

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
    with open(f"/Users/ali/Documents/Programming/AlgoHeur/data/ConnectiesNationaal.csv", 'r') as g:
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

class Baseline_search():

    def __init__(self, stations) -> None:
        self.route_batch = []
        self.ridden_connections = []
        self.twofold_connectioncount = 0
        self.stations = stations
        for station in self.stations:
            self.twofold_connectioncount += len(station.connections)


    def run(self):

        # Initialize variables
        route_count = 0
        
        # Continue if route_count is less than 20 and not all connections have been used
        while (route_count < 20):
            limit = 0
            
            # Set start station
            
            start_station = random.choice(self.stations)
            route = Route(start_station)
            
            # If route-total_time is less than 180, extend route.
            while limit == 0:

                S = random.choice([0, 0, 0, 20, 0])
                connection = random.choice(start_station.connections)
                destination = connection[0]
                time = connection[1]
                route.add_route(destination, time)
                route.total_time += S

                if route.total_time > 180:
                    limit = 1
                    route.delete_route(destination, time)
                    route_count += 1
                    self.route_batch.append(route)
                    break

                self.ridden_connections.append((start_station, destination))
                self.ridden_connections.append((destination, start_station))
                start_station = destination
                continue
        
        # Keep track of iterations
        # print(len(set(self.ridden_connections)))
        # print(self.twofold_connectioncount)
        # print(self.twofold_connectioncount is len(set(self.ridden_connections)))
        # print("Found Route:", self.route_batch)

        Min = 0
        for route in self.route_batch:
            Min += route.total_time
        p = len(set(self.ridden_connections))/(self.twofold_connectioncount) 
        T = len(self.route_batch)
        K = 10000*p - (T*100 + Min)

        return self.ridden_connections, self.route_batch, K
    

    def visualise(self):
        # visualise!
        route_batch = Baseline_search(stations).run()
        route_batch = route_batch[1]

        counter = 1
        for route in route_batch:
            route_length = len(route.route)
            for i in range(0, route_length-2):
                
                plt.plot([route.route[i+1].coordinates[1], route.route[i].coordinates[1]], [route.route[i+1].coordinates[0], route.route[i].coordinates[0]], 'k-', alpha = 0.5, linewidth = 3)
                plt.plot(route.route[i].coordinates[1], route.route[i].coordinates[0], 'ro', alpha = 0.4)
                plt.plot(route.route[i+1].coordinates[1], route.route[i+1].coordinates[0], 'ro', alpha = 0.4)

            for station in stations:
                plt.plot(station.coordinates[1], station.coordinates[0], 'ro', alpha=0.1)
                plt.text(station.coordinates[1], station.coordinates[0], station.name, fontsize= 6)
                for connection in station.connections:
                    plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-', alpha=0.05)  

            # setting title
            plt.title(f"Lijnvoering-element {counter} Route", fontsize=12)
            counter += 1
            
            # setting x-axis label and y-axis label
            plt.xlabel("chart X-coordinate")
            plt.ylabel("chart Y-coordinate")
            plt.show()
        return





def optimize(lines_batch, iteration_count):
    K_list = []
    for i in range(0, iteration_count):
        K_list.append(lines_batch[i][1])
    max_value = max(K_list)
    index = K_list.index(max_value)
    optimal_route = lines_batch[index][0]
    print("Max K-score found:", max_value)
    print("Optimal Line:", optimal_route)
    return optimal_route

# Can be run with both Holland and Nationaal.
#data = random_search(10000)
#print(data)
#sns.distplot(data, hist=True, kde=True, 
#             bins=100, color = 'darkblue', 
#             hist_kws={'edgecolor':'black'},
#             kde_kws={'linewidth': 3})

# Plot formatting
#plt.title('Baseline Results (10000 runs, Setting = Holland)')
#plt.xlabel('K-value')
#plt.ylabel('Density')
#plt.show()


runresult = Baseline_search(stations).run()
print(runresult[2])

#optimize(lines_batch, 1000)