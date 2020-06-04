import numpy as np
import cv2
import pytesseract
from pandas import Series


img = cv2.cvtColor(cv2.imread("test.png"), cv2.IMREAD_COLOR)

lower = np.array([121, 200, 159], dtype="uint8")
upper = np.array([121, 200, 159], dtype="uint8")

mask = cv2.inRange(img, lower, upper)

# 二值化操作
ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

#膨胀操作，因为是对线条进行提取定位，所以腐蚀可能会造成更大间隔的断点，将线条切断，因此仅做膨胀操作
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(binary, kernel, iterations=1)

#获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


answers = []
if len(contours) > 0:
    #cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
    boxes = [cv2.boundingRect(c) for c in contours]
    for box in boxes:
        left, top, w, h = box
        w = w -3
        opponent_img = img[top:top + h, left:left + w]
        result = pytesseract.image_to_string(opponent_img, lang='chi_sim').replace(' ', '').replace("\n", "")
        answers.append(result)

if answers:
    answer = Series(answers).value_counts().index[0]
else:
    answer = None

