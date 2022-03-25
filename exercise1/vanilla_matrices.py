
number = 1
matrix = []
lin_matrix = []


for i in range(7):
    row = []
    for j in range(7):
        row.append(number)
        number += 1
    matrix.append(row)
    
def evenly_spaced(start, stop, values):
    delta = (stop - start) / (values - 1)
    result = [start + i * delta for i in range(values)]
    return result

lin_array = evenly_spaced(0, 5, 100)

for i in range(10):
    array = []
    tens = 0
    for j in range(10):
        array.append(lin_array[j + tens])
    tens += 10
    lin_matrix.append(array)

