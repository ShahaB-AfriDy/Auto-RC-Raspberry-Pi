import os

import cv2.cv2 as cv2
import numpy as np
import Model as mm

# in Raspberry pi make sure to complete path otherwise not work for model
path = r"E:\Python in Sublime\Projects\AutoRC\My AutoRC\Model Training\Save Model\nn_model2.xml"
Model = mm.Model(path)
Model.Load_model()

def Preprocess(Image):
    Gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY).astype(np.uint8)
    return Gray.reshape(1, 120*320).astype(np.float32)
    # height, width = Gray.shape
    # roi = Gray[height // 2:height, :]
    # # cv2.imshow('roi', roi)
    # Image_array = roi.reshape(1, (height // 2) * width).astype(np.float32)
    # return Image_array
# --------------------------------------------------
# Image_Folder = r'E:\Python in Sublime\Projects\AutoRC\My AutoRC\IMG_1'
Image_Folder = r"E:\Python in Sublime\Projects\Practice\Raw Data\Images of npz 18"
Images_List = os.listdir(Image_Folder)
Right,Left,Forward,Reverse = [] , [], [] , []
for u in range(len(Images_List)):
    Image = Image_Folder+'\\'+Images_List[u]
    Image = cv2.imread(Image)
    Image = Preprocess(Image)
    # print(Image.shape)
    prediction = Model.predict(Image)
    print(prediction[0])
    # if prediction[0] == 1:
    #     Right.append((u+1,prediction))
    # if prediction[0] == 0:
    #     Left.append((u+1,prediction))
    # if prediction[0] == 2:
    #     Forward.append((u+1,prediction))
    # if prediction[0] == 3:
    #     Reverse.append((u+1,prediction))

# print(len(Images_List))
# print("Right: ",len(Right))
# print("Left: ",len(Left))
# print("Forward: ",len(Forward))
# print("Reverse: ",len(Reverse))

