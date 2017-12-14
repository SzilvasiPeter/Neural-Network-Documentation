from keras.models import Sequential
from keras.layers import Dense
import numpy
#random seeds
numpy.random.seed(7)

#load dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")

# split the input(X) and output(Y)
X = dataset[:,0:8]
Y = dataset[:,8]

# create model
model = Sequential()
model.add(Dense(12,input_dim=8,activation="relu")) #relu f(x)=log(1+exp(x))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

#Compilie model
model.compile(loss="binary_crossentropy", optimizer='adam', metrics=["accuracy"]) #logaritmic loss ->binary_crossentropy, gradient descent algorith -> adam

# Fit the model
model.fit(X, Y, epochs=150, batch_size=10) #epoch: iterations, batch_size: evaulated before weight update -> CPU/GPU support

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
