import cv2
import matplotlib.pyplot as plt

top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)

image_path = "C:/Users/LianYu/Desktop/dog.png"  # 要读取图像的路径
img = cv2.imread(image_path)

replicate = cv2.copyMakeBorder(img, top_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, left_size, right_size, cv2.BORDER_REFLECT)
reflect[10] = cv2.copyMakeBorder(img, top_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, top_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)

plt.imshow(img, 'gray')