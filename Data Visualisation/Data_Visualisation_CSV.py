from matplotlib import pyplot as plt
from pandas import read_csv

path = r'E:\Python in Sublime\Projects\AutoRC\My AutoRC\Images Collection\CSV Files\Balanced_data_4.csv'
DF = read_csv(path)


def View_Data():

	# Filtering the data for desire cooridnates

	Left = DF["Label"] == 0
	Left = DF.loc[Left,'Label']


	Forward = DF["Label"] == 2
	Forward = DF.loc[Forward,'Label']

	Right = DF["Label"] == 1
	Right = DF.loc[Right,'Label']


	X = [1,2,3]

	# y = [len(Left),len(Forward),len(Right)]
	y = [Left.size,Forward.size,Right.size]


	Labels = ['Left','Forward','Right']
	Color = ['g','b']
	# print(plt.style.available)
	plt.style.use('ggplot')
	plt.xkcd()

	plt.bar(X,y,color=Color,tick_label=Labels,width=0.4)
	plt.title("Total Images")
	plt.show()

if __name__ == "__main__":
	View_Data()