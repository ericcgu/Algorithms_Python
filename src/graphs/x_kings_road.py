matrix = [[False, True,  False],
      [False, False, False],
      [True,  False, False]]

def road(matrix):
    incoming = []
    outgoing = []
    return [column for column in zip(*matrix)]

print(road(matrix))