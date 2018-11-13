# -*- coding: utf-8 -*-
import fileinput

def main():
    lines = []
    #Parse lines of the input
    # inputs = int(fileinput.input())
    # training_size = int(fileinput.input())
    # tests_size = int(fileinput.input())
    inputs = int(input())
    training_size = int(input())
    tests_size = int(input())
    training_data_strings = []
    test_data_strings = []

    for val in range(0, training_size):
        # line = fileinput.input()
        line = list(map(float, input().replace(" ", '').split(',')))
        training_data_strings.append(line)

    for val in range(0, tests_size):
        # line = fileinput.input()
        line2 = list(map(float, input().replace(" ", "").split(',')))
        test_data_strings.append(line2)

    print(inputs)
    print(training_size)
    print(tests_size)
    print(training_data_strings)
    print(test_data_strings)

if __name__ == "__main__":
    main()
