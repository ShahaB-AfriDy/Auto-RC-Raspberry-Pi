__author__ = 'Equal != equal'

import numpy as np
import cv2.cv2 as cv2
import pygame
from pygame.locals import *
import time
import os
from datetime import datetime
from Robot_Collection import *

class CollectTrainingData(object):
    
    def __init__(self,input_size):
   
        self.input_size = input_size
        # for Labels Array create 
        self.k = np.zeros((4, 4), 'float')
        for i in range(4):
            self.k[i, i] = 1

        pygame.init()
        pygame.display.set_mode((250, 250)) # click on this window then start

        self.Car = Car(32,11,13,16,18,33,Speed=30)

    def Create_Dir(self):
        Total_Files = len(os.listdir(os.getcwd()))-1
        Dir_Name = "IMG_" + str(Total_Files)
        if not os.path.exists(str(Total_Files)):
            os.mkdir(Dir_Name) # in Pi Complete path + Dir_Name
        return Dir_Name

    def collect(self):
        Dir = self.Create_Dir()
        saved_frame = 0
        total_frame = 0

        # collect images for training
        print("Start collecting images...")
        print("Press 'q' or 'x' to finish...")
        start = cv2.getTickCount()

        X = np.empty((1, self.input_size),dtype=np.float) # i think not zero 0 it is 1
        y = np.empty((1, 4),dtype=float) # i think not zero 0 it is 1

        # stream video frames one by one
        try:
            frame = 1
            Video = cv2.VideoCapture(0)
            Video.set(3,320)
            Video.set(4,240)
            complex_cmd = False
            while Video.isOpened():
                Reading_Frame, Image = Video.read()

                Time_Now = datetime.now()
                File_Name = Dir + '\\' + Time_Now.strftime('%H_%M_%S') + '.jpg'

                Gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY).astype(np.uint8)

                # select lower half of the image
                height, width  = Gray.shape
                roi = Gray[height//2:height, :]

                # cv2.imshow('image', Image)

                temp_array = roi.reshape(1, height//2 * width).astype(np.float32)

                frame += 1
                total_frame += 1

                # get input from human driver
                for event in pygame.event.get():
                    if event.type == KEYDOWN or complex_cmd:
                        key_input = pygame.key.get_pressed()
                        complex_cmd = False

                        # only save the images where there is user action
                        cv2.imwrite(File_Name, Image)

                        # complex orders
                        if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                            print("Forward Right")
                            X = np.vstack((X, temp_array))
                            y = np.vstack((y, self.k[1]))
                            saved_frame += 1
                            complex_cmd = True
                            Car.Forward_Right()

                        elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                            print("Forward Left")
                            X = np.vstack((X, temp_array))
                            y = np.vstack((y, self.k[0]))
                            saved_frame += 1
                            complex_cmd = True
                            Car.Forward_Left()

                        # simple orders
                        elif key_input[pygame.K_UP]:
                            print("Forward")
                            saved_frame += 1
                            X = np.vstack((X, temp_array))
                            y = np.vstack((y, self.k[2]))
                            Car.Forward()


                        elif key_input[pygame.K_RIGHT]:
                            print("Right")
                            X = np.vstack((X, temp_array))
                            y = np.vstack((y, self.k[1]))
                            saved_frame += 1
                            Car.Right_Side()

                        elif key_input[pygame.K_LEFT]:
                            print("Left")
                            X = np.vstack((X, temp_array))
                            y = np.vstack((y, self.k[0]))
                            saved_frame += 1
                            Car.Left_Side()


                        elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                            print("exit")
                            break
                        else:
                            print("Stop")

                    elif event.type == pygame.KEYUP:...

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            #  # save data as a numpy file
            file_name = str(int(time.time()))
            directory = "Training_Data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            try:
                np.savez(directory + '/' + file_name + '.npz', train=X, train_labels=y)
            except IOError as e:
                print(e)

            end = cv2.getTickCount()
            # calculate streaming duration
            print("Streaming duration: , %.2fs" % ((end - start) / cv2.getTickFrequency()))

            print(X.shape)
            print(y.shape)
            print("Total frame: ", total_frame)
            print("Saved frame: ", saved_frame)
            print("Dropped frame: ", total_frame - saved_frame)

        finally:
           print("finish the session")


if __name__ == '__main__':
    # vector size, half of the image
    s = 120 * 320

    ctd = CollectTrainingData(s)
    ctd.collect()
