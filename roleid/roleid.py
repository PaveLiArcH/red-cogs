import discord
import os
from discord.ext import commands

class RoleId:
    """Displays role id"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roleid(self, ctx, *, role: str):
        """Displays role id"""
        server = ctx.message.server
        roles = [r for r in server.roles if r.name == role]
        if len(roles) == 0:
            await self.bot.say("That role doesn't exist!")
            return
        await self.bot.say(roles[0].id)

def setup(bot):
    bot.add_cog(RoleId(bot))

