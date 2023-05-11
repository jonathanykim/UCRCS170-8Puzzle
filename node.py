from copy import deepcopy
from problem import *

class Node:
  def __init__(self, puzzle, g_n=0):
    self.state = puzzle
    self.g_n = g_n
        
  def getPossibleStates(self):
    for i in range(len(self.state)):
        for j in range(len(self.state[i])):
            if self.state[i][j] == '0':
                emptyRowi = i
                emptyColi = j
                break

    possibleStates = []

    # Can we move up?
    if (emptyRowi > 0) and (emptyRowi < 3):
        nextState = deepcopy(self.state)
        nextState[emptyRowi][emptyColi], nextState[emptyRowi - 1][emptyColi] = nextState[emptyRowi - 1][emptyColi], nextState[emptyRowi][emptyColi]
        node = Node(nextState, self.g_n + 1)
        possibleStates.append(node)

    # Can we move down?
    if (emptyRowi < 2) and (emptyRowi >= 0):
        nextState = deepcopy(self.state)
        nextState[emptyRowi][emptyColi], nextState[emptyRowi + 1][emptyColi] = nextState[emptyRowi + 1][emptyColi], nextState[emptyRowi][emptyColi]
        node = Node(nextState, self.g_n + 1)
        possibleStates.append(node)

    # Can we move left?
    if (emptyColi > 0) and (emptyColi < 3):
        nextState = deepcopy(self.state)
        nextState[emptyRowi][emptyColi], nextState[emptyRowi][emptyColi - 1] = nextState[emptyRowi][emptyColi - 1], nextState[emptyRowi][emptyColi]
        node = Node(nextState, self.g_n + 1)
        possibleStates.append(node)

    # Can we move right?
    if (emptyColi < 2) and (emptyColi >= 0):
        nextState = deepcopy(self.state)
        nextState[emptyRowi][emptyColi], nextState[emptyRowi][emptyColi + 1] = nextState[emptyRowi][emptyColi + 1], nextState[emptyRowi][emptyColi]
        node = Node(nextState, self.g_n + 1)
        possibleStates.append(node)

    return possibleStates