import asyncio
import json
import time
import traceback
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform
system("title "+ "Discord Sniper")

init()
data = {}

with open('token.json') as f:
    data = json.load(f)
token = data['token']

os = platform.system()

if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(Fore.RED + """\
▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄      ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░
   ░     ░        ░  ░ ░          ░ ░     ░        ░             ░           ░  ░              ░  ░   ░
 ░                   ░                           ░
 """ + Fore.RESET)

bot = commands.Bot(command_prefix=".", self_bot=True)
ready = False

codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")

while 1:
    try:
        @bot.event
        async def on_message(ctx):
            global ready
            if not ready:
                print(Fore.LIGHTCYAN_EX + 'Sniping de Codes Discord Nitro et de Giveaways sur ' + str(
                    len(bot.guilds)) + ' Serveurs\n' + Fore.RESET)
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print("[+] Le bot est prêt, connecté en tant que " + str(bot.user.name))
                ready = True
            if codeRegex.search(ctx.content):
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                code = codeRegex.search(ctx.content).group(2)

                start_time = time.time()
                if len(code) < 16:
                    try:
                        print(
                            Fore.LIGHTRED_EX + "[=] Détection automatique d'un faux code: " + code + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                    except:
                        print(
                            Fore.LIGHTRED_EX + "[=] Détection automatique d'un faux code: " + code + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.RESET)

                else:
                    async with httpx.AsyncClient() as client:
                        result = await client.post(
                            'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                            json={'channel_id': str(ctx.channel.id)},
                            headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                        delay = (time.time() - start_time)
                        try:
                            print(
                                Fore.LIGHTGREEN_EX + "[-] Code Snipé: " + Fore.LIGHTRED_EX + code + Fore.RESET + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                        except:
                            print(
                                Fore.LIGHTGREEN_EX + "[-] Code Snipé: " + Fore.LIGHTRED_EX + code + Fore.RESET + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.RESET)

                    if 'This gift has been redeemed already' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTYELLOW_EX + "[-] Le code a déjà été utilisé" + Fore.RESET,
                              end='')
                    elif 'nitro' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.GREEN + "[+] Code appliqué" + Fore.RESET, end='')
                    elif 'Unknown Gift Code' in str(result.content):
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTRED_EX + "[-] Code invalide" + Fore.RESET, end=' ')
                    print(" Délai:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)
            elif (('**giveaway**' in str(ctx.content).lower() or ('react with' in str(
                    ctx.content).lower() and 'giveaway' in str(ctx.content).lower()))):
                try:
                    await asyncio.sleep(randint(100, 200))
                    await ctx.add_reaction("🎉")
                    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                    print(
                        Fore.LIGHTYELLOW_EX + "[-] Nouveau Giveaway " + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                except:
                    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                    print(
                        Fore.LIGHTYELLOW_EX + "[x] Impossible de participer au Giveaway " + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
            elif '<@' + str(bot.user.id) + '>' in ctx.content and (
                    'giveaway' in str(ctx.content).lower() or 'won' in ctx.content or 'winner' in str(
                ctx.content).lower()):
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                try:
                    won = re.search("You won the \*\*(.*)\*\*", ctx.content).group(1)
                except:
                    won = "UNKNOWN"
                print(
                    Fore.GREEN + "[🎉] Félicitations ! Vous avez gagné un Giveaway:: " + Fore.LIGHTCYAN_EX + won + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)


        bot.run(token, bot=False)
    except:
        file = open("traceback.txt", "w")
        file.write(traceback.format_exc())
        file.close()
        exit(0)
