# https://www.codewars.com/kata/52a382ee44408cea2500074c

import unittest
import numpy as np


def determinant(matrix):
    if len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix[0]) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        result = 0
        n = len(matrix[0])
        for i in range(n):
            coeff = matrix[0][i]
            coeff_matrix = np.transpose(matrix[1:])
            coeff_matrix = np.transpose(np.delete(coeff_matrix, i, 0))
            if i % 2 == 0:
                result += coeff*determinant(coeff_matrix)
            else:
                result -= coeff*determinant(coeff_matrix)
        return result


# Tests
class Test(unittest.TestCase):
    def test_1x1(self):
        self.assertEqual(determinant(
            [[5]]), 5, "Determinant of a 1 x 1 matrix yields the value of the one element")

    def test_2x2(self):
        m2 = [[4, 6], [3, 8]]
        self.assertEqual(determinant(m2), 14,
                         "Should return 4*8 - 3*6, i.e. 14")

    def test_3x3(self):
        m3 = [[2, 4, 2], [3, 1, 2], [2, 2, 0]]
        self.assertEqual(determinant(
            m3), 16, "Should return the determinant of [[2,4,2],[3,1,1],[1,2,0]], i.e. 10")

    def test_4x4(self):
        m4 = [[4, 6, 8, 2], [8, 2, 4, 2], [2, 4, 2, 4], [6, 2, 2, 4]]
        self.assertEqual(determinant(m4), 128,
                         "Should return 128")


if __name__ == '__main__':
    unittest.main()
