import cv2
import os

#Otvori video
video= cv2.VideoCapture('C:/Users/Mawijeta/AppData/Local/Programs/Python/Python39-32/vide.mp4')
i=0

#Provjeri postoji li file za spremanje okvira
try:
    if not os.path.exists('okviri'):
        os.makedirs('okviri')
except OSError:
    print ('Error: Creating directory of data')
    
currentframe = 0
while(True):
    ret1,frame1 = video.read()
    if ret1:
        name1 = './okviri/okvir' + str(currentframe) + '.png'
        cv2.imwrite(name1,frame1)
        currentframe += 1
    else:
        break
    
video.release()
cv2.destroyAllWindows()
