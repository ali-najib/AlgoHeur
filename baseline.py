from code.import_data import stations
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys
from code.station import Station
from code.route import Route
from array import *


# Baseline random-search algorithm.
def random_search(iteration_count): 

    # Initialize variables
    data = []
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
        while (route_count <= 20):
            limit = 0
            
            # Set start station
            start_station = random.choice(stations)
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
                    route_batch.append(route)
                    break
                ridden_connections.append((start_station, destination))
                ridden_connections.append(((destination, start_station)))
                start_station = destination

        # Keep track of iterations and scores
        Min = 0
        for route in route_batch:
            Min += route.total_time
        p = len(set(ridden_connections))/(2* twofold_connectioncount) 
        T = len(route_batch)
        K = 10000*p - (T*100 + Min)
        data.append(K)
        print("Connections ridden:", len(set(ridden_connections))/2)
        print("Fraction of Connections ridden:", len(set(ridden_connections))/(twofold_connectioncount))
        with open("out.txt", "a") as f:
            lines_batch.append((route_batch, K))
        counter += 1
        
    return data


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
data = random_search(10000)
print(data)
sns.distplot(data, hist=True, kde=True, 
             bins=100, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 3})

# Plot formatting
plt.title('Baseline Results (10000 runs, Setting = Holland)')
plt.xlabel('K-value')
plt.ylabel('Density')
plt.show()


#optimize(lines_batch, 1000)