import evolve

pop = [[0 for x in xrange(2)] for y in xrange(2)]
popEvolved = evolve.evolve(pop, 2, 2, 1, 0)

if (pop == popEvolved):
   print 'yay!'
