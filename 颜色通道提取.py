import cv2
import img_read
# 截取部分图像数据
img = cv2.imread(img_read.image_path)
dog = img[0:200, 0:200]
# img_read.cv_show('dog', dog)

"""
颜色通道提取
"""
b, g, r = cv2.split(img)
print(r)
# 还原颜色通道
img = cv2.merge((b, g, r))
print(img.shape)
# 只保留R
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
img_read.cv_show('R', cur_img)
# 只保留G
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 2] = 0
img_read.cv_show('G', cur_img)
# 只保留B
cur_img = img.copy()
cur_img[:, :, 1] = 0
cur_img[:, :, 2] = 0
img_read.cv_show('B', cur_img)