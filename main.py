import discord
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def get_video_path():
    video_dir = "videos"
    for filename in os.listdir(video_dir):
        if filename.endswith(".mp4"):
            return os.path.join(video_dir, filename)
    return None

@client.event
async def on_ready():
    print(f"✅ Logado como {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        video_path = get_video_path()
        if video_path:
            await channel.send("", file=discord.File(video_path))
            print("✅ Vídeo enviado com sucesso.")
        else:
            print("❌ Nenhum vídeo .mp4 encontrado na pasta 'videos'")
    else:
        print("❌ Canal não encontrado.")
    await client.close()

client.run(TOKEN)
