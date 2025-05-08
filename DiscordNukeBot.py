import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import discord
import re

# ---------------- Discord Bot Logic ----------------
class SetupBot(discord.Client):
    def __init__(self, config):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.guild_messages = True
        intents.message_content = True
        intents.members = True  # Privileged intent
        super().__init__(intents=intents)
        self.config = config

    async def on_ready(self):
        print(f'[+] Logged in as {self.user}')
        try:
            guild = self.guilds[0]

            created_channels = []
            for i in range(int(self.config["channel_count"])):
                channel = await guild.create_text_channel(f'{self.config["channel_name"]}-{i+1}')
                created_channels.append(channel)

            for i in range(int(self.config["role_count"])):
                await guild.create_role(name=f'{self.config["role_name"]}-{i+1}')

            for channel in created_channels:
                for _ in range(int(self.config["message_count"])):
                    await channel.send(self.config["message"])

            await self.close()
        except Exception as e:
            print(f"[!] Error during bot execution: {e}")
            messagebox.showerror("Bot Error", f"An error occurred:\n{e}")
            await self.close()

def run_bot(config):
    bot = SetupBot(config)
    try:
        bot.run(config["token"])
    except discord.errors.PrivilegedIntentsRequired:
        messagebox.showerror("Missing Privileged Intents",
            "Your bot is missing one or more privileged gateway intents (e.g., GUILD_MEMBERS).\n"
            "Please enable them in the Discord Developer Portal under your bot's settings.")
    except discord.LoginFailure:
        messagebox.showerror("Token Error", "Invalid bot token provided.")
    except Exception as e:
        messagebox.showerror("Bot Startup Error", f"An unexpected error occurred:\n{e}")

# ---------------- GUI Logic ----------------
def open_tutorial():
    webbrowser.open("https://github.com/Apophatic/TWSNukeBot")

def open_creator_page():
    webbrowser.open("https://guns.lol/tws1001")

def is_valid_token(token):
    return re.fullmatch(r"[MN][A-Za-z0-9_\-]{20,100}\.[\w\-]{6,}\.[\w\-]{25,}", token)

def is_valid_number(value):
    return value.isdigit() and int(value) >= 0

def submit():
    token = token_entry.get().strip()
    channel_count = channel_count_entry.get().strip()
    channel_name = channel_name_entry.get().strip()
    message_text = message_entry.get().strip()
    message_count = message_count_entry.get().strip()
    role_count = role_count_entry.get().strip()
    role_name = role_name_entry.get().strip()

    if not token:
        messagebox.showerror("Input Error", "Bot token is required.")
        return
    if not is_valid_token(token):
        messagebox.showerror("Invalid Token", "The bot token appears to be invalid or malformed.")
        return
    if not is_valid_number(channel_count):
        messagebox.showerror("Input Error", "Number of channels must be a non-negative integer.")
        return
    if not channel_name:
        messagebox.showerror("Input Error", "Channel name cannot be empty.")
        return
    if not message_text:
        messagebox.showerror("Input Error", "Message cannot be empty.")
        return
    if not is_valid_number(message_count):
        messagebox.showerror("Input Error", "Messages per channel must be a non-negative integer.")
        return
    if not is_valid_number(role_count):
        messagebox.showerror("Input Error", "Number of roles must be a non-negative integer.")
        return
    if not role_name:
        messagebox.showerror("Input Error", "Role name cannot be empty.")
        return

    config = {
        "token": token,
        "channel_count": channel_count,
        "channel_name": channel_name,
        "message": message_text,
        "message_count": message_count,
        "role_count": role_count,
        "role_name": role_name,
    }

    summary = f"""Token: {'*' * len(token)}
Channels: {channel_count} named '{channel_name}'
Messages per Channel: {message_count}
Message: {message_text}
Roles: {role_count} named '{role_name}'"""
    messagebox.showinfo("Configuration Summary", summary)

    threading.Thread(target=run_bot, args=(config,), daemon=True).start()

# ---------------- Tkinter UI ----------------
root = tk.Tk()
root.title("Discord Server Setup Bot")
root.geometry("430x650")
root.configure(bg="#1e1e1e")

entry_style = {
    "bg": "#2e2e2e",
    "fg": "white",
    "relief": "flat",
    "insertbackground": "white",
    "font": ('Helvetica', 10),
    "width": 40
}

label_style = {
    "bg": "#1e1e1e",
    "fg": "#dcdcdc",
    "font": ('Helvetica', 10, 'bold')
}

def styled_button(parent, text, command, color):
    return tk.Button(
        parent, text=text, command=command,
        bg=color, fg="white", activebackground=color,
        relief="flat", font=('Helvetica', 11, 'bold'),
        padx=10, pady=5, width=25, cursor="hand2"
    )

# TWS' Nuke Bot Header
header_label = tk.Label(root, text="TWS' Nuke Bot", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="#7289da")
header_label.pack(pady=(20, 15))

# Tutorial & Creator Buttons
styled_button(root, "Tutorial Here", open_tutorial, "#7289da").pack(pady=(8, 8))
styled_button(root, "Creator's Page", open_creator_page, "#7289da").pack(pady=(0, 20))

# Token Entry
tk.Label(root, text="Paste Discord Bot Token:", **label_style).pack()
token_entry = tk.Entry(root, **entry_style)
token_entry.pack(pady=5)

# Channel Count
tk.Label(root, text="Number of Channels:", **label_style).pack()
channel_count_entry = tk.Entry(root, **entry_style)
channel_count_entry.pack(pady=5)

# Channel Name
tk.Label(root, text="Channel Name:", **label_style).pack()
channel_name_entry = tk.Entry(root, **entry_style)
channel_name_entry.pack(pady=5)

# Message
tk.Label(root, text="Message to Send:", **label_style).pack()
message_entry = tk.Entry(root, **entry_style)
message_entry.pack(pady=5)

# Message Count
tk.Label(root, text="Messages per Channel:", **label_style).pack()
message_count_entry = tk.Entry(root, **entry_style)
message_count_entry.pack(pady=5)

# Role Count
tk.Label(root, text="Number of Roles:", **label_style).pack()
role_count_entry = tk.Entry(root, **entry_style)
role_count_entry.pack(pady=5)

# Role Name
tk.Label(root, text="Role Name:", **label_style).pack()
role_name_entry = tk.Entry(root, **entry_style)
role_name_entry.pack(pady=5)

# Submit Button
styled_button(root, "Submit Configuration", submit, "#2ecc71").pack(pady=25)

root.mainloop()










