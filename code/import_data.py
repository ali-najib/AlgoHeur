import csv
from code.station import Station

def Stations():
    # Creates list of all stations with coordinates
    stations = []
    with open("data/StationsHolland.csv", 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        if header != None:
            for row in reader:
                station = Station(row[0], float(row[1]), float(row[2]))
                stations.append(station)
    return stations


def Connecties():
    stations = Stations()
    with open("data/ConnectiesHolland.csv", 'r') as g:
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

stations = Connecties()

# connecties = Connecties()


# for station in stations:
#     # print(station.station_name)
#     print(station.connections[0])