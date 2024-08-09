#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit
fi

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installation completed successfully."
