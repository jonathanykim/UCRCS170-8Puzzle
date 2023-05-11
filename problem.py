from queue import PriorityQueue
from heuristics import *
from node import *

class Problem:
  def __init__(self, start):
    self.start = start
    self.frontier = PriorityQueue()
    self.traversed = set()
    self.maxFrontier = 0
    self.goal = [['1','2','3'], ['4','5','6'], ['7','8','0']]

  def solve(self, algorithm):
    if algorithm == "1":
      print("Searching with uniform cost...\n")
      self.uniformCost()
    elif algorithm == "2":
      print("Searching with A* misplaced tile...\n")
      self.aStar(countMisplacedTiles)
    elif algorithm == "3":
      print("Searching with A* Euclidean distance...\n")
      self.aStar(euclideanDistance)
      
  