import cv2
import os
from PIL import Image
import numpy as np
import glob


cam1 = cv2.VideoCapture("v1.mp4")
cam2 = cv2.VideoCapture("v2.mp4")
try:
    if not os.path.exists('data1'):
        os.makedirs('data1')
    if not os.path.exists('data2'):
        os.makedirs('data2')
    if not os.path.exists('data3'):
        os.makedirs('data3')
  
except OSError:
    print ('Error: Creating directory of data')
"""
currentframe = 0

while(True):
      
    ret1,frame1 = cam1.read()
    ret2,frame2 = cam2.read()
  
    if ret1 & ret2:
        name1 = './data1/frame' + str(currentframe) + '.png'
        cv2.imwrite(name1,frame1)
                
        name2 = './data2/frame' + str(currentframe) + '.png'
        cv2.imwrite(name2,frame2)
        currentframe += 1
    else:
        break
"""
total = int(cam1.get(cv2.CAP_PROP_FRAME_COUNT))
print(total)
img=[]
stupci, retci = (500,282)

for x in range (0,58):
               
        slika_1 = Image.open('./data1/frame' + str(x) + '.png')

        slika_2 = Image.open('./data2/frame' + str(x) + '.png')

        stupci, retci = slika_1.size
        
        matrica_sa_pikselima_1 = slika_1.load()
        matrica_sa_pikselima_2 = slika_2.load()
     
        for i in range (0, stupci):
            for j in range (0, retci):
                    r = matrica_sa_pikselima_1[i,j][0]
                    g = matrica_sa_pikselima_1[i,j][1]
                    b = matrica_sa_pikselima_1[i,j][2]
                    r_binary = format(r, '#010b').replace("0b", "")
                    g_binary = format(g, '#010b').replace("0b", "")
                    b_binary = format(b, '#010b').replace("0b", "")
                    
                    r2 = matrica_sa_pikselima_2[i,j][0]
                    g2 = matrica_sa_pikselima_2[i,j][1]
                    b2 = matrica_sa_pikselima_2[i,j][2]
                    
                    r_binary2 = format(r2, '#010b').replace("0b", "")
                    g_binary2 = format(g2, '#010b').replace("0b", "")
                    b_binary2 = format(b2, '#010b').replace("0b", "")
                    
                    novi_r_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                    novi_r_binary[0] = int(r_binary[0])
                    novi_r_binary[1] = int(r_binary[1])
                    novi_r_binary[2] = int(r_binary[2])
                    novi_r_binary[3] = int(r_binary[3])
                    novi_r_binary[4] = int(r_binary2[0])
                    novi_r_binary[5] = int(r_binary2[1])
                    novi_r_binary[6] = int(r_binary2[2])
                    novi_r_binary[7] = int(r_binary2[3])
                           
                    novi_r_int = int("".join(map(str, novi_r_binary)),2)
                    
                    novi_g_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                    novi_g_binary[0] = int(g_binary[0])
                    novi_g_binary[1] = int(g_binary[1])
                    novi_g_binary[2] = int(g_binary[2])
                    novi_g_binary[3] = int(g_binary[3])
                    novi_g_binary[4] = int(g_binary2[0])
                    novi_g_binary[5] = int(g_binary2[1])
                    novi_g_binary[6] = int(g_binary2[2])
                    novi_g_binary[7] = int(g_binary2[3])
                  
                    novi_g_int = int("".join(map(str, novi_g_binary)),2)

                    novi_b_binary = [0, 0, 0, 0, 0, 0, 0, 0]
                    novi_b_binary[0] = int(b_binary[0])
                    novi_b_binary[1] = int(b_binary[1])
                    novi_b_binary[2] = int(b_binary[2])
                    novi_b_binary[3] = int(b_binary[3])
                    novi_b_binary[4] = int(b_binary2[0])
                    novi_b_binary[5] = int(b_binary2[1])
                    novi_b_binary[6] = int(b_binary2[2])
                    novi_b_binary[7] = int(b_binary2[3])
                    
                    novi_b_int = int("".join(map(str, novi_b_binary)),2)
                    matrica_sa_pikselima_1[i,j] = (novi_r_int, novi_g_int, novi_b_int)
                    
        print(x)
      
        if (x<=9):
            slika_1.save('./data3/frame' + '00'+str(x) + '.png')
        elif(x>=10 & x<=99):
            slika_1.save('./data3/frame' + '0'+str(x) + '.png')
        
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

pathIn= './data3/'
pathOut = 'video1.avi'
fps = 30.0
convert_frames_to_video(pathIn, pathOut, fps)




