import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

Bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())

@Bot.event
async def on_ready():
    print(f"{Bot.user.name} successfully logged in!")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await Bot.load_extension(f'cogs.{filename[:-3]}')
    print("All COGs loaded!")

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

Bot.run(token)