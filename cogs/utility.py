import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="Server Information", description=f"Information about the {ctx.guild.name} server:", color=discord.Color.blue())
        embed.add_field(name="Member Count", value=ctx.guild.member_count)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
