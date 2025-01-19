import nextcord
from nextcord import Interaction 
from nextcord.ext import commands
import os  

import mysql.connector

def connect():
    connection = mysql.connector.connect( 
    host = "host",        
    user = "user",
    password = "password",
    database = "database_name",
)
    if connection.is_connected():
        print('connected to my sql')
        return connection


def update(player, deaths, kills):
        connection = connect()
        cursor = connection.cursor()
        query = f"INSERT INTO gtcc(player,deaths,kills) VALUES (%s,%s,%s)"
        cursor.execute(query,(player, deaths, kills))
        connection.commit()
    
class player():
    def __init__(self,name:str):
        self.name = name
        self.total_deaths = []
        self.total_kills = []

    def kills(self):
        connection = connect()
        cursor = connection.cursor()
        column = "player"
        value = self.name
        query = f"SELECT kills FROM gtcc WHERE {column} = %s"
        cursor.execute(query,(value,))
        kills = cursor.fetchall()
        self.total_kills.extend([kill[0] for kill in kills])

    def deaths(self):
        connection = connect()
        cursor = connection.cursor()
        column = "player"
        value = self.name
        query = f"SELECT deaths FROM gtcc WHERE {column} = %s"
        cursor.execute(query,(value,))
        deaths = cursor.fetchall()
        self.total_deaths.extend([death[0] for death in deaths])   ## Because fetchall returns tuple. I have to flatten the tupple and add it to the total_deaths list.
    
    def k_d(self):
        x = sum(self.total_deaths)
        y = sum(self.total_kills)

        if x == 0:
            return ('goated no deaths')
        
        k_d = y/x 
        return k_d

testServerID = ##testserver##

class killss(commands.Cog):
    def __init__(self,client):
        self.client = client

    @nextcord.slash_command(guild_ids=[testServerID], description="updates stats in files", name="update_stats")
    async def update_stats(self, interaction: nextcord.Interaction, player: str, deaths: int, kills: int):
        update(player, deaths, kills)
        await interaction.response.send_message (f"Successfully updated deaths for player: {player} with {deaths} deaths and kills: '{kills}'.")
    
    @nextcord.slash_command(guild_ids=[testServerID], description="when it says 'msg' add your gamertag make sure no typos or wont work", name="kd")
    async def s_kd(self, interaction: nextcord.Interaction, msg:str):
        players = player(msg)
        players.kills()
        players.deaths()
        results = players.k_d()
        await interaction.response.send_message (f"your k/d is {results:.2f}")





def setup(client):
    client.add_cog(killss(client))
