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
      
  def uniformCost(self):
    currNode = Node(self.start)
    numNodes = 1
    count = 1
    
    print("Expanding state")
    for row in currNode.state:
        for tile in row:
            print(tile, end=" ")
        print()
    item = (currNode.g_n, count, currNode)
    self.frontier.put(item)

    puzzleTuple = tuple(map(tuple, currNode.state))
    self.traversed.add(puzzleTuple)

    while not self.frontier.empty():
      self.maxFrontier = max(self.maxFrontier, self.frontier.qsize())
      top = self.frontier.get()
      currNode = top[2]
      puzzleTuple = tuple(map(tuple, currNode.state))
      self.traversed.add(puzzleTuple)
      
      if currNode.state == self.goal:
        print("Goal!!!\n")
        print("To solve this problem the search algorithm expanded a total of {} nodes.".format(numNodes))
        print("The maximum number of nodes in the queue at any one time: {}.\n".format(self.maxFrontier))
        return

      print("The best state to expand with g(n) = {} is...".format(currNode.g_n))
      for row in currNode.state:
        for tile in row:
            print(tile, end=" ")
        print()
      print("Expanding this node...\n")

      possibleStates = currNode.getPossibleStates()

      for node in possibleStates:
        count += 1
        puzzleTuple = tuple(map(tuple, node.state))

        if puzzleTuple not in self.traversed:
          item = (node.g_n, count, node)
          self.frontier.put(item)
      
      numNodes += 1

  def aStar(self, heuristic):
    currNode = Node(self.start)
    numNodes = 0
    count = 1
    
    print("Expanding state")
    for row in currNode.state:
        for tile in row:
            print(tile, end=" ")
        print()
    
    h_n = heuristic(currNode.state, self.goal)
    f_n = currNode.g_n + h_n

    item = (f_n, count, currNode)
    self.frontier.put(item)

    puzzleTuple = tuple(map(tuple, currNode.state))
    self.traversed.add(puzzleTuple)

    while not self.frontier.empty():
      self.maxFrontier = max(self.maxFrontier, self.frontier.qsize())
      top = self.frontier.get()
      curr_f_n = top[0]
      currNode = top[2]
      curr_h_n = curr_f_n - currNode.g_n

      puzzleTuple = tuple(map(tuple, currNode.state))
      self.traversed.add(puzzleTuple)

      if currNode.state == self.goal:
        print("Goal!!!\n")
        print("To solve this problem the search algorithm expanded a total of {} nodes.".format(numNodes))
        print("The maximum number of nodes in the queue at any one time: {}.\n".format(self.maxFrontier))
        return

      print("The best state to expand with g(n) = {} and h(n) = {} is...".format(currNode.g_n, curr_h_n))
      for row in currNode.state:
        for tile in row:
            print(tile, end=" ")
        print()
      print("Expanding this node...\n")

      possibleStates = currNode.getPossibleStates()

      for node in possibleStates:
        count += 1

        puzzleTuple = tuple(map(tuple, node.state))

        if puzzleTuple not in self.traversed:
          h_n = heuristic(node.state, self.goal)
          f_n = node.g_n + h_n

          item = (f_n, count, node)
          self.frontier.put(item)
      
      numNodes += 1