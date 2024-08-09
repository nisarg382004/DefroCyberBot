@echo off

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.x and try again.
    exit /b
)

:: Create a virtual environment
echo Creating a virtual environment...
python -m venv venv

:: Activate the virtual environment
echo Activating the virtual environment...
call venv\Scripts\activate.bat

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo Installation completed successfully.
pause
