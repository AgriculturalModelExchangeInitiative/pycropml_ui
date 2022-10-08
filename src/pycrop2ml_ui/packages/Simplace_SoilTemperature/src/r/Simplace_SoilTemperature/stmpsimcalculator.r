library(gsubfn)

model_stmpsimcalculator <- function (cSoilLayerDepth,
         cFirstDayMeanTemp,
         cAVT,
         cABD,
         cDampingDepth,
         iSoilWaterContent,
         iSoilSurfaceTemperature,
         SoilTempArray,
         pSoilLayerDepth){
    #'- Name: STMPsimCalculator -Version: 001, -Time step: 1
    #'- Description:
    #'            * Title: STMPsimCalculator model
    #'            * Authors: Gunther Krauss, Andreas Enders
    #'            * Reference: Williams, J.R., Izaurralde, C.A., 2005.The APEX model, Blackland Research Center Reports, Vol. 2. Blackland Research Center, USDA, Temple, Texas, USA
    #'            * Institution: INRES Pflanzenbau, Uni Bonn
    #'            * ExtendedDescription: Calculates the soil temperature in n layers depending on climate and soil conditions
    #'            * ShortDescription: None
    #'- inputs:
    #'            * name: cSoilLayerDepth
    #'                          ** description : Depth of soil layer
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : 
    #'                          ** max : 20.0
    #'                          ** min : 0.03
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    #'            * name: cFirstDayMeanTemp
    #'                          ** description : Mean temperature on first day
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 50.0
    #'                          ** min : -40.0
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    #'            * name: cAVT
    #'                          ** description : Constant Temperature of deepest soil layer
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 20.0
    #'                          ** min : -10.0
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    #'            * name: cABD
    #'                          ** description : Mean bulk density
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 4.0
    #'                          ** min : 1.0
    #'                          ** default : 2.0
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/tonne_per_cubic_metre
    #'            * name: cDampingDepth
    #'                          ** description : Initial value for damping depth of soil
    #'                          ** inputtype : parameter
    #'                          ** parametercategory : constant
    #'                          ** datatype : DOUBLE
    #'                          ** max : 20.0
    #'                          ** min : 1.5
    #'                          ** default : 6.0
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    #'            * name: iSoilWaterContent
    #'                          ** description : Content of water in Soil
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 20.0
    #'                          ** min : 1.5
    #'                          ** default : 5.0
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/millimetre
    #'            * name: iSoilSurfaceTemperature
    #'                          ** description : Temperature at soil surface
    #'                          ** inputtype : variable
    #'                          ** variablecategory : exogenous
    #'                          ** datatype : DOUBLE
    #'                          ** max : 20.0
    #'                          ** min : 1.5
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    #'            * name: SoilTempArray
    #'                          ** description : Array of temperature 
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : 
    #'                          ** max : 40
    #'                          ** min : -20
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    #'            * name: pSoilLayerDepth
    #'                          ** description : Depth of soil layer plus additional depth
    #'                          ** inputtype : variable
    #'                          ** variablecategory : state
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** len : 
    #'                          ** max : 20.0
    #'                          ** min : 0.03
    #'                          ** default : 
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/metre
    #'- outputs:
    #'            * name: SoilTempArray
    #'                          ** description : Array of temperature 
    #'                          ** datatype : DOUBLEARRAY
    #'                          ** variablecategory : state
    #'                          ** len : 
    #'                          ** max : 40
    #'                          ** min : -20
    #'                          ** unit : http://www.wurvoc.org/vocabularies/om-1.8/degree_Celsius
    XLAG <- .8
    XLG1 <- 1 - XLAG
    DP <- 1 + (2.5 * cABD / (cABD + exp(6.53 - (5.63 * cABD))))
    WC <- 0.001 * iSoilWaterContent / ((.356 - (.144 * cABD)) * cSoilLayerDepth[(length(cSoilLayerDepth) - 1)+1])
    DD <- exp(log(0.5 / DP) * ((1 - WC) / (1 + WC)) * 2) * DP
    Z1 <- as.double(0)
    for( i in seq(0, length(SoilTempArray)-1, 1)){
        ZD <- 0.5 * (Z1 + pSoilLayerDepth[i+1]) / DD
        RATE <- ZD / (ZD + exp(-.8669 - (2.0775 * ZD))) * (cAVT - iSoilSurfaceTemperature)
        SoilTempArray[i+1] <- XLAG * SoilTempArray[i+1] + (XLG1 * (RATE + iSoilSurfaceTemperature))
        Z1 <- pSoilLayerDepth[i+1]
    }
    return (list('SoilTempArray' = SoilTempArray))
}

init_stmpsimcalculator <- function (cSoilLayerDepth,
         cFirstDayMeanTemp,
         cAVT,
         cABD,
         cDampingDepth,
         iSoilWaterContent,
         iSoilSurfaceTemperature){
    SoilTempArray<- array(numeric())
    pSoilLayerDepth<- array(numeric())
    SoilTempArray <- NULL
    pSoilLayerDepth <- NULL
    tStmp<- array(numeric())
    tz<- array(numeric())
    tProfileDepth <- cSoilLayerDepth[length(cSoilLayerDepth) - 1+1]
    additionalDepth <- cDampingDepth - tProfileDepth
    firstAdditionalLayerHight <- additionalDepth - as.double(floor(additionalDepth))
    layers <- as.integer(abs(as.double(ceiling(additionalDepth)))) + length(cSoilLayerDepth)
    tStmp <- array(numeric(), c(1, layers))
    tz <- array(numeric(), c(1, layers))
    for( i in seq(0, length(tStmp)-1, 1)){
        if (i < length(cSoilLayerDepth))
        {
            depth <- cSoilLayerDepth[i+1]
        }
        else
        {
            depth <- tProfileDepth + firstAdditionalLayerHight + i - length(cSoilLayerDepth)
        }
        tz[i+1] <- depth
        tStmp[i+1] <- (cFirstDayMeanTemp * (cDampingDepth - depth) + (cAVT * depth)) / cDampingDepth
    }
    SoilTempArray <- tStmp
    pSoilLayerDepth <- tz
    return (list ("SoilTempArray" = SoilTempArray,"pSoilLayerDepth" = pSoilLayerDepth))
}