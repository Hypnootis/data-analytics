import numpy

zeroes_list = numpy.zeros(15)
ones_list = numpy.ones(15)
sevens_list = numpy.full(15, 7)
hundred_list = numpy.arange(100, 151)
year_list = numpy.arange(1900, 2022)
evens_list = numpy.arange(0, 101, 2)

leap_years = numpy.arange(1950, 2021)

divisible = leap_years % 4 == 0

leap_years = leap_years[divisible]