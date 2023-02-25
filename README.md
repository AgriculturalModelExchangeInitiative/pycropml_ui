[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AgriculturalModelExchangeInitiative/Pycrop2ml_ui.git/HEAD?urlpath=lab)

# Pycrop2ml_ui

User interface for Pycrop2ML...

    conda install -c amei -c openalea3 -c conda-forge pycrop2ml_ui 'libtiff<4.5'

## On Mac OS X
```bash
export NODE_OPTIONS=--openssl-legacy-provider
conda install -c conda-forge nodejs
jupyter labextension install @jupyter-widgets/jupyterlab-manager@2 qgrid2 --dev-build=False --minimize=False
```
