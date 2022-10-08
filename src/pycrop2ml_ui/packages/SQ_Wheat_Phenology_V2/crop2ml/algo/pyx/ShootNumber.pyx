
cdef int emergedLeaves, shoots, i
emergedLeaves = max(1, ceil(leafNumber - 1.0))
shoots = fibonacci(emergedLeaves)
canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
averageShootNumberPerPlant = canopyShootNumber / sowingDensity
if (canopyShootNumber != canopyShootNumber_t1):
    tilleringProfile = integr(tilleringProfile_t1,canopyShootNumber - canopyShootNumber_t1)
numberTillerCohort = len(tilleringProfile)
