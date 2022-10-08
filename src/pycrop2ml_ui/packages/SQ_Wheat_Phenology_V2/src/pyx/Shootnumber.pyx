import numpy 
from math import *
def model_shootnumber(float canopyShootNumber_t1=288.0,
                      float leafNumber=3.34,
                      float sowingDensity=288.0,
                      float targetFertileShoot=600.0,
                      list tilleringProfile_t1=[288.0],
                      int numberTillerCohort_t1=1):
    """

    CalculateShootNumber Model
    Author: Pierre MARTRE
    Reference: Modeling development phase in the 
                Wheat Simulation Model SiriusQuality.
                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    Institution: INRA/LEPSE Montpellier
    Abstract: calculate the shoot number and update the related variables if needed

    """
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    cdef int emergedLeaves, shoots, i
    emergedLeaves = max(1, ceil(leafNumber - 1.0))
    shoots = fibonacci(emergedLeaves)
    canopyShootNumber = min(shoots * sowingDensity, targetFertileShoot)
    averageShootNumberPerPlant = canopyShootNumber / sowingDensity
    if (canopyShootNumber != canopyShootNumber_t1):
        tilleringProfile = integr(tilleringProfile_t1,canopyShootNumber - canopyShootNumber_t1)
    numberTillerCohort = len(tilleringProfile)
    return  averageShootNumberPerPlant, canopyShootNumber, tilleringProfile, numberTillerCohort
def fibonacci(int n):
    if n<=1: return n
    else: return fibonacci(n-1)+fibonacci(n-2)
def init_shootnumber(float sowingDensity=288.0,
                     float targetFertileShoot=600.0):
    cdef float canopyShootNumber_t1
    cdef float leafNumber
    cdef floatlist tilleringProfile_t1
    cdef int numberTillerCohort_t1
    cdef float averageShootNumberPerPlant
    cdef float canopyShootNumber
    cdef floatlist tilleringProfile
    cdef int numberTillerCohort
    canopyShootNumber = sowingDensity
    averageShootNumberPerPlant = 1.0
    tilleringProfile.append(sowingDensity)
    numberTillerCohort = 1
    return  averageShootNumberPerPlant, canopyShootNumber, tilleringProfile, numberTillerCohort
