#!/bin/bash

# Update package lists
sudo apt-get update

# Install pip if not installed
sudo apt-get install -y python3-pip

# Install dependencies
pip3 install -r requirements.txt
