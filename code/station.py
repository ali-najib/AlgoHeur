"""Class station."""

class Station():
    """Class station."""
    counter = 1
    def __init__(self, name, y, x):
        """Initalize class."""
        self.id = Station.counter
        self.name = name
        self.visited = False
        self.coordinates = (y, x)
        self.connections = []
        Station.counter += 1

    def add_connection(self, destination, time):
        """"""
        self.connections.append((destination, time, False))

    def ridden_connection(self, destination):
        """Sets a connection to ridden"""
        for connection in self.connections:
            if connection[0] == destination:
                connection[2] == True


