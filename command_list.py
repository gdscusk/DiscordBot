import discord
from discord.ext import commands
from decouple import config

# get channel id from .env
Ch_rules = config('Ch_rules')
Ch_announcement = config('Ch_announcement')
Ch_event = config('Ch_event')
Ch_chat = config('Ch_chat')

# general commands


class general(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    # command to check bot status
    async def status(self, ctx):
        await ctx.send("Bot status is online")

    @commands.command(pass_context=True)
    # command to send message to specific channel
    async def msg(self, ctx, *, message=None):
        img = ""

        # check if message is empty
        if message is None:
            await ctx.send("Please enter a message")
        else:
            # asking for attachment
            await ctx.send("Do you want to add an attachment? (y/n)")
            input = await self.client.wait_for('message')
            if input.content == "y":
                await ctx.send("Upload an image")
                img = await self.client.wait_for('message')
                img = img.attachments[0].url
            elif input.content == "n":
                pass
            else:
                await ctx.send("Invalid input")
            await ctx.send("which type of message do you want to send? (number)")
            await ctx.send("1. Event")
            await ctx.send("2. Announcement")
            await ctx.send("3. Rules")
            await ctx.send("4. Announcement only")
            input = await self.client.wait_for('message')

            # check input
            if input.content == "1":
                channel1 = self.client.get_channel(int(Ch_announcement))
                channel2 = self.client.get_channel(int(Ch_event))
                channel3 = self.client.get_channel(int(Ch_chat))
                await channel1.send(message)
                await channel2.send(message)
                await channel3.send(message)
                if img != "":
                    await channel1.send(img)
                    await channel2.send(img)
                    await channel3.send(img)
                await ctx.send("Message sent")
            elif input.content == "2":
                channel1 = self.client.get_channel(int(Ch_announcement))
                channel2 = self.client.get_channel(int(Ch_chat))
                await channel1.send(message)
                await channel2.send(message)
                if img != "":
                    await channel1.send(img)
                    await channel2.send(img)
                await ctx.send("Message sent")
            elif input.content == "3":
                channel1 = self.client.get_channel(int(Ch_rules))
                await channel1.send(message)
                if img != "":
                    await channel1.send(img)
                await ctx.send("Message sent")
            elif input.content == "4":
                channel1 = self.client.get_channel(int(Ch_announcement))
                await channel1.send(message)
                if img != "":
                    await channel1.send(img)
                await ctx.send("Message sent")
            else:
                await ctx.send("Invalid input")
