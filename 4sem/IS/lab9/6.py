from time import sleep
from discord.ext import commands
from ds_bot import token


class HWBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='timer')
    async def timer(self, ctx, seconds):
        sleep(int(seconds))
        await ctx.send("время X наступило!")

bot = commands.Bot(command_prefix='$')
bot.add_cog(HWBot(bot))
bot.run(token)