# Conway's Game of Life, as described here:
# http://prezi.com/ciy0b1veai06/ucar-code-retreat-2013/
#
# A simulation of evolution, based on a few rules:
# a grid of cells, either dead or alive status
# status of cell depends on its 8 surrounding neighbors:
# underpopulation: if cell has < 2 live neighbors, it dies
# overpopulation: if cell has > 3 live neighbors, it dies
# a cell with 2 or 3 live neighbors lives on to the next cycle/generation
# any dead cell with exactly 3 live neighbors becomes a living cell

import random

alive = 1
dead = 0                       
generations = 3                # number of generations
initialPercentAlive = 70.0     # initial percentage of alive 
nRows = 5
nCols = 5

def evolve(pop, nRows, nCols):
  evolvedPop = pop
  for i in range(0, nRows):
    for j in range(0, nCols):
      numAlive = 0
      for k in range(i-1,i+2):
        for l in range(j-1,j+2):
          h = k != i
          m = l != j
          g = h or m
          if (k >= 0 and k <= nRows - 1 and l >= 0 and l <= nCols - 1 and g):
            if (pop[k][l] == alive):
              numAlive = numAlive + 1
      if (numAlive <= 1 or numAlive >= 4):
        evolvedPop[i][j] = dead
      if (numAlive == 3 and pop[i][j] == dead):
        evolvedPop[i][j] = alive
  return evolvedPop

def prettyPrint(matrix, nRows, nCols):
  for i in range(0, nRows):
    s = ' '
    for j in range(0, nCols):
      s = s + str(matrix[i][j]) + ' '
    print s

# Randomly initialize population
pop = [[dead for x in xrange(nCols)] for y in xrange(nRows)]
for i in range(0, nRows):
  for j in range(0, nCols):
    if (random.random() >= 1.0 - 0.01*initialPercentAlive):
      pop[i][j] = alive

# Print initial population
print 'Initial generation:'
prettyPrint(pop, nRows, nCols)

# Evolve population
for i in range(2, generations+1):
  pop = evolve(pop, nRows, nCols)
  print 'Population at generation' + str(i) + ':'
  prettyPrint(pop, nRows, nCols) 
