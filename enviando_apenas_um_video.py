import discord
import os
import asyncio
import aiohttp
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
VIDEO_URL = os.getenv("VIDEO_S3_MEME") # Pegar no bucket da aws

intents = discord.Intents.default()
client = discord.Client(intents=intents)

already_ran = False  # impede reexecução no mesmo ambiente

@client.event
async def on_ready():
    global already_ran
    if already_ran:
        return
    already_ran = True

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        async with aiohttp.ClientSession() as session:
            async with session.get(VIDEO_URL) as resp:
                if resp.status == 200:
                    video_bytes = BytesIO(await resp.read())
                    await channel.send(file=discord.File(video_bytes, filename="video.mp4"))

    await client.close()

def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(client.start(TOKEN))
