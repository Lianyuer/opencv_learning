"""
· cv2.IMREAD_COLOR:彩色图像
· cv2.IMREAD_GRAYSCALE:灰度图像
"""

import cv2  # opencv读取的格式是BGR
import numpy as np

image_path = "C:/Users/LianYu/Desktop/dog.png"  # 要读取图像的路径
img = cv2.imread(image_path)
print(img)

"""# 图像的显示，也可以创建多个窗口
cv2.imshow('image', img)
# 等待时间，毫秒级，0表示任意键终止
cv2.waitKey(0)
cv2.destroyAllWindows()"""


# 定义函数显示图像
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
# img = cv2.imread(image_path, -1)
print(img.shape)  # 参数-1为按原通道读入，不写的话默认读入三通道图片，例如（112，112，3）
print(img.shape[0])  # 读入的时图片的高度height
print(img.shape[1])  # 读入的时图片的宽度weight
"""

# 读取灰度图
img2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
print("灰度图", img2)

# cv_show(image_path, img2)

# 保存
image_path2 = 'C:/Users/LianYu/Desktop/mydog.png'
cv2.imwrite(image_path2, img2)

print(type(img))  # 图像格式
print(img.size)  # 像素点个数
print(img.dtype)  # 查看数据类型
