# My Awesome Project
This is a discord bot that I made using the nextcord module. The bot was made to hold stats of my schools Esports team. Stats include K/D of each player on the team , W/L, and the GTCC schedule. 

## How It's Made:

**Tech used:** Python
The discord bot was made with the purpose of storing data into files and being able to pull out the same data and use it to calculate the stats of the team. The program primarily focuses on appending data and retrieving it. The program uses nextcords modules to really control the progam. The user is able to update the stats manually through the disocrd both and have it store into the file. Through commands on discord the bot is able to hold kills,Deaths,Wins and losses on the team. Its also aboe to show the schedule.


## Optimizations
Although the discord bot does get the job done. I feel as if takingadvantage of an sql server would let me store the data easier.

## Update
**Changes** kills.v2
"I went back into the program and added an SQL Server. Doing so made the program require less code and gave it more flexibility. Previously, the program would need new commands to update each player's stats, and if I wanted to add a new player, I would have to create another command. Thankfully, the SQL Server makes everything easier. I am now able to add as many stats as I want, including new players, without being limited to the number of commands I have. The new code is more efficient and easier to work with. Everything is still accessed using the Discord bot.






