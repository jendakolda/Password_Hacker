import itertools

coords = (int(input()), int(input()))
possible = 0
moves = list(itertools.product([-1, 0, 1], repeat=2))
moves.remove((0, 0))
for move in moves:
    x, y = coords[0] + move[0], coords[1] + move[1]
    if x in range(1, 9) and y in range(1, 9):
        possible += 1
print(possible)
