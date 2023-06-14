import cv2
img1 = cv2.imread("C:/Users/abdulmasood/Downloads/Genshin-Impact-1068x601.png")
img2 = cv2.imread("C:/Users/abdulmasood/Downloads/Genshin-Impact_Key-Art-EN-920x518.png")
roi = img1[100:300, 200:400]
x_offset = 50
y_offset = 100
img2[y_offset:y_offset+roi.shape[0], x_offset:x_offset+roi.shape[1]] = roi
cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
