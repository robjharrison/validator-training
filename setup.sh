#!/bin/bash

# chmod +x setup.sh

# Install additional system-level dependencies/packages
sudo apt-get update    

         
# Install the Python extension for Visual Studio Code
code --install-extension ms-python.python --force

# Install Python dependencies
pip install pytest
pip install pandas
