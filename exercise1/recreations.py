import numpy

matrix1 = [23, 34, 54, 34, 56, 
           33, 56, 78, 65, 78,
           41, 32, 11, 34, 56]

matrix1 = numpy.array(matrix1).reshape(3, 5)

matrix2 = numpy.arange(128, 256).reshape(16, 8)

matrix3 = numpy.linspace(0, 5, 100).reshape(10, 10)