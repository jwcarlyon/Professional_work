# Render and Colormap Tweaker

\-This repository contains python and iPythonNotebook code which works as a GUI.  
Running Framework1 in an ipynb environment will read through a fortran F90 File
and highlight and present key values to be altered or noted.  
Once complete, the program will produce a new file which can be used in place of
the original\-

## What does this do exactly?

The Framework1.ipynb file will create a GUI in an ipynotebook. This GUI guides the user through a complex physics based fortran image rendering code. The attached version will set up the required files for the user then display a range of rgba colormaps which are predefined in srend.F90. The user can select from two of these presets and tweak them, then the python code will interpolate 8 new colormaps between the selected ones. The result is a new srend.F90 file and two image files in any desired format which represent the user-made colormaps.
