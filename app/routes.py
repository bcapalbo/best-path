class Routes:
    def __init__(self, csv_content):
        self.available_routes = csv_content

    def get_available_routes_graph(self):
        graph = {}

        for route in self.available_routes:
            if route[0] not in graph:
                graph[route[0]] = set()

            graph[route[0]].add(route[1])

        return graph

    def get_possible_paths(self, start, goal):
        available_routes_graph = self.get_available_routes_graph()
        queue = [(start, [start])]

        while queue:
            (vertex, path) = queue.pop(0)

            if vertex not in available_routes_graph:
                continue

            for next in available_routes_graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def get_cheapest_path(self, start, goal):
        possible_paths = list(self.get_possible_paths(start, goal))

        if not possible_paths:
            raise Exception('Dead end start was found.')

        routes_price = []

        for option, path in enumerate(possible_paths):
            routes_price.append(0)
            for i in range(len(path)-1):
                routes_price[option] += self.get_route_price(path[i], path[i+1])

        cheapest_path = routes_price.index(min(routes_price))

        return possible_paths[cheapest_path]

    def get_route_price(self, place_a, place_b):
        price_table = {}

        for available_route in self.available_routes:
            index = available_route[0] + '-' + available_route[1]

            price_table[index] = available_route[2]

        route_index = place_a + '-' + place_b

        return int(price_table[route_index])
