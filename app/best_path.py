from routes import Routes
from formatter import *
import sys

class BestPath:
    def start(self):
        routes = Routes(file_name= sys.argv[1])

        goal = parse_origin_goal(goal= sys.argv[2])

        best_path = routes.get_cheaper_path(goal[0], goal[1])

        formatted_best_path = format_output(best_path)
        print('best route: ' + formatted_best_path)

        sys.exit(0)

def main():
    application = BestPath()
    application.start()

if __name__ == '__main__':
    main()
