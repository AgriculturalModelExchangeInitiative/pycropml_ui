import os
import ipywidgets as wg
from IPython.display import display

from pycrop2ml_ui.model import MainMenu
from pycrop2ml_ui.browser.TkinterPath import getPath
from pycropml.cyml import transpile_package


class transformationMenu():

    """
    Class providing the display of the package transformation menu for pycrop2ml's user interface.
    """

    def __init__(self, local):

        self._out = wg.Output()
        self._out2 = wg.Output()
        self.local = local

        self._apply = wg.Button(value=False,description='Apply',disabled=False,button_style='success')
        self._cancel = wg.Button(value=False,description='Quit',disabled=False,button_style='warning')
        
        if self.local == True:
            self._browse = wg.Button(value=False,description='Browse',disabled=False,button_style='primary')
            self._path = wg.Textarea(value='',description='Path:',disabled=True,layout=wg.Layout(height='57px',width='400px'))
            self._pathing = wg.HBox([self._path, self._browse])
        else:
            self._path = wg.Dropdown(options=['None'],value='None',description='Path:',disabled=False,layout=wg.Layout(width='400px',height='35px'))
            self.tmp = []
            self.pkg_directory = "./packages"
            for f in os.listdir(self.pkg_directory):
                self.tmp.append(os.path.join(self.pkg_directory,f))
            self._path.options = self.tmp 
            self._path.disabled = False 
            self._pathing = self._path 
            
        self._java = wg.Checkbox(value=False, description='Java', disabled=False)
        self._csharp = wg.Checkbox(value=False, description='CSharp', disabled=False)
        self._fortran = wg.Checkbox(value=False, description='Fortran', disabled=False)
        self._python = wg.Checkbox(value=False, description='Python', disabled=False)
        self._r = wg.Checkbox(value=False, description='R', disabled=False)
        self._cpp = wg.Checkbox(value=False, description='C++', disabled=False)
        self._simplace = wg.Checkbox(value=False, description='Simplace', disabled=False)
        self._bioma = wg.Checkbox(value=False, description='Bioma', disabled=False)
        self._dssat = wg.Checkbox(value=False, description='Dssat', disabled=False)
        self._openalea = wg.Checkbox(value=False, description='OpenAlea', disabled=False)
        self._record = wg.Checkbox(value=False, description='Record', disabled=False)
        self._stics = wg.Checkbox(value=False, description='Stics', disabled=False)
        self._apsim = wg.Checkbox(value=False, description='Apsim', disabled=False)

        self._displayer = wg.VBox([wg.HTML(value='<font size="5"><b>Crop2ML to Platform</b></font>'), self._pathing, wg.HBox([wg.VBox([self._java, self._csharp, self._fortran, self._python, self._r, self._cpp]),wg.VBox([self._simplace, self._bioma, self._dssat, self._openalea, self._record, self._stics, self._apsim])]), wg.HBox([self._apply, self._cancel])], layout=wg.Layout(align_items='center'))

        self._listlanguage = []



    def _eventApply(self, b):
        """
        Handles apply button on_click event
        """

        self._out2.clear_output()

        if not self._path.value:
            with self._out2:
                print('You must give a package path.')
        else:
            self._listlanguage.clear()

            if self._java.value:
                self._listlanguage.append('java')
            if self._csharp.value:
                self._listlanguage.append('cs')
            if self._fortran.value:
                self._listlanguage.append('f90')
            if self._python.value:
                self._listlanguage.append('py')
            if self._r.value:
                self._listlanguage.append('r')
            if self._cpp.value:
                self._listlanguage.append('cpp')
            if self._simplace.value:
                self._listlanguage.append('simplace')
            if self._bioma.value:
                self._listlanguage.append('bioma')
            if self._dssat.value:
                self._listlanguage.append('dssat')
            if self._openalea.value:
                self._listlanguage.append('openalea')
            if self._record.value:
                self._listlanguage.append('record')
            if self._stics.value:
                self._listlanguage.append('stics')
            if self._apsim.value:
                self._listlanguage.append('apsim')

            if not self._listlanguage:
                with self._out2:
                    print('You must give at least one target language to transform in.')
            
            else:
                for lg in self._listlanguage:
                    try:
                        transpile_package(self._path.value, lg)
                    except:
                        #self._out.clear_output()
                        with self._out:
                            raise Exception('Critical error while transpiling the package {} into {}.'.format(self._path.value, lg))

                self._out.clear_output()
                self._out2.clear_output()
                
        with self._out:
            display(self._displayer)



    def _eventBrowse(self, b):
        """
        Handles browse button on_click event
        """

        self._out2.clear_output()
        self._path.value = getPath() 

        if 'crop2ml' not in os.listdir(self._path.value):
            self._path.value = ''
            with self._out2:
                print('This repository is not a model package.')



    def _eventCancel(self, b):
        """
        Handles cancel button on_click event
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:  
            try:
                tmp = MainMenu.mainMenu(self.local)
                tmp.displayMenu()
            except:
                raise Exception('Could not load mainmenu.')



    def displayMenu(self): 
        """
        Displays the package transformation menu of pyrcop2ml's UI.

        This method is the only one available for the user in this class. Any other attribute or
        method call may break the code.
        """

        display(self._out)
        display(self._out2)

        with self._out:
            display(self._displayer)

        self._apply.on_click(self._eventApply)
        self._cancel.on_click(self._eventCancel)
        if self.local==True: self._browse.on_click(self._eventBrowse)
