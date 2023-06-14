import cv2
import numpy as np
img = cv2.imread("C:/Users/abdulmasood/Downloads/Genshin-Impact_Key-Art-EN-920x518.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)t
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original", img)
cv2.imshow("Gradient", grad)
cv2.waitKey
