grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# reddit example
# for x in range(len(grid[0])):
#     for y in range(len(grid)):
#         if y == len(grid)-1:
#             print(grid[y][x])
#         else:
#             print(grid[y][x],end="")


# example given by author
for j in range(len(grid[0])):           # sets j to the current row in the loop
    for i in range(len(grid)):          # sets i to the character within a row
        print(grid[i][j],end='')        #
    print('')

print(len(grid))

