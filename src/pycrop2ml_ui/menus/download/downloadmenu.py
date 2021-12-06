import ipywidgets as wg
import os

from IPython.display import display

from zipfile import ZipFile

from pycrop2ml_ui.browser.TkinterPath import getPath
from pycrop2ml_ui.model import MainMenu


class DownloadMenu():

    def __init__(self, local):

        self._out = wg.Output()
        self._out2 = wg.Output()
        self.local = local

        # inputs

        if self.local:
            self._modelPath = wg.Textarea(value='', description='Model path:',disabled=True,layout=wg.Layout(width='400px',height='57px'))
            self._browse = wg.Button(value=False, description='Browse', disabled=False, button_style='primary')
            self._pathing = wg.HBox([self._modelPath, self._browse])

        else:
            self._modelPath = wg.Dropdown(options=['None'],value='None',description='Model path:',disabled=False,layout=wg.Layout(width='400px',height='35px'))
            self.tmp = [""]
            self.pkg_directory = "./packages"
            for f in os.listdir(self.pkg_directory):
                self.tmp.append(os.path.join(self.pkg_directory,f))
            self._modelPath.options = self.tmp
            self._modelPath.disabled = False
            self._pathing = self._modelPath

        # buttons

        self._download = wg.Button(value=False, description='Download', disabled=False, button_style='success')
        self._cancel = wg.Button(value=False, description='Cancel', disabled=False, button_style='warning')

        self._displayer = wg.VBox([wg.HTML(value='<font size="5"><b>Model download</b></font>'),
                                   self._pathing, wg.HBox([self._download, self._cancel])],
                                  layout=wg.Layout(align_items='center'))

   def _eventBrowse(self, b):
        """
        Handles browse button on_click event
        """

        self._out2.clear_output()
        self._modelPath.value = getPath()

        if 'crop2ml' not in os.listdir(self._modelPath.value):
            self._modelPath.value = ''
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
                raise Exception('Could not load mainMenu.')

    def displayMenu(self):
        """
        Displays the model edition menu of pyrcop2ml's UI.

        This method is the only one available for the user in this class. Any other attribute or
        method call may break the code.
        """

        display(self._out)

        with self._out:
            display(self._displayer)

        self._download.on_click(self._eventDownload)
        if self.local:
            self._browse.on_click(self._eventBrowse)
        self._cancel.on_click(self._eventCancel)
        self._modelPath.observe(self._on_value_change, names='value')