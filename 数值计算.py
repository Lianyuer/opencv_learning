import cv2

img_cat = cv2.imread('cat.jpg')
img_dog = cv2.imread('dog.png')
img_cat = img_cat + 10
img_dog[:5, :, 0]

img_dog2 = img_dog + 10
img_dog2[:5, :, 0] # 打印前五行，全部列

# 相当于 %256
(img_dog + img_dog2)[:5, :, 0]

cv2.add(img_dog, img_dog2)[:5, :, 0] # 越界就取最大值255