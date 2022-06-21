import cv2
from time import sleep as d
def snap(numero_foto,nomefile):
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