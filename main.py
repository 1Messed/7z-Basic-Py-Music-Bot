# Code Credits to - 1Messed
import discord
from discord.ext import commands

# Create a bot instance with a default prefix
default_prefix = '!'
bot = commands.Bot(command_prefix=default_prefix)

# Event: Bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Command: Set the bot prefix
@bot.command()
async def setprefix(ctx, prefix):
    global default_prefix
    default_prefix = prefix
    await ctx.send(f'Bot prefix set to: {prefix}')

# Command: Join a voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()

# Command: Leave the voice channel
@bot.command()
async def leave(ctx):
import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='-')

# Event: Bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Command: Join a voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()

# Command: Leave the voice channel
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Command: Play a song from a YouTube URL
@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_channel = await channel.connect()

    if not ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        source = await discord.FFmpegOpusAudio.from_probe(url)
        ctx.voice_client.play(source)
        await ctx.send(f'Now playing: {url}')
    else:
        await ctx.send("I'm already playing a song!")

# Command: Pause the currently playing song
@bot.command()
async def pause(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Song paused.")
    else:
        await ctx.send("I'm not currently playing anything.")

# Command: Resume the currently paused song
@bot.command()
async def resume(ctx):
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Song resumed.")
    else:
        await ctx.send("I'm not currently paused.")

# Command: Display the currently playing song
@bot.command()
async def nowplaying(ctx):
    if ctx.voice_client.is_playing():
        current_song = ctx.voice_client.source.title
        await ctx.send(f'Currently playing: {current_song}')
    else:
        await ctx.send("I'm not currently playing anything.")

# Command: Show available commands
@bot.command()
async def help(ctx):
    prefix = bot.command_prefix
    help_message = f'Available commands:\n\n' \
                   f'{prefix}join: Join a voice channel.\n' \
                   f'{prefix}leave: Leave the voice channel.\n' \
                   f'{prefix}play <url>: Play a song from a YouTube URL.\n' \
                   f'{prefix}pause: Pause the currently playing song.\n' \
                   f'{prefix}resume: Resume the currently paused song.\n' \
                   f'{prefix}nowplaying: Display the currently playing song.\n' \
                   f'{prefix}help: Show available commands.'
    await ctx.send(help_message)

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')
