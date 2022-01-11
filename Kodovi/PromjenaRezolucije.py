import numpy as np
import cv2
import moviepy.editor as mp

cap = cv2.VideoCapture('video.mp4')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  cap.get(cv2.CAP_PROP_FPS)
print('Širina: ',width)
print('Visina: ',height)
print('Fps: ',fps)

cap = mp.VideoFileClip("video.mp4")
cap1=cap.resize((100,100))
cap1.write_videofile("movie_resized.mp4")

print(cap1.size)

cap.release()
cv2.destroyAllWindows()
