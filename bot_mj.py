# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjUxMzg3MTM0Njk1MDQ3MTg4.XeZKVg.9FmuAT2quXw14v7ocK1kx3GLuhU'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'mj_lv':
        await message.channel.send("<@!588392127919161357>" + '　mj大好き💚')
    elif message.content == 'mj_gm':
        await message.channel.send("<@!588392127919161357>" + '　mjおはよ️️️💚')
    elif message.content == 'mj_gt':
        await message.channel.send("<@!588392127919161357>" + '　mjないとれだよ💙')
    elif message.content == 'mj_ft':
        await message.channel.send("<@!588392127919161357>" + '　mj今日も頑張れ💛')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)