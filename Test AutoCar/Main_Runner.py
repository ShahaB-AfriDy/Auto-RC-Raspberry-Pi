import cv2.cv2 as cv2
import numpy as np
import Model_Module as mm
from Auto_Car_Module import Car

# --------------------------------------------
Auto_RC = Car(32,11,13,16,18,33,Speed=40)
# --------------------------------------------
# model path
# in Raspberry pi make sure to complete path otherwise not work for model
path = "saved_model/nn_model.xml"
Model = mm.Model(path)
Model.Load_model()
# ----------------------------------------------
Video = cv2.VideoCapture(0)
Video.set(3,320)
Video.set(4,240)
# ----------------------------------------------
def Preprocess(Image):
    # BGR2GRAY or RGB2GRAY
    Gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY).astype(np.uint8)
    # Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY).astype(np.uint8)
    height, width = Gray.shape
    roi = Gray[height // 2:height, :]
    # reshape the roi image into a vector
    Image_array = roi.reshape(1, (height // 2) * width).astype(np.float32)
    return Image_array
# --------------------------------------------------
while Video.isOpened():
    _,Image = Video.read()
    Img2 = Image.copy()
    image_array = Preprocess(Img2)
    prediction = Model.predict(image_array)

    # cv2.imshow("Video",Image)

    if prediction == 2:
        Auto_RC.Forward()
    elif prediction == 0:
        Auto_RC.Left_Side()
    elif prediction == 1:
        Auto_RC.Right_Side()
    else:
        Auto_RC.Stop_Car()

    cv2.waitKey(1)

