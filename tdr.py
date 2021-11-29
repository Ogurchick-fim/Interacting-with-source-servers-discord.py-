import  discord
from discord.flags import Intents
from discord_components import DiscordComponents, Button, ButtonStyle 
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get 
from steam import game_servers as gs

import valve.source
import valve.source.a2s
import valve.source.master_server

from socket import *
from socket import socket

import asyncio

import datetime

from asyncio import sleep
import asyncio

from discord.utils import get
import json

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

db = DiscordComponents(  client)
@client.event

async def on_ready():
    DiscordComponents(client)
    print('online')

with open("C:\\Users\\DO YOU LIKE BESHBAR\Desktop\\tdr  bot\\monitorning\\info.json", "r") as json_info:
    a = json.load(json_info)

@client.command( pass_context = True)

async def infoq(ctx, *,  amount = 1):
    with open("C:\\Users\\DO YOU LIKE BESHBAR\Desktop\\tdr  bot\\monitorning\\info.json", "r") as json_info:
        a = json.load(json_info)
    
    SERVER_ADDRESS = (a["SERVER_ADDRESS"],a["port"])
    def infogame():
        SERVER_ADDRESS = (a["SERVER_ADDRESS"],a["port"])
        try:
            with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
                return server.info()
        except:
            return None
    info = infogame()

    if info is None :
        embed = discord.Embed(name = 'Статус',description =  ' 🔴 **ofline**', color=0xff1f1f)
        
        msga = await ctx.send(embed = embed)
        
    else:
        
        embed = discord.Embed(title = '  {server_name}'.format(**info), color=0x007bff)
        embed.add_field(name = 'Статус',value =  ' 🟢 **online**')
        embed.add_field(name = ':man_frowning: Заполненость сервера:',value = ' {player_count}/{max_players}'.format(**info))
        embed.add_field(name = 'Тип игры',value =  '{folder}'.format(**info))
        embed.add_field(name = ':map: Карта',value = '{map}'.format(**info))
        ser = f'{a["SERVER_ADDRESS"]}:{a["port"]}'
        embed.add_field(name = "IP сервера",value =  f" **{ser}**")
        embed.add_field(name = "Подключения",value =  f"steam://connect/{ser}",inline=False)
        
      
        with open("C:\\Users\\DO YOU LIKE BESHBAR\Desktop\\tdr  bot\\monitorning\\info.json", "r") as json_info:
            a = json.load(json_info)
        #=======================================
        
        with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
            players =  server.players() 
        playerNames=[]
        playerTime=[]
        for player in players["players"]:
            playerNames.append(player["name"])
            playerduration = player["duration"]
            time = round(round(playerduration))
            time1 = str(datetime.timedelta(seconds=time)) 
            playerTime.append(time1)
        while '' in playerNames:
            idex = playerNames.index('')
            del playerNames[idex]
            del playerTime[idex]
        n1 = len(playerNames)
        if (len(playerNames)) == 0:
            None
        else:
            if (len(playerNames)) > 25:
                while len(playerNames) > 20:
                    del playerTime[-1]
                    del playerNames[-1]
                n2 = len(playerNames)
                playerss = '        \n'.join(playerNames)
                timer = '        \n'.join(playerTime)
                n3 = n1 - n2
                embed.add_field(name='Игроки',value=f'''```{playerss} \nещё {n3} людей```''',inline=True)
                embed.add_field(name='Время',value=f'''```{timer} \n...```''',inline=True)
                
            else:
                playerss = '        \n'.join(playerNames)
                timer = '        \n'.join(playerTime)
                embed.add_field(name='Игроки',value=f'''```{playerss}```''',inline=True)
                embed.add_field(name='Время',value=f'''```{timer}```''',inline=True)
            #========================================
            
            msg = await ctx.send(embed = embed)
        await asyncio.sleep(10)
        
    @tasks.loop(seconds=10)
    async def update():
        while True:
            
            with open("C:\\Users\\DO YOU LIKE BESHBAR\Desktop\\tdr  bot\\monitorning\\info.json", "r") as json_info:
                a = json.load(json_info)
            def infogame():
                
                SERVER_ADDRESS = (a["SERVER_ADDRESS"],a["port"])
                try:
                    with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
                        return server.info()
                except :
                    return None
            info = infogame()
            def infoping():
                SERVER_ADDRESS = (a["SERVER_ADDRESS"],a["port"])
                
                try:
                    return gs.a2s_info(SERVER_ADDRESS)
                except:
                    return None
            ping = infoping()    
            
            if info is None :
                umbeda = discord.Embed(name = 'Статус',description =  ' 🔴 **ofline**', color=0xff1f1f)
                await msga.edit(embed = umbeda)
                await asyncio.sleep(10) 

            else:
            
                uembed = discord.Embed(title = '  {server_name}'.format(**info), color=0x007bff)
                uembed.add_field(name = 'Статус',value =  ' 🟢 **online**')
                uembed.add_field(name = ':man_frowning: Заполненость сервера:',value = ' {player_count}/{max_players}'.format(**info))
                uembed.add_field(name = 'Тип игры',value =  '{folder}'.format(**info))
                uembed.add_field(name = ':map: Карта',value = '{map}'.format(**info))
                ser = ser = f'{a["SERVER_ADDRESS"]}:{a["port"]}'
                uembed.add_field(name = "IP сервера",value =  f"**{ser}**")
                uembed.add_field(name = "Подключения",value =  f"steam://connect/{ser}",inline=False)
                
                
                   
                with open("C:\\Users\\DO YOU LIKE BESHBAR\Desktop\\tdr  bot\\monitorning\\info.json", "r") as json_info:
                    a = json.load(json_info)
                #=======================================
                
                with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
                    players =  server.players()
                playerNames=[]
                playerTime=[]
                for player in players["players"]:
                    playerNames.append(player["name"])
                    playerduration = player["duration"]
                    time = round(round(playerduration))
                    time1 = str(datetime.timedelta(seconds=time)) 
                    playerTime.append(time1)
                while '' in playerNames:
                    idex = playerNames.index('')
                    del playerNames[idex]
                    del playerTime[idex]
                n1 = len(playerNames)
                if (len(playerNames)) == 0:
                    None
                else:
                    if (len(playerNames)) > 25:
                        while len(playerNames) > 20:
                            del playerTime[-1]
                            del playerNames[-1]
                        n2 = len(playerNames)
                        playerss = '        \n'.join(playerNames)
                        timer = '        \n'.join(playerTime)
                        n3 = n1 - n2
                        uembed.add_field(name='Игроки',value=f'''```{playerss} \nещё {n3} людей```''',inline=True)
                        uembed.add_field(name='Время',value=f'''```{timer} \n...```''',inline=True)
                    else:
                        playerss = '        \n'.join(playerNames)
                        timer = '        \n'.join(playerTime)
                        uembed.add_field(name='Игроки',value=f'''```{playerss}```''',inline=True)
                        uembed.add_field(name='Время',value=f'''```{timer}```''',inline=True)
                    #========================================
                
                    
                await asyncio.sleep(10)
                        
                await msg.edit(embed = uembed)
                await asyncio.sleep(10)   
    update.start() 
      
token = a["token"]

client.run(token)   