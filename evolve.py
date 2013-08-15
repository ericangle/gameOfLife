def evolve(pop, nRows, nCols, alive, dead):
  evolvedPop = [[dead for x in xrange(nCols)] for y in xrange(nRows)]  
  for i in range(0, nRows):
    for j in range(0, nCols):
      evolvedPop[i][j] = pop[i][j]

  for i in range(0, nRows):
    for j in range(0, nCols):
      numAlive = 0
      for k in range(i-1,i+2):
        for l in range(j-1,j+2):
          # Determine if (k,l) ne (i,j)
          klNEij = k != i or l != j
        
          # Determine if k,l valid indices for pop
          kValid = (k >= 0 and k <= nRows - 1)
          lValid = (l >= 0 and l <= nCols - 1)

          klValid = kValid and lValid and klNEij

          if (klValid):
            if (pop[k][l] == alive):
              numAlive = numAlive + 1

      # if cell has < 2 or > 3 live neighbors, it dies
      if (numAlive < 2 or numAlive > 3):
        evolvedPop[i][j] = dead

      # any dead cell with exactly 3 live neighbors becomes a living cell
      if (numAlive == 3 and pop[i][j] == dead):
        evolvedPop[i][j] = alive

  return evolvedPop
