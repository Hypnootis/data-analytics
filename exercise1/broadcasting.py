import numpy

dataset = numpy.arange(1, 50).reshape(7, 7)

add_fifty = dataset + 50

sums = numpy.sum(dataset)

odd_sums = numpy.sum(dataset[dataset % 2 != 0])

std_deviation = numpy.std(dataset)

row_sums = numpy.sum(dataset, axis = 1)

column_sums = numpy.sum(dataset, axis = 0)