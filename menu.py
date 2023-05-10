trivial = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '0']
]

veryEasy = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '0', '8']
]

easy = [
  ['1', '2', '0'],
  ['4', '5', '3'],
  ['7', '8', '6']
]

doable = [
  ['0', '1', '2'],
  ['4', '5', '3'],
  ['7', '8', '6']
]

ohBoy = [
  ['8', '7', '1'],
  ['6', '0', '2'],
  ['5', '4', '3']
]

def defaultPuzzle():
  print("Choose a default puzzle.")
  print("1. Trivial")
  print("2. Very Easy")
  print("3. Easy")
  print("4. Doable")
  print("5. Oh Boy")

  pickPuzzle = input("Enter your selection: ")
  if pickPuzzle == '1':
    return trivial
  elif pickPuzzle == '2':
    return veryEasy
  elif pickPuzzle == '3':
    return easy
  elif pickPuzzle == '4':
    return doable
  elif pickPuzzle == '5':
    return ohBoy
  
def customPuzzle():
  print("Enter your puzzle, use a zero to represent the blank.")
  firstRow = input("Enter the first row, use space or tabs between numbers ")
  secondRow = input("Enter the second row, use space or tabs between numbers ")
  thirdRow = input("Enter the third row, use space or tabs between numbers ")

  row1 = firstRow.split(" ")
  row2 = secondRow.split(" ")
  row3 = thirdRow.split(" ")

  return [row1, row2, row3]

def menu():
    menu = "Welcome to 862157074 8 puzzle solver\n"
    menu += "Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n"

    puzzle = input(menu)

    start = []
    if puzzle == '1':
        start = defaultPuzzle()
    elif puzzle == '2':
        start = customPuzzle()

    return start