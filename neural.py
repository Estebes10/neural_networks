# -*- coding: utf-8 -*-

def main():
    lines = []
    inputs = 0
    #Parse lines of the input
    inputs = fileinput.input()
    training_size = fileinput.input()
    tests_size = fileinput.input()
    training_data = []
    test_data = []

    for line in range(0, training_size):
        training_data.append(line)

    for line in range(0, tests_size):
        test_data.append(line)

    print(inputs)
    print(training_size)
    print(tests_size)
    print(training_data)
    print(test_data)

if __name__ == "__main__":
    main()
