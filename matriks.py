import sys

import numpy

matriks_non_numpy = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]

matriks_with_numpy = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matriks_non_numpy)
print("Ukuran keseluruhan elemen list dalam bytes = ", sys.getsizeof(matriks_non_numpy) * len(matriks_non_numpy))
print(matriks_with_numpy)
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", matriks_with_numpy.size * matriks_with_numpy.itemsize)
