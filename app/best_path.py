from routes import Routes
from formatter import *
import csv, sys

class BestPath:
    def start(self):
        csv_content = self.read_csv_file(sys.argv[1])

        routes = Routes(csv_content)

        goal = parse_origin_goal(goal= sys.argv[2])

        best_path = routes.get_cheapest_path(goal[0], goal[1])

        formatted_best_path = format_output(best_path)
        print('best route: ' + formatted_best_path)

        sys.exit(0)

    def read_csv_file(self, file_name):
        file_content = []

        with open(file_name, 'rb') as file:
            reader = csv.reader(file)
            try:
                for row in reader:
                    file_content.append(row)
            except csv.Error as e:
                sys.exit('file %s, row %d: %s' % (file_name, reader.line_num, e))

        return file_content

def main():
    application = BestPath()
    application.start()

if __name__ == '__main__':
    main()
