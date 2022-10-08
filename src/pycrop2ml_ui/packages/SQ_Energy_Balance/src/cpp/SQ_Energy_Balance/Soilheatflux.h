#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include "EnergybalanceState.h"
#include "EnergybalanceRate.h"
#include "EnergybalanceAuxiliary.h"
#include "EnergybalanceExogenous.h"
using namespace std;
class Soilheatflux
{
    private:
        double tau;
    public:
        Soilheatflux();
        void  Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a, EnergybalanceExogenous& ex);
        double gettau();
        void settau(double _tau);

};