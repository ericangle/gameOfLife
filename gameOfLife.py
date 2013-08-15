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
import numpy, math, os, sys 
#import matplotlib.pyplot as plt
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i","--initPerAlive",type="float",
                  help="Initial percent of population that is alive.")
parser.add_option("-g","--gen",type="int",
                  help="Number of generations to simulate.")
parser.add_option("-r","--rows",type="int",
                  help="Number of people in horizontal direction.")
parser.add_option("-c","--cols",type="int",
                  help="Number of people in vertical direction.")

(options,args) = parser.parse_args()

# Read in user-specified parameters                                                                                                      
if (options.initPerAlive == None):
  print "WARNING:"
  print "Initial percent of population that is alive"
  print "is not specified. Setting to 50.0."
  print " "
  initialPercentAlive = 50.0
else:
  initialPercentAlive = options.initPerAlive

if (options.gen == None):
  print "WARNING:"
  print "Number of generations to simulate"
  print "is not specified. Setting to 1."
  print " "
  generations = 1
else:
  generations = options.gen

if (options.rows == None):
  print "WARNING:"
  print "Number of people in horizontal direction"
  print "is not specified. Setting to 10."
  print " "
  nRows = 10
else:
  nRows = options.rows

if (options.cols == None):
  print "WARNING:"
  print "Number of people in vertical direction"
  print "is not specified. Setting to 10."
  print " "
  nCols = 10
else:
  nCols = options.cols

alive = 1
dead = 0                       

# Prints array in nice format
def prettyPrint(array, nRows, nCols):
  for i in range(0, nRows):
    s = ' '
    for j in range(0, nCols):
      s = s + str(array[i][j]) + ' '
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
