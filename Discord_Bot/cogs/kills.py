import nextcord
from nextcord import Interaction 
from nextcord.ext import commands
import os

testServerID = 1203996727728807996

class kills(commands.Cog):
    def __init__(self,client):
        self.client = client
    @nextcord.slash_command(guild_ids=[testServerID], description = "updates kills in files",name = "update_spookys_kills" )
    async def update_spookys_kills (self, interaction: nextcord.Interaction, message: str):
        with open("kills.txt", 'a') as file:
            file.write (message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')

    @nextcord.slash_command(guild_ids=[testServerID], description="Updates your deaths", name="update_spookys_deaths")
    async def update_spookys_deaths(self, interaction: Interaction, message: str):
        with open("deaths.txt", 'a') as file:
            file.write(message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')
    @nextcord.slash_command(guild_ids=[testServerID], description="spookys kd", name="spookys_kd")
    async def spookys_kd(self, interaction: Interaction):
        with open("kills.txt", "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line.strip()))
        total = sum(numbers)

        with open("deaths.txt", "r") as file:
            numberz = []
            for line in file:
                 numberz.append(int(line.strip()))
        Deaths = sum(numberz)
        kd = total/Deaths
        await interaction.response.send_message(f'Your kd is {kd:.2f}!')
    @nextcord.slash_command(guild_ids=[testServerID], description = "updates kills in files",name = "update_sprafty_kills" )
    async def update_sprafty_kills (self, interaction: nextcord.Interaction, message: str):
        with open("skills.txt", 'a') as file:
            file.write (message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')

    @nextcord.slash_command(guild_ids=[testServerID], description="Updates your deaths", name="update_sprafty_deaths")
    async def update_sprafty_deaths(self, interaction: Interaction, message: str):
        with open("sdeaths.txt", 'a') as file:
            file.write(message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')
    @nextcord.slash_command(guild_ids=[testServerID], description="spraftys kd", name="spraftys_kd")
    async def spraftys_kd(self, interaction: Interaction):
        with open("skills.txt", "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line.strip()))
        total = sum(numbers)  # Moved outside the loop

        with open("sdeaths.txt", "r") as file:
            numberz = []
            for line in file:
                numberz.append(int(line.strip()))
        Deaths = sum(numberz)  # Moved outside the loop

        kd = total / Deaths

        await interaction.response.send_message(f'Your kd is {kd:.2f}!')

    @nextcord.slash_command(guild_ids=[testServerID], description = "updates kills in files",name = "update_wockys_kills" )
    async def update_wockys_kills (self, interaction: nextcord.Interaction, message: str):
        with open("wkills.txt", 'a') as file:
            file.write (message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')

    @nextcord.slash_command(guild_ids=[testServerID], description="Updates your deaths", name="update_wockys_deaths")
    async def update_wockys_deaths(self, interaction: Interaction, message: str):
        with open("wdeaths.txt", 'a') as file:
            file.write(message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')
    @nextcord.slash_command(guild_ids=[testServerID], description="wockyss kd", name="wockys_kd")
    async def wockys_kd(self, interaction: Interaction):
        with open("wkills.txt", "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line.strip()))
                total = sum(numbers)

        with open("wdeaths.txt", "r") as file:
            numberz = []
            for line in file:
                 numberz.append(int(line.strip()))
                 Deaths = sum(numberz)
                 kd = total/Deaths
                 await interaction.response.send_message(f'Your kd is {kd:.2f}!')
    
    @nextcord.slash_command(guild_ids=[testServerID], description = "updates kills in files",name = "update_milkyduds_kills" )
    async def update_milkyduds_kills (self, interaction: nextcord.Interaction, message: str):
        with open("mkills.txt", 'a') as file:
            file.write (message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')

    @nextcord.slash_command(guild_ids=[testServerID], description="Updates your deaths", name="update_milkyduds_deaths")
    async def update_milkyduds_deaths(self, interaction: Interaction, message: str):
        with open("mdeaths.txt", 'a') as file:
            file.write(message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')
    @nextcord.slash_command(guild_ids=[testServerID], description="milkyduds kd", name="milkyduds_kd")
    async def milkyduds_kd(self, interaction: Interaction):
        with open("mkills.txt", "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line.strip()))
        total = sum(numbers)

        with open("mdeaths.txt", "r") as file:
            numberz = []
            for line in file:
                 numberz.append(int(line.strip()))
                 Deaths = sum(numberz)
        kd = total/Deaths
        await interaction.response.send_message(f'Your kd is {kd:.2f}!')

    @nextcord.slash_command(guild_ids=[testServerID], description = "updates kills in files",name = "update_perkys_kills" )
    async def update_perky_kills (self, interaction: nextcord.Interaction, message: str):
        with open("pkills.txt", 'a') as file:
            file.write (message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')

    @nextcord.slash_command(guild_ids=[testServerID], description="Updates your deaths", name="update_perkys_deaths")
    async def update_perky_deaths(self, interaction: Interaction, message: str):
        with open("pdeaths.txt", 'a') as file:
            file.write(message + "\n")
            await interaction.response.send_message(f'Your message has been stored!')
    @nextcord.slash_command(guild_ids=[testServerID], description="perkys kd", name="perkys_kd")
    async def perky_kd(self, interaction: Interaction):
        with open("pkills.txt", "r") as file:
            numbers = []
            for line in file:
                numbers.append(int(line.strip()))
        total = sum(numbers)

        with open("pdeaths.txt", "r") as file:
            numberz = []
            for line in file:
                 numberz.append(int(line.strip()))

        Deaths = sum(numberz)
        kd = total/Deaths
        
        await interaction.response.send_message(f'Your kd is {kd:.2f}!')


def setup(client):
    client.add_cog(kills(client))