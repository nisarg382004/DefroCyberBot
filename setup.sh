#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install additional Python dependencies
pip install schedule SpeechRecognition aiohttp requests beautifulsoup4 spacy

# Download and install the spaCy model
python -m spacy download en_core_web_sm

echo "Setup complete. You can now run 'python3 cli.py' to start the bot."
