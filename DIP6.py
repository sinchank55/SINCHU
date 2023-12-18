import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread("C:/Users/User/Pictures/Camera Roll/WIN_20231202_12_42_35_Pro.jpg")
h,w,c=img.shape

R=np.zeros([h,w],dtype=np.uint8)
G=np.zeros([h,w],dtype=np.uint8)
B=np.zeros([h,w],dtype=np.uint8)
Z=np.zeros([h,w],dtype=np.uint8)


for i in range(h):
    for j in range(w):
        B[i,j]=img[i,j,0]
        G[i,j]=img[i,j,1]
        R[i,j]=img[i,j,2]

B=cv2.merge([B,Z,Z])
G=cv2.merge([Z,G,Z])
R=cv2.merge([Z,Z,R])


cv2.imshow('R',R)
cv2.imshow('G',G)
cv2.imshow('B',B)


cv2.waitKey(0)
cv2.destroyAllWindows()