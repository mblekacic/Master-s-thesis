import cv2
import os
from PIL import Image
import numpy as np
import glob


cam1 = cv2.VideoCapture("video1.avi")

try:
    if not os.path.exists('data4'):
        os.makedirs('data4')
    if not os.path.exists('data5'):
        os.makedirs('data5')

except OSError:
    print ('Error: Creating directory of data')

currentframe = 1
while(True):
      
    ret1,frame1 = cam1.read()
  
    if ret1:
        name1 = './data4/frame' + str(currentframe) + '.png'
        cv2.imwrite(name1,frame1)
        currentframe += 1
    else:
        break


total = int(cam1.get(cv2.CAP_PROP_FRAME_COUNT))
img=[]
stupci, retci = (500,282)


for x in range (0,58):
        if(x<=9):
            slika_1 = Image.open('./data4/frame' +'00'+str(x) + '.png')
        else:
            slika_1 = Image.open('./data4/frame' +'0'+str(x) + '.png')
        stupci, retci = slika_1.size

        matrica_sa_pikselima_1 = slika_1.load()
 

        for i in range (0, stupci):
                for j in range (0, retci):
                        r = matrica_sa_pikselima_1[i,j][0]
                        g = matrica_sa_pikselima_1[i,j][1]
                        b = matrica_sa_pikselima_1[i,j][2]
                        
                        

                        r_binary = format(r, '#010b').replace("0b", "")
                        g_binary = format(g, '#010b').replace("0b", "")
                        b_binary = format(b, '#010b').replace("0b", "")
                        
                               
                        novi_r_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                        novi_r_binary[0] = int(r_binary[4])
                        novi_r_binary[1] = int(r_binary[5])
                        novi_r_binary[2] = int(r_binary[6])
                        novi_r_binary[3] = int(r_binary[7])
                                
                        
                        novi_r_int = int("".join(map(str, novi_r_binary)),2)
                       
                        novi_g_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                        novi_g_binary[0] = int(g_binary[4])
                        novi_g_binary[1] = int(g_binary[5])
                        novi_g_binary[2] = int(g_binary[6])
                        novi_g_binary[3] = int(g_binary[7])
                       
                        novi_g_int = int("".join(map(str, novi_g_binary)),2)
                       
                        novi_b_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                        novi_b_binary[0] = int(b_binary[4])
                        novi_b_binary[1] = int(b_binary[5])
                        novi_b_binary[2] = int(b_binary[6])
                        novi_b_binary[3] = int(b_binary[7])
                        
                      
                        novi_b_int = int("".join(map(str, novi_b_binary)),2)
                        matrica_sa_pikselima_1[i,j] = (novi_r_int, novi_g_int, novi_b_int)
                        
        print(x)
        if (x<=9):
            slika_1.save('./data5/frame' + '00'+str(x) + '.png')
        elif(x>=10 & x<=99):
            slika_1.save('./data5/frame' + '0'+str(x) + '.png')
        img.append(slika_1)
        
from os.path import isfile, join
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    # for sorting the file names properly
    files.sort(key = lambda x: x[5])
    files.sort()
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    
    for i in range(len(files)):
        filename=pathIn + files[i]
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
    
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

pathIn= './data5/'
pathOut = 'video2.avi'
fps = 30.0
convert_frames_to_video(pathIn, pathOut, fps)


