from PIL import Image
import cv2
import os
#Otvori video
video= cv2.VideoCapture('C:/Users/Mawijeta/AppData/Local/Programs/Python/Python39-32/vide.mp4')
i=0
frame=5
while(True):
    ret1,frame1 = video.read()
    if ret1:
        name1 = './thumbnail' + str(frame) + '.png'
        cv2.imwrite(name1,frame1)
    else:
        break
    
image = Image.open(r'C:\Users\Mawijeta\AppData\Local\Programs\Python\Python39-32\thumbnail' + str(frame) + '.png')
MAX_SIZE = (100, 100)
image.thumbnail(MAX_SIZE)

image.save('pythonthumb.png')
image.show()
video.release()
cv2.destroyAllWindows()

