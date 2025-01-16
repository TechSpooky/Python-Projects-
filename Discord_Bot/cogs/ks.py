import nextcord
from nextcord import Interaction 
from nextcord.ext import commands
import os

testServerID = 1203996727728807996


class ks(commands.Cog):
    def __init__(self,client):
        self.client = client
    @nextcord.slash_command(guild_ids=[testServerID], description="All scrim matches", name="scrim_record")
    async def scrim_record(self, interaction: Interaction):
        with open("scrim.txt", "r") as file:
            stats = []
            for line in file:
                stats.append(str(line.strip()))
            formatted_stats = '\n'.join(stats)
            await interaction.response.send_message(f'```\n{formatted_stats}\n```')
    
    @nextcord.slash_command(guild_ids=[testServerID], description="All matches", name="gtccs_schedule")
    async def gtccs_schedule(self, interaction: Interaction):
        with open("gtccs_schedule.md", "r") as file:
            stats = []
            for line in file:
                stats.append(str(line.strip()))
            formatted_stats = '\n'.join(stats)
            await interaction.response.send_message(f'{formatted_stats}')


                


def setup(client):
    client.add_cog(ks(client))


