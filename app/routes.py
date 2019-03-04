from dijkstra import *

class Routes:
    def __init__(self, csv_content):
        self.available_routes = csv_content

    def get_available_routes_graph(self):
        graph = []

        for route in self.available_routes:
            graph.append(tuple(route))

        return graph

    def get_cheapest_path(self, start, goal):
        graph = Graph(self.get_available_routes_graph())

        cheapest_path = graph.dijkstra(start, goal)

        if not cheapest_path:
            raise Exception('Dead end was found.')

        return cheapest_path
