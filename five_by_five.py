## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'], #0
    ['X','X','0','0','0'], #0
    ['X','0','X','0','X'], #X
    ['0','X','X','X','X'], #0
    ['X','0','0','X','X'], #X
]

# first step is to add colum 6 and row 6
# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
# output the grid with the flipped card
counter = 0
for item in range(len(five_by_five_grid)):
    x_count = five_by_five_grid[counter].count('X')
    if x_count % 2 == 0:
        five_by_five_grid[counter].append('0')
    else:
        five_by_five_grid[counter].append('X')
    counter += 1

for item in five_by_five_grid:
    print(item)

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)

# Ideas

