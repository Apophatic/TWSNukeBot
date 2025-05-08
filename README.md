💣 TWS' Nuke Bot – GUI Discord Server Setup Tool
This project is a Python GUI tool that uses a Discord bot token to create multiple channels, roles, and spam messages in a server. It is intended for educational and testing purposes only.

⚠️ Disclaimer: Misusing this tool to destroy or spam Discord servers you do not own is a violation of Discord's Terms of Service. Use responsibly.

📋 Features
Create multiple text channels

Spam custom messages into each channel

Create multiple roles

Beautiful GUI interface using tkinter

Error handling and token validation

🖥️ Requirements
Before running this program, you must have the following:

✅ 1. Python Installed
Download and install Python 3.10+ from:
🔗 https://www.python.org/downloads/

Make sure to check the box that says "Add Python to PATH" during installation.

✅ 2. Required Python Libraries
Open a terminal (Command Prompt) and run this to install dependencies:

bat
Copy
Edit
@echo off
python -m pip install --upgrade pip
pip install discord.py
Note: tkinter comes with Python by default on Windows. If it’s missing, reinstall Python and ensure the "tcl/tk" option is checked.

⚙️ Setup Instructions
1. Clone or Download the Repository
Click Code > Download ZIP or run:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/tws-nuke-bot.git
cd tws-nuke-bot
2. Create Your Discord Bot
Go to the Discord Developer Portal

Click "New Application"

Give it a name (e.g., TWS Bot)

Go to the Bot tab → Click "Add Bot"

Enable the following Privileged Gateway Intents:

Server Members Intent

Message Content Intent

Copy your bot token

Go to the OAuth2 > URL Generator

Select bot

Give it permissions: Manage Channels, Manage Roles, Send Messages

Copy the generated URL and use it to invite the bot to your server

3. Run the GUI Tool
Once everything is ready:

Open main.py (or whatever you named the Python file)

Paste your Discord Bot Token

Fill in the rest of the form:

Number of Channels

Channel Name

Message to Spam

Messages per Channel

Number of Roles

Role Name

Click Submit Configuration

The bot will log in, create the resources, and spam the messages as configured.

🛠 Optional: Install Everything with a Batch File
You can install all dependencies using this included batch file:

install_requirements.bat
bat
Copy
Edit
@echo off
python --version || (
    echo [!] Python is not installed.
    pause
    exit /b
)
python -m pip install --upgrade pip
pip install discord.py
python -c "import tkinter" || (
    echo [!] tkinter is missing.
    pause
    exit /b
)
echo [*] All set!
pause
Run this once by double-clicking it.

👨‍💻 Credits
Made by TWS1001

🧠 Educational Use Only
This project is provided for learning purposes only.
Misuse can lead to account suspension or legal consequences.

