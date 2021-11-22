import ipywidgets as wg
import pandas as pd
import os
from IPython.display import display
import matplotlib.pyplot as plt


class VisualizationMenu():

    def __init__(self, res):
           
        #outputs
        self._out = wg.Output()
        self._out2 = wg.Output()
        self.res = res

        opts = self.res.columns.values
        self.selector = wg.SelectMultiple(
        options=opts,
        value=[opts[1]],
        rows=len(opts),
        description='Variables',
        disabled=False)
    
    def multiplot(self, widg):
        choices = widg['new']
        data = self.res.loc[:, choices] if choices else self.res
        display(self._out2)
        with self._out2:
            ax = data.plot()
            plt.show() 
    
    def displayMenu(self):
        """
        """
        self._out.clear_output()
        display(self._out)
        display(self._out2)
        with self._out:
            display(self.selector) 
        self.selector.observe(self.multiplot, names='value')    
