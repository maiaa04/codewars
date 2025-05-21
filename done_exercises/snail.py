import math

def snail(snail_map):
    n = len(snail_map[0])
    if n == 0:
        return []
    arr = [snail_map[0][0]]
    count = 0
    while arr[-1] != snail_map[math.floor(n/2)][math.ceil(n/2)-1]:
        # top horizontal (>)
        for x in range(count, n-count):
            arr.append(snail_map[count][x])
        # right vertical (v)
        for x in range(count+1, n-count):
            arr.append(snail_map[x][n-count-1])
        # bottom horizontal (<)
        for x in range(n-count-2, count-1, -1):
            arr.append(snail_map[n-count-1][x])
        # left vertical (^)
        for x in range(n-count-2, count, -1):
            arr.append(snail_map[x][count])
        count += 1
    if count != 0:
        arr.pop(0)
    return arr


array = [[1, 2, 3, 4, 5],
         [16, 17, 18, 19, 6],
         [15, 24, 25, 20, 7],
         [14, 23, 22, 21, 8],
         [13, 12, 11, 10, 9]]
array_even = [[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]]
print(snail(array))
