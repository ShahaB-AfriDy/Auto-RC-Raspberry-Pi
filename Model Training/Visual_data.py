`import numpy as np
import time, glob, sys, cv2.cv2 as cv2

from sklearn.model_selection import train_test_split

Image_Path = r'E:\Python in Sublime\Projects\AutoRC\My AutoRC\Model Training\Training Data\16_05_24_Test_16.npz'


def load_data(input_size, path):
    print("Loading training data...")
    start = time.time()

    X = np.empty((0, input_size))
    y = np.empty((0, 4))

    training_data = glob.glob(path)

    # for single_npz in training_data:
    #     with np.load(single_npz) as data:
    #         train = data['train']
    #         train_labels = data['train_labels']

    with np.load(training_data[0]) as data:
        trained = data['train']
        Image = trained[9].reshape((120 ,320)).astype(np.uint8)
        cv2.imshow("Image", Image)
        cv2.waitKey(0)

load_data(120 * 320, Image_Path)