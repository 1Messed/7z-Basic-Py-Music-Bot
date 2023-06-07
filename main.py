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

# Command: Skip the currently playing song
@bot.command()
async def skip(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Skipping the current song.")
    else:
        await ctx.send("I'm not currently playing anything.")

# Function to get the bot prefix based on the server
def get_prefix(bot, message):
    # You can modify this function to implement custom prefix logic (e.g., database lookup)
    return commands.when_mentioned_or(default_prefix)(bot, message)

# Update the bot prefix dynamically
bot.command_prefix = get_prefix

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')
