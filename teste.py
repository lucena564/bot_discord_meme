# import discord
# import os
# import asyncio
# import aiohttp
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv("DISCORD_TOKEN")
# CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# intents = discord.Intents.default()
# client = discord.Client(intents=intents)

VIDEO_URL = "https://trecodiscordmeme.s3.us-east-2.amazonaws.com/lul_video2.mp4?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLWVhc3QtMiJHMEUCIQCQnQY337EIXJruFlTD2Wq%2B79PDbvZALyKSph7lpd6MPwIgUCDA8wJ4BqgugHvIMHMVA8rEAbclK8X2XjTcrNSDY7oqwgMIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwyMzM2OTQ1MTY5NDEiDLXvtHl79Cgt2n2WJiqWA8Zuv2749p7UvMUH1Vd6tyq91hm4aC2TKQmyV5FIT765sgeUzgC5SDYcezlgQY0k%2Fqgbze%2BnKaFybDkOCj%2BRkbpJrrnIL1TVHQJ%2BG9LGh%2BiLLly%2FOtlbLNGzVwA0hZGq2%2BZiWtzipDYdMVMouN%2FuunHAY38OuDMh%2FYcLDQqGQOJwB%2BGVwqRmYEkaD8m46GI%2BQ3rTXTCpz1vufIdbnWcKCgmpGW6ub%2FXH75gzbZDG1TkAOr4l1OXM5UUNY%2BslXv6VTtqp3xjMKMIpwj7XgaKzzRTdZ0%2Fvpo6P96nzV6RBfY%2FCca2A947xiGTl82vUKg%2FUnxAMqq87C%2BErqdmAX7Ao1ecx47Y0Qxl46kCqIe6YDIdzZ%2F0jrRi8%2BNrvzLVaiSMrLvVLnuABt%2BqRB81k7hFMBOYRUvgUzjwaz%2B825SE5%2FTHpYy8vGKfNRZ2ckd5wGb9rvtLqRO3OL3PU7W1%2F3hyRC3kIhmVROgOPBGS5pn0PeZBCmKbbmxb0pBIUp82mcqgNxxVsuQMY%2FHKn35aT37BpypswM0KIYKowl97fvwY63gIMt5jPC6VdS73g%2FTfyIcogS8X0kV7IZS24WQEk3W0EHEsPKfbK%2FkpiD5p1yi9LOkbc2jddHlJQTwjWFf%2FmZZsugB5DOyIhNjbYMgxnuRnovLpDb8K%2FD%2Bli643ZFwjH%2BN2gFzERg9oiX%2BpYQ8qDN8pkzOMPw9TqThDP04lZC8xkS9Cnvv3Q28qhXBcxuHOs87xV2DGjQrCD3iCKNaF6QNCPJ5DXve4x0TwPwURnhcsiJgEy%2FW%2FgWRvXV9ltCcw08MGcXWEuhLnSFvd2DAP%2B9Hobt%2FCJeCLSXl4Qumhy62W4q93ZlNXd0LpJKU2Wz81KOmZuaFBkpkbb9FLEXsop4XmD0tBc2QvTY0QhtaqM%2F%2BH%2B%2Bb%2B3EzgnvnXLsf9Th6gLg1nvEKsAWpuqoR0eZGfOaqm1m%2BmLTxfw2znL53GbpgUj6j4qjupH1pYvOV7jxRZgbpJ4KkS9f17ZCuNQIRhLRw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATM2KHK3GYMDPGRLM%2F20250410%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T171749Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=73d8780afaa168808fd9d1c152e05d1db476159513b7ccad38d8b765ebd2d253"

# @client.event
# async def on_ready():
#     print(f"✅ Logado como {client.user}")
#     channel = client.get_channel(CHANNEL_ID)
#     if channel:
#         # --------------------------------------------------------------------------------------------------------
#         # # Modo 1: Enviar só o link (Discord pode gerar preview dependendo do link)
#         # await channel.send(f"{VIDEO_URL}")
        
#         # # # Modo 2: Opcional, enviar um embed com o link como texto clicável
#         # embed = discord.Embed(
#         #     title="Vamooooooooos riiiiiir",
#         #     description=f"[Clique aqui para assistir]({VIDEO_URL})",
#         #     color=0x00ff00, 
#         # )

#         # embed.add_field(name="Link do vídeo", value=f"[Clique aqui para assistir]({VIDEO_URL})", inline=False)

#         # print("✅ Mensagem enviada com sucesso.")
#         # ---------------------------------------------------------------------------------------------------------

#         async with aiohttp.ClientSession() as session:
#             async with session.get(VIDEO_URL) as resp:
#                 if resp.status == 200:
#                     video_data = await resp.read()
#                     file = discord.File(fp=bytes(video_data), filename="lul_video.mp4")
#                     await channel.send(file=file)
#                     print("✅ Vídeo enviado com sucesso.")
#                 else:
#                     print(f"❌ Erro ao baixar vídeo: {resp.status}")
#     else:
#         print("❌ Canal não encontrado.")
    
#     await client.close()

# asyncio.run(client.start(TOKEN))

# # def lambda_handler(event, context):
# #     asyncio.run(client.start(TOKEN))


import discord
import os
import asyncio
import aiohttp
from io import BytesIO

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        async with aiohttp.ClientSession() as session:
            async with session.get(VIDEO_URL) as resp:
                if resp.status == 200:
                    video_bytes = BytesIO(await resp.read())
                    await channel.send(file=discord.File(video_bytes, filename="video.mp4"))
    await client.close()

asyncio.run(client.start(TOKEN))

# def lambda_handler(event, context)0:
#     asyncio.run(client.start(TOKEN))
