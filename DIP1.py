import numpy as np
import cv2
img=cv2.imread("D:/Sinchu documents/NCC/SUO SINCHAN KARMAKAR.JPG")
h,w,c = img.shape
R,G,B=cv2.split(img)
gray=np.zeros([h,w],dtype=np.uint8)
for i in range(h):
    for j in range(w):
        gray[i,j]=int((R[i,j]+G[i,j]+B[i,j])/3)
cv2.imshow('Gray image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()