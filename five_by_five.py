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

# Checks the row total and appends accordingly
counter = 0
for row in range(len(five_by_five_grid)):
    x_count_row = five_by_five_grid[0].count('X')
    if x_count_row % 2 == 0:
        five_by_five_grid[counter].append('0')
    else:
        five_by_five_grid[counter].append('X')
    counter += 1

# Checks the column total and extends accordingly
counter = 0
for col in range(0, 6):
    x_count_col = row[col].count('X')
# extended_cul=[]
# for col in range(0,6):
#    my_sum =0
#    for row in five_by_five_grid:
#        x_counter = row[col].count('X')
#        my_sum = my_sum + x_counter
#    if my_sum %2 == 0:
#        extended_cul.append('0')
#    else:
#        extended_cul.append('X')
# five_by_five_grid.append(extended_cul)

# Reprints the 5x5 grid

for item in five_by_five_grid:
    print(item)



## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)

# Ideas

