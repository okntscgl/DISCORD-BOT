# Discord Bot

This project is a basic Discord bot built with **discord.py** using a Cog-based structure.  
It includes simple fun commands, moderation features, and a utility command to display server information.

The bot is intended for learning purposes and small Discord servers.

---

## Features

### Fun Commands
- `!hello` – Sends a simple greeting message.
- `!ping` – Displays the bot latency in milliseconds.

### Moderation Commands
> Requires appropriate Discord permissions.

- `!kick @user [reason]` – Kicks a member from the server.
- `!ban @user [reason]` – Bans a member from the server.

### Utility Commands
- `!info` – Shows basic server information such as member count and server icon.

---

## Requirements

- Python 3.8 or higher
- A Discord bot token
- Required Python libraries:
  - `discord.py`
  - `python-dotenv`

Install dependencies:
```bash
pip install discord.py python-dotenv
Setup
Clone the repository:

bash
git clone https://github.com/okntscgl/discord-bot.git
cd discord-bot
Create a .env file and add your bot token:

DISCORD_TOKEN=your_bot_token_here
Run the bot:

bash
python main.py
Notes
The bot uses all Discord intents.

Commands are permission-restricted where necessary.

Cogs are loaded automatically from the cogs directory on startup.

This project is for educational purposes and basic server management.

Disclaimer
Use moderation commands responsibly.
The developer is not responsible for misuse of this bot.
