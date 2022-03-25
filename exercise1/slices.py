import numpy

dataset = numpy.arange(1, 37).reshape(6, 6)

first_slice = dataset[3:, 2:]
second_slice = dataset[0:4, 3]
third_slice = dataset[2, 0:]
fourth_slice = dataset[3:, :5]