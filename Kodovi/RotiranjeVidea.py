import numpy as np
import cv2
import moviepy.editor as mp

cap = mp.VideoFileClip("video.mp4")
cap2 = cap.add_mask().rotate(72)
cap2.write_videofile("movie_rotated.mp4")

cap.release()
cv2.destroyAllWindows()
