import csv



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
print(stations)





# connecties = Connecties()
# for station in stations:
#     # print(station.station_name)
#     print(station.connections[0])