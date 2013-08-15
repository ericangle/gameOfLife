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
import evolve

alive = 1
dead = 0                       
generations = 3                # number of generations
initialPercentAlive = 70.0     # initial percentage of alive 
nRows = 5
nCols = 5

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
  pop = evolve.evolve(pop, nRows, nCols, alive, dead)
  print 'Population at generation' + str(i) + ':'
  prettyPrint(pop, nRows, nCols) 
