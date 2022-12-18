import settings
import discord
from discord.ext import commands


logger = settings.logging.getLogger("bot")

def run():

    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user} Id:{bot.user.id}")

        print("------------------")
    

    bot.run(settings.DISCORD_API_SECRETKEY, root_logger=True)


if __name__ == "__main__":
    run()