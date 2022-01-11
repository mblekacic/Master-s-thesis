import cv2
import numpy as np
def bgr(mirror=False):
    cap = cv2.VideoCapture('video.mp4')
    cv2.namedWindow('RGB',cv2.WINDOW_NORMAL)
    zeros = None
    while True:
        ret_val, frame = cap.read()
        if ret_val == True:
            if mirror:
                frame = cv2.flip(frame, 1)
            height, width, layers = frame.shape
            zeroImgMatrix = np.zeros((height, width), dtype="uint8")
            (B, G, R) = cv2.split(frame)
            
            B = cv2.merge([B, zeroImgMatrix, zeroImgMatrix])
            G = cv2.merge([zeroImgMatrix, G, zeroImgMatrix])
            R = cv2.merge([zeroImgMatrix, zeroImgMatrix, R])
        
            final = np.zeros((height * 2, width * 2, 3), dtype="uint8")
            final[0:height, 0:width] = frame 
            final[0:height, width:width * 2] = B 
            final[height:height * 2, 0:width] = G  
            final[height:height * 2, width:width * 2] = R 
            cv2.imshow('RGB', final)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
    cap.release()
    cv2.destroyAllWindows()
def main():
    bgr(mirror=True)
if __name__ == '__main__':
    main()
