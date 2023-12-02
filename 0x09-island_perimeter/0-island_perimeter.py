#!/usr/bin/python3
''' create a function that returns
the perimeter of the island described in grid
'''


def island_perimeter(grid):
    '''return perimeter of island
    '''
    perimeter = 0
    #iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            #checking for land cells
            if grid[i][j] == 1:
                #check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                #check bottom cell
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                #check left cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                #check right cell
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
