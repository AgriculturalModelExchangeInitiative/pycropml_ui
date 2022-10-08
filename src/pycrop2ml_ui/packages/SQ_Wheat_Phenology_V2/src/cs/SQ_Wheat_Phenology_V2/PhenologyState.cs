using System;
using System.Collections.Generic;
public class PhenologyState 
{
    private double _phyllochron;
    private double _minFinalNumber;
    private List<DateTime> _calendarDates = new List<DateTime>();
    private List<string> _calendarMoments = new List<string>();
    private double _ptq;
    private double _gAImean;
    private double _leafNumber;
    private List<double> _listPARTTWindowForPTQ = new List<double>();
    private List<double> _listTTShootWindowForPTQ = new List<double>();
    private List<double> _listGAITTWindowForPTQ = new List<double>();
    private List<double> _calendarCumuls = new List<double>();
    private double _vernaprog;
    private int _hasLastPrimordiumAppeared;
    private double _phase;
    private double _finalLeafNumber;
    private int _hasZadokStageChanged;
    private string _currentZadokStage;
    private int _hasFlagLeafLiguleAppeared;
    private List<double> _tilleringProfile = new List<double>();
    private double _canopyShootNumber;
    private int _numberTillerCohort;
    private double _averageShootNumberPerPlant;
    private int _isMomentRegistredZC_39;
    
    public PhenologyState() { }
    
    
    public PhenologyState(PhenologyState toCopy, bool copyAll) // copy constructor 
    {
    if (copyAll)
    {
    
    _phyllochron = toCopy._phyllochron;
    _minFinalNumber = toCopy._minFinalNumber;
    calendarDates = new List<DateTime>();
            for (int i = 0; i < toCopy.calendarDates.Count; i++)
            { calendarDates.Add(toCopy.calendarDates[i]); }
    
    calendarMoments = new List<string>();
            for (int i = 0; i < toCopy.calendarMoments.Count; i++)
            { calendarMoments.Add(toCopy.calendarMoments[i]); }
    
    _ptq = toCopy._ptq;
    _gAImean = toCopy._gAImean;
    _leafNumber = toCopy._leafNumber;
    listPARTTWindowForPTQ = new List<double>();
            for (int i = 0; i < toCopy.listPARTTWindowForPTQ.Count; i++)
            { listPARTTWindowForPTQ.Add(toCopy.listPARTTWindowForPTQ[i]); }
    
    listTTShootWindowForPTQ = new List<double>();
            for (int i = 0; i < toCopy.listTTShootWindowForPTQ.Count; i++)
            { listTTShootWindowForPTQ.Add(toCopy.listTTShootWindowForPTQ[i]); }
    
    listGAITTWindowForPTQ = new List<double>();
            for (int i = 0; i < toCopy.listGAITTWindowForPTQ.Count; i++)
            { listGAITTWindowForPTQ.Add(toCopy.listGAITTWindowForPTQ[i]); }
    
    calendarCumuls = new List<double>();
            for (int i = 0; i < toCopy.calendarCumuls.Count; i++)
            { calendarCumuls.Add(toCopy.calendarCumuls[i]); }
    
    _vernaprog = toCopy._vernaprog;
    _hasLastPrimordiumAppeared = toCopy._hasLastPrimordiumAppeared;
    _phase = toCopy._phase;
    _finalLeafNumber = toCopy._finalLeafNumber;
    _hasZadokStageChanged = toCopy._hasZadokStageChanged;
    _currentZadokStage = toCopy._currentZadokStage;
    _hasFlagLeafLiguleAppeared = toCopy._hasFlagLeafLiguleAppeared;
    tilleringProfile = new List<double>();
            for (int i = 0; i < toCopy.tilleringProfile.Count; i++)
            { tilleringProfile.Add(toCopy.tilleringProfile[i]); }
    
    _canopyShootNumber = toCopy._canopyShootNumber;
    _numberTillerCohort = toCopy._numberTillerCohort;
    _averageShootNumberPerPlant = toCopy._averageShootNumberPerPlant;
    _isMomentRegistredZC_39 = toCopy._isMomentRegistredZC_39;
    }
    }
    public double phyllochron
        {
            get { return this._phyllochron; }
            set { this._phyllochron= value; } 
        }
    public double minFinalNumber
        {
            get { return this._minFinalNumber; }
            set { this._minFinalNumber= value; } 
        }
    public List<DateTime> calendarDates
        {
            get { return this._calendarDates; }
            set { this._calendarDates= value; } 
        }
    public List<string> calendarMoments
        {
            get { return this._calendarMoments; }
            set { this._calendarMoments= value; } 
        }
    public double ptq
        {
            get { return this._ptq; }
            set { this._ptq= value; } 
        }
    public double gAImean
        {
            get { return this._gAImean; }
            set { this._gAImean= value; } 
        }
    public double leafNumber
        {
            get { return this._leafNumber; }
            set { this._leafNumber= value; } 
        }
    public List<double> listPARTTWindowForPTQ
        {
            get { return this._listPARTTWindowForPTQ; }
            set { this._listPARTTWindowForPTQ= value; } 
        }
    public List<double> listTTShootWindowForPTQ
        {
            get { return this._listTTShootWindowForPTQ; }
            set { this._listTTShootWindowForPTQ= value; } 
        }
    public List<double> listGAITTWindowForPTQ
        {
            get { return this._listGAITTWindowForPTQ; }
            set { this._listGAITTWindowForPTQ= value; } 
        }
    public List<double> calendarCumuls
        {
            get { return this._calendarCumuls; }
            set { this._calendarCumuls= value; } 
        }
    public double vernaprog
        {
            get { return this._vernaprog; }
            set { this._vernaprog= value; } 
        }
    public int hasLastPrimordiumAppeared
        {
            get { return this._hasLastPrimordiumAppeared; }
            set { this._hasLastPrimordiumAppeared= value; } 
        }
    public double phase
        {
            get { return this._phase; }
            set { this._phase= value; } 
        }
    public double finalLeafNumber
        {
            get { return this._finalLeafNumber; }
            set { this._finalLeafNumber= value; } 
        }
    public int hasZadokStageChanged
        {
            get { return this._hasZadokStageChanged; }
            set { this._hasZadokStageChanged= value; } 
        }
    public string currentZadokStage
        {
            get { return this._currentZadokStage; }
            set { this._currentZadokStage= value; } 
        }
    public int hasFlagLeafLiguleAppeared
        {
            get { return this._hasFlagLeafLiguleAppeared; }
            set { this._hasFlagLeafLiguleAppeared= value; } 
        }
    public List<double> tilleringProfile
        {
            get { return this._tilleringProfile; }
            set { this._tilleringProfile= value; } 
        }
    public double canopyShootNumber
        {
            get { return this._canopyShootNumber; }
            set { this._canopyShootNumber= value; } 
        }
    public int numberTillerCohort
        {
            get { return this._numberTillerCohort; }
            set { this._numberTillerCohort= value; } 
        }
    public double averageShootNumberPerPlant
        {
            get { return this._averageShootNumberPerPlant; }
            set { this._averageShootNumberPerPlant= value; } 
        }
    public int isMomentRegistredZC_39
        {
            get { return this._isMomentRegistredZC_39; }
            set { this._isMomentRegistredZC_39= value; } 
        }
}