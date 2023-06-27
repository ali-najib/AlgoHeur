from code.algorithms.baseline import Baseline_search
from code.algorithms.Hillclimber import Hillclimber
from code.algorithms.SimulatedAnnealing import SimulatedAnnealing
from code.algorithms.Hillclimber_prime import Hillclimber_prime
from code.algorithms.SimulatedAnnealing_prime import SimulatedAnnealing_prime
from code.algorithms.import_data import stations
from code.algorithms.opdrachtsolver import visualize
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import random
import sys

for station in stations:
    plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
    plt.text(station.coordinates[1], station.coordinates[0], station.name, fontsize= 6)
    for connection in station.connections:
        plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')
# setting title
plt.title("Map of all stations and their interconnections, Nationally")

# setting x-axis label and y-axis label
plt.xlabel("chart X-coordinate")
plt.ylabel("chart Y-coordinate")

plt.show()  