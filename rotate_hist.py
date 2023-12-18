import matplotlib.pyplot as plt
import numpy as np
import cv2
def grayConversion(img):
    h, w, c = img.shape
    R, G, B = cv2.split(img)
    gray = np.zeros([h, w], dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            gray[i, j] = int(R[i, j] * 0.114 + G[i, j] * 0.587 + B[i, j] * 0.299)
    return gray
def rotateImage(img):
    h, w = img.shape
    transpose=np.zeros([w,h],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            transpose[j,i]=img[i,j]
    return transpose

def histogram(img):
    h, w = img.shape
    hist=np.zeros([256],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            ind=img[i,j]
            hist[ind]=hist[ind]+1
    return hist


img=cv2.imread("C:/Users/User/OneDrive/Pictures/267434.jpg")
grayImg=grayConversion(img)
rot=rotateImage(grayImg)
img2=cv2.imshow("Rotate image",rot)
hist=histogram(grayImg)
plt.bar(np.arange(len(hist)),hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()