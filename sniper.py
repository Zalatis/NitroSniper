import asyncio
import json
import time
import traceback
from os import system
from random import randint
from discord.ext import commands
import re, requests
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
            if ('**giveaway**' in str(ctx.content).lower() or ('react with' in str(
                    ctx.content).lower() and 'giveaway' in str(ctx.content).lower())):
                #emote = "🎉"
                #try:
                #    emote = re.search("React with (.*) ", ctx.content).group(1)
                #except:
                #    emote = "🎉"
                try:
                    #try:
                    #    toJoin = re.search("https://discord.gg/(.*) ", ctx.content).group(1)
                    #    r = requests
                    #    r.post('https://discordapp.com/api/v6/invites/invitecode' + toJoin,
                    #           json={"channel_id": str(ctx.channel.id)}, headers={'authorization': token}).text()
                    #except:
                    #    pass
                    await asyncio.sleep(randint(10, 20))
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
                    Fore.GREEN + "[🎉] Félicitations ! Vous avez gagné un cadeau: " + Fore.LIGHTCYAN_EX + won + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
            elif 'discordapp.com/gifts/' in ctx.content or 'discord.gift/' in ctx.content:
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                try:
                    code = re.search("discordapp.com/gifts/([a-zA-Z0-9_]+)", ctx.content).group(1)
                except:
                    code = re.search("discord.gift/([a-zA-Z0-9]+)", ctx.content).group(1)
                start_time = time.time()
                if len(code) != 16:
                    print(
                        Fore.LIGHTRED_EX + "[=] Détection automatique d'un faux code: " + code + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                else:
                    r = requests
                    result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                                    json={"channel_id": str(ctx.channel.id)}, headers={'authorization': token}).text
                    delay = (time.time() - start_time)
                    print(
                        Fore.LIGHTGREEN_EX + "[-] Code Snipé: " + Fore.LIGHTRED_EX + code + Fore.RESET + " De " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                    if 'This gift has been redeemed already.' in result:
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTYELLOW_EX + "[-] Le code a déjà été utilisé" + Fore.RESET,
                              end='')
                    elif 'nitro' in result:
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.GREEN + "[+] Code appliqué" + Fore.RESET, end='')
                    elif 'Unknown Gift Code' in result:
                        print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                        print(Fore.LIGHTRED_EX + "[-] Code invalide" + Fore.RESET, end=' ')
                    print(" Délai:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)


        bot.run(token, bot=False)
    except:
        file = open("traceback.txt", "w")
        file.write(traceback.format_exc())
        file.close()
        exit(0)
