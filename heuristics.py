from math import sqrt, pow

def countMisplacedTiles(currState, goal):
  numMisplaced = 0

  for i in range(3):
    for j in range(len(3)):
      currTile = currState[i][j]
      goalTile = goal[i][j]

      if currTile != goalTile:
        numMisplaced += 1
    
  return numMisplaced - 1

def euclideanDistance(currState, goal):
  totDistance = 0

  currMappings = {}
  goalMappings = {}

  for i in range(3):
    for j in range(3):
      currTile = currState[i][j]
      goalTile = goal[i][j]

      index = (i, j)
      currMappings[currTile] = index
      goalMappings[goalTile] = index
  
  del currMappings['0']
  
  for tile, index in currMappings.items():
    destination = goalMappings[tile]

    x1, y1 = index
    x2, y2 = destination
    distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    totDistance += distance
  
  return totDistance