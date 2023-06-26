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
import math
import random


####################################################################################
#### Convert to a class, and add visualize functions!


class SimulatedAnnealing():
    
    def __init__(self, stations, route_duration, route_count):
        """
        Initialise variables pertaining to the SimulatedAnnealing class and used in this implementation
        of the SimulatedAnnealing search-algorithm.
        """
        
        # Initialize Annealing-variables to be manipulated in iterate
        self.twofold_connectioncount = 0
        for station in stations:
            self.twofold_connectioncount += len(station.connections)

        # Retreive result from Baseline_search
        self.runresults = Baseline_search(stations).run(route_duration, route_count)

        # Ridden_connections keeps track of all connections have already been used in some route.
        self.ridden_connections = self.runresults[0]

        # Retrieve the Baseline_search lijnvoering and name it route_batch
        self.route_batch = self.runresults[1]

        # Initilize variables with which variables are kept track of.
        self.annealing_score = []
        self.annealing_search = []
        self.iteration_numbers = []
        

    def iterate(self, iteration_count, temperature, temperature_function, alpha, route_duration):
        """
        Performs the Simulated Annealing search-algorithm.
        """

        # Retrieve K-score corresponding to Baseline_search lijnvoering for comparison with newfound values of K, i.e., for performing Hillclimber-search.
        K1 = self.runresults[2]
        
        # Keep track of iteration number
        iteration_number = 0

        # Initialize temperature
        T0 = temperature
        T = T0
        
        # Run Simulated-Annealing iteration_count amount of times.
        for j in range(0, iteration_count):

            # Choose route to potentially be replaced in lijnvoering.
            route1 = random.choice(self.route_batch)

            # Retrieve the length of this route.
            route1_length = len(route1.route)

            # For each connection pertaining to the retrieved route, remove this connection from ridden_connections 
            # Since this route is now removed from the current state of the lijnvoering (and perhaps to be replaced by another route).
            for i in range(0, route1_length - 2):

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

            # Perform Simulated Annealing
            old_value = K1
            new_value = K2

            # Define delta as using to calculate probability
            delta = new_value - old_value

            # If the growth is too High, no growth at all occurs; annealing must happen gradually or by 'annealing' through profound shrinkage.
            probability = math.exp(-0.01*(delta)/T)

            # If additionally newfound K is higher, update old K to new K and keep new route in lijnvoering.
            if random.random() < probability and K2 >= K1:
                K1 = K2
            # else keep old lijnvoering and old K.
            else:
                self.route_batch.remove(route)
                self.route_batch.append(route1)

            # Print K-score for keeping track of K1 score
            print("Annealing-score:", K1)
            print("Iteration-number:", iteration_number)

            # According on alpha and the temperature-function, update T.
            alpha = alpha
            if temperature_function == 1:
                T = T * alpha
            elif temperature_function == 2:
                T = T - T0/iteration_count

            # Keep track of iteration numbers for later use in performing eperiments and plotting the results
            iteration_number += 1
            self.iteration_numbers.append(iteration_number)


            # Keep track of K-scores, both old and new, for later use in performing experiments and plotting the results.
            self.annealing_score.append(K1)
            self.annealing_search.append(K2)

        # return all objects necessary for later use in experimentation and visualisation
        return self.iteration_numbers, self.annealing_score, self.annealing_search, self.route_batch



 ##################### Experiment and visualize! #######################


    
    def plot_expo(self, iteration_count, route_duration, route_count):
        """
        Performs experiment for simulated annealing: 
            Choose Exponential Temperature-function
            Vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
        
        And plots the results.
        """

        # For alpha = 0, 0.1, 0.2, 0.3, ..., 1, perform experiment.
        for i in range(0,11):
            alpha = i/10
            Annealing_result = SimulatedAnnealing(stations, route_duration, route_count).iterate(iteration_count, 10000, 1, alpha, route_duration)
            plt.plot(Annealing_result[0], Annealing_result[1], linewidth=0.8, label="alpha = {}".format(alpha))

        # Plot the results
        plt.title(r'Simulated Annealing, score vs iteration under $\alpha$ and Exponential-Annealing.')
        plt.xlabel("Iteration Count")
        plt.ylabel(r'Annealing Score')
        plt.legend()
        plt.show()


    
    def plot_linear(self, iteration_count, route_duration, route_count):
        """
        Performs experiment for simulated annealing: 
            Choose Linear Temperature-function
            Vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
        
        And plots the results.
        """

        # For alpha = 0, 0.1, 0.2, 0.3, ..., 1, perform experiment.
        for i in range(0,11):
            alpha = i/10
            Annealing_result = SimulatedAnnealing(stations, route_duration, route_count).iterate(iteration_count, 10000, 2, alpha, route_duration)
            plt.plot(Annealing_result[0], Annealing_result[1], linewidth=0.8, label="alpha = {}".format(alpha))

        # Plot the results
        plt.title(r'Simulated Annealing, score vs iteration under $\alpha$ and Linear-Annealing.')
        plt.xlabel("Iteration Count")
        plt.ylabel(r'Annealing Score')
        plt.legend()
        plt.show()


    def search_vs_score(self, iteration_count, route_duration, route_count):
        """
        Gives an impression of the inner-workings of Simulated Annealing whilst maximizing K.
        Does this via a plot.
        """

        # Fix alpha at an arbitrary, e.g., alpha = 0.9.
        alpha = 0.9

        # Perform simulated annealing under chosen alpha
        Annealing_result = SimulatedAnnealing(stations, route_duration, route_count).iterate(iteration_count, 10000, 1, alpha, route_duration)
        plt.plot(Annealing_result[0], Annealing_result[1], label = 'Annealing K-score')
        plt.plot(Annealing_result[0], Annealing_result[2], linewidth = 0.9, label = 'Intermediate K-scores')

        # Plot the results
        plt.title(r'Simulated Annealing, score vs iteration Exponential Annealing.')
        plt.xlabel("Iteration Count")
        plt.ylabel(r'Annealing K-score, $\alpha = 0.9$')
        plt.legend()
        plt.show()
        
 
    def Optimal_lijnvoering_finder(self, iteration_count, route_duration, route_count):
        """
        Calculates and plots the lijnvoering found upon applying simulated annealing optimization with 
        a chosen amount of iterations. 
        
        Here, an experiment is conducted under:
            Vary the Temperature function over Linear and Exponential
            Vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
        
        We choose the lijnvoering with highest K under variable alpha and temperature function, and
        chosen amount of iterations.

        Finally, we give plots of the resuting optimal lijnvoering.
        """

        # Initialize lists of K-scores to maximized over upon searching for the optimal lijnvoering
        K_list_linear = []
        K_list_expo = []
        K_list1 = []
        K_list2 = []
        k = 0

        # Fill the list of K-scores-lists under a linear temperature function by lists of K-scores (for each iteration) under various alpha.
        for i in range(0, 11):
            alpha = i/10
            K_list_linear.append(SimulatedAnnealing(stations, route_duration, route_count).iterate(iteration_count, 1000, 2, alpha, route_duration))

        # Fill the list K_list1 by the maximum K-score in each list in K_list_linear.
        for i in range(0,11):
            max_value = max(K_list_linear[i][1])
            K_list1.append(max_value)

        # Find the index for which K_list1 reaches its maximum value.
        index = K_list1.index(max(K_list1))

        # Acces the K_list_linear under this index and retrieve its resulting route_batch, i.e. lijnvoering
        route_batch_linear = K_list_linear[index][3]


        # Perform a similar procedure for the Exponential Temperature function
        for i in range(0, 11):
            alpha = i/10
            K_list_expo.append(SimulatedAnnealing(stations, route_duration, route_count).iterate(iteration_count, 1000, 1, alpha, route_duration))
        for i in range(0,11):
            max_value = max(K_list_expo[i][1])
            K_list2.append(max_value)
        index = K_list2.index(max(K_list2))
        route_batch_expo = K_list_expo[index][3]

        # We now have two optimal lijvoeringen, one from linear and one from exponential temp. function.
        # Choose for the lijnvoering with highest K-score from the two.
        if max(K_list2) > max(K_list1):
            route_batch_optimal = route_batch_expo
            score = max(K_list2)
            k = 1
        else:
            route_batch_optimal = route_batch_linear
            k = 2
            score = max(K_list1)


        # Now write the optimal lijnvoering out to output_annealing so as to observe the lijnvoering in text-form.
        f = open("results/output_annealing.csv", "w")
        f.truncate()
        f.close()
        with open("results/output_annealing.csv", 'w', newline='') as file:
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
            plt.title(f"Lijnvoering(score = {score})-element {counter}")
            counter += 1
            
            # setting x-axis label and y-axis label
            plt.xlabel("chart X-coordinate")
            plt.ylabel("chart Y-coordinate")

            # Show plots
            plt.show()


# Now simulate!
# Delete or add a hashtag in front of the below lines in order to run or disable them.

#SimulatedAnnealing(stations).plot_linear(10000, 180)
#SimulatedAnnealing(stations).plot_expo(10000, 180)
#SimulatedAnnealing(stations).search_vs_score(10000, 180)
#SimulatedAnnealing(stations).Optimal_lijnvoering_finder(10000, 180)
