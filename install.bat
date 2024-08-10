@echo off
REM Install pip if not installed
python -m ensurepip --upgrade

REM Install dependencies
pip install -r requirements.txt
