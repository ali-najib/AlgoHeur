from code.import_data import stations
import matplotlib.pyplot as plt
import csv
import random
from code.station import Station
from code.route import Route


# Only run search1() with StationHolland.csv and ConnectiesHolland.csv!.
# search2() then solves Opdracht 1!

class Baseline_search2():

    def __init__(self, stations) -> None:
        self.route_batch = []
        self.ridden_connections = []
        self.twofold_connectioncount = 0
        self.stations = stations
        for station in self.stations:
            self.twofold_connectioncount += len(station.connections)

        self.run()


    def run(self):
        
        # Continue if not all conections have been used
        while len(self.ridden_connections) is not self.twofold_connectioncount:

            # Initialize variables
            self.route_batch = []
            self.ridden_connections = []
            route_count = 0
            
            # Continue if route_count is less than 7 and not all connections have been used
            while (route_count <= 7) and (len(self.ridden_connections) is not self.twofold_connectioncount):
                limit = 0
                
                # Set start station
                for station in self.stations:
                    if station.visited == False:
                        start_station = station
                        route = Route(start_station)
                        station.visited == True
                        break
                
                # If route-total_time is less than 120, extend route.
                while limit == 0:
                    connection_iterator = 0
                    for connection in start_station.connections:
                        destination = connection[0]
                        time = connection[1]
                        connection_iterator += 1

                        # If connection between start_station and destination has not yet been ridden
                        if (start_station, destination) not in self.ridden_connections:
                            route.add_route(destination, time)
                            if route.total_time > 120:
                                limit = 1
                                route.delete_route(destination, time)
                                route_count += 1
                                self.route_batch.append(route)
                                break
                            self.ridden_connections.append((start_station, destination))
                            self.ridden_connections.append(((destination, start_station)))
                            start_station = destination
                            continue

                        # If there's no unridden connection from start_station
                        if connection_iterator == len(start_station.connections):
                            connection = random.choice(start_station.connections)
                            destination = connection[0]
                            route.add_route(destination, time)
                            if route.total_time > 120:
                                limit = 1
                                route.delete_route(destination, time)
                                route_count += 1
                                self.route_batch.append(route)
                                break
                            start_station = destination
                            continue
        
        # Keep track of iterations
        print(len(set(self.ridden_connections)))
        print(self.twofold_connectioncount)
        print(self.twofold_connectioncount is len(set(self.ridden_connections)))
        print("Found Route:", self.route_batch)
        return self.ridden_connections, self.route_batch
    
    def visualise(self):
        # visualise!
        route_batch = Baseline_search2(stations).run()
        route_batch = route_batch[1]

        for route in route_batch:
            route_length = len(route.route)
            for i in range(0, route_length-2):
                
                plt.plot([route.route[i+1].coordinates[1], route.route[i].coordinates[1]], [route.route[i+1].coordinates[0], route.route[i].coordinates[0]], 'k-')
                plt.plot(route.route[i].coordinates[1], route.route[i].coordinates[0], 'ro')
                plt.plot(route.route[i+1].coordinates[1], route.route[i+1].coordinates[0], 'ro')


            for station in stations:
                plt.plot(station.coordinates[1], station.coordinates[0], 'ro', alpha=0.1)
                for connection in station.connections:
                    plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-', alpha=0.1)
            
            plt.show()

        
        return


# Only run search2() with StationHolland.csv and ConnectiesHolland.csv!.
Baseline_search2(stations)
Baseline_search2(stations).visualise()

##--------------------------------------------------------------------------------##



class Baseline_search1():

    def __init__(self, stations) -> None:
        self.route_batch = []
        self.ridden_connections = []
        self.twofold_connectioncount = 0
        self.stations = stations
        for station in self.stations:
            self.twofold_connectioncount += len(station.connections)

        self.run()


    def run(self, iteration_count):
        
        # Initialize variables
        data = []
        lines_batch = []  # This is a batch of route_batch 'es.

        # Repeat search algorithm 100000 times.
        counter = 0
        while counter < iteration_count:

            # Initialize variables
            route_batch = []
            for station in stations:
                for connection in station.connections:
                    connection[2] = False
            route_count = 0
            
            # Current search algorithm maximizes p, and minimizes T given p. Can be better with Min-minimization.
            # Continue if route_count is less than 20 and not all connections have been used
            while (route_count <= 20):
                limit = 0
                
                # Set start station
                start_station = random.choice(stations)
                route = Route(start_station)
                
                # If route-total_time is less than 180, extend route.
                while limit == 0:

                    #S = random.choice([0, 0, 0, 20, 0])
                    connection = random.choice(start_station.connections)
                    destination = connection[0]
                    time = connection[1]
                    route.add_route(destination, time)
                    #route.total_time += S
                    if route.total_time > 180:
                        limit = 1
                        route.delete_route(destination, time)
                        route_count += 1
                        route_batch.append(route)
                        break
                    start_station.ride_connection(destination)
                    destination.ride_connection(start_station)
                    start_station = destination

            # Keep track of iterations and scores
            ridden_connectioncount = 0
            twofold_connectioncount = 0
            for station in stations:
                twofold_connectioncount += len(station.connections)
                for connection in station.connections:
                    ridden_connectioncount += connection[2]
        
        # Keep track of iterations
        print(len(set(self.ridden_connections)))
        print(self.twofold_connectioncount)
        print(self.twofold_connectioncount is len(set(self.ridden_connections)))
        print("Found Route:", self.route_batch)
        return self.ridden_connections, self.route_batch
    
    def visualise(self):
        # visualise!
        route_batch = Baseline_search2(stations).run()
        route_batch = route_batch[1]
        print("Found Route:", route_batch[1])

        #for route in self.route_batch:
        for route in route_batch:
            for station in route.route:
                plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
                for connection in station.connections:
                    plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')
            plt.show()
        
        return

# Only run search1() with StationHolland.csv and ConnectiesHolland.csv!.
Baseline_search2(stations)
#Baseline_search2(stations).visualise()




####--------------------------##################


# Baseline random-search algorithm.

#### Need debugger to work!!

def random_search(iteration_count): 

    # Initialize variables
    data = []
    lines_batch = []  # This is a batch of route_batch 'es.

    # Repeat search algorithm 100000 times.
    counter = 0
    while counter < iteration_count:

        # Initialize variables
        route_batch = []
        for station in stations:
            for connection in station.connections:
                connection[2] = False
        route_count = 0
        
        # Current search algorithm maximizes p, and minimizes T given p. Can be better with Min-minimization.
        # Continue if route_count is less than 20 and not all connections have been used
        while (route_count <= 20):
            limit = 0
            
            # Set start station
            start_station = random.choice(stations)
            route = Route(start_station)
            
            # If route-total_time is less than 180, extend route.
            while limit == 0:

                #S = random.choice([0, 0, 0, 20, 0])
                connection = random.choice(start_station.connections)
                destination = connection[0]
                time = connection[1]
                route.add_route(destination, time)
                #route.total_time += S
                if route.total_time > 180:
                    limit = 1
                    route.delete_route(destination, time)
                    route_count += 1
                    route_batch.append(route)
                    break
                start_station.ride_connection(destination)
                destination.ride_connection(start_station)
                start_station = destination

        # Keep track of iterations and scores
        ridden_connectioncount = 0
        twofold_connectioncount = 0
        for station in stations:
            twofold_connectioncount += len(station.connections)
            for connection in station.connections:
                ridden_connectioncount += connection[2]

        Min = 0
        for route in route_batch:
            Min += route.total_time
        p = ridden_connectioncount/(twofold_connectioncount) 
        T = len(route_batch)
        K = 10000*p - (T*100 + Min)
        data.append(K)
        print("Connections ridden:", ridden_connectioncount)
        print("Fraction of Connections ridden:", p)
        print("K:", K)
        lines_batch.append((route_batch, K))
        with open("out.txt", "a") as f:
            print("K:", K, file=f)
        counter += 1
    return data

#random_search(1000)


######--------------------------#########














# search2() solves Opdracht 1 and first part of Opdracht 2, but better solutions exist.
def search2(iteration_count): 

    # Initialize variables
    lines_batch = []  # This is a batch of route_batch 'es.
    ridden_connections = []
    twofold_connectioncount = 0
    for station in stations:
        twofold_connectioncount += len(station.connections)
    
    # Repeat search algorithm 100000 times.
    counter = 0
    while counter < iteration_count:

        # Initialize variables
        route_batch = []
        ridden_connections = []
        route_count = 0
        
        # Current search algorithm maximizes p, and minimizes T given p. Can be better with Min-minimization.
        # Continue if route_count is less than 20 and not all connections have been used
        while (route_count <= 20) and (len(ridden_connections) is not twofold_connectioncount):
            limit = 0
            
            # Set start station
            start_station = random.choice(stations)
            route = Route(start_station)
            
            # If route-total_time is less than 180, extend route.
            while limit == 0:
                connection_iterator = 0
                for connection in start_station.connections:
                    destination = connection[0]
                    time = connection[1]
                    connection_iterator += 1

                    # If connection between start_station and destination has not yet been ridden
                    if (start_station, destination) not in ridden_connections:
                        route.add_route(destination, time)
                        if route.total_time > 180:
                            limit = 1
                            route.delete_route(destination, time)
                            route_count += 1
                            route_batch.append(route)
                            break
                        ridden_connections.append((start_station, destination))
                        ridden_connections.append(((destination, start_station)))
                        start_station = destination
                        continue

                    # If there's no unridden connection from start_station
                    if connection_iterator == len(start_station.connections):
                        connection = random.choice(start_station.connections)
                        destination = connection[0]
                        route.add_route(destination, time)
                        if route.total_time > 180:
                            limit = 1
                            route.delete_route(destination, time)
                            route_count += 1
                            route_batch.append(route)
                            break
                        start_station = destination
                        continue
        
        # Keep track of iterations and scores
        print("Connections ridden:", len(set(ridden_connections))/2)
        Min = 0
        for route in route_batch:
            Min += route.total_time
        p = len(set(ridden_connections))/( twofold_connectioncount) 
        T = len(route_batch)
        K = 10000*p - (T*100 + Min)
        print("K:", K)
        lines_batch.append((route_batch, K))
        counter += 1

    return lines_batch


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
#lines_batch = search2(100000)
#optimize(lines_batch, 100000)