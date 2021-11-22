import ipywidgets as wg
import pandas as pd
import qgrid
import os
from path import Path
from IPython.display import display
from pycrop2ml_ui.browser.TkinterPath import getPath, getFile
import tkinter as tk
from tkinter.filedialog import askopenfilename
from pycropml.topology import Topology
from ipyfilechooser import FileChooser
from . import visualization  



class ExecutionMenu():

    def __init__(self):
           
        #outputs
        
        self._out = wg.Output()
        self._out2 = wg.Output()
        self._out3 = wg.Output()
        
        data_dir = os.getcwd()
        self.fc = FileChooser(data_dir)
        
        #inputs
        self._modelPath = wg.Textarea(value='',description='Model path:',disabled=True,layout=wg.Layout(width='400px',height='57px'))
        self._dataPath = wg.Textarea(value='',description='Data path:',disabled=True,layout=wg.Layout(width='400px',height='57px'))
        self._selecter = wg.Dropdown(options=['None'],value='None',description='Model:',disabled=True,layout=wg.Layout(width='400px',height='35px'))
        #buttons
        self._browse = wg.Button(value=False,description='Browse',disabled=False,button_style='primary')
        self._browse_data = wg.Button(value=False,description='Browse',disabled=False,button_style='primary')
        self._visualization = wg.Button(value=False,description='Visualization',disabled=False,button_style='primary')
        self._edit = wg.Button(value=False,description='Apply',disabled=False,button_style='success')
        self._cancel = wg.Button(value=False,description='Cancel',disabled=False,button_style='warning')
        self._save_connection = wg.Button(value=False,description='Save',disabled=False,button_style='warning')
        self._load_connection = wg.Button(value=False,description='Load',disabled=False,button_style='warning')
        self._save_params = wg.Button(value=False,description='Save',disabled=False,button_style='warning')
        self._load_params = wg.Button(value=False,description='Load',disabled=False,button_style='warning')
        self._save_init = wg.Button(value=False,description='Save',disabled=False,button_style='warning')
        self._load_init = wg.Button(value=False,description='Load',disabled=False,button_style='warning')
        self._pathing = wg.VBox([wg.HBox([self._modelPath, self._browse]), self._selecter])

        self._connection = wg.Button(value=False,description='Data-Model link',disabled=False, button_style='primary')
        self._disp_Parameters = wg.Button(value=False,description='Parameters values',disabled=False, button_style='primary')
        self._disp_init = wg.Button(value=False,description='Initialization values',disabled=False, button_style='primary')
        self._disp_output_generation = wg.Button(value=False,description='Output generation',disabled=False, button_style='primary')
        self._disp_output_plot = wg.Button(value=False,description='Output plot',disabled=False, button_style='primary')        
        self.variables = []
        self.datacolumns = []
        self.parameters = []
        self.outputs = []
        self.stateInit = []  

        #global displayer
        self._disp_model = wg.HBox([wg.HTML(value='<font size="5"><b>Model selection </b></font>', layout=wg.Layout(width='190px')), self._pathing])
        self._disp_data = wg.HBox([wg.HTML(value='<font size="5"><b>Model data </b></font>', layout=wg.Layout(width='190px')), wg.HBox([self._dataPath, wg.VBox([self._browse_data, self._visualization])])])
        self._displayer = wg.VBox([self._disp_model, self._disp_data,self._connection, wg.HBox([wg.HTML(value='<font size="5"><b> </b></font>', layout=wg.Layout(width='110px'))])]) # ,self._edit, self._cancel
        
        self._paths = dict()
        
        self.buttons = wg.ToggleButtons(
        value=None,
        options=["Apply", "Reset", "Close"],
        tooltips=["Apply", "Reset", "Close"],
            button_style="primary",
        )
        self.buttons.style.button_width = "80px"
        self.filechooser_widget = wg.VBox([self.fc, self.buttons])
           
    def _eventConnection(self, b):
        self._disp_Parameters.disabled=False
        pkgPath = self._modelPath.value
        pkgName = self._modelPath.value.split(os.path.sep)[-1]
        T = Topology(name=pkgName, pkg=pkgPath)
        self.parameters = []
        self.variables = []
        self.stateInit = []
        for inp in T.model.inputs:
            if "parametercategory" in dir(inp):
                self.parameters.append({"name":inp.name, "value":inp.default})
            if "variablecategory" in  dir(inp) and not inp.name.endswith("_t1"):
                self.variables.append(inp.name)
            if "variablecategory" in  dir(inp) and inp.name.endswith("_t1"):
                self.stateInit.append({"name":inp.name, "value":''})
        for out in T.model.outputs:
            self.outputs.append(out.name)
        df = pd.read_csv(self._dataPath.value, delimiter=";")
        datacolumns = list(df.columns.values)

        self._dfVarData = pd.DataFrame(data={
                'Variables': self.variables,
                'Data columns': pd.Categorical(['']*len(self.variables), categories=datacolumns),
                })
        self._dfVarDataqgrid = qgrid.show_grid(self._dfVarData,grid_options={'forceFitColumns': False, 'defaultColumnWidth': 200, 'editable':True, 'sortable':False}, show_toolbar=False)
        #self._out2.clear_output()
        with self._out:
            z = wg.HBox([self._dfVarDataqgrid, self._save_connection, self._load_connection], layout=wg.Layout(width='40%'))
            z.overflow_x = 'auto'
            display(z)
            display(self._disp_Parameters)
        self._disp_Parameters.on_click(self._eventParameters)
        self._save_connection.on_click(self._event_save_connection)
        self._load_connection.on_click(self._event_load_connection)
    
    def _eventParameters(self, b):
        self._disp_init.disabled = False
        self._dfParams = pd.DataFrame(self.parameters)
        self._dfParamqgrid = qgrid.show_grid(self._dfParams,grid_options={'forceFitColumns': False, 'defaultColumnWidth': 200, 'editable':True, 'sortable':False}, show_toolbar=False)
        with self._out:
            z = wg.HBox([self._dfParamqgrid, self._save_params, self._load_params], layout=wg.Layout(width='50%'))
            z.overflow_x = 'auto'
            display(z)
            display(self._disp_init)
            self._disp_Parameters.disabled=True
        self._disp_init.on_click(self._eventInit)
        self._save_params.on_click(self._event_save_params)
        self._load_params.on_click(self._event_load_params)
    
    def _eventInit(self, b):
        self._dfInit = pd.DataFrame(self.stateInit)
        self._dfInitqgrid = qgrid.show_grid(self._dfInit,grid_options={'forceFitColumns': False, 'defaultColumnWidth': 200, 'editable':True, 'sortable':False}, show_toolbar=False)
        with self._out:
            z = wg.HBox([self._dfInitqgrid, self._save_init, self._load_init], layout=wg.Layout(width='40%'))
            z.overflow_x = 'auto'
            display(z)
            display(self._disp_output_generation)
            self._disp_init.disabled = True
        self._disp_output_generation.on_click(self._event_simulation)
        self._save_init.on_click(self._event_save_init)
        self._load_init.on_click(self._event_load_init)

    def _event_save_init(self, b):
        self._initvalues =  self._dfInitqgrid.get_changed_df()
        self._initvalues.reset_index(inplace=True)
        self._initvalues.to_csv(os.path.join(os.path.dirname(self._dataPath.value),"initvalues.csv"), sep=";" , index=False)
    
    def _event_load_init(self, b):
        self._initfile = getFile()
        if self._initfile.split(".")[-1] != "csv":
            self._initfile = ''
            with self._out2:
                print('This data file is not the required data format.')
        
        if self._initfile:
            self._initvalues = pd.read_csv(self._initfile, sep=";")
            for nrow in range(0, self._initvalues.shape[0]):
                self._dfInitqgrid.edit_cell(nrow,"name", self._initvalues["name"][nrow])
                self._dfInitqgrid.edit_cell(nrow,"value", self._initvalues["value"][nrow])

    def _event_save_connection(self, b):
        self._datamodelconnection = self._dfVarDataqgrid.get_changed_df()
        self._datamodelconnection.reset_index(inplace=True)
        self._datamodelconnection.to_csv(os.path.join(os.path.dirname(self._dataPath.value),"datamodel.csv"), sep=";", index=False )
    
    def _event_load_connection(self, b):
        self._datamodelfile = getFile()
        if self._datamodelfile.split(".")[-1] != "csv":
            self._datamodelfile = ''
            with self._out2:
                print('This data file is not the required data format.')
        
        if self._datamodelfile:
            self._datamodelconnection = pd.read_csv(self._datamodelfile, sep=";")
            for nrow in range(0, self._datamodelconnection.shape[0]):
                self._dfVarDataqgrid.edit_cell(nrow,"Variables", self._datamodelconnection["Variables"][nrow])
                self._dfVarDataqgrid.edit_cell(nrow,"Data columns", self._datamodelconnection["Data columns"][nrow])

    def _event_save_params(self, b):

        self._newdfParamqgrid = self._dfParamqgrid.get_changed_df()
        self._newdfParamqgrid.reset_index(inplace=True)
        self.params = pd.DataFrame({"name": [n for n in self._newdfParamqgrid["name"]],
                                    "value":[v for v in self._newdfParamqgrid["value"]]})
        self.params.to_csv(os.path.join(os.path.dirname(self._dataPath.value),"parameters.csv"), sep=";", index=False )
        
    def _event_load_params(self, b):
        self._paramsfile = getFile()
        if self._paramsfile.split(".")[-1] != "csv":
            self._paramsfile = ''
            with self._out2:
                print('This data file is not the required data format.')
        
        if self._paramsfile:
            self.params = pd.read_csv(self._paramsfile, sep=";")
            for nrow in range(0, self.params.shape[0]):
                self._dfParamqgrid.edit_cell(nrow,"name", self.params["name"][nrow])
                self._dfParamqgrid.edit_cell(nrow,"value", self.params["value"][nrow])

    def _event_simulation(self, b):
        import pip._internal as pip
        import importlib
        def install(package, model):
            try:
                return importlib.import_module(".simulation",model)
            except ImportError:
                pip.main(['install', package])
            return importlib.import_module(".simulation",model)

        package = self._modelPath.value + os.path.sep + "src" + os.path.sep + "py"
        model = self._modelPath.value.split(os.path.sep)[-1]
        module = install(package, model)
        #module = importlib.import_module(".simulation",model)
        self.res = module.simulation(self._dataPath.value,self._datamodelconnection,self.params,self._initvalues)
        print(self.res)
        self._out2.clear_output()
        with self._out:
            display(self._disp_output_plot)
        self._disp_output_plot.on_click(self._event_plot)

    def _event_plot(self, b):
        self._out2.clear_output()
        display(self._out2)
        with self._out2:
            visualization.VisualizationMenu(self.res).displayMenu()

    def button_click(self, change):
        if change["new"] == "Apply" and self.fc.selected is not None:
            self._modelPath.value = Path(self.fc.selected_path)
            if 'crop2ml' not in os.listdir(self._modelPath.value):
                self._modelPath.value = ''
                with self._out2:
                    print('This repository is not a model package.')
        elif change["new"] == "Reset":
            self.fc.reset()
        elif change["new"] == "Close":
            self._out2.clear_output()
            with self._out2: # out
                pass
                #display(self._displayer)        

    def _eventClose(self, b):
        self._out2.clear_output()
        with self._out:
            display(self._displayer) 
                
    def _eventBrowse(self, b):
        """
        Handles browse button on_click event
        """ 
        self._out2.clear_output()
        #self._out.clear_output()
        with self._out2:
            display(self.filechooser_widget)
            
        self.buttons.observe(self.button_click, "value") 

    def _eventVisualize(self, b):
        
        """
        Handles browse button on_click event
        """
        _close = wg.Button(value=False, description='Close', disabled=False, button_style='warning')

        def _eventClose_vis(b):
            from copy import copy
            """
            Handles cancel button on_click event
            """
            self._out2.clear_output()
            with self._out:
                display(self._displayer)  

        def displayMenu_vis():
            from copy import copy
            self._out2.clear_output()
            df = pd.read_csv(self._dataPath.value, delimiter=";", index_col=0)
            self._qgridIn = qgrid.show_grid(df,grid_options={'forceFitColumns': False, 'defaultColumnWidth': 100, 'editable':False, 'sortable':False}, show_toolbar=False)
            tab = wg.Tab()
            tab.children = [self._qgridIn]
            self._out.clear_output()
            with self._out2:
                display(wg.VBox([wg.HTML(value='<b><font size="5">Model data '), tab, _close]))
            _close.on_click(_eventClose_vis)
        
        displayMenu_vis()

    def _eventBrowse_data(self, b):
        """
        Handles browse button on_click event
        """
        
        self._out2.clear_output()
        self._dataPath.value = getFile()
        if self._dataPath.value.split(".")[-1] != "csv":
            self._dataPath.value = ''
            with self._out2:
                print('This data file is not the required data format.')
        
        if self._dataPath.value and self._modelPath.value:
            self._out.clear_output()
            with self._out:
                display(self._displayer) 

    def _on_value_change(self, change):
        """
        Handles changes from the attribute _modelPath.

        Find every model in xml format in the selected path.
        """
        global g 
        self._paths.clear()
        self.tmp = []
        for f in os.listdir(self._modelPath.value+os.path.sep+'crop2ml'):
            split = f.split('.')
            if all([split[-1] == 'xml', split[0] =='composition']):
                self._paths[f] = self._modelPath.value+os.path.sep+'crop2ml'+os.path.sep+f
                self.tmp.append(f)
        self._selecter.options = self.tmp    
        self._selecter.disabled = False
        g = self.tmp

    def displayMenu(self):
        """
        Displays the model edition menu of pyrcop2ml's UI.

        This method is the only one available for the user in this class. Any other attribute or
        method call may break the code.
        """

        display(self._out)
        display(self._out2)
        with self._out:
            display(self._displayer)     
        self._browse.on_click(self._eventBrowse)     
        self._modelPath.observe(self._on_value_change, names='value')
        self._browse_data.on_click(self._eventBrowse_data) 
        self._visualization.on_click(self._eventVisualize)
        self._connection.on_click(self._eventConnection)
    


