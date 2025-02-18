import discord
from discord.ext import commands
from cogs import ping_control, slot_management

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

bot.add_cog(ping_control.PingControl(bot))
bot.add_cog(slot_management.SlotManagement(bot))

bot.run('YOUR_BOT_TOKEN')