import  java.io.*;
import  java.util.*;
import java.time.LocalDateTime;
public class SoilTemperatureState
{
    private Double SoilSurfaceTemperature;
    private Double SnowWaterContent;
    private Double [] SoilTempArray;
    
    public SoilTemperatureState() { }
    
    public SoilTemperatureState(SoilTemperatureState toCopy, boolean copyAll) // copy constructor 
    {
        if (copyAll)
        {
            this.SoilSurfaceTemperature = toCopy.getSoilSurfaceTemperature();
            this.SnowWaterContent = toCopy.getSnowWaterContent();
            SoilTempArray = new Double[toCopy.getSoilTempArray().length];
        for (int i = 0; i < toCopy.getSoilTempArray().length; i++)
        {
            SoilTempArray[i] = toCopy.getSoilTempArray()[i];
        }
        }
    }
    public Double getSoilSurfaceTemperature()
    { return SoilSurfaceTemperature; }

    public void setSoilSurfaceTemperature(Double _SoilSurfaceTemperature)
    { this.SoilSurfaceTemperature= _SoilSurfaceTemperature; } 
    
    public Double getSnowWaterContent()
    { return SnowWaterContent; }

    public void setSnowWaterContent(Double _SnowWaterContent)
    { this.SnowWaterContent= _SnowWaterContent; } 
    
    public Double [] getSoilTempArray()
    { return SoilTempArray; }

    public void setSoilTempArray(Double [] _SoilTempArray)
    { this.SoilTempArray= _SoilTempArray; } 
    
}