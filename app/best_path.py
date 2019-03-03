from routes import Routes
from formatter import *
import sys

class BestPath:
    def start(self):
        #carrega arquivo csv
        routes = Routes(file_name= sys.argv[1])

        #le entrada
        goal = parse_origin_goal(goal= sys.argv[2])

        #decide melhor rota
        #retorna a melhor rota

def main():
    application = BestPath()
    application.start()

if __name__ == '__main__':
    main()
