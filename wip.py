# Only run search1() with StationHolland.csv and ConnectiesHolland.csv!.
# search1() then solves Opdracht 1!
def search1(): 

    # Initialize variables
    ridden_connections = []
    twofold_connectioncount = 0
    for station in stations:
        twofold_connectioncount += len(station.connections)
    
    # Continue if not all conections have been used
    while len(ridden_connections) is not twofold_connectioncount:

        # Initialize variables
        route_batch = []
        ridden_connections = []
        route_count = 0
        
        # Continue if route_count is less than 7 and not all connections have been used
        while (route_count <= 7) and (len(ridden_connections) is not twofold_connectioncount):
            limit = 0
            
            # Set start station
            for station in stations:
                if station.visited == False:
                    start_station = station
                    route = Route(start_station)
                    break
            
            # If route-total_time is less than 120, extend route.
            while limit == 0:
                connection_iterator = 0
                for connection in start_station.connections:
                    destination = connection[0]
                    time = connection[1]
                    connection_iterator += 1

                    # If connection between start_station and destination has not yet been ridden
                    if (start_station, destination) not in ridden_connections:
                        route.add_route(destination, time)
                        if route.total_time > 120:
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
                        if route.total_time > 120:
                            limit = 1
                            route.delete_route(destination, time)
                            route_count += 1
                            route_batch.append(route)
                            break
                        start_station = destination
                        continue
        
        # Keep track of iterations
        print(len(ridden_connections))

    print(twofold_connectioncount)
    print(len(set(ridden_connections)))
    print(twofold_connectioncount is len(ridden_connections))
    print("Found Route:", route_batch)
    return ridden_connections, route_batch

# Only run search1() with StationHolland.csv and ConnectiesHolland.csv!.
search1()