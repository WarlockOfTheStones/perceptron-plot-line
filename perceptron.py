# -*- coding: utf-8 -*-
"""perceptron.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OLrYZBleM-lzMcFKLxdLZUDGyPhr8GhB
"""

import random
import sys
from matplotlib import pyplot as plt
import matplotlib.animation as animation

MAX_POINT = 100
NUM_POINTS = 20

class Perceptron:
    def __init__(self, num_inputs = 2, weights = [1,1], bias = 1, learning_rate = 0.001):
        self.num_inputs = num_inputs
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate

    def generate_training_set(num_points):
        x_coordinates = [random.randint(0, MAX_POINT) for i in range(num_points)]
        y_coordinates = [random.randint(0, MAX_POINT) for i in range(num_points)]
        training_set = dict()
        for x, y in zip(x_coordinates, y_coordinates):
            if x <= 90-y:
                training_set[(x,y)] = 1
            elif x > 90-y:
                training_set[(x,y)] = -1
        return training_set

    def weighted_sum(self, inputs):
        weighted_sum = 0
        weighted_bias = 0 #initalise weighted sum
        for i in range(self.num_inputs): #go through each input and weight
            weighted_sum += self.weights[i] * inputs[i]
        return weighted_sum + self.bias

    def activation(self, weighted_sum): #prediction on whether point is above or below the line
        if weighted_sum >= 0:
            return 1
        elif weighted_sum <0:
            return -1

    def training(self, training_set):
        best_line = False #initalise state of line of best fit
        while not best_line:
            total_error = 0 #initalise error
            for inputs in training_set:
                prediction = self.activation(self.weighted_sum(inputs)) #predicted classification of value
                actual = training_set[inputs] #actual classification of value
                error = (actual - prediction)
                total_error += abs(error) #update total error
                for i in range(self.num_inputs): #go through each weights
                    self.weights[i] += (error * inputs[i])* self.learning_rate
                    self.bias += error #apply perceptron algorithm
            slope = -self.weights[0]/self.weights[1]
            intercept = -myPerceptron.bias/myPerceptron.weights[1]
            y1 = (slope * 0) + intercept
            y2 = (slope * 100) + intercept
            lines.append([[0,100], [y1, y2]])
            weight_list.append([self.weights[0], self.weights[1], self.bias])
            if total_error == 0:
                best_line = True #when algorithm is complete

training_set = Perceptron.generate_training_set(NUM_POINTS)

x_plus = []
y_plus = []
x_minus = []
y_minus = []
lines = []
weight_list = []

for data in training_set:
	if training_set[data] == 1:
		x_plus.append(data[0])
		y_plus.append(data[1])
	elif training_set[data] == -1:
		x_minus.append(data[0])
		y_minus.append(data[1])


myPerceptron = Perceptron()
myPerceptron.training(training_set)
#print(training_set)

fig = plt.figure()
ax = plt.axes(xlim=(-10, 110), ylim=(-10, 110))
line, = ax.plot([], [], lw=2)
plt.scatter(x_plus, y_plus, marker = 'o', s = 40, linewidth = 2, facecolors='none', edgecolors='g' )
plt.scatter(x_minus, y_minus, marker = 'x', c = 'red', s = 40, linewidth = 2,)

def animate(i):
    print(weight_list[i])
    line.set_xdata(lines[i][0])
    line.set_ydata(lines[i][1])
    return line,

def init():
    line.set_data([],[])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(lines), init_func=init, interval = 50 ,blit = True, repeat = False)
ani.save('animation.gif', writer='imagemagick', fps=60)
#slope = -myPerceptron.weights[0]/myPerceptron.weights[1]
#intercept = -myPerceptron.bias/myPerceptron.weights[1]
#y1 = (slope * 0) + intercept
#y2 = (slope * 50) + intercept
#line, = ax.plot([0,50], [y1, y2], lw=2)
plt.show()