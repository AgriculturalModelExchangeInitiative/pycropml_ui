[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AgriculturalModelExchangeInitiative/Pycrop2ml_ui.git/HEAD?urlpath=lab)

# Pycrop2ml_ui

User interface for Pycrop2ML...

    conda install -c amei -c openalea3 -c conda-forge pycrop2ml_ui 'libtiff<4.5'

## On Mac OS X
```bash
export NODE_OPTIONS=--openssl-legacy-provider
conda install -c conda-forge nodejs
jupyter labextension install @jupyter-widgets/jupyterlab-manager@2 qgrid2 --dev-build=False --minimize=False

git clone https://github.com/AgriculturalModelExchangeInitiative/Pycrop2ml_ui

mkdir work
cp Pycrop2ml_ui/src/pycrop2ml_ui/AppLauncher.ipynb work/AppLauncher.ipynb
cd work
jupyter lab AppLauncher.ipynb
```

## Install other kernels on Linux & Mac

<details>
<summary>
        
### Install R kernel
   
</summary>

    conda install -y -q -c conda-forge  r-base r-ikernel r-devtools r-htmlwidgets r-rmarkdown
</details>

<details>
<summary>
        
### Install C# kernel
   
</summary>

## TODO

</details>

<details>
<summary>
        
### Install Fortran kernel
   
</summary>

## TODO

</details>




