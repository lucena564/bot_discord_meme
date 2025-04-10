import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Enviando mensagem de teste para o canal específico.

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("🚀 Bot funcionando!")
    await client.close()


# # Verificando as pastas do servidor.

# @client.event
# async def on_ready():
#     print(f"✅ Logado como {client.user}")
#     for guild in client.guilds:
#         print(f"\n📁 Servidor: {guild.name}")
#         for channel in guild.text_channels:
#             print(f"➡️  Canal: {channel.name} (ID: {channel.id})")
#     await client.close()

client.run(TOKEN)