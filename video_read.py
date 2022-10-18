"""
· cv2.VideoCapture可以捕获摄像头，用数字来控制不同的设备，例如0，1.
· 如果是视频文件，直接指定好路径即可
"""

import cv2

video_path = 'C:/Users/LianYu/Desktop/test.mp4'
vc = cv2.VideoCapture(video_path)
# 检查是否打开正确
if vc.isOpened():
    open, frame = vc.read()  # vc.read()取视频中的每一帧，返回open为布尔类型，true表示这一帧能读进来;frame表示当前这一帧图像的三维数组
else:
    open = False

# 只要能打开就遍历每一帧
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
