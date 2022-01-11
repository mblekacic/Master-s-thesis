import cv2 as cv
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, img = vid.read()
    cv.imshow("img", img)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.xlabel('Intenzitet od tamnog prema svijetlom')
    plt.ylabel('Broj piksela')
    plt.title('Histogram')
    plt.draw()
    plt.pause(0.1)
    plt.clf()

vid.release()
cv.destroyAllWindows()
