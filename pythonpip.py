# python PI(python package installer) -- pip is a package manager for python packages, modules
# a package contains all the files you need for a module, modules are py libraries 
# package is a collection of python files/modules
# numpy, pandas, flask
# use installed package
import camelcase
c= camelcase.CamelCase()
txt="hello keerthi"
print(c.hump(txt))

# remove package -- hence removed

# list installed package -- pip list

# upgrade package 

# install specific vesrsion
#pip install numpy==1.26.4

# showing package details
# pip show numpy

# save project packages
# pip freeze > requirements.txt
# numpy=1.26.4
#pandas==2.2.2


# where packages come from: PyPI(python package index)
# it is offcial python package website

# common beginer errors
# pip is not recognized

# we can fix by -- python -m pip install package_name


''' 
difference b/w module and package 
module .py file eg: math.py
package is folder containing many modules
numpy/

Most Used PIP Commands (Quick Revision)
Command	Purpose
pip --version	-check pip
pip install package	 -install
pip uninstall package	-remove
pip list	-list packages
pip show package	-package details
pip freeze	-save dependencies
pip install -r file.txt -install from file
pip install --upgrade package	-update

'''