#!/bin/bash

# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Install virtualenv
sudo apt install -y python3-venv

# Install Git
sudo apt install -y git

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

echo "Installation complete. Run './setup.sh' to set up the project."
