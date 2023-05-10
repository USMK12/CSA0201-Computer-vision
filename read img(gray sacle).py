#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="C:/Users/Abdul/AppData/Local/Programs/Python/Python311/image/Screenshot 2023-04-16 214321.png"
img =  cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Lena",img)
cv2.imshow("GrayScale",imgGray)
