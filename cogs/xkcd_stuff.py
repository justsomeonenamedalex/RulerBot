import discord
from discord.ext import commands
import requests
import random


def xkcd_embed(data: dict) -> discord.Embed:
    e = discord.Embed()
    e.title = data["safe_title"]
    e.description = data["alt"]
    e.set_image(url=data["img"])
    e.set_footer(text=f"xkcd-{data['num']}")
    return e


class XkcdStuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog <XkcdStuff.py> is online.")

    @commands.command()
    async def xkcd(self, ctx, number: int = None):
        if not number:
            current_number = requests.get("https://xkcd.com/info.0.json").json()["num"]
            number = random.randint(1, current_number)
        url = f"http://xkcd.com/{number}/info.0.json"
        response = requests.get(url)
        if response:
            data = response.json()

        embed = xkcd_embed(data)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(XkcdStuff(client))
