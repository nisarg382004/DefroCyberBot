@echo off

:: Activate the virtual environment
echo Activating the virtual environment...
call venv\Scripts\activate.bat

:: Run the bot
echo Starting DefroCyberBot...
python src\bot.py

pause