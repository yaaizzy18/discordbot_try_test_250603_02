import discord
from discord.ext import commands
import os

# デバッグ用ログ
print("Starting bot...")
print(f"Environment variables: {dict(os.environ)}")
print(f"DISCORD_TOKEN found: {'DISCORD_TOKEN' in os.environ}")
print(f"Token value: {os.environ.get('DISCORD_TOKEN')}")

# .envファイルからトークンを読み込む
TOKEN = os.environ.get('DISCORD_TOKEN')

# ボットのインスタンスを作成
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Botとしてログインしました: {bot.user.name}')
    print(f'ID: {bot.user.id}')

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは！私はテスト用のDiscordボットです！')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# ボットを起動
bot.run(TOKEN)
