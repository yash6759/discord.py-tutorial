import discord
import asyncio
from discord.ext import commands

client = commands.Bot(description="MultiVerse Official Bot", command_prefix="mv!", pm_help = True)
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started BOT')
    
    
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '<welcome channel name here>':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check <#491281610503618561> and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.add_field(name='Your join position is', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)
    
client.run('Token')