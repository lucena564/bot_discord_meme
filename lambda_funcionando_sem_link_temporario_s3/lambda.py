import discord
import os
import asyncio
import aiohttp
import boto3
from io import BytesIO
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
S3_KEY = os.getenv("S3_OBJECT_KEY")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

already_ran = False

def generate_presigned_url(bucket, key, expiration=3600):
    s3_client = boto3.client("s3")
    return s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": key},
        ExpiresIn=expiration
    )

import sys

@client.event
async def on_ready():
    global already_ran
    if already_ran:
        return
    already_ran = True

    presigned_url = generate_presigned_url(S3_BUCKET, S3_KEY)

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        async with aiohttp.ClientSession() as session:
            async with session.get(presigned_url) as resp:
                if resp.status == 200:
                    video_bytes = BytesIO(await resp.read())
                    await channel.send(file=discord.File(video_bytes, filename="video.mp4"))

    await client.close()
    sys.exit(0)

def lambda_handler(event, context):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.run_until_complete(client.start(TOKEN))
    except Exception as e:
        logging.error(f"Erro na Lambda: {e}", exc_info=True)
        return {"statusCode": 500, "body": str(e)}