from matplotlib import pyplot as plt
import numpy as np
import glob
path = r'10_46_24New11.npz'
X = np.empty((0, 120*320))
y = np.empty((0, 4))

training_data = glob.glob(path)

for single_npz in training_data:
    # with np.load(os.path.basename(single_npz)) as data:
    with np.load(single_npz) as data:
        train = data['train']
        train_labels = data['train_labels']

    X = np.vstack((X, train))
    y = np.vstack((y, train_labels))


plt.plot(X,y)
plt.show()

print(X.shape)
print(y.shape)