# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

import unittest


def pick_peaks(arr):
    pos = []
    peaks = []
    for x in range(1, len(arr)-1):
        plateau = []
        count = 0
        if max(max(arr[x-1], arr[x]), arr[x+1]) == arr[x] and arr[x] > arr[x-1] and arr[x] >= arr[x+1]:
            for y in range(x, len(arr)):
                plateau.append(arr[y])
                if arr[y] == arr[x]:
                    count += 1
            print(f'{x} {plateau} {count}')
            if (arr[x] == arr[-1] and len(plateau) != count):
                break
            else:
                pos.append(x)
                peaks.append(arr[x])
    return ({"pos": pos, "peaks": peaks})


def pick_peaks_2(arr):
    pos = []
    peaks = []
    for x in range(1, len(arr)-1): #* from 1 -> 1st value never is peak, to len(arr)-1 -> last value never is peak
        left = -1
        right = -1
        for y in range(x-1, -1, -1): #* checking values before arr[x]
            if arr[y] >= arr[x]:
                break
            if arr[y] < arr[x]:
                left = y
                break
        for y in range (x, len(arr)): #* checking values after arr[x]
            if arr[y] > arr[x]:
                break
            if arr[y] < arr[x]:
                right = y
                break
        if left != -1 and right != -1:
            pos.append(x)
            peaks.append(arr[x])
    return ({"pos": pos, "peaks": peaks})


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pick_peaks_2([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
        self.assertEqual(pick_peaks_2([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
        self.assertEqual(pick_peaks_2([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
        self.assertEqual(pick_peaks_2([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
        self.assertEqual(pick_peaks_2([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks_2([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks_2([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks_2([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]),
                         {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
        self.assertEqual(pick_peaks_2([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]),{'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
        self.assertEqual(pick_peaks_2([]),{"pos":[],"peaks":[]})
        self.assertEqual(pick_peaks_2([1,1,1,1]),{"pos":[],"peaks":[]})
        self.assertEqual(pick_peaks_2([1,2,1,3,2]),{"pos":[1, 3],"peaks":[2, 3]})


if __name__ == '__main__':
    unittest.main()
