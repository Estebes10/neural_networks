# -*- coding: utf-8 -*-
import fileinput
import random
import math

def random_weights(inputs_size):
    weightsTemp = []
    for i in range(0, inputs_size):
        weightAux = random.randrange(0,1)
        weightsTemp.append(weightAux)

    return weightsTemp

def activation(weights, threshold, x):
    act = 0
    for i in range(0,len(x)):
        act = act + (x[i] * weights[i])

    if act > threshold:
        return 1
    else:
        return 0

def update_weights(weights, threshold, trainingVal):
    updated_weights = []

    val = trainingVal[1]
    #need activation method
    #newCalc should be equals to activation
    newCalc = activation(weights, threshold, trainingVal[0])
    #error = val - newCalc
    error = val - newCalc

    for index, val in enumerate(weights):
        weights[index] += error * trainingVal[0][index]

    updated_weights.append(error)
    updated_weights.append(weights)

    return updated_weights

def main():
    #Parse lines of the input
    # inputs = int(fileinput.input())
    # training_size = int(fileinput.input())
    # tests_size = int(fileinput.input())
    times = 100
    #d
    inputs = int(input())
    #m
    training_size = int(input())
    #n
    tests_size = int(input())
    training_data_strings = []
    test_data_strings = []
    weights = []

    for val in range(0, training_size):
        line = input()
        line = (line.rstrip('\n').rstrip('\r')).replace(" ", "").split(",")
        lineArr = ([float(value) for value in line[0:-1]])
        data = ((lineArr), float(line[-1]))
        training_data_strings.append(data)

    for val in range(0, tests_size):
        line2 = input()
        line2 = (line2.rstrip('\n').rstrip('\r')).replace(" ", "").split(",")
        line2Arr = ([float(value) for value in line2])
        test_data_strings.append(line2Arr)

    weights = random_weights(inputs)

    threshold = random.randrange(1,10)

    while times >= 0:
        error = 0
        for trainingVal in training_data_strings:
            updated_weights = update_weights(weights, threshold, trainingVal)
            nError = updated_weights[0]
            weights = updated_weights[1]

            error = error + (nError ** 2)
        if(error == 0):
            break
        times = times - 1

    if(error >= 1):
        print("no solution found")
    else:
        for x in test_data_strings:
            print(activation(weights, threshold, x))

    #print(inputs)
    #print(training_size)
    #print(tests_size)
    #print(training_data_strings)
    #print(test_data_strings)
    #print(weights)

if __name__ == "__main__":
    main()
