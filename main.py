import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix=',', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot Online")


@client.command()
async def userinfo(ctx, member:discord.Member=None):
    if member is None:
        member = ctx.author
    elif member is not None:
        member = member

    e1 = discord.Embed(title=f"{member.name}'s user infromation", description="All infromation about this user!", color=member.color)
    e1.add_field(name="Name:", value=member.name, inline=False)
    e1.add_field(name="Nickname:", value=member.display_name, inline=False)
    e1.add_field(name="Discriminator:", value=member.discriminator, inline=False)
    e1.add_field(name="ID:", value=member.id, inline=False)
    e1.add_field(name="Top Roles:", value=member.top_role, inline=False)
    e1.add_field(name="Status:", value=member.status, inline=False)
    e1.add_field(name="Bot User?", value=member.bot, inline=False)
    e1.add_field(name="Creation Date:", value=member.created_at.__format__("%A, %d, %B %Y @ %H:%M:%S"), inline=False)

    await ctx.send(embed=e1)

client.run("TOKEN")