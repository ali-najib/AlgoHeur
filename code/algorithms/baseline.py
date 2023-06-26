from code.algorithms.import_data import stations
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys
from code.classes.station import Station
from code.classes.route import Route
from array import *
import time


####################################################################################


class Baseline_search():

    def __init__(self, stations) -> None:
        """
        Initializes the twofold_connectioncount variable using the stations import
        """

        # Initialize twofold_connectioncount variable using the stations argument
        self.route_batch = []
        self.ridden_connections = []
        self.twofold_connectioncount = 0
        self.stations = stations
        for station in self.stations:
            self.twofold_connectioncount += len(station.connections)

    def run(self, route_duration, rcount):
        """
        Runs the Baseline-search algorithm
        """

        # Initialize baseline_search (i.e. random-search) variables
        self.route_batch = []
        self.ridden_connections = []
        self.twofold_connectioncount = 0
        for station in self.stations:
            self.twofold_connectioncount += len(station.connections)
        route_count = 0
        
        # Continue if route_count is less than 20 and not all connections have been used
        while (route_count < rcount):
            limit = 0
            
            # Set start station
            start_station = random.choice(self.stations)
            route = Route(start_station)
            
            # Loop while route can be extented
            while limit == 0:

                connection = random.choice(start_station.connections)
                destination = connection[0]
                time = connection[1]
                route.add_route(destination, time)

                # If total time consumed by is greater than route_duration, e.g. 120 or 180, break while loop
                if route.total_time > route_duration:
                    limit = 1
                    route.delete_route(destination, time)
                    route_count += 1
                    self.route_batch.append(route)
                    break

                # Update ridden_connections by inserting connection newly ridden by newly constructed route.
                self.ridden_connections.append((start_station, destination))
                self.ridden_connections.append((destination, start_station))

                # Update start station upon further extension of route
                start_station = destination
                continue
    
        # Compute the score K for found route_batch, i.e. lijnvoering
        Min = 0
        for route in self.route_batch:
            Min += route.total_time

        # Using the list of ridden_connection calculate fraction of all connections ridden
        p = len(set(self.ridden_connections))/(self.twofold_connectioncount) 
       
        # Retreive amount of routes in the lijnvoering
        T = len(self.route_batch)

        #Calculate K
        K = 10000*p - (T*100 + Min)

        # return all objects necessary for later use in experimentation and visualisation
        return self.ridden_connections, self.route_batch, K
    

    def visualise(self, route_duration, rcount):
        """
        Constructs a map of the stations with their interconnections, and enforces a route on the map.
        """

        # Retrieve results from Baseline_search(stations).run(), initialize route_batch
        route_batch = Baseline_search(stations).run(route_duration, rcount)
        route_batch = route_batch[1]

        # Perform visualisation by plotting each route on one coordinate system seperately
        counter = 1

        # iterate over route_batch, plot each route on a seperate coordinate system.
        for route in route_batch:
            route_length = len(route.route)

            # Plot the route
            for i in range(0, route_length-2):
                
                plt.plot([route.route[i+1].coordinates[1], route.route[i].coordinates[1]], [route.route[i+1].coordinates[0], route.route[i].coordinates[0]], 'k-', alpha = 0.5, linewidth = 3)
                plt.plot(route.route[i].coordinates[1], route.route[i].coordinates[0], 'ro', alpha = 0.4)
                plt.plot(route.route[i+1].coordinates[1], route.route[i+1].coordinates[0], 'ro', alpha = 0.4)

            # Plot the coordinate system
            for station in stations:
                plt.plot(station.coordinates[1], station.coordinates[0], 'ro', alpha=0.1)
                plt.text(station.coordinates[1], station.coordinates[0], station.name, fontsize= 6)
                for connection in station.connections:
                    plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-', alpha=0.05)  

            # Set plot title
            plt.title(f"Lijnvoering-element {counter} Route", fontsize=12)
            counter += 1
            
            # Set x-axis label and y-axis label
            plt.xlabel("chart X-coordinate")
            plt.ylabel("chart Y-coordinate")
            plt.show()
        return
    

    def density_plot(self, iteration_count, route_duration, rcount):
        """
        Constructs a density plot of K-scores found after running Baseline-search.
        Important for knowing where initial values from running Hillclimber and SimulatedAnnealing comes from.
        """

        # Initialize variables
        data = []
        counter = 0

        # For each run, append its resulting K to data
        while counter < iteration_count:
            runresults = Baseline_search(stations).run(route_duration, rcount)
            data.append(runresults[2])
            counter += 1

        # Plot the results
        sns.distplot(data, hist=True, kde=True, 
             bins=100, color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 3})

        #Plot formatting
        plt.title(f'Baseline Results ({iteration_count} runs, Setting = Nationaal)')
        plt.xlabel('K-value')
        plt.ylabel('Density')
        plt.show()


# Now simulate!
#Baseline_search(stations).density_plot(10000, 180)
#Baseline_search(stations).visualise()