__author__ = 'Equal != equal'

import numpy as np
import cv2.cv2 as cv2
from Robot_Collection import Car
from Key_Press import getKey,init
import time
import os
from datetime import datetime


class CollectTrainingData(object):

    def __init__(self, input_size):
        self.input_size = input_size
        # for Labels Array create
        self.Label_Array = np.zeros((4, 4), 'float')
        for i in range(4):
            self.Label_Array[i, i] = 1
        init() # for pygame window
        self.Car = Car(32,11, 13, 16, 18,33,Speed=25)

    def Collect(self):
        if "Images Folder" not in os.listdir(os.getcwd()):
            os.mkdir('Images Folder')
        Current_Path = os.getcwd() + "\\Images Folder"

        saved_frame = 0
        total_frame = 0

        # collect images for training
        print("Start collecting images...")
        print("Press 'q' or 'x' to finish...")

        X = np.empty((0, self.input_size))  # i think not zero 0 it is 1
        y = np.empty((0, 4))  # i think not zero 0 it is 1

        # stream video frames one by one
        frame = 1
        Video = cv2.VideoCapture(0)
        Video.set(3, 320)
        Video.set(4, 240)
        while Video.isOpened():
            _, Image = Video.read()
            Time_Now = datetime.now()
            File_Name = Current_Path + '\\' + Time_Now.strftime('%H_%M_%S') + '.jpg'
            # np.uint8 must see
            Gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY).astype(np.uint8)
            # select lower half of the image
            height, width = Gray.shape
            roi = Gray[height // 2 :height, :]

            # reshape the roi image into a vector
            temp_array = roi.reshape(1, (height // 2) * width).astype(np.float32)

            cv2.imshow('image', Image)
            cv2.waitKey(1)

            frame += 1
            total_frame += 1

            # get input from human driver
            # complex orders
            if getKey('UP') and getKey('RIGHT'):
                self.Car.Forward_Left()
                print("Forward Right")
                X = np.vstack((X, temp_array))
                y = np.vstack((y, self.Label_Array[1]))
                cv2.imwrite(File_Name,Image)
                saved_frame += 1

            elif getKey('UP') and getKey('LEFT'):
                self.Car.Forward_Right()
                print("Forward Left")
                X = np.vstack((X, temp_array))
                y = np.vstack((y, self.Label_Array[0]))
                cv2.imwrite(File_Name, Image)
                saved_frame += 1

            # simple orders
            elif getKey('UP'):
                self.Car.Forward()
                print("Forward")
                X = np.vstack((X, temp_array))
                y = np.vstack( (y, self.Label_Array[2]))
                cv2.imwrite(File_Name, Image)
                saved_frame += 1

            elif getKey('RIGHT'):
                self.Car.Right_Side()
                print("Right")
                X = np.vstack((X, temp_array))
                y = np.vstack((y, self.Label_Array[1]))
                cv2.imwrite(File_Name, Image)
                saved_frame += 1

            elif getKey('LEFT'):
                self.Car.Left_Side()
                print("Left")
                X = np.vstack((X, temp_array))
                y = np.vstack((y, self.Label_Array[0]))
                cv2.imwrite(File_Name, Image)
                saved_frame += 1

            else:
                print("Stop")
                self.Car.Stop_Car()
            if getKey('c'):
                break

        print(saved_frame)
        print(len(os.listdir('Images Folder')))
        # # save data as a numpy file
        file_name = str(int(time.time()))
        directory = "training_data"
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            np.savez(directory + '/' + file_name + '.npz', train=X, train_labels=y)
        except IOError as e:
            print(e)

        print(X.shape)
        print(y.shape)
        print("Total frame: ", total_frame)
        print("Saved frame: ", saved_frame)
        print("Dropped frame: ", total_frame - saved_frame)
        print("finish the session")


if __name__ == '__main__':
    # vector size, half of the image
    s = 120 * 320
    ctd = CollectTrainingData(s)
    ctd.Collect()
