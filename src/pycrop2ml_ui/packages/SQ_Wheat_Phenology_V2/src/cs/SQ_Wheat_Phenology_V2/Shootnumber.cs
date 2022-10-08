using System;
using System.Collections.Generic;
using System.Linq;
public class ShootNumber
{
    private double _sowingDensity;
    public double sowingDensity
        {
            get { return this._sowingDensity; }
            set { this._sowingDensity= value; } 
        }
    private double _targetFertileShoot;
    public double targetFertileShoot
        {
            get { return this._targetFertileShoot; }
            set { this._targetFertileShoot= value; } 
        }
    public ShootNumber() { }
    
    public void  CalculateModel(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a, PhenologyExogenous ex)
    {
        //- Name: ShootNumber -Version: 1.0, -Time step: 1
        //- Description:
    //            * Title: CalculateShootNumber Model
    //            * Author: Pierre MARTRE
    //            * Reference: Modeling development phase in the 
    //                Wheat Simulation Model SiriusQuality.
    //                See documentation at http://www1.clermont.inra.fr/siriusquality/?page_id=427
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: calculate the shoot number and update the related variables if needed
        //- inputs:
    //            * name: canopyShootNumber_t1
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 288.0
    //                          ** unit : shoot m-2
    //                          ** inputtype : variable
    //            * name: leafNumber
    //                          ** description : Leaf number 
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 3.34
    //                          ** unit : leaf
    //            * name: sowingDensity
    //                          ** description : number of plant /m²
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 500
    //                          ** default : 288.0
    //                          ** unit : plant m-2
    //                          ** inputtype : parameter
    //            * name: targetFertileShoot
    //                          ** description : max value of shoot number for the canopy
    //                          ** parametercategory : species
    //                          ** datatype : DOUBLE
    //                          ** min : 280
    //                          ** max : 1000
    //                          ** default : 600.0
    //                          ** unit : shoot
    //                          ** inputtype : variable
    //            * name: tilleringProfile_t1
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** default : [288.0]
    //                          ** unit : 
    //                          ** inputtype : variable
    //            * name: numberTillerCohort_t1
    //                          ** description :  Number of tiller which appears
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 1
    //                          ** unit : 
    //                          ** inputtype : variable
        //- outputs:
    //            * name: averageShootNumberPerPlant
    //                          ** description : average shoot number per plant in the canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: canopyShootNumber
    //                          ** description : shoot number for the whole canopy
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : shoot m-2
    //            * name: tilleringProfile
    //                          ** description :  store the amount of new tiller created at each time a new tiller appears
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLELIST
    //                          ** unit : dimensionless
    //            * name: numberTillerCohort
    //                          ** description : Number of tiller which appears
    //                          ** variablecategory : state
    //                          ** datatype : INT
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : dimensionless
        double canopyShootNumber_t1 = s1.canopyShootNumber;
        double leafNumber = s.leafNumber;
        List<double> tilleringProfile_t1 = s1.tilleringProfile;
        int numberTillerCohort_t1 = s1.numberTillerCohort;
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<double> tilleringProfile = new List<double>();
        int numberTillerCohort;
        int emergedLeaves;
        int shoots;
        int i;
        emergedLeaves = Math.Max(1, (int) Math.Ceiling(leafNumber - 1.0d));
        shoots = fibonacci(emergedLeaves);
        canopyShootNumber = Math.Min(shoots * sowingDensity, targetFertileShoot);
        averageShootNumberPerPlant = canopyShootNumber / sowingDensity;
        if (canopyShootNumber != canopyShootNumber_t1)
        {
            tilleringProfile = new List<double>(tilleringProfile_t1);
            tilleringProfile.Add(canopyShootNumber - canopyShootNumber_t1);
        }
        numberTillerCohort = tilleringProfile.Count;
        s.averageShootNumberPerPlant= averageShootNumberPerPlant;
        s.canopyShootNumber= canopyShootNumber;
        s.tilleringProfile= tilleringProfile;
        s.numberTillerCohort= numberTillerCohort;
    }
    public static int fibonacci(int n)
    {
        if (n <= 1)
        {
            return n;
        }
        else
        {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    public void Init(PhenologyState s, PhenologyState s1, PhenologyRate r, PhenologyAuxiliary a, PhenologyExogenous ex)
    {
        double canopyShootNumber_t1;
        double leafNumber;
        List<double> tilleringProfile_t1 = new List<double>();
        int numberTillerCohort_t1;
        double averageShootNumberPerPlant;
        double canopyShootNumber;
        List<double> tilleringProfile = new List<double>();
        int numberTillerCohort;
        canopyShootNumber = sowingDensity;
        averageShootNumberPerPlant = 1.0d;
        tilleringProfile.Add(sowingDensity);
        numberTillerCohort = 1;
        s.averageShootNumberPerPlant= averageShootNumberPerPlant;
        s.canopyShootNumber= canopyShootNumber;
        s.tilleringProfile= tilleringProfile;
        s.numberTillerCohort= numberTillerCohort;
    }
}