from matplotlib import pyplot as plt
import numpy as np
from glob import glob

data_path = r'E:\Python in Sublime\Projects\AutoRC\My AutoRC\Images Collection\Prepared Data\20_25_45.npz'

def load_data(path):
    Left = 0
    Forward = 0
    Right = 0

    npz_file = glob(path)

    for npz_files in npz_file:
        with np.load(npz_files) as data:
            # train = data['train']
            train_labels = data['train_labels']

    # converting float64 data type  into int8

    train_labels = train_labels.astype(np.int8)
    
    for u in train_labels: # u = 2dim, 1 * 4  = row * col
        if u[0] == 1:
            Left += 1
        elif u[2] == 1:
            Forward += 1
        elif u[1] == 1:
            Right += 1
    
    # print(f'Left: {Left}')
    # print(f'Forward: {Forward}')
    # print(f'Right: {Right}')

    return Left,Forward,Right


Left, Forward, Right = load_data(data_path)

def View_Data():
    X = [1,2,3]
    y = [Left,Forward,Right]
    Labels = ["Left","Forward","Right"]
    Color = ['g','c']
    # print(plt.style.available)
    plt.style.use('ggplot')
    plt.xkcd()

    plt.bar(X,y,color=Color,tick_label=Labels,width=0.3)
    plt.title("Total Images")
    plt.show()


if __name__ == "__main__":
    View_Data()





