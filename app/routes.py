import csv

class Routes:
    available_routes = []

    def __init__(self, file_name):
        with open(file_name, 'rb') as file:
            reader = csv.reader(file)
            try:
                for row in reader:
                    self.available_routes.append(row)
            except csv.Error as e:
                sys.exit('file %s, row %d: %s' % (file_name, reader.line_num, e))

