from code.algorithms.import_data import stations
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys
from code.classes.station import Station
from code.classes.route import Route
from array import *
from code.algorithms.baseline import Baseline_search



## The Hillclimber-search algorithm
class Hillclimber():

    def __init__(self, stations) -> None:
        """
        Initialise variables pertaining to the Hillclimber class and used in this implementation
        of the hillclimber search-algorithm.
        """

        # Initialize Hillclimber-variables to be manipulated in iterate
        self.twofold_connectioncount = 0
        for station in stations:
            self.twofold_connectioncount += len(station.connections)
        self.hillclimber_score = []
        self.hillsearcher_score = []
        self.iteration_number = []


    def iterate(self, iteration_count, route_duration, route_count):
        """
        Performs the Hillclimber search-algorithm.
        """

        # Retreive result from Baseline_search
        self.runresults = Baseline_search(stations).run(route_duration, route_count)

        # Ridden_connections keeps track of all connections have already been used in some route.
        self.ridden_connections = self.runresults[0]

        # Retrieve the Baseline_search lijnvoering and name it route_batch
        self.route_batch = self.runresults[1]

        # Retrieve its corresponding K-score for comparison with newfound values of K, i.e., for performing Hillclimber-search.
        K1 = self.runresults[2]
        
        # Keep track of iteration number
        iteration_number = 0

        # Run Hillclimber iteration_count amount of times.
        for j in range(0, iteration_count):

            # Choose route to potentially be replaced in lijnvoering.
            route1 = random.choice(self.route_batch)

            # Retrieve the length of this route.
            route1_length = len(route1.route)

            # For each connection pertaining to the retrieved route, remove this connection from ridden_connections 
            # Since this route is now removed from the current state of the lijnvoering (and perhaps to be replaced by another route).
            for i in range(0, route1_length - 1):

                if (route1.route[i], route1.route[i+1]) in self.ridden_connections:
                    self.ridden_connections.remove((route1.route[i], route1.route[i+1]))
                if (route1.route[i+1], route1.route[i]) in self.ridden_connections:
                    self.ridden_connections.remove((route1.route[i+1], route1.route[i]))

            # Remove chosen route, route1, from the current state of the lijnvoering.
            # If this removal is the first removal, the current state of the lijnvoering is the baseline-lijnvoering.
            self.route_batch.remove(route1)

            # Choose a new start station, for constructing a new route to be included in the current lijnvoering.
            start_station = random.choice(stations)

            # Intialize new route
            route = Route(start_station)

            # Construct new route
            limit = 0

            # Loop while route can be extented
            while limit == 0:

                connection = random.choice(start_station.connections)
                destination = connection[0]
                time = connection[1]
                route.add_route(destination, time)

                # If total time consumed by is greater than route_duration, e.g. 120 or 180, break while loop
                if route.total_time > route_duration:
                    route.delete_route(destination, time)
                    limit = 1

                    # Include route constructed so far in the current state of the lijnvoering
                    self.route_batch.append(route)
                    break

                # Update ridden_connections by inserting connection newly ridden by newly constructed route.
                self.ridden_connections.append((start_station, destination))
                self.ridden_connections.append((destination, start_station))

                # Update start station upon further extension of route
                start_station = destination
                continue

            # Calculate the K-score for current state of the lijnvoering
            Min = 0
            for route in self.route_batch:
                Min += route.total_time

            # Using the list of ridden_connection calculate fraction of all connections ridden
            p = len(set(self.ridden_connections))/(self.twofold_connectioncount) 

            # Retreive amount of routes in the lijnvoering
            T = len(self.route_batch)

            #Calculate K
            K2 = 10000*p - (T*100 + Min)

            # Perform Hillclimber-search by comparing newly found K, i.e. K2, with the old K, i.e. K1.
            # If newfound K is higher, update old K to new K and keep new route in lijnvoering.
            if K2 >= K1:
                K1 = K2
            # else keep old lijnvoering and old K.
            else:
                self.route_batch.remove(route)
                self.route_batch.append(route1)

            # Print K scores for keeping track of K-scores.
            print("Hillcimber-score:", K1)
            print("Iteration-number:", iteration_number)

            # Keep track of K-scores, both old and new, for later use in performing experiments and plotting the results.
            self.hillclimber_score.append(K1)
            self.hillsearcher_score.append(K2)

            # Keep track of iteration numbers for later use in performing eperiments and plotting the results
            iteration_number += 1
            self.iteration_number.append(iteration_number)

            # Print iteration number for keeping track of iterations.
            print(iteration_number)

        # return all objects necessary for later use in experimentation and visualisation
        return self.iteration_number, self.hillclimber_score, self.hillsearcher_score, self.route_batch
    
    

########################### Visualize and experiment ##############################
    


    def plot(self, iteration_count, route_duration, route_count):
        """
        Visualizes the Hill-algorithm by plotting both the K-score for the Hillclimber
        and each K-score upon searching for the optimal K-score
        """

        # Retrieves results from running the Hillclimber algorithm
        Hillclimb_results = Hillclimber(stations).iterate(iteration_count, route_duration, route_count)

        # Plot the optimal K-score for the Hillclimber-search algorithm
        plt.plot(Hillclimb_results[0], Hillclimb_results[1], label='Hillclimber K-score')

        # Plot the K-score intermediate in every step of Hillclimber-search
        plt.plot(Hillclimb_results[0], Hillclimb_results[2], linewidth = 0.9, alpha = 0.8, label='Intermediate search-scores')

        # Form the plot and show it
        plt.title(r'Hillclimber, score vs iteration, setting Holland')
        plt.xlabel("Iteration Count")
        plt.ylabel(r'Hillclimber\'s K-score')
        plt.legend()
        plt.show()


    def optimal_lijnvoering_finder(self, iteration_count, route_duration, route_count):
        """
        Calculates and plots the lijnvoering found upon applying Hillclimber optimization with 
        a chosen amount of iterations. 

        We give plots of the resuting optimal lijnvoering.
        """
    
        # Retreive result from running the Hillclimber search algorithm that are relevant for finding the optimal lijnvoering.
        runresults = Hillclimber.iterate(self, iteration_count, route_duration, route_count)
        score = max(runresults[1])
        route_batch_optimal = runresults[3]

        # Now write the optimal lijnvoering out to output_annealing so as to observe the lijnvoering in text-form.
        f = open("results/output_hillcimber.csv", "w")
        f.truncate()
        f.close()

        with open("results/output_hillcimber.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["train", "stations"])
            for route in route_batch_optimal:
                names = []
                for station in route.route:
                    names.append(station.name)
                writer.writerow(["train_{}".format(route.id),f'[{", ".join(names)}]'])
            writer.writerow(["score", "{}".format(score)])

        # Now plot the optimal lijnvoering as usual.
        counter = 0
        for route in route_batch_optimal:
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
            plt.title(f"Lijnvoering(score = {score})-element {counter}", fontsize=10)
            counter += 1
            
            # setting x-axis label and y-axis label
            plt.xlabel("chart X-coordinate")
            plt.ylabel("chart Y-coordinate")
        
            plt.show()

