# -*- coding: utf-8 -*-
import os

from IPython.display import display
import ipywidgets as wg
from io import BytesIO
from zipfile import ZipFile

from pycrop2ml_ui.menus.creation import createmenu
from pycrop2ml_ui.menus.edition import editmenu
from pycrop2ml_ui.cpackage.createpackage import createPackage
from pycrop2ml_ui.menus.transformation import transformationmenu
from pycrop2ml_ui.menus.ptransformation import ptransformationmenu
from pycrop2ml_ui.menus.display.displaymenu import displayMenu
from pycrop2ml_ui.menus.execution import executionmenu
from pycrop2ml_ui.menus.download import downloadmenu


class mainMenu():

    """
    Class providing the launching of pycrop2ml's user interface.
    It is aiming to enhance the model management of pycrop2ml models as well
    as decorating the xml format used to write model attributes.

    It requires mainly pycrop2ml, ipywidgets, pandas and qgrid to run the whole set of 
    menus. Refering to python's coding manners, do not use methods and class
    attributes beginning with an underscore otherwise code can break.

    The class mainMenu contains 5 branches refering to creation, edition,
    display, transformation and package creation :\n
    package creation -> createPackage\n
    creation -> class createMenu\n
    edition -> class editMenu\n
    transformation -> class transformationMenu\n
    ptransformation -> class ptransformationMenu\n
    display -> class displayMenu

    displayMenu() displays the main menu of the user interface and provides
    four buttons clickable leading to each branch. This is the only method
    usable in this class and does not require any argument.

    To run a mainMenu, use :\n
    mainmenu = mainMenu() #creates an instance of mainMenu\n
    mainmenu.displayMenu()       #calls displayMenu() method
    """

    def __init__(self, local=True):

        self.local = local
        self._layout = wg.Layout(width='300px', height='60px')
        self._layout_thin = wg.Layout(width='150px', height='60px')
        self._create = wg.Button(value=False,description='Model creation',disabled=False,layout=self._layout)
        self._edit = wg.Button(value=False,description='Model edition',disabled=False,layout=self._layout)
        self._transformation = wg.Button(value=False,description='Crop2ML to Platform',disabled=False,layout=self._layout)
        self._ptransformation = wg.Button(value=False,description='Platform to Crop2ML',disabled=False,layout=self._layout)
        self._execution = wg.Button(value=False,description='Model execution',disabled=False,layout=self._layout)
        self._display = wg.Button(value=False,description='Model display',disabled=False,layout=self._layout)
        self._download = wg.Button(value=False, description='Model download', disabled=False, layout=self._layout)
        self._about = wg.Button(value=False,description='About',disabled=False,layout=self._layout)

        if self.local==False:
            self._import = wg.FileUpload(accept='.zip', description='Package import', disabled=False, layout=self._layout_thin)
            self._mkdir = wg.Button(value=False,description='Package creation',disabled=False,layout=self._layout_thin)
            self._disabled = [self._create, self._edit, self._transformation, self._execution, self._display, self._download]
            self.pkg_directory = "./packages"
            if not os.path.isdir(self.pkg_directory) or not os.listdir(self.pkg_directory):
                for w in self._disabled:
                    w.disabled = True
            self._displayer = wg.VBox([wg.HTML(value='<font size="5"><b>Model manager for Pycrop2ml</b></font>'),
                                       wg.HBox([self._mkdir, self._import]),
                                       self._create,
                                       self._edit,
                                       self._transformation,
                                       self._ptransformation,
                                       self._execution,
                                       self._display,
                                       self._download,
                                       self._about
                                       ], layout=wg.Layout(align_items='center'))

        else:
            self._mkdir = wg.Button(value=False,description='Package creation',disabled=False,layout=self._layout)
            self._displayer = wg.VBox([wg.HTML(value='<font size="5"><b>Model manager for Pycrop2ml</b></font>'),
                                       self._mkdir,
                                       self._create,
                                       self._edit,
                                       self._transformation,
                                       self._ptransformation,
                                       self._execution,
                                       self._display,
                                       self._download,
                                       self._about
                                       ], layout=wg.Layout(align_items='center'))
            
        self._out = wg.Output()
        self._out2 = wg.Output()

    def _eventMkdir(self, b):
        """
        Displays package creation menu
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out: 
            try:
                menu = createPackage(self.local)
                menu.displayMenu()
            except:
                raise Exception('Could not load package creation menu.')

    def _eventImport(self, event):
        """
        Import package from zip
        """

        if not os.path.isdir(self.pkg_directory):
            os.mkdir(self.pkg_directory)

        v = event.owner.value
        with ZipFile(BytesIO(v[list(v.keys())[0]]['content'])) as zip:
            zip.extractall(self.pkg_directory)

        for w in self._disabled:
            w.disabled = False

    def _eventCreate(self, b):
        """
        Displays model creation menu
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                createWg = createmenu.createMenu(self.local)
                createWg.displayMenu()          
            except:
                raise Exception('Could not load creation menu.')
            
    def _eventEdit(self, b):
        """
        Displays model edition menu
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                editWg = editmenu.editMenu(self.local)
                editWg.displayMenu()          
            except:
                raise Exception('Could not load edition menu.')

    def _eventTransformation(self, b):
        """
        Displays package transformation menu
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                menu = transformationmenu.transformationMenu(self.local)
                menu.displayMenu()     
            except:
                raise Exception('Could not load transformation menu.')

    def _eventpTransformation(self, b):
        """
        Displays package transformation menu
        """

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                menu = ptransformationmenu.ptransformationMenu(self.local)
                menu.displayMenu()     
            except:
                raise Exception('Could not load transformation menu.')

    def _eventDisplay(self, b):
        """
        Display the model display menu
        """
        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                menu = displayMenu(self.local)
                menu.displayMenu()     
            except:
                raise Exception('Could not load model display menu.')

    def _eventExecution(self, b):
        """
        Execute the model menu
        """
        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                menu = executionmenu.ExecutionMenu(self.local)
                menu.displayMenu()     
            except:
                raise Exception('Could not execute model .')

    def _eventDownload(self, b):

        self._out.clear_output()
        self._out2.clear_output()

        with self._out:
            try:
                menu = downloadmenu.DownloadMenu(self.local)
                menu.displayMenu()
            except:
                raise Exception('Could not open download menu.')

    def _eventAbout(self, b):
        """
        Prints the description of the mainMenu class
        """

        self._out2.clear_output()

        with self._out2:
            display(wg.HTML("""
                • Class providing the launching of pycrop2ml's user interface. It is aiming to enhance the model management of pycrop2ml models as well
                as decorating the xml format used to write model attributes.<br>

                It requires mainly pycrop2ml, ipywidgets, pandas and qgrid to run the whole set of menus. Refering to python's coding manners, do not use methods and class
                attributes beginning with an underscore otherwise code can break.<br><br>

                • The class mainMenu contains 5 branches refering to creation, edition, display, transformation and package creation :<br>
                - package creation -> createPackage<br>
                - creation -> class createMenu<br>
                - edition -> class editMenu<br>
                - transformation -> class transformationMenu<br>
                - ptransformation -> class ptransformationMenu<br>
                - display -> class displayMenu<br><br>

                • displayMenu() displays the main menu of the user interface and provides three buttons clickable leading to each branch. This is the only method
                usable in this class and does not require any argument.<br>

                To create a mainMenu, use :<br>
                - mainmenu = mainMenu() #creates an instance of mainMenu<br>
                - mainmenu.displayMenu()       #calls displayMenu() method
                """))

    def displayMenu(self):
        """
        Displays the main menu of pycrop2ml's UI.
        
        This method is the only one available for the user in this class. Any other attribute or
        method call may break the code.
        """

        display(self._out)
        display(self._out2)

        with self._out:
            display(self._displayer)
        
        self._mkdir.on_click(self._eventMkdir)
        if self.local==False: 
            self._import.observe(self._eventImport, names='value')
        self._create.on_click(self._eventCreate)
        self._edit.on_click(self._eventEdit)
        self._transformation.on_click(self._eventTransformation)
        self._ptransformation.on_click(self._eventpTransformation)
        self._display.on_click(self._eventDisplay)
        self._execution.on_click(self._eventExecution)
        self._download.on_click(self._eventDownload)
        self._about.on_click(self._eventAbout)
        

def main(local=True):

    output = mainMenu(local)
    output.displayMenu()

