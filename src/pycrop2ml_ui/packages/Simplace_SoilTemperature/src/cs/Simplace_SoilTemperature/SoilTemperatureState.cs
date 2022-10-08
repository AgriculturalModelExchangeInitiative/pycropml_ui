using System;
using System.Collections.Generic;
public class SoilTemperatureState 
{
    private double _SoilSurfaceTemperature;
    private double _SnowWaterContent;
    private double[] _SoilTempArray;
    
        public SoilTemperatureState() { }
    
    
    public SoilTemperatureState(SoilTemperatureState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _SoilSurfaceTemperature = toCopy._SoilSurfaceTemperature;
    _SnowWaterContent = toCopy._SnowWaterContent;
    SoilTempArray = new double[toCopy._SoilTempArray.Length];
            for (int i = 0; i < toCopy._SoilTempArray.Length; i++)
            { _SoilTempArray[i] = toCopy._SoilTempArray[i]; }
    
    }
    }
    public double SoilSurfaceTemperature
        {
            get { return this._SoilSurfaceTemperature; }
            set { this._SoilSurfaceTemperature= value; } 
        }
    public double SnowWaterContent
        {
            get { return this._SnowWaterContent; }
            set { this._SnowWaterContent= value; } 
        }
    public double[] SoilTempArray
        {
            get { return this._SoilTempArray; }
            set { this._SoilTempArray= value; } 
        }
}