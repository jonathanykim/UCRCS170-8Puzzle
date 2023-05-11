from menu import *
from problem import *

if __name__ == '__main__':
    start = menu()
    
    puzzle = Problem(start)

    option = pickAlgorithm()

    puzzle.solve(option)