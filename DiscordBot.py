import discord


class DiscordBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        channel = self.get_channel(89017811220844544)
        with open('gif_test.gif', 'rb') as fp:
            await channel.send(file=discord.File(fp, 'test.gif'))
