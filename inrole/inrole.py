import discord
import os
from discord.ext import commands

class InRole:
    """Displays users by role"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def inrole(self, ctx, *, role: str):
        """Displays users by role"""
        server = ctx.message.server
        roles = [r for r in server.roles if r.name == role]
        if len(roles) == 0:
            await self.bot.say("That role doesn't exist!")
            return
        members_to_show = [m for m in server.members if roles[0] in m.roles]
        members_to_show = sorted(members_to_show, key=lambda member: member.display_name)
        reply_string = "**" + str(len(members_to_show)) + " members in role " + roles[0].name + ":** "
        counter = 0
        for member in members_to_show:
            if len(reply_string) + len(member.display_name) > 1900:
                reply_string += ", "
                await self.bot.say(reply_string)
                reply_string = ""
                counter = 0
            if counter > 0:
                reply_string += ", "
            reply_string += "`" + member.display_name + "`"
            counter += 1
        if len(reply_string) > 0:
            await self.bot.say(reply_string)

def setup(bot):
    bot.add_cog(InRole(bot))

