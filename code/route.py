"""Route class."""
class Route():
    """Class route."""
    counter = 1
    def __init__(self, start):
        self.id = Route.counter
        self.route = [start]
        self.total_time = 0
        Route.counter += 1

    def add_route(self, destination, time):
        self.route.append(destination)
        self.total_time += time

    def delete_route(self, destination, time):
        self.route.remove(destination)
        self.total_time -= time
