import evolve

pop = [[0 for x in xrange(2)] for y in xrange(2)]
pop[1][0] = 1
pop[0][1] = 1
pop[1][1] = 1
popAccept = [[1 for x in xrange(2)] for y in xrange(2)]
popEvolved = evolve.evolve(pop, 2, 2, 1, 0)
if (popEvolved == popAccept):
  print 'SUCCESS'
else:
  print 'FAILURE'
