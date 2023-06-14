from code.import_data import stations
import matplotlib.pyplot as plt
import csv
import random

from code.station import Station
from code.route import Route



def Route_():
    route = Route(random.choice(stations))

    for i in range(0,6):
        
        current_station = route.route[-1]
        destination = random.choice(current_station.connections)
        object = destination[0]
        time = destination[1]

        route.add_route(object, time)
    
    return route


def Plot():
    """give visual representation of the data"""

    for station in stations:
        plt.plot(station.coordinates[1], station.coordinates[0], 'ro')
        for connection in station.connections:
            plt.plot([connection[0].coordinates[1], station.coordinates[1]], [connection[0].coordinates[0], station.coordinates[0]], 'k-')

    # plt.axis([4.2, 5.2, 51.5, 53.5])
    plt.show()

Plot()

def Output(route, score):
    names = []
    for station in route.route:
        names.append(station.name)

    with open("resultaten/output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["train", "stations"])
        writer.writerow(["train_{}".format(route.id),f'[{", ".join(names)}]'])
        writer.writerow(["score", "{}".format(score)])


route = Route_()
Output(route, 8300)