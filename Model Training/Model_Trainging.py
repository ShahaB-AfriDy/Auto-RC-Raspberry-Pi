__author__ = 'Equal != equal'

from Model import load_data, NeuralNetwork

input_size = 120 * 320
data_path = r'E:\Python in Sublime\Projects\AutoRC\My AutoRC\Images Collection\Prepared Data\16_28_11.npz'
X_train, X_valid, y_train, y_valid = load_data(input_size, data_path)

# train a neural network
layer_sizes = [input_size, 32, 4]
nn = NeuralNetwork()
nn.create(layer_sizes)
nn.Train(X_train, y_train)

# evaluate on train data
train_accuracy = nn.evaluate(X_train, y_train)
print("Train accuracy: ", "{0:.2f}%".format(train_accuracy * 100))

# evaluate on validation data
validation_accuracy = nn.evaluate(X_valid, y_valid)
print("Validation accuracy: ", "{0:.2f}%".format(validation_accuracy * 100))

# save model
model_path = r"E:\Python in Sublime\Projects\AutoRC\My AutoRC\Model Training\Save Model\nn_model_56.xml"
nn.save_model(model_path)