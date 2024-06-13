import discord

intents = discord.Intents.default()
intents.message_content = True

leo = discord.Client(intents=intents)

# config
token = 'YourToken'
# config end

@leo.event
async def on_ready():
    print('We are logged in as: ' + str(leo.user))

leo.run(token)
