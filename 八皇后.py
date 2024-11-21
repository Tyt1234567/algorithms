import math
import random
import sys

d = 3

def initgrid(d):
    grid= [[(x+1,y+1) for y in range(d)] for x in range(d)]
    return grid

def fill(grid, rowindex, position, backtracking):
    row = grid[rowindex]
    optional = []
    if len(position) != 0:
        for column in row:
            available = True
            for item in position:
                if column[1] == item[1] or column[0]+column[1] == item[0]+item[1] or \
                    column [0]-column[1] == item[0]-item[1] or column in backtracking:
                        available = False
            if available:
                optional.append(column)
    else:
        optional = row
    if len(optional)==0:
        return 0
    else:
        randomindex = math.floor(len(optional)*random.random())
        pick = optional[randomindex]
        position.append(pick)
        return 1

def show(positions):
    figure = ''
    for row in range(d):
        for line in range(d):
            if (row +1,line+1) in positions:
                figure += 'Q'
            else:
                figure +='.'
        figure += '\n'
    return figure

grid = initgrid(d)
position = []
backtracking = [[] for i in range(d)]
row = 0
while row < d:
    success = fill(grid, row, position, backtracking[row])
    if success ==1:
        row+=1
    else:
        row-=1
        backtracking[row].append(position.pop())
    if row < d-1:
        backtracking[row+1] = []

print(show(position))
