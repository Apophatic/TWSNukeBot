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
Download the batch file named 'requirements' from the repository and run it

⚙️ Setup Instructions
1. Clone or Download the Repository
Click Code > Download ZIP or run:

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

👨‍💻 Credits
Made by TWS1001

🧠 Educational Use Only
This project is provided for learning purposes only.
Misuse can lead to account suspension or legal consequences.

