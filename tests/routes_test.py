import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../app"))
import pytest
from routes import Routes
from collections import deque

class TestRoutes:

    def test_get_cheapest_path(self):
        expected = deque(['GRU', 'BRC', 'SCL', 'ORL', 'CDG'])

        csv_content_mock = [
            ['GRU', 'BRC', '10'],
            ['BRC', 'SCL', '5'],
            ['GRU', 'CDG', '75'],
            ['GRU', 'SCL', '20'],
            ['GRU', 'ORL', '56'],
            ['ORL', 'CDG', '53'],
            ['ORL', 'CDG', '8'],
            ['SCL', 'ORL', '20']
        ]

        routes = Routes(csv_content_mock)

        cheapest_path = routes.get_cheapest_path('GRU', 'CDG')

        assert cheapest_path == expected

    def test_get_available_routes_graph(self):
        expected = [
            ('GRU', 'BRC', '10'),
            ('BRC', 'SCL', '5'),
            ('GRU', 'CDG', '75'),
            ('GRU', 'SCL', '20'),
            ('GRU', 'ORL', '56'),
            ('ORL', 'CDG', '53'),
            ('ORL', 'CDG', '8'),
            ('SCL', 'ORL', '20')
        ]

        csv_content_mock = [
            ['GRU', 'BRC', '10'],
            ['BRC', 'SCL', '5'],
            ['GRU', 'CDG', '75'],
            ['GRU', 'SCL', '20'],
            ['GRU', 'ORL', '56'],
            ['ORL', 'CDG', '53'],
            ['ORL', 'CDG', '8'],
            ['SCL', 'ORL', '20']
        ]

        routes = Routes(csv_content_mock)

        routes_graph = routes.get_available_routes_graph()

        assert routes_graph == expected
