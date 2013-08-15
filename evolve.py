def evolve(pop, nRows, nCols, alive, dead):
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
