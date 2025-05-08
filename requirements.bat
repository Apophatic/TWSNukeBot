@echo off
echo [*] Checking Python version...
python --version || (
    echo [!] Python is not installed. Please install it from https://python.org
    pause
    exit /b
)

echo [*] Installing required Python packages...

:: Optional: Create and activate a virtual environment
:: python -m venv venv
:: call venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install discord.py
pip install -U discord.py

:: tkinter is built-in with Python on Windows. We'll check for it.
python -c "import tkinter" || (
    echo [!] tkinter is not installed or broken. Reinstall Python with the 'tcl/tk' option enabled.
    pause
    exit /b
)

echo [*] All required packages have been installed.
pause
