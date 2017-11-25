grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# def picture_flipper(user_grid):
#     output = ''
#     for i in range(len(user_grid[0])):
#         for n in range(len(user_grid)):
#             output += user_grid[n][i]
#         output += '\n'
#     return output
#
# print(picture_flipper(grid))

def picture_flipper(user_grid):
    n = 0
    while n < len(user_grid[0]):
        for i in range(len(user_grid)):
            print(user_grid[i][n], end='')
        print('')
        n += 1

picture_flipper(grid)
