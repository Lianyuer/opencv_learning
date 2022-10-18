import cv2

image_path = "dog.png"  # 要读取图像的路径
img = cv2.imread(image_path)

##边界填充

top_size,bottom_size,left_size,right_size=(50,50,50,50)
replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)

"""
· BORDER_REPLICATE：复制法，也就是复制最边缘像素
· BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制。例如：fedcba|abcdefgh|hgfedcb
· BORDER_REFLECT101：反射法，也就是以最边缘像素为轴，对称。例如：gfedcb|abcdefgh|gfedcba
· BORDER_WRAP：外包装法，cdefgh|abcdefgh|abcdefg
· BORDER_CONSTANT：常量法，常数值填充
"""