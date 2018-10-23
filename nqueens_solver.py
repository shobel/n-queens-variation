#!/usr/bin/python
import os
from itertools import combinations

numPolice = 0
numScooters = 0
gridSize = 0
grid = [[]]
solutions = []
policemen = []
emptyRows = []

def main():
    inputFilename = 'input.txt'
    if not os.path.isfile(inputFilename):
        print("Input file does not exist")
        exit()

    counter = 0
    global grid, gridSize, numPolice, numScooters
    with open(inputFilename) as f:
        for line in f:
            if counter == 0:
                grid = [[0 for i in xrange(int(line))] for i in xrange(int(line))]
                gridSize = int(line)
            elif counter == 1:
                numPolice = int(line)
            elif counter == 2:
                numScooters = int(line)
            else:
                splitLine = line.split(',')
                x = int(splitLine[0])
                y = int(splitLine[1].rstrip('\n'))
                grid[x][y] += 1
            counter += 1

    set_empty_rows()
    solve()

    outputFilename = 'output.txt'
    outputFile = open(outputFilename, "w")
    outputFile.write(str(find_best_solution()) + "\n")

def set_empty_rows():
    global emptyRows
    numEmpty = gridSize - numPolice
    if numEmpty == 0:
        emptyRows = [None]
        return
    l = []
    for x in range(0, gridSize):
        l.append(x)
    comb = combinations(l, numEmpty)
    for i in list(comb):
        emptyRows.append(i)

def can_place_policeman(row, col):
    for r, c in enumerate(policemen):
        if c == None:
            continue
        if r == row or c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve():
    global solutions, policemen
    for i, emptySet in enumerate(emptyRows):
        col = row = 0
        while True:
            while col < gridSize and not can_place_policeman(row, col):
                col += 1
            if col < gridSize:
                toAppend = col
                if emptySet != None:
                    for emptyrow in emptySet:
                        if row == emptyrow:
                            toAppend = None
                            break
                policemen.append(toAppend)
                if gridSize - 1 <= row:
                    solutions.append(list(policemen))
                    policemen.pop()
                    col = gridSize
                else:
                    row += 1
                    col = 0
            if gridSize <= col:
                if row == 0:
                    break
                p = policemen.pop()
                if p != None:
                    col = p + 1
                row -= 1

def find_best_solution():
    best_score = 0
    for solution in solutions:
        current_score = 0
        for i, p in enumerate(solution):
            if p != None:
                current_score += grid[i][p]
        if current_score > best_score:
            best_score = current_score

    return best_score

main()
