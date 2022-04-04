# import cv2.cv2 as cv2
#
# import  numpy as np
# Video = cv2.VideoCapture(0)
#
# Video.set(3, 320)
# Video.set(4, 220)
# while Video.isOpened():
#     Reading_Frame, Image = Video.read()
#     # in preverse code datatype  which is this dtype=np.uint8
#     C = Image.copy()
#     # Gray = cv2.cvtColor(C, cv2.IMREAD_GRAYSCALE)
#     Gray = cv2.cvtColor(C, cv2.COLOR_RGB2GRAY)
#     Gray = Gray.astype(np.int8)
#     print(Gray.shape)
#     height, width = Gray.shape
#     roi = Gray[height//2:height, :] # 120
#
#     roi.reshape(1, height//2*width)
#
#     # cv2.imshow('image', Image)
#     # reshape the roi image into a vector
#     # temp_array = roi.reshape(1, height // 2 * width).astype(np.float32)
#
#     if cv2.waitKey(1) == 27:
#         break


def Curve(c=0):
    print(c)

def Runer():
    l = -1
    if l == 1:
        Curve(l)
    elif l ==-1:
        Curve(l)
    else:
        Curve()

Runer()